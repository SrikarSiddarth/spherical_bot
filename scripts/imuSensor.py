#! /usr/bin/env python
import rospy
from tf import transformations
from sensor_msgs.msg import Imu


def imu_cb(msg):
	quaternion = (
		msg.orientation.x,
		msg.orientation.y,
		msg.orientation.z,
		msg.orientation.w)
	euler = transformations.euler_from_quaternion(quaternion)
	print(euler)
	'''
		euler[0] gives the rotation in x axis which is parallel to the wheels
		euler[1] gives the rotation in y axis which is normal to the wheels
		euler[2] gives the yaw , that is its rotation wrt z axis
	'''

if __name__ == '__main__':
	rospy.init_node('imuSensor')
	sub = rospy.Subscriber('/imu',Imu,imu_cb)
	rospy.spin()
	# rate = rospy.Rate(30)
	# while not rospy.is_shutdown():
		