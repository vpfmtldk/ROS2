#!/usr/bin/env bash
# 이 저장소의 ROS2(Jazzy) 실습 환경을 활성화하는 헬퍼 스크립트.
# 사용법: source scripts/activate_ros2.sh
export MAMBA_ROOT_PREFIX=/home/user/micromamba
eval "$(/home/user/tools/micromamba shell hook -s posix)"
micromamba activate ros2
