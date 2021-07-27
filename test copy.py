#!/usr/bin/python3
import os,sys
from aiohttp import web

async def test(request):
    print('Handler function called')
    return web.Response(text="Hello")

@web.middleware
async def middleware1(request, handler):
    print('Middleware 1 called')
    response = await handler(request)
    print('Middleware 1 finished')
    return response

@web.middleware
async def middleware2(request, handler):
    print('Middleware 2 called')
    response = await handler(request)
    print('Middleware 2 finished')
    return response
async def hello(request):
    return web.Response(text='Hello Aiohttp!')

def setup_routes(app):
    app.router.add_get('/hello', hello)

print('Handler function called')
app = web.Application(middlewares=[middleware1, middleware2])
# app = web.Application()
print(app)
setup_routes(app)
# app.router.add_get('/', test)
# web.run_app(app)
web.run_app(app, host='127.0.0.1', port=8070)