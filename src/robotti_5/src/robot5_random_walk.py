#! /usr/bin/python3

import rospy, random
from std_msgs.msg import Float64
from nav_msgs.msg import Odometry

def callback(data):
    vel_l_msg = Float64()
    vel_r_msg = Float64()
    vel_bl_msg = Float64()
    vel_br_msg = Float64()
    vel_fl_msg = Float64()
    vel_fr_msg = Float64()
    position_x = data.pose.pose.position.x
    position_y = data.pose.pose.position.y
    if position_x < 0.5:
        velocity_l = -10
        velocity_r = -3
        velocity_bl = 10
        velocity_br = -3
        velocity_fl = 10
        velocity_fr = -3
    elif position_y < 0.5:
        velocity_l = -10
        velocity_r = -3
        velocity_bl = 10
        velocity_br = -3
        velocity_fl = 10
        velocity_fr = -3
    elif position_x > 2.5:
        velocity_l = -3
        velocity_r = -10
        velocity_bl = -3
        velocity_br = -10
        velocity_fl = -3
        velocity_fr = -10
    elif position_y > 2.5:
        velocity_l = -3
        velocity_r = -10
        velocity_bl = -3
        velocity_br = 10
        velocity_fl = -3
        velocity_fr = 10
    else:
        velocity_l = random.uniform(-0.1,-10)
        velocity_r = random.uniform(-0.1,-10)
        velocity_bl = random.uniform(-0.1,-10)
        velocity_br = random.uniform(-0.1,-10)
        velocity_fl = random.uniform(-0.1,-10)
        velocity_fr = random.uniform(-0.1,-10)

    vel_l_msg.data = velocity_l
    vel_r_msg.data = velocity_r
    vel_bl_msg.data = velocity_bl
    vel_br_msg.data = velocity_br
    vel_fl_msg.data = velocity_fl
    vel_fr_msg.data = velocity_fr
    velocity_l_publisher.publish(vel_l_msg)
    velocity_r_publisher.publish(vel_r_msg)
    velocity_bl_publisher.publish(vel_bl_msg)
    velocity_br_publisher.publish(vel_br_msg)
    velocity_fl_publisher.publish(vel_fl_msg)
    velocity_fr_publisher.publish(vel_fr_msg)



if __name__ == "__main__":
    while not rospy.is_shutdown():
        rospy.init_node("robot5_random_walk")
        velocity_l_publisher = rospy.Publisher('/robot5/wheel_l_velocity_controller/command',Float64,queue_size=1)
        velocity_r_publisher = rospy.Publisher('/robot5/wheel_r_velocity_controller/command',Float64,queue_size=1)
        velocity_bl_publisher = rospy.Publisher('/robot5/wheel_bl_velocity_controller/command',Float64,queue_size=1)
        velocity_br_publisher = rospy.Publisher('/robot5/wheel_br_velocity_controller/command',Float64,queue_size=1)
        velocity_fl_publisher = rospy.Publisher('/robot5/wheel_fl_velocity_controller/command',Float64,queue_size=1)
        velocity_fr_publisher = rospy.Publisher('/robot5/wheel_fr_velocity_controller/command',Float64,queue_size=1)
        rospy.Subscriber("/robot5/odom", Odometry, callback)
        rospy.spin()