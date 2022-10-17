#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: 200.53666687
    y: -78.2764129639
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: 0.98435844345
    w: 0.17617733909
lane_driving_sweeping_mode: 2
free_space_sweeping_mode: 0
mission_order: 38"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 