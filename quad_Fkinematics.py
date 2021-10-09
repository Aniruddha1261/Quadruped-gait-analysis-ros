#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import rospy
from std_msgs.msg import Float64
import math
import forward_kinematics_module

theta = [math.pi/2,0]
d = [0,0]
alpha = [0,0]
a = [120,109.25]

def forward_kinematics_publisher():
    limb1 = rospy.Publisher('/manipulator/limb1_controller/command',Float64, queue_size=10)
    leg1  = rospy.Publisher('/manipulator/leg1_controller/command',Float64, queue_size=10)
    rospy.init_node('forward_kinematics_publisher', anonymous=True)
    rate = rospy.Rate(10)   #10hz
    while not rospy.is_shutdown():
        theta_limb1 = float(input("{:22s}".format("Enter theta_limb1: ")))
        theta_leg1 = float(input("{:22s}".format("Enter theta_leg1: ")))
        theta = [theta_limb1, theta_leg1, 0]

        if 0.0 <= theta_limb1 <= 180.0 and 0.0 <= theta_leg1 <= 180.0: 
            limb1[0] = (theta_limb1)*math.pi/180
            leg1[1] = (theta_leg1)*math.pi/180

            rospy.loginfo("\ntheta_base = %f\ntheta_shoulder = %f\ntheta_elbow = %f", limb1[0], leg1[1])
            theta_limb1.publish(limb1[0])
            theta_limb1.publish(leg1[1])
            print ("=========================\n")

    limb2 = rospy.Publisher('/manipulator/limb2_controller/command',Float64, queue_size=10)
    leg2  = rospy.Publisher('/manipulator/leg2_controller/command',Float64, queue_size=10)
    rospy.init_node('forward_kinematics_publisher', anonymous=True)
    rate = rospy.Rate(10)   #10hz
    while not rospy.is_shutdown():
        theta_limb2 = float(input("{:22s}".format("Enter theta_limb2: ")))
        theta_leg2 = float(input("{:22s}".format("Enter theta_leg2: ")))
        theta = [theta_limb2, theta_leg2, 0]

        if 0.0 <= theta_limb2 <= 180.0 and 0.0 <= theta_leg2 <= 180.0: 
            limb2[0] = (theta_limb2)*math.pi/180
            leg2[1] = (theta_leg2)*math.pi/180

            rospy.loginfo("\ntheta_base = %f\ntheta_shoulder = %f\ntheta_elbow = %f", limb2[0], leg2[1])
            theta_limb2.publish(limb2[0])
            theta_limb2.publish(leg2[1])
            print ("=========================\n")

    limb3= rospy.Publisher('/manipulator/limb3_controller/command',Float64, queue_size=10)
    leg3  = rospy.Publisher('/manipulator/leg3_controller/command',Float64, queue_size=10)
    rospy.init_node('forward_kinematics_publisher', anonymous=True)
    rate = rospy.Rate(10)   #10hz
    while not rospy.is_shutdown():
        theta_limb3 = float(input("{:22s}".format("Enter theta_limb3: ")))
        theta_leg3 = float(input("{:22s}".format("Enter theta_leg3: ")))
        theta = [theta_limb3, theta_leg3, 0]

        if 0.0 <= theta_limb3 <= 180.0 and 0.0 <= theta_leg3 <= 180.0: 
            limb3[0] = (theta_limb3)*math.pi/180
            leg3[1] = (theta_leg3)*math.pi/180

            rospy.loginfo("\ntheta_base = %f\ntheta_shoulder = %f\ntheta_elbow = %f", limb3[0], leg3[1])
            theta_limb3.publish(limb3[0])
            theta_limb3.publish(leg3[1])
            print ("=========================\n")

    limb4 = rospy.Publisher('/manipulator/limb4_controller/command',Float64, queue_size=10)
    leg4  = rospy.Publisher('/manipulator/leg4_controller/command',Float64, queue_size=10)
    rospy.init_node('forward_kinematics_publisher', anonymous=True)
    rate = rospy.Rate(10)   #10hz
    while not rospy.is_shutdown():
        theta_limb4 = float(input("{:22s}".format("Enter theta_limb4: ")))
        theta_leg4 = float(input("{:22s}".format("Enter theta_leg4 ")))
        theta = [theta_limb4, theta_leg4, 0]

        if 0.0 <= theta_limb4 <= 180.0 and 0.0 <= theta_leg4 <= 180.0: 
            limb4[0] = (theta_limb4)*math.pi/180
            leg4[1] = (theta_leg4)*math.pi/180

            rospy.loginfo("\ntheta_base = %f\ntheta_shoulder = %f\ntheta_elbow = %f", limb4[0], leg4[1])
            theta_limb4.publish(limb4[0])
            theta_limb4.publish(leg4[1])
            print ("=========================\n")

    final_transformation_matrix = forward_kinematics_module.compute_coordinates(theta, d, alpha, a)
    

if __name__ == '__main__':
    try:
        forward_kinematics_publisher()
    except rospy.ROSInterruptException: 
        pass
