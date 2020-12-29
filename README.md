# spherical_bot
ROS package that simulates a spherical bot

# to achieve wifi connectivity between ROS and nodeMCU
1) Setup a wifi accesspoint / hotspot from your laptop.
2) Step modify the network details and burn the test.ino into the nodeMCU.
3) Get the IP address of the nodeMCU and modify it in test.py
4) run the following in different terminals
```sh
roscore
```
```sh
rosrun spherical_bot teleop.py
```
```sh
rorun spherical_bot test.py
```
