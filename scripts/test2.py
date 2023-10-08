#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import PoseStamped, Pose, Point, Quaternion



if __name__ == '__main__':
    rospy.init_node("tb2/move_xy")
    pub = rospy.Publisher("tb2/move_base_simple/goal", PoseStamped, queue_size=10)


    x,y = (input("Enter X, Y coordinates: ")).split() #liest user input und teilt in x und y auf
    x = float(x)
    y = float(y)
    print(x,y)
    
    xy_goal = PoseStamped() 

    xy_goal.header.seq = 0
    xy_goal.header.frame_id = 'tb2/map'
    xy_goal.header.stamp = rospy.Time.now()
    xy_goal.pose = Pose(Point(x,y,0.0) , Quaternion(0,0,0,1))
    

    pub.publish(xy_goal)
    
    rospy.spin()