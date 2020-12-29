#! /usr/bin/env python
import rospy
import requests as req
# import socket
url = 'http://10.42.0.11'
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
	response = req.post(url,params=key)
	r = response.json()
	x = 1

if __name__ == '__main__':
	rospy.init_node('comm_mcu')
	r = rospy.Rate(30)
	sub = rospy.Subscriber('/key',UInt8,getKey)
	while not rospy.is_shutdown():
		if x:
			response = req.post(url)
			r = response.json()
