#!/usr/bin/env python  
import rospy

import math
import tf2_ros
import geometry_msgs.msg
import turtlesim.srv
import random

def spawneo(c):
    spawneador = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
    turtle_name = 'turtle' + str(c+1)
    spawneador(random.randint(0, 5), random.randint(0, 5), 0, turtle_name)
    turtles_names.append(turtle_name)
    buffers.append(tf2_ros.Buffer())
    listeners.append(tf2_ros.TransformListener(buffers[len(buffers)-1]))
    publishers.append(rospy.Publisher('%s/cmd_vel' % turtle_name, geometry_msgs.msg.Twist, queue_size=1))
    msg_list.append(geometry_msgs.msg.Twist())
    flags.append(False)

def rolling(p,c):

    #trans = buffers[0].lookup_transform_full(
               # target_frame=turtles_names[0],
               # target_time=rospy.Time.now(),
               # source_frame='carrot1',
               # source_time=p,
               # fixed_frame='world',
               # timeout=rospy.Duration(1.0)
               # )

    for i in range(c):
        transs.append(buffers[0].lookup_transform_full(
                    target_frame=turtles_names[i],
                    target_time=rospy.Time.now(),
                    source_frame='carrot1',
                    source_time=p,
                    fixed_frame='world',
                    timeout=rospy.Duration(float(c))))
                

    for i in range(c):
        x_pose = transs[i].transform.translation.x
        y_pose = transs[i].transform.translation.y

        if (math.sqrt(x_pose ** 2 + y_pose ** 2)) < 1:
            flags[i] = True

        if(flags[i]):    
            msg_list[i].angular.z = 6 * math.atan2(y_pose, x_pose)
            msg_list[i].linear.x = 2 * math.sqrt(x_pose ** 2 + y_pose ** 2)
        
    #turtle_vel.publish(msg)    
    for i in range(len(publishers)):
        publishers[i].publish(msg_list[i])


if __name__ == '__main__':

    rospy.init_node('tf2_turtle_listener')

    rate = rospy.Rate(10.0)
    
    flags = [False]

    antes = rospy.Time.now()

    counter = 1 #only one turtle at the beginning

    turtles_names = []

    buffers = []

    listeners = []

    transs = []

    publishers = []

    msg_list = []

    #tfBuffer = tf2_ros.Buffer()
    buffers.append(tf2_ros.Buffer())

    #listener = tf2_ros.TransformListener(tfBuffer)
    listeners.append(tf2_ros.TransformListener(buffers[0]))

    rospy.wait_for_service('spawn')
    spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
    turtles_names.append(rospy.get_param('turtle', 'turtle2'))
    spawner(4, 2, 0, turtles_names[0])

    #turtle_vel = rospy.Publisher('%s/cmd_vel' % turtles_names[0], geometry_msgs.msg.Twist, queue_size=1)
    publishers.append(rospy.Publisher('%s/cmd_vel' % turtles_names[0], geometry_msgs.msg.Twist, queue_size=1))
    msg_list.append(geometry_msgs.msg.Twist())

    

    while not rospy.is_shutdown():
        try:

            if(rospy.Time.now() - antes > rospy.Duration(10.0)):
                counter += 1
                spawneo(counter)
                antes = rospy.Time.now()
            
            past = rospy.Time.now() - rospy.Duration(1.0)

            rolling(past,counter)

        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            rate.sleep()
            continue

        rate.sleep()