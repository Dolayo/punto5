#!/usr/bin/env python  
import rospy

import math
import tf2_ros
import geometry_msgs.msg
import turtlesim.srv
import random
from std_srvs.srv import Empty



def my_callback(event):

    global counter
    counter+=1

    spawner(random.randint(0,9), random.randint(0,9),0, turtle_names[counter-1])
    colorinchis = rospy.ServiceProxy(turtle_names[counter-1] + '/set_pen', turtlesim.srv.SetPen)
    colorinchis(255,0,0,3,0)
    return


if __name__ == '__main__':
    rospy.init_node('tf2_turtle_listener')

    tfBuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfBuffer)

    rospy.wait_for_service('spawn')
    spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)

    turtle_name = rospy.get_param('turtle', 'turtle2')
    turtle_name2 = rospy.get_param('turtle', 'turtle3')
    turtle_name3 = rospy.get_param('turtle', 'turtle4')
    turtle_name4 = rospy.get_param('turtle', 'turtle5')


    turtle_names = [turtle_name,turtle_name2,turtle_name3,turtle_name4]

    spawner(4, 2, 0, turtle_name)
    color = rospy.ServiceProxy('turtle1/set_pen', turtlesim.srv.SetPen)
    color(255,0,0,3,0)
    color2 = rospy.ServiceProxy('turtle2/set_pen', turtlesim.srv.SetPen)
    color2(255,0,0,3,0)

    

    

    turtle_vel = rospy.Publisher('%s/cmd_vel' % turtle_name, geometry_msgs.msg.Twist, queue_size=1)
    turtle_vel2 = rospy.Publisher('%s/cmd_vel' % turtle_name2, geometry_msgs.msg.Twist, queue_size=1)
    turtle_vel3 = rospy.Publisher('%s/cmd_vel' % turtle_name3, geometry_msgs.msg.Twist, queue_size=1)
    turtle_vel4 = rospy.Publisher('%s/cmd_vel' % turtle_name4, geometry_msgs.msg.Twist, queue_size=1)

    speed_l = 2
    speed_r = 5


    flag1 = False
    flag2 = False
    flag2b = False
    flag3 = False
    flag4 = False
    flag2c = True

    counter = 1

    my_timer = rospy.Timer(rospy.Duration(4), my_callback)

    #rospy.set_param('/background_b',0)
    #rospy.set_param('/background_r',255)
    #rospy.set_param('/background_g',255)
    #clearer = rospy.ServiceProxy('clear',Empty)
    #clearer() #no funciona, no se por que

    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        try:
            if(counter==4):
                rospy.Timer.shutdown(my_timer)

            trans = tfBuffer.lookup_transform(turtle_name, 'carrot1', rospy.Time())
            trans2 = tfBuffer.lookup_transform(turtle_name2, 'carrot2', rospy.Time())
            trans3 = tfBuffer.lookup_transform(turtle_name3, 'carrot3', rospy.Time())
            trans4 = tfBuffer.lookup_transform(turtle_name3, 'carrot3', rospy.Time())


        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            rate.sleep()
            continue

        msg = geometry_msgs.msg.Twist()

        x_pose1 = trans.transform.translation.x
        y_pose1 = trans.transform.translation.y

        if (math.sqrt(x_pose1 ** 2 + y_pose1 ** 2)) < 1:
            flag1 = True


        if (flag1):
            msg.angular.z = speed_r * math.atan2(y_pose1, x_pose1)
            msg.linear.x = speed_l * math.sqrt(x_pose1 ** 2 + y_pose1 ** 2)
            
        msg2 = geometry_msgs.msg.Twist()

        x_pose2 = trans2.transform.translation.x
        y_pose2 = trans2.transform.translation.y

        if (math.sqrt(x_pose2 ** 2 + y_pose2 ** 2)) < 1:
            flag2 = True

        if (flag2):
            msg2.angular.z = speed_r * math.atan2(y_pose2, x_pose2)
            msg2.linear.x = speed_l * math.sqrt(x_pose2 ** 2 + y_pose2 ** 2)

        
        msg3 = geometry_msgs.msg.Twist()

        x_pose3 = trans3.transform.translation.x
        y_pose3 = trans3.transform.translation.y

        if (math.sqrt(x_pose3 ** 2 + y_pose3 ** 2)) < 1:
            flag3 = True
            flag2b = True
    

        if (flag3):
            msg3.angular.z = speed_r * math.atan2(y_pose3, x_pose3)
            msg3.linear.x = speed_l * math.sqrt(x_pose3 ** 2 + y_pose3 ** 2)
        
        if (flag2b and flag2c):
            if ((math.sqrt(x_pose1 ** 2 + y_pose1 ** 2)) < 0.5):
    
                killer = rospy.ServiceProxy('kill', turtlesim.srv.Kill)
                killer('turtle3')
                killer('turtle4')
                flag2b = False
                flag2c = False

        msg4 = geometry_msgs.msg.Twist()

        x_pose4 = trans4.transform.translation.x
        y_pose4 = trans4.transform.translation.y

        if (math.sqrt(x_pose4 ** 2 + y_pose4 ** 2)) < 1:
            flag4 = True

        if (flag4):
            #msg4.angular.z = speed_r * math.atan2(y_pose4, x_pose4)
            #msg4.linear.x = speed_l * math.sqrt(x_pose4 ** 2 + y_pose4 ** 2)
            teleporter = rospy.ServiceProxy('turtle5/teleport_relative', turtlesim.srv.TeleportRelative)
            teleporter(3,0.7)
            flag4 = False


        
        turtle_vel.publish(msg)
        turtle_vel2.publish(msg2)
        turtle_vel3.publish(msg3)
        turtle_vel4.publish(msg4)
        


        rate.sleep()
