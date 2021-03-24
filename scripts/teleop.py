#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
# from nav_msgs.msg import Odometry
from std_msgs.msg import UInt8, Float64
import numpy as np
import sys, select, termios, tty
msg = '''
Control Bot using 
		w
	a 		d
		s

 and b for brake
'''

def getKey():
	tty.setraw(sys.stdin.fileno())
	rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
	if rlist:
		key = sys.stdin.read(1)
	else:
		key = ''
	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
	return key



if __name__ == '__main__':
	rospy.init_node('mm_teleop')
	settings = termios.tcgetattr(sys.stdin)
	pub = rospy.Publisher('/hamster_bot/base_to_first_joint_position_controller/command', Float64, queue_size=10)
	pub2 = rospy.Publisher('/hamster_bot/base_to_second_joint_position_controller/command', Float64, queue_size=10)

	# pub1 = rospy.Publisher('key',UInt8,queue_size=20)
	# vmax = 0.4
	# amax = 0.1
	try:
		print(msg)
		s = 20
		# speed_z = 0
		# speed_x = 0.0
		while(1):
			num = 0
			# cmd = Twist()
			key = getKey()
			speed_l = 0.0
			speed_r = 0.0
			if key=='w':
				speed_l = s
				speed_r = s
				# num = 1
				# pub1.publish(num)
			elif key=='b':
				speed_l = 0.0
				speed_r = 0.0
				# pub1.publish(num)
			elif key=='s':
				speed_l = -1*s
				speed_r = -1*s
				# num = 2
				# pub1.publish(num)
			elif key=='d':
				speed_l = -1*s
				speed_r = s
				# num = 3
				# pub1.publish(num)
			elif key=='a':
				speed_l = s
				speed_r = -1*s
				# num = 4
				# pub1.publish(num)
			elif (key == '\x03'):
				break
			# if speed_x>vmax:
			# 	speed_x = vmax
			# elif speed_x<-1*vmax:
			# 	speed_x = -1*vmax
			# if speed_z>amax:
			# 	speed_z = amax
			# elif speed_z<-1*amax:
			# 	speed_z = -1*amax
			# cmd.linear.x = speed_x
			# cmd.angular.z = speed_z
			pub.publish(speed_r)
			pub2.publish(speed_l)


			
	except Exception as e:
		print(e)
	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)