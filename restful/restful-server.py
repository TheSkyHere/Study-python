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
async def response1(request):
    return web.Response(text='Hello this /api!')
async def response2(request):
    return web.Response(text='Hello this /api/m1!')
async def response3(request):
    return web.Response(text='Hello this /api/m2!')
async def response4(request):
    return web.Response(text='Hello this /api/m3!')
async def response5(request):
    return web.Response(text='Hello this /api/m4!')
async def response6(request):
    return web.Response(text='Hello this /api/m5!')
async def response7(request):
    return web.Response(text='Hello this /api/m5/1!')
async def response8(request):
    return web.Response(text='Hello this /api/m5/1!')
async def response9(request):

    return web.Response(text='Hello this /api/m5/1!')

def setup_routes(app):
    app.router.add_get('/api', response1)
    app.router.add_get('/api/m1', response2)
    app.router.add_get('/api/m2', response3)
    app.router.add_get('/api/m3', response4)
    app.router.add_get('/api/m4', response5)
    app.router.add_get('/api/m5', response6)
    app.router.add_get('/api/m5/1', response7)
    app.router.add_get('/api/m5/2', response8)
    app.router.add_get('/api/m5/3', response9)

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
        print("morton-debug-1",route)
        string = str(route)
        rest_route_path = string[string.index("  "):].split("/")
        print("morton-debug-2",rest_route_path)
        if len(rest_route_path) > position and path in string:
            print("morton-debug-3",rest_route_path)
            endpoints.add(rest_route_path[position])
    return sorted(endpoints)

    # for route in app.router.resources():
    #     string = str(route)
    #     rest_route_path = string[string.index(" "):].split("/")
    #     if len(rest_route_path) > position and path in string:
    #         endpoints.add(rest_route_path[position])
    # return sorted(endpoints)


print(_instance)
print('Handler function called')

app = app()
app2 = get_app()
print(_instance)
print(app)
print(app2)

setup_routes(app)
string = get_endpoints("/api")
print(string)

web.run_app(app, host='127.0.0.1', port=8090)



# curl -X GET localhost:8090/api/m5 