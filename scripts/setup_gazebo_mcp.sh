#!/usr/bin/env bash
# Install kvgork/gazebo-mcp into ~/.local/share/gazebo-mcp (clone + venv).
# ROS 2 (Jazzy or Humble) must be installed separately; see scripts/activate_ros2.sh.
set -euo pipefail

DEST="${GAZEBO_MCP_HOME:-$HOME/.local/share/gazebo-mcp}"

if [ -d "$DEST/.git" ]; then
  git -C "$DEST" pull --ff-only
else
  git clone --depth 1 https://github.com/kvgork/gazebo-mcp "$DEST"
fi

# Run this inside the activated ROS 2 env so the venv can see rclpy.
python3 -m venv --system-site-packages "$DEST/.venv"
# The server imports mcp.server.fastmcp, which mcp 2.x removed, so pin 1.x.
"$DEST/.venv/bin/pip" install -q "$DEST" "mcp>=1.27,<2"
echo "Installed to $DEST"
