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
        admink = conn.masbom.serverss.find_one({"pos": "adminskey"}, {'bombkey': 1, '_id': 0})
        return (admink['bombkey'])
    except Exception as e:
        return {"status: Control Server Error"}

async def getupi():
    try:
        userv = conn.masbom.serverss.find_one({"pos": "maintain"}, {'upicode': 1, '_id': 0})
        return (userv['upicode'])
    except Exception as e:
        return {"status: Control Server Error"}

async def adminupi():
    try:
        aserv = conn.masbom.serverss.find_one({"pos": "adminskey"}, {'upikeyy': 1, '_id': 0})
        return (aserv['upikeyy'])
    except Exception as e:
        return {"status: Control Server Error"}



