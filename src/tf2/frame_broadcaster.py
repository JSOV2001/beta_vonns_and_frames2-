#!/usr/bin/env python3
import rospy
import tf2_ros
from tf_conversions import transformations 
from geometry_msgs.msg import TransformStamped
import serial
import math

rospy.init_node("transform_broadcaster_tf2")
transform_broadcaster = tf2_ros.TransformBroadcaster()

with serial.Serial('/dev/ttyUSB1', 9600, timeout=1) as my_serial_port:
    while not rospy.is_shutdown():
        angle_byte = my_serial_port.readline()
        angle_int = 0
        if angle_byte.decode("utf-8") == "":
            continue
        else:
            angle_int = int(angle_byte.decode('utf-8'))
            
        transform_broadcaster = tf2_ros.TransformBroadcaster()
        transformation_data = TransformStamped()

        #Se define los frames en cuestion
        transformation_data.header.frame_id = "laser"
        transformation_data.child_frame_id = "link1"
        #Se define cuando se toma la ultima transformacion del frame
        transformation_data.header.stamp = rospy.Time.now()
        #Se definen los datos de la traslacion
        transformation_data.transform.translation.x = 0.0
        transformation_data.transform.translation.y = 0.0
        transformation_data.transform.translation.z = 0.0
        #Se definen los datos de la rotacion
        quaternions = transformations.quaternion_from_euler(0.0, math.radians(angle_int), 0.0)
        transformation_data.transform.rotation.x = quaternions[0]
        transformation_data.transform.rotation.y = quaternions[1]
        transformation_data.transform.rotation.z = quaternions[2]
        transformation_data.transform.rotation.w = quaternions[3]

        transform_broadcaster.sendTransform(transformation_data)
        
        print(angle_int)
        if angle_int == 45:
            break