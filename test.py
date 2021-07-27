#!/usr/bin/python3
import os,sys
from aiohttp import web


_instance = None


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
    app.router.add_get('/api', hello)
    app.router.add_get('/api/m1', hello)
    app.router.add_get('/api/m2', hello)
    app.router.add_get('/api/m3', hello)
    app.router.add_get('/api/m4', hello)
    app.router.add_get('/api/m5', hello)

def app():
    global _instance
    _instance = web.Application(middlewares=[middleware1, middleware2])
    return _instance

def get_app():
    global _instance
    print(_instance)
    return _instance

def get_endpoints(path: str):
    app = get_app()
    print(app)
    endpoints = set()
    splitpaths = {}
    splitpaths = path.split("/")
    position = len(splitpaths)
    for route in app.router.resources():
        print(route)
        rest_route_path = route.url().split("/")
        # if len(rest_route_path) > position and path in route.url():
        #     endpoints.add(rest_route_path[position])
    return sorted(endpoints)


print(_instance)
print('Handler function called')

app = app()
app2 = get_app()
print(_instance)
print(app)
print(app2)

setup_routes(app)

web.run_app(app, host='127.0.0.1', port=8090)

test_str = get_endpoints("/api2")
print(test_str)
print('Handler function called')
