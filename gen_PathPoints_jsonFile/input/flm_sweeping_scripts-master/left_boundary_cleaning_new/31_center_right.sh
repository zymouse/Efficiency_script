#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: 24.1874465942
    y: 133.975875854
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: 0.622516182849
    w: 0.782606926938
lane_driving_sweeping_mode: 3
free_space_sweeping_mode: 0
mission_order: 31"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 