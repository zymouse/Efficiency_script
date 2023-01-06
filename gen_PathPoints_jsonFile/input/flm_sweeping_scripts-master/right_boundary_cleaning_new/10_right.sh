#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: 262.855651855
    y: 222.081512451
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: -0.0948559213943
    w: 0.9954910116
lane_driving_sweeping_mode: 3
free_space_sweeping_mode: 0
mission_order: 10"
 
rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 