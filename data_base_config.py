import motor.motor_asyncio

mongodb_url = 'mongodb://localhost:27017'

client = motor.motor_asyncio.AsyncIOMotorClient(mongodb_url)

database = client.fast_api_tutorial

