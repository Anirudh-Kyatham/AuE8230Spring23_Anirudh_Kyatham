#!/usr/bin/python3.8

import rospy
from geometry_msgs.msg import Twist

def circle():
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('circle_motion', anonymous=True)
    rate = rospy.Rate(10) # 10Hz
    vel_msg = Twist()

    vel_msg.linear.x = 5
    vel_msg.angular.z = 5

    while not rospy.is_shutdown():
        pub.publish(vel_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        circle()
    except rospy.ROSInterruptException:
        pass