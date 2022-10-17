#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: -8.14317131042
    y: -33.8598899841
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: 0.795631311361
    w: 0.605781162122
lane_driving_sweeping_mode: 2
free_space_sweeping_mode: 0
mission_order: 18"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 