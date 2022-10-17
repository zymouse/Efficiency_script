#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: 18.6484565735
    y: -46.8025398254
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: 0.995404340472
    w: 0.0957611558472
lane_driving_sweeping_mode: 3
free_space_sweeping_mode: 0
mission_order: 29"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 