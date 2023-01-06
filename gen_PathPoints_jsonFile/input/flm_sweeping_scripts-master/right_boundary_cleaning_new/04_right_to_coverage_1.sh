#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: -4.34990692139
    y: -34.2332992554
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: 0.895301412974
    w: 0.445460862397
lane_driving_sweeping_mode: 3
free_space_sweeping_mode: 0
mission_order: 4"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 