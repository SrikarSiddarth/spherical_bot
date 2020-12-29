#! /usr/bin/env python
import rospy
import requests as req
from std_msgs.msg import UInt8
# import socket
url = 'http://10.42.0.11'
x = 1
# serverHost = 'localhost'
# serverPort = 80
# response = req.get(url)
# toSend = '2'
# response = req.post(url,params=toSend)
# print(response.status_code)     # To print http response code  
# print(response.text)            # To print formatted JSON response 
# print(response.json())
# r = response.json()
# print(r['age'])
def getKey(msg):
	global key, x, response, r
	x = 0
	key = str(msg.data)
	response = req.get(url,params=key)
	if response:
		r = response.json()
		print(r['age'])
	x = 1
	

if __name__ == '__main__':
	rospy.init_node('comm_mcu')
	r = rospy.Rate(30)
	sub = rospy.Subscriber('/key',UInt8,getKey)
	rospy.spin()
	# while not rospy.is_shutdown():
	# 	if x:
	# 		response = req.get(url)
			# print(response.status_code)
			# if response:
			# 	r = response.json()
