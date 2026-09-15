"""[실습] 직접 작성하는 Subscriber 노드.

my_publisher.py와 같은 토픽 이름, 같은 메시지 타입을 써야 서로 연결됩니다!
"""
# TODO 1: rclpy, Node, String을 import 하세요. (publisher와 동일)


class MySubscriber(Node):
    def __init__(self):
        # TODO 2: super().__init__('노드이름')으로 노드 이름을 지어주세요.
        #         (publisher와 이름이 겹치면 안 됩니다 - 서로 다른 노드니까요)

        # TODO 3: create_subscription(메시지타입, 토픽이름, 콜백함수, 큐사이즈)으로
        #         구독을 만드세요. 토픽이름은 my_publisher.py에서 쓴 이름과 반드시 같아야 합니다!
        #   힌트: self.subscription = self.create_subscription(
        #             String, '토픽이름', self.listener_callback, 10)
        pass

    def listener_callback(self, msg):
        # TODO 4: 전달받은 msg.data를 로그로 출력하세요.
        #   힌트: self.get_logger().info(f'받음: "{msg.data}"')
        pass


def main(args=None):
    # TODO 5: publisher의 main()과 똑같은 패턴입니다.
    #   1) rclpy.init(args=args)
    #   2) node = MySubscriber()
    #   3) rclpy.spin(node)
    #   4) node.destroy_node() / rclpy.shutdown()
    pass


if __name__ == '__main__':
    main()
