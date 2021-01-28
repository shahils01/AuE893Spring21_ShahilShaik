import rospy
from geometry_msgs.msg import Twist
PI = 3.1415926535897

def move_squareopen():
	
	#start a new node
	rospy.init_node('robot_cleaner', anonymous=True)
	vel_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)
	vel_msg = Twist()
	
	print("Lets move the robot")
	#i = 0
	distance = 2
	angle = 90*2*PI/360
	
	for i in range(4):
	
		current_distance = 0
		current_angle = 0
		t0 = rospy.Time.now().to_sec()
		
		while(current_distance < distance):

			vel_msg.linear.x = 1
			vel_msg.angular.z = 0
			
			#publish the velocity
			vel_pub.publish(vel_msg)
			
			#Takes actual time to velocity calculus
			t1 = rospy.Time.now().to_sec()
			#Calculates distancePoseStamped
			current_distance = 1*(t1-t0)
			print(current_distance)
		
		else:
			vel_msg.linear.x = 0
			vel_pub.publish(vel_msg)
			
			while(current_angle < angle):
				print("2nd loop start")
				vel_msg.linear.x = 0
				vel_msg.angular.z = 0.2
				vel_pub.publish(vel_msg)
				t2 = rospy.Time.now().to_sec()
				current_angle = 0.2*(t2-t1)
				print("current angle:", current_angle)
			print("2nd loop end")
		vel_msg.angular.z = 0
		vel_pub.publish(vel_msg)
		current_distance = 0
		current_angle = 0
			
	#Forcing robot ot stop
	vel_msg.linear.x = 0
	vel_pub.publish(vel_msg)
	
if __name__ == '__main__':
	try:
		move_squareopen()
	except rospy.ROSInterruptException: pass
