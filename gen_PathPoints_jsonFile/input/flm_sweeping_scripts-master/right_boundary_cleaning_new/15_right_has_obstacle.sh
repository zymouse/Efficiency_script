#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: 243.045440674
    y: -85.467590332
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: 0.996389624372
    w: 0.0848982711526
lane_driving_sweeping_mode: 3
free_space_sweeping_mode: 0
mission_order: 16"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 