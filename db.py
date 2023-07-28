from pymongo.mongo_client import MongoClient
import asyncio
conn = MongoClient("mongodb+srv://jatinkalwar:shifaanam@mbomb.ghtntua.mongodb.net")
async def serverf():
    try:
        serv = conn.masbom.serverss.find_one({"pos": "maintain"}, {'server': 1, '_id': 0})
        return (serv['server'])
    except Exception as e:
        return {"status: Control Server Error"}

async def accessk():
    try:
        serr = conn.masbom.serverss.find_one({"pos": "maintain"}, {'access': 1, '_id': 0})
        return (serr['access'])
    except Exception as e:
        return {"status: Control Server Error"}

async def adminacc():
    try:
        se = conn.masbom.serverss.find_one({"pos": "adminskey"}, {'bombkey': 1, '_id': 0})
        return se['bombkey']
    except Exception as e:
        return {"status: Control Server Error"}


