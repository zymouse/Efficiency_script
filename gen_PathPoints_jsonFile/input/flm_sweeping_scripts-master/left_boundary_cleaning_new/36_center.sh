#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: 464.401977539
    y: -26.9041023254
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: 0.995161950407
    w: 0.0982481168383
lane_driving_sweeping_mode: 2
free_space_sweeping_mode: 0
mission_order: 36"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 