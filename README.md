# ROS2 공부 저장소

처음부터 차근차근 ROS2(Robot Operating System 2)를 공부하기 위한 저장소입니다.
개념 설명 + 직접 실행해보는 실습 코드를 한 과씩(Lesson) 쌓아갑니다.

## 진행 방식

- 한 번에 한 Lesson씩 진행합니다. 이해가 안 되면 언제든 질문하세요.
- 이론(개념) → 실습(코드 실행) → 정리 순서로 구성합니다.
- 실습 코드는 `src/` 아래에 ROS2 패키지로 만들어 실제로 빌드/실행하면서 확인합니다.
- 이 환경(클라우드 컨테이너)에는 GUI가 없어서 RViz, Gazebo 같은 시각화 도구는
  화면으로 직접 보여드리긴 어렵습니다. 대신 커맨드라인 도구(`ros2 topic`,
  `ros2 node`, `ros2 service` 등)와 터미널 로그로 결과를 확인합니다.

## 개발 환경

- OS: Ubuntu 24.04 (Noble)
- ROS2 배포판: **Jazzy Jalisco** (24.04 LTS 대응 버전)
- 설치 방법: 이 환경은 공식 `packages.ros.org` APT 저장소에 접근이 막혀 있어서,
  대신 **RoboStack**(conda/micromamba 기반 ROS2 배포판)으로 설치합니다.
  → 자세한 이유와 방법은 [`docs/01-install.md`](docs/01-install.md) 참고.

## 목차 (커리큘럼)

- [Lesson 0. ROS2란 무엇인가](docs/00-overview.md)
- [Lesson 1. 설치 및 환경 구성](docs/01-install.md)
- Lesson 2. 워크스페이스와 패키지 (예정)
- Lesson 3. 노드(Node)와 `ros2 run` (예정)
- Lesson 4. 토픽(Topic)과 Publisher/Subscriber (예정)
- Lesson 5. 서비스(Service)와 Client/Server (예정)
- Lesson 6. 파라미터(Parameter) (예정)
- Lesson 7. 액션(Action) (예정)
- Lesson 8. launch 파일 (예정)
- Lesson 9. TF2 / URDF 맛보기 (예정)

> 목차는 진행하면서 계속 업데이트됩니다.
