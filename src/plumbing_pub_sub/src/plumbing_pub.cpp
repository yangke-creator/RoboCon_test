#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sstream>

int main(int argc, char *argv[])
{
    setlocale(LC_ALL, "");
    //初始化ROS节点
    ros::init(argc, argv, "pub");
    //创建节点句柄
    ros::NodeHandle nh;
    //创建发布者对象
    ros::Publisher pub = nh.advertise<std_msgs::String>("xuehao", 10);
    //创建被发布的消息
    std_msgs::String msg;
    //设置发布频率
    ros::Rate rate(10);
    //设置编号
    int count = 0;
    //编写循环
    ros::Duration(3).sleep();
    while (ros::ok())
    {
        count++;
        std::stringstream ss;
        ss << "("<< count <<"):"<<"2023111733";
        msg.data = ss.str();
        // msg.data = "2023111733";
        pub.publish(msg);
        //添加日志
        ROS_INFO("我的学号%s", msg.data.c_str());
        rate.sleep();  //每隔10HZ发布一次数据
    }
    
    return 0;
}