# Raspberry-Pi-Monitor
工程打造了一款画面可视；实时遥控；操作界面可视化；操作平台多元化；外网远程控制；成本可接受的网络监控。<br/><br/>
 - [X]  【树莓派-网络监控（1）分析准备】[基于树莓派搭建可视化可远程遥控网络监控——工程分析及前期准备](https://blog.csdn.net/deng_xj/article/details/98464826)
 - [X] 【树莓派-网络监控（2）画面传输】[基于mjpg-stream实现监控画面的传输](https://blog.csdn.net/deng_xj/article/details/98487595)
 - [X] 【树莓派-网络监控（3）角度遥控】[基于python3控制两自由度舵机，实现摄像头拍摄角度的遥控](https://blog.csdn.net/deng_xj/article/details/98620290)
 - [X] 【树莓派-网络监控（4）数据交互】[基于python异步io框架Tornado,实现监控遥控命令与Web网页触发事件的绑定及前后端的数据交互](https://dengxj.blog.csdn.net/article/details/98736117)
 - [X] 【树莓派-网络监控（5）前端搭建】[基于iframe标签,集成监控实时画面与遥控功能，完成网络监控的搭建与调试](https://blog.csdn.net/deng_xj/article/details/98871101)
 - [X] 【树莓派-网络监控（6）远程访问】[基于内网穿透实现树莓派监控的公网远程访问与遥控](https://blog.csdn.net/deng_xj/article/details/99211554)
<br/><br/>
文件结构：

```
/home/pi
│ 
└── 111
    ├── index.html
    ├── index.py
    ├── steering.py
    └── static
        ├── css
        │   ├── bootstrap.min.css
        │   └── style.css
        │
        ├── js
        │   ├── bootstrap.min.js
        │   └── functions.js
        │   └── jquery.min.js
        │
        └── img
            ├── skin-blue.jpg
            ├── skin-chrome.jpg
            ├── skin-city.jpg
            ├── skin-cloth.jpg
            ├── skin-greenish.jpg
            ├── skin-kiwi.jpg
            ├── skin-lights.jpg
            ├── skin-night.jpg
            ├── skin-ocean.jpg
            ├── skin-sunny.jpg
            ├── skin-sunset.jpg
            ├── skin-tectile.jpg
            ├── skin-violate.jpg
            ├── skin-yellow.jpg
            │
            ├── icon
            │   └── search.png
            │
            └── body
                └── blue.jpg
                └── chrome.jpg
                └── city.jpg
                └── cloth.jpg
                └── greenish.jpg
                └── kiwi.jpg
                └── night.jpg
                └── lights.jpg
                └── ocean.jpg
                └── sunny.jpg
 				           └── sunset.jpg
                └── tectile.jpg
                └── violate.jpg
                └── yellow.jpg
```

