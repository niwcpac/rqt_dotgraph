^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package rqt_dotgraph
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Forthcoming
===========
* Contributors: Alexander Xydes, Thomas Denewiler

Fixed
-----
* Use a Python virtual environment when installing Python dependencies with pip.

  - Fixes issue with GitHub Actions running on rolling, based on Ubuntu 22.04 with Python 3.10.

0.0.3 (2024-10-02)
==================
* Contributors: Alexander Xydes, Thomas Denewiler

Added
-----
* First ROS 2 package release.

0.0.2 (2024-03-08)
==================
* Contributors: Alexander Xydes, Thomas Denewiler

Added
-----
* Troubleshooting:

  - Tips for some runtime crashes due to missing dependencies. (#13)
  - Details about fixing plugin file not found error. (#9)
* Run actions on a schedule or `workflow_dispatch` as well as pull request and push. (#10)
* Update actions used in workflows. (#14)
* Update CI to use newer versions of actions and test on multiple ROS distributions. (#12)
* Update list of maintainers. (#18)

Fixed
-----
* Add PySide2 and PyQt5 dependencies to package.xml. (#16)
* Switch from hyphen to underscore in setup.cfg to avoid deprecated Python variables. (#11)
* Explicitly specifying file encoding when opening a file with Python. Fixes pylint warning (Statick). (#6)
* Continuous integration fixes.

  - Use setup-python and setup-node actions.
  - Remove sudo from pip install commands.
  - Add Jazzy to the ROS distribution matrix.

Removed
-------
* Remove version pinning for pycodestyle in workflow. (#15)

0.0.1 (2021-05-17)
==================
* Initial release of a ROS2 node and an rqt plugin for visualizing dot graph files.
* Contributors: Alexander Xydes

Added
-----
* Github actions workflow to test and lint the package.
* Automatically zooming to fit dotgraph only the first time a graph is received on a topic.
  Zooming to fit upon loading dotgraph file.

Fixed
-----
* Properly destroying old subscription.
