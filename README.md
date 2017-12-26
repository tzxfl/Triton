# Triton
基于tushare完成的一个A股基本分析工具
安装过程
1、下载Nginx
2、安装python与pip
3、建立虚拟环境
```
    pip install virtualenv
    mkdir myproject
    cd myproject
    virtualenv venv
    激活虚拟环境
    venv\scripts\activate
```
4、安装flask
    pip install flask
5、安装tornado
    pip install tornado
    pip install pycurl
6、然后在创建tornado_server.py
7、配置nginx
```
 server {
        listen       80;
        server_name  www.xxx.com;

        charset utf-8;

        #access_log  logs/host.access.log  main;

        location / {
            proxy_pass         http://127.0.0.1:5000/;
            proxy_redirect     off;

            proxy_set_header   Host             $host;
            proxy_set_header   X-Real-IP        $remote_addr;
            proxy_set_header   X-Forwarded-For  $proxy_add_x_forwarded_for;
        }

        error_page  404              /404.html;

        # redirect server error pages to the static page /50x.html
        #
        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   html;
        }

    }

```
8、启动
```
Nginx.exe
python tornado_server.py
```
9、访问xxx.com即可