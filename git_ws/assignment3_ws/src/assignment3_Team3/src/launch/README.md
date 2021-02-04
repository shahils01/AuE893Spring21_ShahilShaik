For the first part of the assignment, we will need to run "move.launch" which is a launch file.
This file takes an input command to determine which code it needs to run.
The input is stored in the variable "code"
After building the package using "catkin_make" and sourcing the package, we need to export the turtlebot using "export TURTLEBOT3_MODEL=burger"
We can then used the following commands to move the Turtlebot:
	- command for "circle": "roslaunch assignment3_Team3 move.py code:=circle"
	- command for "squre": "roslaunch assignment3_Team3 move.py code:=square"
