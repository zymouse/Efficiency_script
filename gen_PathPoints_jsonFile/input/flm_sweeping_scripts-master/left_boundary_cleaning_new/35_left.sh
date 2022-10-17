#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: 485.181274414
    y: -22.8851356506
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: -0.773157072114
    w: 0.634214586587
lane_driving_sweeping_mode: 4
free_space_sweeping_mode: 0
mission_order: 35"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 