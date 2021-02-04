#!/usr/bin/env python
import rospy # Python library for ROS
from sensor_msgs.msg import LaserScan #import library for lidar sensor
from nav_msgs.msg import Odometry #import library for position and orientation data
from geometry_msgs.msg import Twist

class Circling(): #main class
   
    def __init__(self): #main function
        global circle
        circle = Twist() #create object of twist type  
        self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10) #publish message
        self.sub = rospy.Subscriber("/scan", LaserScan, self.callback) #subscribe message 
        self.sub = rospy.Subscriber("/odom", Odometry, self.odometry) #subscribe message

    def callback(self, msg): #function for obstacle avoidance
        #print ('-------RECEIVING LIDAR SENSOR DATA-------')
        #print ('Front: {}').format(msg.ranges[0]) #lidar data for front side
        #print ('Left:  {}').format(msg.ranges[90]) #lidar data for left side
        #print ('Right: {}').format(msg.ranges[270]) #lidar data for right side
        #print ('Back: {}').format(msg.ranges[180]) #lidar data for back side
      
      	#Obstacle Avoidance
        self.distance = 0.7
        if msg.ranges[0] > self.distance and msg.ranges[15] > self.distance and msg.ranges[345] > self.distance: 
        #when no any obstacle near detected
            circle.linear.x = 0.5 # go (linear velocity)
            rospy.loginfo("Moving") #state situation constantly
        else: #when an obstacle near detected
            rospy.loginfo("An Obstacle Detected") #state case of detection
            circle.linear.x = 0.0 # stop
        self.pub.publish(circle) # publish the move object

    def odometry(self, msg): #function for odometry
        print (msg.pose.pose) #print position and orientation of turtlebot

if __name__ == '__main__':
    rospy.init_node('obstacle_avoidance_node') #initilize node
    Circling() #run class
    rospy.spin() #loop it
