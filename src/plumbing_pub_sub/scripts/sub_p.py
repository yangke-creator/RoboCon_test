#! usr/bin/env python
import rospy
from std_msgs.msg import String

def do_Msg(msg):
    rospy.loginfo(msg.data)

if __name__ == "__main__":
    #初始化ROS节点
    rospy.init_node("sub")
    #创建订阅者对象
    sub = rospy.Subscriber("xuehao",String,do_Msg,queue_size=10)
    #回到回调函数
    rospy.spin()

