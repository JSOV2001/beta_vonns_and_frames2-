#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import PointCloud

def callback_function(message):
    print(message)

if __name__ == "__main__":
    rospy.init_node("pointcloud1_subscriber")
    
    pointcloud1_subscriber = rospy.Subscriber("/pointcloud1", PointCloud, callback_function)
    
    rospy.spin()