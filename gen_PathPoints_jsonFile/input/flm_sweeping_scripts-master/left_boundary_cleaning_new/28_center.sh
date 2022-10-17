#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: 195.061950684
    y: -81.2122192383
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: 0.994178587251
    w: 0.107744775518
lane_driving_sweeping_mode: 4
free_space_sweeping_mode: 0
mission_order: 28"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 