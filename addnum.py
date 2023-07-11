from pymongo.mongo_client import MongoClient
import asyncio
conn = MongoClient("mongodb+srv://jatinkalwar:shifaanam@mbomb.ghtntua.mongodb.net")


async def addnumm(mobn , unam):
    print("uooo")
    try:
        return conn.masbom.protect.insert_one({"status": "true", "mob": mobn , "admin": "no" ,"name": unam })
    except Exception as e:
        return {"status": "failed"}

async def unban(mobn):
    try:
         conn.masbom.protect.update_one({ "mob": (mobn) }, { '$set':  { 'status': "false" }})
         return {"status": "ok"}
    except Exception as e:
        return {"status": "failed"}

async def verifyfind(mobn):
    jo =conn.masbom.protect.find_one({"mob": mobn} , {'mob': 1 , 'status': 1 , '_id': 0})
    return jo

async def passret(mobn):
    try:
        pas = conn.masbom.protect.find_one({"mob": mobn} , {'password': 1 , '_id': 0})
        return pas['password']
    except Exception as e:
         return "server error"
