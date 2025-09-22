#!/usr/bin/env bash

USER=tester

dev install-deps

echo "Initial build."
dev build

echo "" >> ~/.bashrc
echo "# Activate environment." >> ~/.bashrc
# shellcheck disable=SC2016
echo ". /opt/ros/humble/setup.bash" >> "${HOME}"/.bashrc
echo ". /home/tester/ws/install/setup.bash" >> "${HOME}"/.bashrc

dev --help
echo ""
echo "Setup complete. Development environment ready to go!!"
echo "Use the command 'dev --help' to get started."
