import asyncio
from aiohttp import web
from umongo.fields import ObjectId
from routes.routes import routes
from models.Product import Product

@routes.post('/product')
async def createProduct(request):
    body = await request.json()

    # every field may be null
    productToCreate = Product(
        name = body.get("name", None),
        description = body.get("description", None),
        properties = body.get("properties", None)
    )

    await productToCreate.commit()
    return web.json_response({ 'id': str(productToCreate.id) })    

@routes.get('/product/{id}')
async def getProductById(request):
    productId = request.match_info["id"]
    product = await Product.find_one({ 'id': ObjectId(productId) })
    return web.json_response(product.toFullDict())


@routes.get('/product')
async def getProductByFilter(request):
    body = await request.json()
    name = body.get('name', None)
    properties = body.get('properties', None)

    filterOption = {}
    if name is not None: filterOption['name'] = name

    if properties is not None and isinstance(properties, dict):
        for key, value in properties.items():
            filterOption[f'properties.{key}'] = value

    prodList = [p.toSmallDict() async for p in Product.find(filterOption)]
    return web.json_response(prodList)

@routes.delete('/product')
async def deleteAllProducts(request):
    async for p in Product.find(): await p.delete()
    return web.Response(status = 200)


