#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: 471.615234375
    y: -115.447975159
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: -0.774056852623
    w: 0.633116094336
lane_driving_sweeping_mode: 4
free_space_sweeping_mode: 0
mission_order: 25"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 