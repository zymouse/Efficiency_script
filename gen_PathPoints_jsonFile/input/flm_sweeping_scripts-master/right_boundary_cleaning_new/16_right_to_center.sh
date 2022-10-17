#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: 209.057769775
    y: -85.006729126
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: 0.995724733
    w: 0.0923702121479
lane_driving_sweeping_mode: 3
free_space_sweeping_mode: 0
mission_order: 17"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 