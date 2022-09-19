### 在日常生活中，录制ros-bag包，静态TF录制不下来的原因。这是应该专门静态坐标发布生成器，生成`.launch`文件来发布
## 1.0 依赖
```
ros melodic
sudo apt install libignition-math2
```
## 2.0 使用方法：
```
填写`input/config.ini`,把父子坐标名字填写进去，需要多对就填写对多
```

## 3.0 测试
```
rosrun tf static_transform_publisher  1  2  3   0  0 0 a1 b1 10
./g_TF_Static.py

```
