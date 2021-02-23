"""rqt GUI plugin to visualize dot graphs."""

from setuptools import setup

PACKAGE_NAME = "rqt_dotgraph"

setup(
    name=PACKAGE_NAME,
    version="0.0.0",
    packages=[PACKAGE_NAME],
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + PACKAGE_NAME]),
        ("share/" + PACKAGE_NAME + "/resource", ["resource/rqt_dotgraph.ui"]),
        ("share/" + PACKAGE_NAME, ["package.xml"]),
        ("share/" + PACKAGE_NAME, ["plugin.xml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Alexander Xydes",
    maintainer_email="alexander.xydes@navy.mil",
    description="rqt GUI plugin to visualize dot graphs.",
    license="U.S. Navy",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": ["rqt_dotgraph = rqt_dotgraph.rqt_dotgraph:main"],
    },
)
