#! /usr/bin/env python

import rospy
from std_msgs.msg import String #发布的消息的类型

if __name__ == "__main__":
    #初始化ROS节点
    rospy.init_node("pub")
    #创建发布者对象
    pub = rospy.Publisher("xuehao", String, queue_size = 10)
    #编写发布逻辑并发布数据
    msg = String()
    #指定发布频率
    rate = rospy.Rate(1)
    #设置计数器
    count = 0
    rospy.sleep(1)
    while not rospy.is_shutdown():
        count += 1
        msg.data = "我的学号：("+str(count)+")2023111733"
        #发布数据
        pub.publish(msg)
        rospy.loginfo(msg.data)
        rate.sleep()   #每隔1HZ发布一次数据
