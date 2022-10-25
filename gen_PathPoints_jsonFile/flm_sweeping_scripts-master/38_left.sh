#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: 209.22215271
    y: -80.9563598633
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: 0.999482543725
    w: 0.0321658948002
lane_driving_sweeping_mode: 4
free_space_sweeping_mode: 0
mission_order: 38"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 