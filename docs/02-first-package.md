# Lesson 2. 워크스페이스와 첫 패키지 만들기

## 1. 워크스페이스 구조

ROS2에서는 여러 패키지를 `src/` 폴더 아래 모아두고, 그 상위 폴더(**워크스페이스**)에서
`colcon build`로 한꺼번에 빌드합니다. 이 저장소 자체가 워크스페이스입니다:

```
ROS2/                      <- 워크스페이스 루트
├── src/                   <- 패키지 소스 코드 (git으로 관리)
│   └── my_first_pkg/
├── build/                 <- 빌드 중간 산출물 (git 제외, .gitignore)
├── install/               <- 빌드 결과물, 실행 파일들이 여기 설치됨 (git 제외)
└── log/                   <- 빌드/실행 로그 (git 제외)
```

`build/ install/ log/`는 언제든 다시 만들어낼 수 있는 산출물이라 `.gitignore`에 추가했습니다.

## 2. 패키지 생성

```bash
cd src
ros2 pkg create --build-type ament_python my_first_pkg --dependencies rclpy std_msgs
```

- `--build-type ament_python`: Python 패키지로 만든다 (C++이면 `ament_cmake`)
- `--dependencies rclpy std_msgs`: 이 패키지가 `rclpy`(ROS2 파이썬 클라이언트 라이브러리)와
  `std_msgs`(기본 제공 메시지 타입 모음, 여기선 `String` 사용)에 의존한다고 명시

생성된 구조 중 중요한 파일:

- `package.xml` — 패키지 메타데이터(이름/의존성/버전)
- `setup.py` — 어떤 파이썬 파일을 "실행 파일(entry point)"로 노출할지 지정
- `my_first_pkg/` (같은 이름의 하위 폴더) — 실제 파이썬 코드가 들어가는 곳

## 3. Publisher 노드 작성 (`my_first_pkg/my_publisher.py`)

```python
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MyPublisher(Node):
    def __init__(self):
        super().__init__('my_publisher')                      # 노드 이름
        self.publisher_ = self.create_publisher(String, 'my_topic', 10)  # 토픽 발행자 생성
        self.timer = self.create_timer(1.0, self.timer_callback)          # 1초마다 콜백 호출
        self.count = 0

    def timer_callback(self):
        msg = String()
        msg.data = f'안녕, ROS2! {self.count}번째 메시지'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')
        self.count += 1

def main(args=None):
    rclpy.init(args=args)
    node = MyPublisher()
    rclpy.spin(node)          # 노드를 계속 살려두고 콜백을 계속 실행
    node.destroy_node()
    rclpy.shutdown()
```

**핵심 API 3개만 기억하면 됩니다:**

- `create_publisher(타입, 토픽이름, 큐크기)` — 발행자 생성
- `create_timer(주기, 콜백)` — 주기적으로 함수 실행
- `rclpy.spin(node)` — 콜백이 실제로 호출되게 만드는 이벤트 루프 (이게 없으면 타이머도 안 돌아감)

## 4. Subscriber 노드 작성 (`my_first_pkg/my_subscriber.py`)

```python
class MySubscriber(Node):
    def __init__(self):
        super().__init__('my_subscriber')
        self.subscription = self.create_subscription(
            String, 'my_topic', self.listener_callback, 10)

    def listener_callback(self, msg: String):
        self.get_logger().info(f'받음: "{msg.data}"')
```

**주의**: publisher와 subscriber는 서로 **같은 토픽 이름('my_topic')과 같은 메시지 타입(String)**을
써야만 연결됩니다. 이름이나 타입이 다르면 서로 조용히 무시하고 아무 에러도 나지 않으니
처음 배울 때 가장 흔히 하는 실수입니다.

## 5. `setup.py`에 실행 파일 등록

```python
entry_points={
    'console_scripts': [
        'my_publisher = my_first_pkg.my_publisher:main',
        'my_subscriber = my_first_pkg.my_subscriber:main',
    ],
},
```

이렇게 등록해야 `ros2 run my_first_pkg my_publisher` 처럼 실행할 수 있습니다.
(`패키지이름 my_publisher.py의 main함수` 형태로 매핑)

## 6. 빌드 & 실행

```bash
cd ~/ROS2                      # 워크스페이스 루트
colcon build --packages-select my_first_pkg
source install/setup.bash      # 방금 빌드한 패키지를 셸에서 쓸 수 있게 등록
ros2 run my_first_pkg my_publisher     # 터미널 1
ros2 run my_first_pkg my_subscriber    # 터미널 2
```

## 7. 실제 실행 결과 (검증됨)

```
$ ros2 node list
/my_publisher
/my_subscriber

$ ros2 topic list
/my_topic
/parameter_events
/rosout

$ ros2 topic info /my_topic
Type: std_msgs/msg/String
Publisher count: 1
Subscription count: 1

[my_publisher]:  Publishing: "안녕, ROS2! 3번째 메시지"
[my_subscriber]: 받음: "안녕, ROS2! 3번째 메시지"
```

`talker`/`listener`는 남이 만든 예제였지만, 이번엔 **직접 작성한 코드**로 두 프로세스가
토픽을 통해 통신하는 걸 확인했습니다.

## 8. 알아두면 좋은 명령어

| 명령 | 설명 |
|---|---|
| `ros2 node list` | 현재 떠 있는 노드 목록 |
| `ros2 topic list` | 현재 존재하는 토픽 목록 |
| `ros2 topic echo /my_topic` | 토픽에 흐르는 메시지를 실시간으로 화면에 출력 |
| `ros2 topic info /my_topic` | 토픽의 타입, publisher/subscriber 개수 |
| `ros2 topic hz /my_topic` | 토픽이 초당 몇 번 발행되는지 측정 |

---

**다음: Lesson 3. 서비스(Service) — 요청/응답 통신 만들어보기**
