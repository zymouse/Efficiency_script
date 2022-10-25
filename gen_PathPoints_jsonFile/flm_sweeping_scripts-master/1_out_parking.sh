#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: 223.105545044
    y: 109.348129272
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: -0.0873882243187
    w: 0.996174331255
lane_driving_sweeping_mode: 1
free_space_sweeping_mode: 8
mission_order: 1"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 