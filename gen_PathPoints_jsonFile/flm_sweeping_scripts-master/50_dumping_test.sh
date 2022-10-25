#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: 211.284378052
    y: 103.658149719
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: 0.629103642962
    w: 0.777321430563
lane_driving_sweeping_mode: 1
free_space_sweeping_mode: 10
mission_order: 50"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 
