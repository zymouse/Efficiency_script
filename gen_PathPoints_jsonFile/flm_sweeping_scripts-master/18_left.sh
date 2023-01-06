#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: 34.5584793091
    y: -51.2854652405
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: 0.995003988744
    w: 0.0998351760825
lane_driving_sweeping_mode: 4
free_space_sweeping_mode: 0
mission_order: 18"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 