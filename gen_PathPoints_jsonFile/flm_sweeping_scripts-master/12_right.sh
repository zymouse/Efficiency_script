#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: 490.024536133
    y: 16.7386894226
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: -0.768754379457
    w: 0.6395441377
lane_driving_sweeping_mode: 3
free_space_sweeping_mode: 0
mission_order: 12"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 