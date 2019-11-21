from aiohttp import web
#asyncio 提供的@asyncio.coroutine（async）可以把
#generator标记为coroutine类型，然后在协程内部
#用yield from（await） 调用另一个协程实现异步操作
async def hello(request):
	return web.Request(text='HEllo,world')

app = web.Application()
app.router.add_get('/',hello)
web.run_app(app)