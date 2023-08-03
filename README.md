# 艺术二维码生成 API
-    https://api.zhishuyun.com/qrart/generate
-    艺术二维码是一种兼具实用性和艺术美感的二维码，本 API 提供了此类二维码的生成能力，可以通过输入绘制指令和二维码内容生成艺术二维码。

## 快速开始
====
- __步骤一：安装__

    Python3.7+ 
    ```bash
    git clone https://github.com/hbqjzx/qrcode.git
    ```
    ## cd qrcode
    
    ```bash
    python3 -m venv my_env
    source my_env/bin/activate
    pip3 install Flask requests jsonify  flask_bootstrap
    python app.py
    ```

- __步骤二：申请API__
    ```bash
    https://auth.zhishuyun.com/auth/login?inviter_id=b01a5684-a3e4-43d6-a7c1-61105ccf9a8c&redirect=https://data.zhishuyun.com/services/38ecf158-36f2-42f2-8e7f-6786cdfc2452
    ```
    申请免费试用的艺术二维码 API 次数，创建并复制好token，在下面测试备用
    
- __步骤三：测试__
    ## 本地测试
    http://127.0.0.1:8000 

    ## 在线测试网址
    ```bash
    http://qr.morecale.com
    ```

- __步骤四：开发应用__
    
    可利用该 API 接口开发微信小程序或在线网站生成艺术二维码。
    

## 作者

 weixin: mytimeruniu

## 其它
知数云智慧平台
## 声明
===
本项目仅用于交流学习
