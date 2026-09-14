"""내가 직접 만드는 첫 ROS2 Publisher 노드.

1초마다 "안녕, ROS2! N번째 메시지" 같은 문자열을 /my_topic 토픽에 발행한다.
"""
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class MyPublisher(Node):
    def __init__(self):
        # Node.__init__에 넘기는 문자열이 이 노드의 이름이 된다. (ros2 node list에 보임)
        super().__init__('my_publisher')

        # create_publisher(메시지타입, 토픽이름, QoS큐사이즈)
        self.publisher_ = self.create_publisher(String, 'my_topic', 10)

        # create_timer(주기(초), 콜백함수): 1초마다 timer_callback을 호출
        self.timer_period = 1.0
        self.timer = self.create_timer(self.timer_period, self.timer_callback)
        self.count = 0

    def timer_callback(self):
        msg = String()
        msg.data = f'안녕, ROS2! {self.count}번째 메시지'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')
        self.count += 1


def main(args=None):
    rclpy.init(args=args)          # ROS2 통신 시스템 초기화 (필수, 항상 맨 먼저)
    node = MyPublisher()
    try:
        rclpy.spin(node)            # 콜백들이 계속 호출되도록 이벤트 루프를 돌림 (Ctrl+C 전까지)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()            # 마무리 정리


if __name__ == '__main__':
    main()
