#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: 18.9592952728
    y: -47.6741752625
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: 0.994492327942
    w: 0.104809396829
lane_driving_sweeping_mode: 3
free_space_sweeping_mode: 0
mission_order: 28"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 