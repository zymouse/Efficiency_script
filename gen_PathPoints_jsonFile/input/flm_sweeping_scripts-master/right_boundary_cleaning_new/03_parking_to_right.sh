#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: 246.421661377
    y: 69.0346755981
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: -0.764584701021
    w: 0.644523261772
lane_driving_sweeping_mode: 2
free_space_sweeping_mode: 0
mission_order: 3"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 