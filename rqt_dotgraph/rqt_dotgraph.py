"""
rqt GUI plugin to visualize dot graphs.

This software was developed by employees of the Federal Government in the course of
their official duties. Pursuant to title 17 Section 105 of the United States Code, this
software is not subject to copyright protection and is in the public domain. The
Government assumes no responsibility whatsoever for its use by other parties, and the
software is provided "AS IS" without warranty or guarantee of any kind, express or
implied, including, but not limited to, the warranties of merchantability, fitness for a
particular purpose, and noninfringement. In no event shall the Government be liable for
any claim, damages or other liability, whether in an action of contract, tort or other
dealings in the software. The software is not designed for use in (i) the design,
construction, operation or maintenance of any nuclear facility; (ii) navigating or
operating aircraft or any manned vehicle; or (iii) any life-saving, life-support or
life-critical medical equipment. The Government has no obligation hereunder to provide
maintenance, support, updates, enhancements, or modifications.  We would appreciate
acknowledgement if the software is used. This software can be redistributed and/or
modified freely provided that any derivative works bear some notice that they are
derived from it, and any modified versions bear some notice that they have been
modified.
"""

import contextlib
import io
import os
import sys

from ament_index_python import get_resource

# pylint doesn't support how python_qt_bindings modules are added:
# https://github.com/PyCQA/pylint/issues/3398
# pylint: disable=no-name-in-module,import-error
from python_qt_binding import loadUi
from python_qt_binding.QtGui import QImageWriter
from python_qt_binding.QtSvg import QSvgGenerator
from python_qt_binding.QtWidgets import QFileDialog, QWidget

# pylint: enable=no-name-in-module,import-error

from rqt_gui.main import Main

from rqt_gui_py.plugin import Plugin

from std_msgs.msg import String

from rqt_dotgraph.xdot_qt import DotWidget


class RqtDotGraphViewer(Plugin):
    """rqt GUI plugin to visualize dot graphs."""

    def __init__(self, context):
        """Initialize the plugin."""
        super().__init__(context)
        self._context = context
        self.subscription = None
        self.graph = None
        self.filename = None

        # only declare the parameter if running standalone or it's the first instance
        if self._context.serial_number() <= 1:
            self._context.node.declare_parameter("title", "Dot Graph Viewer")
        self.title = self._context.node.get_parameter("title").value

        supported_formats = QImageWriter.supportedImageFormats()
        self.image_filter = (
            ";;".join(["*.{}".format(fo.data().decode()) for fo in supported_formats])
            + ";;*.svg"
        )

        self._widget = QWidget()
        self.setObjectName(self.title)

        _, package_path = get_resource("packages", "rqt_dotgraph")
        ui_file = os.path.join(
            package_path, "share", "rqt_dotgraph", "resource", "rqt_dotgraph.ui"
        )
        loadUi(ui_file, self._widget, {"DotWidget": DotWidget})
        self._widget.setObjectName(self.title + "UI")

        self._widget.refreshButton.clicked[bool].connect(self.update_subscriber)
        self._widget.loadButton.clicked[bool].connect(self.load_graph)
        self._widget.saveButton.clicked[bool].connect(self.save_graph)

        title = self.title
        if self._context.serial_number() > 1:
            title += " (%d)" % self._context.serial_number()

        self._context.add_widget(self._widget)

        self._widget.setWindowTitle(title)
        # only set main window title if running standalone
        if self._context.serial_number() < 1:
            self._widget.window().setWindowTitle(self.title)

        self.setup_subscription("dot_graph")

    def update_subscriber(self):
        """Update ROS 2 subscription with topic from text box."""
        if self.subscription is not None:
            self._context.node.destroy_subscription(self.subscription)
            self.subscription = None
            self.graph = None
        topic = self._widget.topicText.text()
        self.setup_subscription(topic)

    def setup_subscription(self, topic):
        """Create the ROS 2 subscription."""
        self.subscription = self._context.node.create_subscription(
            String, topic, self.plan_graph_callback, 10
        )
        self._widget.topicText.setText(self.subscription.topic_name)

    def plan_graph_callback(self, msg):
        """Receive the dot graph string."""
        zoom_to_fit = self.graph is None
        self.graph = msg.data
        self.refresh_graph(zoom_to_fit)

    def refresh_graph(self, zoom_to_fit):
        """Update the dot graph displayed by the plugin."""
        if self.graph is None:
            return
        self._context.node.get_logger().debug(self.graph)

        # Capture stdout and stderr and output as an info level log
        # because ROS2 logging levels when launching are broken.
        new_out = io.StringIO()
        new_err = io.StringIO()
        with contextlib.redirect_stdout(new_out):
            with contextlib.redirect_stderr(new_err):
                self._widget.xdot_widget.set_dotcode(self.graph)
        self._context.node.get_logger().debug(new_out.getvalue())
        self._context.node.get_logger().debug(new_err.getvalue())

        if zoom_to_fit:
            self._widget.xdot_widget.zoom_to_fit()
        self._widget.xdot_widget.update()

    def load_graph(self):
        """Load a dot graph from a file."""
        ret = QFileDialog.getOpenFileName(
            self._widget, "Load graph", "untitled.dot", "Dot files (*.dot *.xdot)"
        )
        if ret[0]:
            with open(ret[0], "r") as dotfile:
                self.filename = ret[0]
                self.graph = dotfile.read()
                self.refresh_graph(True)
                if self.subscription is not None:
                    self.subscription.destroy()
                    self.subscription = None

    def save_graph(self):
        """Save the current dot graph as an image."""
        if self.graph is None:
            return

        ret = QFileDialog.getSaveFileName(
            self._widget, "Save graph as", "untitled.png", self.image_filter, "*.png"
        )
        if ret[0]:
            _, extension = os.path.splitext(ret[0])
            if extension == ".svg":
                gen = QSvgGenerator()
                gen.setFileName(ret[0])
                gen.setSize(self._widget.xdot_widget.size())
                gen.setViewBox(self._widget.xdot_widget.rect())
                self._widget.xdot_widget.grab().save(ret[0])
                self._widget.xdot_widget.render(gen)
            else:
                self._widget.xdot_widget.grab().save(ret[0])

    # Qt methods
    def shutdown_plugin(self):
        """Shutdown plugin."""

    def save_settings(self, plugin_settings, instance_settings):
        """Save settings."""

    def restore_settings(self, plugin_settings, instance_settings):
        """Restore settings."""


def main():
    """Run the plugin."""
    sys.exit(Main().main(sys.argv, standalone="rqt_dotgraph.rqt_dotgraph"))


if __name__ == "__main__":
    main()
