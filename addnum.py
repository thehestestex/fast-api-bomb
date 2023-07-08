from pymongo.mongo_client import MongoClient
conn = MongoClient("mongodb+srv://jatinkalwar:shifaanam@mbomb.ghtntua.mongodb.net")


def addnumm(mobn , unam):
    try:
        return conn.masbom.protect.insert_one({"status": "true", "mob": mobn , "admin": "no" ,"name": unam })
    except Exception as e:
        return {"status": "failed"}

def unban(mobn):
    try:
         return conn.masbom.protect.update_one({ "mob": int(mobn) }, { '$set':  { 'status': "false" }})
    except Exception as e:
        return {"status": "failedd"}
