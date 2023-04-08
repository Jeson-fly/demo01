#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Time     : 2023/3/5 10:33
  @Author   : lining
  @email    : 18810578664@163.com
  @des      : 
"""
from sanic.blueprints import Blueprint
from sanic import json

bp = Blueprint(name="bp1", url_prefix="/bp")


@bp.get("/index")
async def index(request):
    return json({"key": "bp1"})

