#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: 394.649963379
    y: -114.681739807
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: 0.995966586469
    w: 0.089724905336
lane_driving_sweeping_mode: 3
free_space_sweeping_mode: 0
mission_order: 15"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 