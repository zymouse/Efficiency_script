#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: -4.45888137817
    y: -14.088435173
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: 0.615422373158
    w: 0.78819750229
lane_driving_sweeping_mode: 2
free_space_sweeping_mode: 0
mission_order: 29"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 