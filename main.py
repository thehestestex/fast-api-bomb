from addnum import *
from fastapi import FastAPI
from pymongo.mongo_client import MongoClient
from india import *

app = FastAPI()

conn = MongoClient("mongodb+srv://jatinkalwar:shifaanam@mbomb.ghtntua.mongodb.net")

@app.get("/num/verify/{mobn}")
async def root(mobn):
    chnu = str(mobn)
    if (len(chnu)!=10):
        return {"status": "failed" , "reason":"10 Digit"}
    else:
        try:
            out = conn.masbom.protect.find_one({"mob": int(mobn)} , {"mob": 1 , 'status': 1 , '_id': 0 , 'name': 1})
            if (out != None):
                return out
            else:
                return { "status": "false", "mob": mobn }
        except Exception as e:
            return { "status": "Server Error", "mob": mobn }

@app.get("/num/add/{mobn}/{unam}")
def nnew(mobn ,unam):
    chnu = str(mobn)
    if (len(chnu)!=10):
        return {"status": "failed" , "reason":"10 Digit"}
    else:
        if (addnumm(int(mobn) , str(unam)) != None):
            return {"status":"ok"}
        else:
            return {"status":"failed"}

@app.get("/num/unban/{mobn}/{key}")
def unbid(mobn , key):
    chnu = str(mobn)
    if (len(chnu)!=10):
        return {"status": "failed" , "reason":"10 Digit"}
    else:
        if (key=="teamkvj"):
            if (unban(mobn) != None):
                uno = conn.masbom.protect.find_one({"mob": int(mobn)}, {"mob": 1, 'status': "ok", '_id': 0, 'name': 1})
                return uno
            else:
                return {"status": "failed"}
        else:
            return {"status": "Wrong key"}

@app.get("/bomb/smss/{tarnumm}")
async def bombb(tarnumm):
    try:
        indsms(tarnumm)
        return {"status":"ok"}
    except Exception as e:
        print(e)
