# Spherical Bot
## The Institution of Engineers, NITK Chapter
ROS package that simulates a spherical bot

# to start the simulation
```sh
roscore
```
```sh
roslaunch spherical_bot bot.launch
```
```sh
rosrun spherical_bot teleop.py
```
# to achieve wifi connectivity between ROS and nodeMCU
1) Setup a wifi accesspoint / hotspot from your laptop.
2) Step modify the network details and burn the test.ino into the nodeMCU.
3) Get the IP address of the nodeMCU and modify it in test.py
4) run the following
```sh
rosrun spherical_bot test.py
```
ros tutorials : http://wiki.ros.org/ROS/Tutorials
