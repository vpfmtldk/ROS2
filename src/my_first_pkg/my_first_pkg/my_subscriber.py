"""내가 직접 만드는 첫 ROS2 Subscriber 노드.

/my_topic 토픽을 구독하다가, 메시지가 도착할 때마다 콜백이 호출되어 로그를 남긴다.
"""
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class MySubscriber(Node):
    def __init__(self):
        super().__init__('my_subscriber')

        # create_subscription(메시지타입, 토픽이름, 콜백함수, QoS큐사이즈)
        # publisher와 "토픽 이름"과 "메시지 타입"이 반드시 같아야 서로 연결된다.
        self.subscription = self.create_subscription(
            String,
            'my_topic',
            self.listener_callback,
            10)

    def listener_callback(self, msg: String):
        self.get_logger().info(f'받음: "{msg.data}"')


def main(args=None):
    rclpy.init(args=args)
    node = MySubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
