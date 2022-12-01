import rclpy
from rclpy.node import Node
from person_msgs.msg import Int16

def cd(msg):
    global node
    node.get_logger().info("Listen: %s" % msg)

rclpy.init()
node = Node("Listener")
pub = node.create_subscription(Person, "countup", cd, 10)
rclpy.spin(node)
