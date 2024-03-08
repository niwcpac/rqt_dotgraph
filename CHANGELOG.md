# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)

## Unreleased

### Added

- Troubleshooting:
  - Tips for some runtime crashes due to missing dependencies. (#13)
  - Details about fixing plugin file not found error. (#9)
- Run actions on a schedule or `workflow_dispatch` as well as pull request and push. (#10)
- Update actions used in workflows. (#14)
- Update CI to use newer versions of actions and test on multiple ROS distributions. (#12)
- Update list of maintainers. (#18)

### Fixed

- Add PySide2 and PyQt5 dependencies to package.xml. (#16)
- Switch from hyphen to underscore in setup.cfg to avoid deprecated Python variables. (#11)
- Explicitly specifying file encoding when opening a file with Python. Fixes pylint warning (Statick). (#6)

### Removed

- Remove version pinning for pycodestyle in workflow. (#15)

## v0.0.1 - 2021-05-17

Initial release of a ROS2 node and an rqt plugin for visualizing dot graph files.

### Added

- Github actions workflow to test and lint the package.
- Automatically zooming to fit dotgraph only the first time a graph is received on a topic.
  Zooming to fit upon loading dotgraph file.

### Fixed

- Properly destroying old subscription.
