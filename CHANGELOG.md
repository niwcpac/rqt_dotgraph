# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)

## Unreleased

### Added

### Fixed

### Removed

## v0.0.1 - 2021-05-17

Initial release of a ROS2 node and an rqt plugin for visualizing dot graph files.

### Added

- Github actions workflow to test and lint the package.
- Automatically zooming to fit dotgraph only the first time a graph is received on a topic.
  Zooming to fit upon loading dotgraph file.

### Fixed

- Properly destroying old subscription.
