# 建图需要的topic开启与录制
#!/bin/bash
rosbag record --split --size=2048 --buffsize=1024 $(cat ./buildingMapTopics.txt)