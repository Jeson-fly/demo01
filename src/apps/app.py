#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Time     : 2023/3/5 9:56
  @Author   : lining
  @email    : 18810578664@163.com
  @des      : 
"""
from sanic import Sanic
from sanic import json
from views.author import AuthorHttpMethod

app = Sanic(name="my_dev")


@app.get("/index")
def index(request):
    return json({"key": "hello world"})


@app.get("/index_async")
async def index(request):
    return json({"key": "async hello world"})


# 监听器
@app.main_process_start
async def main_process_start(request):
    """主进程开启的动作"""


@app.main_process_stop
async def main_process_stop(request):
    """主进程结束"""


@app.before_server_start
async def before_server_start(request):
    """子进程开启动作"""


@app.after_server_start
async def after_server_start(request):
    """"""


@app.before_server_stop
async def before_server_stop(request):
    """"""


@app.after_server_stop
async def after_server_stop(request):
    """子进程结束后的动作"""


# 请求中间件
@app.on_request
async def before_request_handler(request):
    """"""


# 请求中间件
@app.middleware("request")
async def before_request_handler(request):
    """"""


app.add_route(AuthorHttpMethod.as_view(), "/author", version="/v1", )

if __name__ == '__main__':
    app.run(debug=True, auto_reload=True)
