from addnum import *
from fastapi import FastAPI , Request
from pymongo.mongo_client import MongoClient
from india import *
import uvicorn

app = FastAPI()

conn = MongoClient("mongodb+srv://jatinkalwar:shifaanam@mbomb.ghtntua.mongodb.net")
@app.get("/num/verify/{mobn}")
async def verify(mobn):
    chnu = str(mobn)
    #verifying length of input number
    if (len(chnu)!=10):
        return {"status": "failed" , "reason": "only 10 Digit allowed" , "mob": mobn}
    #number recieved is numeric or not verifying here
    elif ((mobn.isnumeric())==False):
        return {"status": "failed" , "reason": "only integer allowed" , "mob":mobn}
    else:
        try:

            #verify number is protected or not it will return true or false
            out = await verifyfind(mobn)
            #if above code return null it means any error in mongoDB
            if (out != None):
                return out
            else:
                return { "status": "false", "mob": mobn }
        #execption handle for this url
        except Exception as e:
            return { "status": "Server Error", "mob": mobn }

@app.get("/num/add/{mobn}/{unam}/{passs}")
async def nnew(mobn ,unam , passs):
        if (len(mobn) != 10):
            return {"status": "failed" , "reason":"10 Digit"}
        elif ((mobn.isnumeric()) == False):
            return {"status": "failed", "reason": "only integer allowed", "mob": mobn}
        elif (len(passs)>6):
            return {"status": "failed", "reason": "maximum 5 digit password", "mob": mobn}
        else:
            def check(mobn , passs):
                out = conn.masbom.protect.find_one({"mob": mobn}, {'status': 1})
                if (out!=None):
                    dat = out['status']
                else:
                    dat="not"
                if (dat=="false"):
                    try:
                        conn.masbom.protect.update_one({ "mob": mobn }, { "$set":  { 'status': "true" , 'password': passs}})
                        return {"status:": "ok"}
                    except Exception as e:
                        return {"status": "failed"}
                elif(dat=="not"):
                    adi = conn.masbom.protect.insert_one({"status": "true", "mob": mobn , "admin": "no" ,"name": unam , "password": passs})
                    if(adi!=None):
                        return {"status": "ok"}
                    else:
                        return {"status": "failed"}
                else:
                    return {"status": "already protected" , "mob": mobn}
            ret = check(mobn , passs)
            return ret


@app.get("/num/unban/{mobn}/{key}")
async def unbid(mobn , key):
    chnu = str(mobn)
    if (len(chnu)!=10):
        return {"status": "failed" , "reason": "10 Digit"}
    elif ((mobn.isnumeric())==False):
        return {"status": "failed" , "reason": "only integer allowed" , "mob":mobn}
    else:
        ou = await passret(mobn)
        if (key=="teamkvj"):
            if (await unban(str(mobn)) != None):
                return {"status:": "ok"}
            else:
                return {"status:": "failed"}
        elif (ou==key):
            if (await unban(str(mobn)) != None):
                return {"status:": "ok"}
            else:
                return {"status:": "failed"}
        elif (ou=="server error"):
            return {"status": "server error"}
        else:
            return {"status": "Wrong key"}

@app.get("/bomb/smss/{tarnumm}")
async def bombb(tarnumm):
    try:
        await indsms(tarnumm)
        return {"status":"ok"}
    except Exception as e:
        print(e)
        
@app.get("/")
def read_root( request: Request):
    item_id="njn"
    client_host = request.client.host
    print(client_host)
    return {"item_id": item_id}
