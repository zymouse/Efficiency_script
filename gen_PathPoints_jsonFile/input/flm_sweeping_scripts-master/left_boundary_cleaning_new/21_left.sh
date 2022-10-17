#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: 18.9845561981
    y: 123.387496948
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: 0.629492984189
    w: 0.77700616655
lane_driving_sweeping_mode: 4
free_space_sweeping_mode: 0
mission_order: 21"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 