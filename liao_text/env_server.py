#从wsgiref模块导入：
from wsgiref.simple_server import make_server
#导入自己的applicaiton函数：
from hello_app import application

#创服务器，IP地址为空端口8000，处理函数是application:
httpd = make_server('', 8000,application)
print('Serving HTTP on port 8000...')
#开始监听HTTP请求：
httpd.serve_forever()