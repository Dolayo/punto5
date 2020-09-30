#!/usr/bin/env python  
import rospy

import math
import tf2_ros
import geometry_msgs.msg
import turtlesim.srv

def my_callback(event):
    global flag3 
    flag3 = False
    print(flag3, 'HE ENTRADOOOOOOOOOOO')
    spawner(2, 4, 0, turtle_name2)
    return



if __name__ == '__main__':
    rospy.init_node('tf2_turtle_listener')

    tfBuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfBuffer)

    rospy.wait_for_service('spawn')
    spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
    turtle_name = rospy.get_param('turtle', 'turtle2')
    turtle_name2 = rospy.get_param('turtle', 'turtle3')
    spawner(4, 2, 0, turtle_name)
    
    

    turtle_vel = rospy.Publisher('%s/cmd_vel' % turtle_name, geometry_msgs.msg.Twist, queue_size=1)
    turtle_vel2 = rospy.Publisher('%s/cmd_vel' % turtle_name2, geometry_msgs.msg.Twist, queue_size=1)


    flag1 = False
    flag2 = False
    flag3 = True
    #antes = rospy.Time.now()
    if(flag3):
        rospy.Timer(rospy.Duration(4), my_callback,oneshot=True ,reset=True)
        print(flag3)

    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        try:

            #if((rospy.Time.now() - antes > 2.0) and flag3):
                #spawner(2, 4, 0, turtle_name2)
                #antes = rospy.Time.now()
                #flag3 = False
            
            print('estoy rn rl LOOOOOOP', flag3)
            past = rospy.Time.now() - rospy.Duration(1.0)#aqui por el tiempo que vaya por detras
            trans = tfBuffer.lookup_transform(turtle_name, 'carrot1', rospy.Time())
            trans2 = tfBuffer.lookup_transform(turtle_name2, 'carrot2', rospy.Time())
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
            msg2.angular.z = 6 * math.atan2(trans2.transform.translation.y, trans2.transform.translation.x)
            msg2.linear.x = 3 * math.sqrt(trans2.transform.translation.x ** 2 + trans2.transform.translation.y ** 2)

        
        turtle_vel.publish(msg)
        #turtle_vel = rospy.Publisher('%s/cmd_vel' % turtle_name, geometry_msgs.msg.Twist, queue_size=1)
        turtle_vel2.publish(msg2)

        rate.sleep()
