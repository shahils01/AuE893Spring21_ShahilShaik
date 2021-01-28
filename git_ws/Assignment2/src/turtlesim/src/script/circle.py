import rospy
from geometry_msgs.msg import Twist
PI = 3.1415926535897

def move_circle():

    #Starts a new node
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    # Receiveing the user's input
    print("Let's move your robot")
    speed = float(input("Input your speed (degrees/sec):"))
    angle = float(input("Type your distance (degrees):"))
    time = float(input("movement duration: "))
    clockwise = input("Clowkise?: ") #True or false

    #We wont use linear components
    vel_msg.linear.x = speed

    # Checking if our movement is CW or CCW
    if clockwise:
        vel_msg.angular.z = -abs(angle)
    else:
        vel_msg.angular.z = abs(angle)
    
    now = rospy.Time.now()

     # For the next 6 seconds publish cmd_vel move commands to Turtlesim
    while rospy.Time.now() < now + rospy.Duration.from_sec(time):
        velocity_publisher.publish(vel_msg)

    #Forcing our robot to stop
    vel_msg.angular.z = 0
    vel_msg.linear.x = 0
    velocity_publisher.publish(vel_msg)
    rospy.spin()

if __name__ == '__main__':
    try:
        # Testing our function
        move_circle()
    except rospy.ROSInterruptException:
        pass

