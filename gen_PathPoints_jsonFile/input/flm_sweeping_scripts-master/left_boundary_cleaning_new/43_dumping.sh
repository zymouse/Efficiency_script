#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: 208.844772339
    y: 104.432426453
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: 0.633961033485
    w: 0.773364990171
lane_driving_sweeping_mode: 1
free_space_sweeping_mode: 10
mission_order: 43"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 