#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: 213.629598029
    y: 102.864852047
    z: -1.26940822601
  orientation: 
    x: 0.00585238196426
    y: -0.00369484945178
    z: 0.625935588386
    w: 0.779844046528
lane_driving_sweeping_mode: 1
free_space_sweeping_mode: 9
mission_order: 44"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 