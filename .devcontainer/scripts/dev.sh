#!/usr/bin/env bash

# Function to display help information.
show_help() {
  echo "Developer Commands:"
  echo "  dev build - Run colcon build."
  echo "  dev install-deps - Install needed dependencies."
  echo "  dev source - Re-source workspace."
}

# Match the `workspaceFolder` in the .devcontainer.json.
APP_HOME="/home/tester/ws"
export APP_HOME

# Function to execute commands
execute_command() {
    case $1 in
    build)
        pushd /home/tester/ws
        colcon build --symlink-install
        popd
        ;;
    install-deps)
        echo "Installing dependencies."
        source /opt/ros/humble/setup.bash
        pushd /home/tester/ws
        sudo apt-get update
        rosdep update
        rosdep install -y -r -q --from-paths src --ignore-src --rosdistro ${ROS_DISTRO} --os ubuntu:jammy
        popd
        ;;
    source)
        echo "Resourcing ROS and dev workspace."
        source /opt/ros/humble/setup.bash
        source /home/tester/ws/install/setup.bash
        ;;
    *)
        echo "Unknown command: $1"
        show_help
        echo "Use 'dev --help' for a list of available commands."
        ;;
    esac
}

# Check for --help argument
if [ -z "$1" ] || [ "$1" == "--help" ]; then
    show_help
else
    execute_command "$1"
fi
