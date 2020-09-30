#!/usr/bin/env python  
import rospy

import math
import tf2_ros
import geometry_msgs.msg
import turtlesim.srv
import random

def my_callback(event):

    global counter
    counter+=1

    spawner(random.randint(0, 5), random.randint(0, 5), 0, turtle_names[counter])
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
    turtle_name5 = rospy.get_param('turtle', 'turtle6')
    turtle_name6 = rospy.get_param('turtle', 'turtle7')
    turtle_name7 = rospy.get_param('turtle', 'turtle8')
    turtle_name8 = rospy.get_param('turtle', 'turtle9')
    turtle_name9 = rospy.get_param('turtle', 'turtle10')

    turtle_names = [turtle_name,turtle_name2,turtle_name3,turtle_name4,turtle_name5,turtle_name6,turtle_name7,turtle_name8,turtle_name9]

    spawner(4, 2, 0, turtle_name)
    
    

    turtle_vel = rospy.Publisher('%s/cmd_vel' % turtle_name, geometry_msgs.msg.Twist, queue_size=1)
    turtle_vel2 = rospy.Publisher('%s/cmd_vel' % turtle_name2, geometry_msgs.msg.Twist, queue_size=1)
    turtle_vel3 = rospy.Publisher('%s/cmd_vel' % turtle_name3, geometry_msgs.msg.Twist, queue_size=1)
    turtle_vel4 = rospy.Publisher('%s/cmd_vel' % turtle_name4, geometry_msgs.msg.Twist, queue_size=1)
    turtle_vel5 = rospy.Publisher('%s/cmd_vel' % turtle_name5, geometry_msgs.msg.Twist, queue_size=1)
    turtle_vel6 = rospy.Publisher('%s/cmd_vel' % turtle_name6, geometry_msgs.msg.Twist, queue_size=1)
    turtle_vel7 = rospy.Publisher('%s/cmd_vel' % turtle_name7, geometry_msgs.msg.Twist, queue_size=1)
    turtle_vel8 = rospy.Publisher('%s/cmd_vel' % turtle_name8, geometry_msgs.msg.Twist, queue_size=1)
    turtle_vel9 = rospy.Publisher('%s/cmd_vel' % turtle_name9, geometry_msgs.msg.Twist, queue_size=1)



    flag1 = False
    flag2 = False
    flag3 = False
    flag4 = False
    flag5 = False
    flag6 = False
    flag7 = False
    flag8 = False
    flag9 = False
    counter = 1
    #antes = rospy.Time.now()

    rospy.Timer(rospy.Duration(4), my_callback)
    if(counter==9):
        rospy.Timer.shutdown()



    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        try:

            #if((rospy.Time.now() - antes > 2.0) and flag3):
                #spawner(2, 4, 0, turtle_name2)
                #antes = rospy.Time.now()
                #flag3 = False
            
            #past = rospy.Time.now() - rospy.Duration(1.0)#aqui por el tiempo que vaya por detras

            trans = tfBuffer.lookup_transform(turtle_name, 'carrot1', rospy.Time())
            trans2 = tfBuffer.lookup_transform(turtle_name2, 'carrot2', rospy.Time())
            trans3 = tfBuffer.lookup_transform(turtle_name3, 'carrot3', rospy.Time())
            trans4 = tfBuffer.lookup_transform(turtle_name4, 'carrot4', rospy.Time())
            trans5 = tfBuffer.lookup_transform(turtle_name5, 'carrot5', rospy.Time())
            trans6 = tfBuffer.lookup_transform(turtle_name6, 'carrot6', rospy.Time())
            trans7 = tfBuffer.lookup_transform(turtle_name7, 'carrot7', rospy.Time())
            trans8 = tfBuffer.lookup_transform(turtle_name8, 'carrot8', rospy.Time())
            trans9 = tfBuffer.lookup_transform(turtle_name9, 'carrot9', rospy.Time())

        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            rate.sleep()
            continue

        msg = geometry_msgs.msg.Twist()

        x_pose = trans.transform.translation.x
        y_pose = trans.transform.translation.y

        if (math.sqrt(x_pose ** 2 + y_pose ** 2)) < 1:
            flag1 = True

        if (flag1):
            msg.angular.z = 4 * math.atan2(y_pose, x_pose)
            msg.linear.x = 0.5 * math.sqrt(x_pose ** 2 + y_pose ** 2)

        msg2 = geometry_msgs.msg.Twist()

        x_pose = trans2.transform.translation.x
        y_pose = trans2.transform.translation.y

        if (math.sqrt(x_pose ** 2 + y_pose ** 2)) < 1:
            flag2 = True

        if (flag2):
            msg2.angular.z = 6 * math.atan2(y_pose, x_pose)
            msg2.linear.x = 3 * math.sqrt(x_pose ** 2 + y_pose ** 2)
        
        msg3 = geometry_msgs.msg.Twist()

        x_pose = trans3.transform.translation.x
        y_pose = trans3.transform.translation.y

        if (math.sqrt(x_pose ** 2 + y_pose ** 2)) < 1:
            flag3 = True

        if (flag3):
            msg3.angular.z = 6 * math.atan2(y_pose, x_pose)
            msg3.linear.x = 3 * math.sqrt(x_pose ** 2 + y_pose ** 2)

        msg4 = geometry_msgs.msg.Twist()

        x_pose = trans4.transform.translation.x
        y_pose = trans4.transform.translation.y

        if (math.sqrt(x_pose ** 2 + y_pose ** 2)) < 1:
            flag4 = True

        if (flag4):
            msg4.angular.z = 6 * math.atan2(y_pose, x_pose)
            msg4.linear.x = 3 * math.sqrt(x_pose ** 2 + y_pose ** 2)

        msg5 = geometry_msgs.msg.Twist()

        x_pose = trans5.transform.translation.x
        y_pose = trans5.transform.translation.y

        if (math.sqrt(x_pose ** 2 + y_pose ** 2)) < 1:
            flag5 = True

        if (flag5):
            msg5.angular.z = 6 * math.atan2(y_pose, x_pose)
            msg5.linear.x = 3 * math.sqrt(x_pose ** 2 + y_pose ** 2)

        msg6 = geometry_msgs.msg.Twist()

        x_pose = trans6.transform.translation.x
        y_pose = trans6.transform.translation.y

        if (math.sqrt(x_pose ** 2 + y_pose ** 2)) < 1:
            flag6 = True

        if (flag6):
            msg6.angular.z = 6 * math.atan2(y_pose, x_pose)
            msg6.linear.x = 3 * math.sqrt(x_pose ** 2 + y_pose ** 2)

        msg7 = geometry_msgs.msg.Twist()

        x_pose = trans7.transform.translation.x
        y_pose = trans7.transform.translation.y

        if (math.sqrt(x_pose ** 2 + y_pose ** 2)) < 1:
            flag7 = True

        if (flag7):
            msg7.angular.z = 6 * math.atan2(y_pose, x_pose)
            msg7.linear.x = 3 * math.sqrt(x_pose ** 2 + y_pose ** 2)

        msg8 = geometry_msgs.msg.Twist()

        x_pose = trans8.transform.translation.x
        y_pose = trans8.transform.translation.y

        if (math.sqrt(x_pose ** 2 + y_pose ** 2)) < 1:
            flag8 = True

        if (flag4):
            msg8.angular.z = 6 * math.atan2(y_pose, x_pose)
            msg8.linear.x = 3 * math.sqrt(x_pose ** 2 + y_pose ** 2)

        msg9 = geometry_msgs.msg.Twist()

        x_pose = trans9.transform.translation.x
        y_pose = trans9.transform.translation.y

        if (math.sqrt(x_pose ** 2 + y_pose ** 2)) < 1:
            flag9 = True

        if (flag9):
            msg9.angular.z = 6 * math.atan2(y_pose, x_pose)
            msg9.linear.x = 3 * math.sqrt(x_pose ** 2 + y_pose ** 2)



        
        turtle_vel.publish(msg)
        turtle_vel2.publish(msg2)
        turtle_vel3.publish(msg3)
        turtle_vel4.publish(msg4)
        turtle_vel5.publish(msg5)
        turtle_vel6.publish(msg6)
        turtle_vel7.publish(msg7)
        turtle_vel8.publish(msg8)
        turtle_vel9.publish(msg9)

        rate.sleep()
