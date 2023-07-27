from addnum import *
from db import *
from extra import *
from india import *
from encryption import *
from pymongo.mongo_client import MongoClient
from fastapi import FastAPI , Request , BackgroundTasks
from fastapi.responses import HTMLResponse
import requests

import json
from fastapi.responses import FileResponse


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

@app.get("/num/add/{mobn}/{unam}/")
async def nnew(mobn ,unam , passs , key):
        if key==None:
            return {"status": "failed" , "reason": "no key found"}
        else:
            chkey = await checkkeyexits(key)
            if chkey==None:
                return {"status": "failed" , "reason": "Enter valid key"}
            else:
                if (len(mobn) != 10):
                    return {"status": "failed" , "reason":"10 Digit"}
                elif ((mobn.isnumeric()) == False):
                    return {"status": "failed", "reason": "only integer allowed", "mob": mobn}
                elif (len(passs)>6):
                    return {"status": "failed", "reason": "maximum 5 digit password", "mob": mobn}
                else:
                    async def check(mobn , passs):
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
                            adi = conn.masbom.protect.insert_one({"status": "true", "mob": mobn , "admin": "no" ,"name": unam , "password": passs ,"key": key})
                            if(adi!=None):
                                return {"status": "ok"}
                            else:
                                return {"status": "failed"}
                        else:
                            return {"status": "already protected" , "mob": mobn}
                    ret =await check(mobn , passs)
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

@app.get("/bomber/sms/{coun}/{tarnumm}/{key}")
async def bombb( request: Request , coun , tarnumm , key , bd: BackgroundTasks):
    ip = request.client.host
    try:
        skey = await lookk(ip)
        if skey=="no":
            return False
        ser= await serverf()
        if ser=="on":
            acce= await accessk()
            adminacce = await adminacc()
            if (acce==key or key==adminacce):
                if coun=="91":
                    await downloadindsms(tarnumm , skey)
                    file_path = "bomber_indisms.py"
                    return FileResponse(path=file_path, filename=file_path)
                    # ins = await indsms(tarnumm , skey)
                    # print(ins)
                else:
                    return {"status": "failed", "reason": "Country is not Supported"}
            else:
                return {"status": "failed" , "reason": "Wrong Access Key"}
        else:
            return {"status": "failed" , "reason": "server off"}
    except Exception as e:
        print(e)
        return {"status": "failed" , "reason": "Internal server error"}
@app.get("/starr/")
async def star(key: str , code: str):
    print(key, code)
    return (await randomv())

@app.get("/")
# async def mains():
#     htmlres= await htmll()
#     return HTMLResponse(content=htmlres , status_code=200)

def read_root( request: Request):
    file_path="india.py"
    return FileResponse(path=file_path , filename=file_path)
@app.get("/loginn/")
async def loginn(request: Request , keyss):
    ip = request.client.host
    log = await loo(ip)
    if log=="no":
        seclog = await afterlog(ip , keyss)
        if seclog=="ok":
            return {"status": "ok"}
        else:
            return {"status": "failed"}
    else:
        return log

@app.get("/firstlogin/")
async def firstlogin(request: Request , name , keys):
    ip = request.client.host
    if keys==None:
        jk = await inner(ip , name)
        return jk
    else:
        jj = await checkacckey(keys , ip , name)
        return jj

        # skey = chec['sec']
        # no = chec['no']
        # kk = await adnewip(ip ,skey , no )
        # if kk=="ok":
        #     return "ok"
        # else:
        #     return "failed"
@app.get("/bomber/access/")
async def acesskey(acess):
    uskey = await accessk()
    print(uskey)
    adkey = await adminacc()
    print(adkey)
    if (uskey==acess or adkey==acess):
        return True
    else:
        return False

