#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: 465.611450195
    y: -110.367698669
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: -0.765474659067
    w: 0.643466041315
lane_driving_sweeping_mode: 3
free_space_sweeping_mode: 0
mission_order: 14"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 