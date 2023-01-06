#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: -5.63780784607
    y: -11.9293937683
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: 0.636143457709
    w: 0.771570801167
lane_driving_sweeping_mode: 2
free_space_sweeping_mode: 0
mission_order: 30"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 