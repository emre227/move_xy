#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import PoseStamped, Pose, Point, Quaternion


#def pose_msgs_constructor(x, y):
    
    #cons_msg = PoseStamped( 0 , Pose(Point(x,y,0.0) , Quaternion(0,0,0,1)) )
    #return cons_msg


if __name__ == '__main__':
    rospy.init_node("move_xy")
    pub = rospy.Publisher("/move_base_simple/goal", PoseStamped, queue_size=10)

    while not rospy.is_shutdown():
        x,y = (input("Enter X, Y coordinates: ")).split() #liest user input und teilt in x und y auf
        x = float(x)
        y = float(y)
        print(x,y)
    
        xy_goal = PoseStamped() 

        xy_goal.header.seq = 0
        xy_goal.header.frame_id = 'map'
        xy_goal.header.stamp = rospy.Time.now()
        xy_goal.pose = Pose(Point(x,y,0.0) , Quaternion(0,0,0,1))
    

        pub.publish(xy_goal)
    
   