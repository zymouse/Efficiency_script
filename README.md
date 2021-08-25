# Efficiency_script
# 这是一个提升工作效率的脚本
## 包含功能：
```
1.0 超声波雷达触发ros程序
2.0 ouster雷达自动固化ip脚本
```
## 1.0 ouster雷达自动固化ip脚本使用教程
#### 1.1 设置工控机ip为自动获取
![image](https://user-images.githubusercontent.com/46778435/130753680-53a5078d-d7d5-4d2f-92d4-f824a9d7aaac.png)
#### 1.2 设置完成后，检测，是否自动获取到ip
![image](https://user-images.githubusercontent.com/46778435/130753801-21d6dfd1-11cc-4e9e-8785-f2890f22d965.png)
#### 1.3 启动脚本开始修改
```
# <ipv4> 为想要设置的ip地址
# 不填写 <ipv4>，则是把ouster设置成默认的ip(192.168.1.110)
$ python3 update_ipv4.py <ipv4>
```
#### 1.4 检测是否设置成功
```
# 我把雷达ip设置为 192.168.1.110
$  ping 192.168.1.110
```
