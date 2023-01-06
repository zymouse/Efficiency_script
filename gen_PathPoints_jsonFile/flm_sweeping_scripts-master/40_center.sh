#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: -2.80240535736
    y: -17.253868103
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: 0.647646826636
    w: 0.761940672197
lane_driving_sweeping_mode: 2
free_space_sweeping_mode: 0
mission_order: 40"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 