# Lesson 1. 설치 및 환경 구성

## 1. 이 실습 환경(클라우드)에서는 어떻게 설치했는가

보통 Ubuntu 24.04에서 ROS2 Jazzy를 설치하는 공식 방법은 `packages.ros.org`라는
APT 저장소를 등록하고 `apt install ros-jazzy-desktop`을 실행하는 것입니다.

하지만 **이 클라우드 실습 환경은 보안상 `packages.ros.org`로 나가는 네트워크가 막혀 있습니다**
(프록시가 403을 반환). 그래서 대신 **[RoboStack](https://robostack.github.io/)**을 사용했습니다.

> RoboStack이란? ROS/ROS2를 conda 패키지로 다시 빌드해서 배포하는 커뮤니티 프로젝트입니다.
> `apt`나 `sudo` 없이, 사용자 계정 권한만으로 원하는 경로에 ROS2를 설치할 수 있습니다.
> conda 패키지 서버(`conda.anaconda.org`)는 이 환경에서 접근이 가능해서 이 방법을 썼습니다.

설치 과정 (참고용, 이미 실행 완료됨):

```bash
# 1) micromamba(conda 호환의 초경량 패키지 매니저) 설치
curl -sSL -o ~/tools/micromamba \
  "https://github.com/mamba-org/micromamba-releases/releases/latest/download/micromamba-linux-64"
chmod +x ~/tools/micromamba

# 2) RoboStack 채널에서 ROS2 Jazzy(ros-base) + 빌드 도구 설치
export MAMBA_ROOT_PREFIX=~/micromamba
~/tools/micromamba create -y -n ros2 \
  -c robostack-jazzy -c conda-forge --strict-channel-priority \
  ros-jazzy-ros-base compilers cmake pkg-config make ninja colcon-common-extensions

# 3) 데모/예제 패키지 추가 설치
~/tools/micromamba install -y -n ros2 \
  -c robostack-jazzy -c conda-forge --strict-channel-priority \
  ros-jazzy-demo-nodes-py ros-jazzy-demo-nodes-cpp ros-jazzy-example-interfaces
```

**설치한 것: `ros-jazzy-ros-base`** (GUI 도구인 RViz, rqt, Gazebo는 제외한 핵심 구성 —
어차피 이 환경엔 화면이 없어서 필요 없습니다). 필요하면 나중에 언제든 추가 설치 가능합니다.

## 2. 매번 환경을 켜는 방법

이 저장소에는 활성화를 쉽게 해주는 스크립트가 있습니다:

```bash
source scripts/activate_ros2.sh
```

이렇게 하면 `ros2`, `colcon`, `rclpy` 등을 쓸 수 있는 셸이 됩니다. (Claude가 실습 중 이 명령을
매번 대신 실행해 줄 것입니다 — 여러분이 직접 셸을 열어 타이핑하는 세션이 아니기 때문입니다.)

## 3. 설치 확인

```bash
$ ros2 pkg list | wc -l
2xx   # 200개 안팎의 패키지가 잡히면 정상

$ python3 -c "import rclpy; print(rclpy.__file__)"
/home/user/micromamba/envs/ros2/lib/python3.12/site-packages/rclpy/__init__.py
```

## 4. 참고: 여러분의 개인 PC(Ubuntu)에 설치할 때는?

이 프로젝트를 떠나 **본인 컴퓨터(리눅스, 인터넷 제한 없음)**에 ROS2를 설치할 때는
RoboStack을 쓸 필요 없이 **공식 방법**을 쓰는 게 더 간단하고 표준적입니다:

- Ubuntu 24.04 → ROS2 **Jazzy** 공식 apt 설치: https://docs.ros.org/en/jazzy/Installation.html
- Ubuntu 22.04 → ROS2 **Humble** 공식 apt 설치: https://docs.ros.org/en/humble/Installation.html
- Windows/macOS나 apt를 쓰기 애매한 경우에만 RoboStack(`https://robostack.github.io/`) 고려

즉, RoboStack은 "이 클라우드 환경의 네트워크 제약"을 우회하기 위한 선택이었고,
개념적으로 배우는 ROS2 자체는 공식 설치든 RoboStack이든 완전히 동일합니다.

---

**다음: Lesson 2. 워크스페이스와 첫 패키지 만들기**
