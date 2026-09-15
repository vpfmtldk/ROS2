"""[실습] 직접 작성하는 Publisher 노드.

아래 TODO를 순서대로 채워서 완성하세요.
막히면 Lesson 2 문서(docs/02-first-package.md)나 완성본 예제
(src/my_first_pkg/my_first_pkg/my_publisher.py)를 참고해도 됩니다.
"""
# TODO 1: rclpy와 Node를 import 하세요.
#   힌트: import rclpy
#         from rclpy.node import Node

# TODO 2: 발행할 메시지 타입을 import 하세요. (문자열 메시지 = std_msgs.msg.String)
#   힌트: from std_msgs.msg import String


class MyPublisher(Node):
    def __init__(self):
        # TODO 3: 부모 클래스(Node)의 __init__을 호출하면서 노드 이름을 지어주세요.
        #   힌트: super().__init__('노드이름')

        # TODO 4: create_publisher(메시지타입, 토픽이름, 큐사이즈)로 퍼블리셔를 만들고
        #         self.publisher_ 에 저장하세요.
        #   힌트: self.publisher_ = self.create_publisher(String, '토픽이름', 10)

        # TODO 5: create_timer(주기(초), 콜백함수)로 타이머를 만들어서
        #         일정 주기마다 아래 timer_callback이 호출되게 하세요.
        #   힌트: self.timer = self.create_timer(1.0, self.timer_callback)

        self.count = 0  # 몇 번째 메시지인지 세는 용도 (미리 준비해둠)

    def timer_callback(self):
        # TODO 6: 메시지 객체를 만들고, .data 필드에 원하는 문자열을 채우세요.
        #   힌트: msg = String()
        #         msg.data = f'...{self.count}...'

        # TODO 7: self.publisher_로 메시지를 발행(publish)하세요.
        #   힌트: self.publisher_.publish(msg)

        # TODO 8 (선택): self.get_logger().info(...)로 로그를 남겨서
        #                무엇을 보냈는지 터미널에서 확인할 수 있게 하세요.

        self.count += 1


def main(args=None):
    # TODO 9: rclpy 통신 시스템을 초기화하세요.
    #   힌트: rclpy.init(args=args)

    # TODO 10: MyPublisher 노드 인스턴스를 만드세요.
    #   힌트: node = MyPublisher()

    # TODO 11: rclpy.spin(node)로 노드를 계속 살아있게 하세요.
    #          (Ctrl+C로 멈출 때까지 콜백들이 계속 호출됨)

    # TODO 12: 정리 작업 - node.destroy_node()와 rclpy.shutdown()을 호출하세요.
    pass


if __name__ == '__main__':
    main()
