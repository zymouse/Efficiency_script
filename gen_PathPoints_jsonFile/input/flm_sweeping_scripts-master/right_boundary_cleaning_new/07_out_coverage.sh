#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: -2.10937547684
    y: -17.9534454346
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: 0.646431602014
    w: 0.762971941763
lane_driving_sweeping_mode: 1
free_space_sweeping_mode: 8
mission_order: 7"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 