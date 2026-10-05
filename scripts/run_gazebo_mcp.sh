#!/usr/bin/env bash
# Launch the gazebo-mcp server over stdio (used by .mcp.json).
set -e
DEST="${GAZEBO_MCP_HOME:-$HOME/.local/share/gazebo-mcp}"

# Prefer this repo's micromamba "ros2" env (scripts/activate_ros2.sh) when present.
if [ -x /home/user/tools/micromamba ]; then
  export MAMBA_ROOT_PREFIX=/home/user/micromamba
  eval "$(/home/user/tools/micromamba shell hook -s posix)"
  micromamba activate ros2
fi

for distro in jazzy humble; do
  if [ -f "/opt/ros/$distro/setup.bash" ]; then
    # shellcheck disable=SC1090
    source "/opt/ros/$distro/setup.bash"
    break
  fi
done

export PYTHONUNBUFFERED=1
export GAZEBO_BACKEND="${GAZEBO_BACKEND:-modern}"
export GAZEBO_WORLD_NAME="${GAZEBO_WORLD_NAME:-empty}"
# The server resolves the top-level gz_mcp_server package from the repo root.
export PYTHONPATH="$DEST:$DEST/src${PYTHONPATH:+:$PYTHONPATH}"
exec "$DEST/.venv/bin/python" -m gazebo_mcp.fastmcp_server
