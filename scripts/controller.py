#! /usr/bin/env python
'''
	This node takes information from the imu and sets the direction of the spherical bot.
'''

import rospy
from sensor_msgs.msg import Imu
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64
from tf import transformations
import numpy as np
import time
import math

class controller():
	def __init__(self):
		
		# self.cmd = Twist()
		self.sample_time = 0.033   #1/rate
		self.angles = [None]*3

		
		# print(goal_angle)
		self.last_yaw = None
		self.maxAnglularVel = 5
		self.Kp =  8     #5
		self.Ki =  0      #0
		self.Kd =  0      #0.5
		self.errSum = 0
		self.tolerance = 0.1
		self.lastTime = int(round(time.time()*1000))
		# self.direction = [1,0,3,2]					# means the angles are pi/2,0,-pi/2,pi
		self.key = 3
		self.flag = 0


		sub = rospy.Subscriber('/imu',Imu,self.imu_cb)
		# sub1 = rospy.Subscriber('/odom',Odometry,self.odom_cb)


		# self.pub_vel = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
		self.pub = rospy.Publisher('/hamster_bot/base_to_first_joint_position_controller/command', Float64, queue_size=10)
		self.pub2 = rospy.Publisher('/hamster_bot/base_to_second_joint_position_controller/command', Float64, queue_size=10)
		
		


	def imu_cb(self,msg):
		quaternion = (
		msg.orientation.x,
		msg.orientation.y,
		msg.orientation.z,
		msg.orientation.w)
		e = transformations.euler_from_quaternion(quaternion)
		# print(e[2])
		'''
			e[0] gives the rotation in x axis which is parallel to the wheels
			e[1] gives the rotation in y axis which is normal to the wheels
			e[2] gives the yaw , that is its rotation wrt z axis
		'''
		if self.angles[2]<np.pi and self.angles[2]>-np.pi*0.5:
			self.angles = [e[0],e[1],e[2]-np.pi*0.5]
			self.flag = 1
		else:
			self.angles = [e[0],e[1],e[2]+np.pi*1.5]
			self.flag = 2
		# self.angles = e

	def odom_cb(self,msg):
		pass

	def norm(self,angle):
		if(math.fabs(angle) > math.pi):
			angle = angle - (2 * math.pi * angle) / (math.fabs(angle))
		return angle

	def rotate(self):
		# print(abs(self.norm(goal_angle - self.angles[2])))
		
		if self.angles[2] is not None:
			self.goal_angle = self.norm(self.key*np.pi/2)
			self.last_yaw = self.angles[2]
			now = int(round(time.time()*1000))
			timeChange = now - self.lastTime
			if timeChange>=self.sample_time :
				error = self.norm(self.goal_angle - self.angles[2])
				
				if np.pi - abs(error)<self.tolerance:
					print('om')
					self.pub.publish(0)
					self.pub2.publish(0)
				else:
					self.errSum += error*timeChange*0.001
					dErr = (self.angles[2] - self.last_yaw)/(timeChange*0.01)
					out_error= self.Kp*error + self.Ki*self.errSum - self.Kd*dErr
					self.last_yaw = self.angles[2]
					if out_error>self.maxAnglularVel:
						out_error = self.maxAnglularVel
					elif out_error<-1*self.maxAnglularVel:
						out_error = -1*self.maxAnglularVel
						# self.cmd.angular.z = out_error
					# self.pub_vel.publish(self.cmd)
					self.pub.publish(out_error)
					self.pub2.publish(-1*out_error)
				print(self.flag,self.angles[2],self.goal_angle,error)

			self.lastTime = now
			



if __name__ == '__main__':
	rospy.init_node('controller')
	
	
	c = controller()
	r = rospy.Rate(30)
	while not rospy.is_shutdown():
	  c.rotate()
	  r.sleep()