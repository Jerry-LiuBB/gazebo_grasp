#! /usr/bin/env python
import sys
import rospy
import moveit_commander
import geometry_msgs
import tf
 
# 
moveit_commander.roscpp_initializer.roscpp_initialize(sys.argv)
rospy.init_node('move_group_grasp', anonymous=True)
robot = moveit_commander.robot.RobotCommander()
 
arm_group = moveit_commander.move_group.MoveGroupCommander("arm")
hand_group = moveit_commander.move_group.MoveGroupCommander("hand")
 
# #hand_group.set_named_target("close")
# #plan = hand_group.go()
 
hand_group.set_joint_value_target([0, 0, 0, 0, 0, 0,0, 0, 0.3, -0.799, 0, 0])

hand_group.go(wait=True)
 
arm_group.set_named_target("grasp1")
plan = arm_group.go()
 
print("Point 1")
 

 
arm_group.set_named_target("grasp2")
plan = arm_group.go()
 
print("Point 2")

# # Open
hand_group.set_joint_value_target([0, 0, 0, 0, 0, 0,0, 0, -0.705, -0.799, 0, 0])

hand_group.go(wait=True)
# #print("Point 2")
# hand_group.set_named_target("grip")
# plan = hand_group.go()
# print("Point 2")
hand_group.set_joint_value_target([-0.63, -0.67, -0.636, -0.676, -0.641, -0.69, -0.645, -0.69, -0.7, -0.73, -0.2,-0.8])

hand_group.go(wait=True) 


arm_group.set_joint_value_target([0, 0, 0, 0, 0, 0])

arm_group.go(wait=True)
 
# pose_target = arm_group.get_current_pose().pose
 
# # Block point
# pose_target.position.x = 0.35
# pose_target.position.y = -0.7
# pose_target.position.z = 0.8
 
 
 
# arm_group.set_pose_target(pose_target)
# arm_group.go(wait=True)
# print("Point 3")
 
# # Block point
# pose_target.position.x = 0.69
# pose_target.position.y = 0.0
# pose_target.position.z = pose_target.position.z-0.23
 
 
 
# arm_group.set_pose_target(pose_target)
# arm_group.go(wait=True)
# print("Point 4")
 
 
# hand_group.set_named_target("close")
# plan = hand_group.go()
# print("Point 5")
 
# pose_target.position.z = pose_target.position.z+0.1
# arm_group.set_pose_target(pose_target)
# plan = arm_group.go()
# print("Point 6")
 
 
# pose_target.position.z = pose_target.position.z
# pose_target.position.x = 1.0
# arm_group.set_pose_target(pose_target)
# plan = arm_group.go()
# print("Point 7")
 
 
 
# hand_group.set_named_target("open")
# plan = hand_group.go()
# print("Point 8")
 
moveit_commander.roscpp_initializer.roscpp_shutdown()
