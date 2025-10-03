#include "ros/ros.h"
#include "std_msgs/String.h"

//subscribe的回调函数
void doMsg(const std_msgs::String::ConstPtr msg)
{
    //通过msg获取并操作订阅到的数据
    ROS_INFO("我收到的学号%s", msg->data.c_str());
}

int main(int argc, char *argv[])
{
    setlocale(LC_ALL, "");
    //初始化ROS节点
    ros::init(argc, argv, "sub");
    //创建节点句柄
    ros::NodeHandle nh;
    //创建订阅者对象
    ros::Subscriber sub = nh.subscribe("xuehao", 10, doMsg);

    ros::spin();          //回到回调函数
    return 0;
}