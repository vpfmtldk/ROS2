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

# Make rclpy visible to the venv: use the sourced ROS 2 install if no env is active.
if ! python3 -c "import rclpy" 2>/dev/null; then
  for distro in jazzy humble; do
    if [ -f "/opt/ros/$distro/setup.bash" ]; then
      set +u
      # shellcheck disable=SC1090
      source "/opt/ros/$distro/setup.bash"
      set -u
      break
    fi
  done
fi
python3 -m venv --system-site-packages "$DEST/.venv"
# The system setuptools/packaging (apt) are too old to build the package and would
# shadow newer ones, so upgrade them inside the venv first.
"$DEST/.venv/bin/pip" install -q -U pip setuptools wheel "packaging>=24"
# The server imports mcp.server.fastmcp, which mcp 2.x removed, so pin 1.x.
"$DEST/.venv/bin/pip" install -q "$DEST" "mcp>=1.27,<2"
echo "Installed to $DEST"
