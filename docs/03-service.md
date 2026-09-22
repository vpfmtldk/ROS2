# Lesson 3. 서비스(Service)

## 1. 토픽과 뭐가 다른가

| | 토픽(Topic) | 서비스(Service) |
|---|---|---|
| 통신 방향 | 단방향 (발행 → 구독) | 양방향 (요청 → 응답) |
| 동작 방식 | 비동기 방송 (라디오) | 동기적 요청-응답 (전화 통화) |
| 참여자 수 | N:N (여러 발행자, 여러 구독자) | 보통 1:1 (요청 하나에 응답 하나) |
| 데이터 흐름 | 계속 흐름 | 호출할 때만 1회성 |
| 비유 | 라디오 방송 | 자판기 (버튼 누르면 물건 하나 나옴) |

토픽은 "카메라 영상을 계속 뿌린다" 같은 **지속적인 스트림**에 맞고,
서비스는 "지도를 저장해줘", "두 수를 더해줘" 같은 **한 번 요청하고 결과를 받는 작업**에 맞습니다.

## 2. 서비스의 데이터 구조: `.srv` 파일

토픽이 메시지 타입(`.msg`) 하나를 쓴다면, 서비스는 **요청(Request)과 응답(Response)이 합쳐진**
`.srv` 파일을 씁니다. 예를 들어 이번에 쓸 `example_interfaces/AddTwoInts`는 이렇게 생겼습니다:

```
int64 a
int64 b
---
int64 sum
```

`---` 위쪽이 요청 필드, 아래쪽이 응답 필드입니다. 즉 "정수 a, b를 보내면 sum을 돌려준다"는 계약입니다.
(직접 커스텀 `.srv`를 만드는 법은 나중 Lesson에서 다룹니다 — 이번엔 이미 만들어져 있는
`example_interfaces`를 가져다 씁니다.)

## 3. 서버(Server) 쪽 API 모양

```python
from example_interfaces.srv import AddTwoInts

self.srv = self.create_service(AddTwoInts, '서비스이름', self.콜백함수)

def 콜백함수(self, request, response):
    # request.a, request.b 로 들어온 값을 읽고
    response.sum = request.a + request.b   # response 필드를 채워서
    return response                         # 반드시 response를 return 해야 함
```

Publisher/Subscriber와 다른 점: 콜백이 `request`와 `response` **두 개**를 받고,
끝에 `response`를 **return**해야 클라이언트에게 결과가 전달됩니다.

## 4. 클라이언트(Client) 쪽 API 모양

```python
from example_interfaces.srv import AddTwoInts

self.cli = self.create_client(AddTwoInts, '서비스이름')

# 서버가 아직 안 떠 있을 수도 있으니 기다림
while not self.cli.wait_for_service(timeout_sec=1.0):
    self.get_logger().info('서비스 기다리는 중...')

request = AddTwoInts.Request()
request.a = 1
request.b = 2
future = self.cli.call_async(request)          # 비동기 호출 (future를 즉시 반환)
rclpy.spin_until_future_complete(self, future)  # 응답 올 때까지 대기
response = future.result()
print(response.sum)
```

**중요한 함정**: `call_async` 대신 그냥 `call()`(동기 호출)을 쓰면, 노드 자기 자신의 콜백 안에서
호출했을 때 **데드락**에 빠질 수 있습니다 (응답을 처리해야 할 스레드가 이미 호출 때문에 막혀 있어서).
그래서 rclpy에서는 거의 항상 `call_async` + `spin_until_future_complete` 조합을 씁니다.

## 5. 터미널에서 바로 테스트하는 법 (노드 코드 없이)

서버 노드 하나만 띄워놓고, 클라이언트 코드를 안 짜도 CLI로 바로 호출해볼 수 있습니다:

```bash
ros2 service list                 # 떠 있는 서비스 목록
ros2 service type /서비스이름      # 이 서비스가 어떤 .srv 타입인지
ros2 service call /서비스이름 example_interfaces/srv/AddTwoInts "{a: 3, b: 5}"
```

## 6. 실습

패키지 뼈대(`src/my_service_pkg/`)는 미리 만들어져 있습니다 (`package.xml`, `setup.py`만 —
로직은 없음). 아래 두 파일을 직접 작성하면 됩니다:

- `src/my_service_pkg/my_service_pkg/my_server.py` — 두 수를 더해주는 서비스 서버
- `src/my_service_pkg/my_service_pkg/my_client.py` — 그 서비스를 호출하는 클라이언트

`ros2 run my_service_pkg my_server` / `ros2 run my_service_pkg my_client`로 실행되게
`setup.py`에 미리 연결해뒀습니다.

---

**다음: Lesson 4. 파라미터(Parameter)**
