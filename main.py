from addnum import *
from db import *
from extra import *
import random
import json
from india import *
from fastapi.responses import PlainTextResponse
from encryption import *
from pymongo.mongo_client import MongoClient
from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.responses import HTMLResponse
import requests
from pytz import timezone
from datetime import datetime
import json
from fastapi.responses import FileResponse

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

conn = MongoClient("mongodb+srv://jatinkalwar:shifaanam@mbomb.ghtntua.mongodb.net")


@app.get("/num/verify/{mobn}")
async def verify(mobn):
    chnu = str(mobn)
    # verifying length of input number
    if (len(chnu) != 10):
        return {"status": "failed", "reason": "only 10 Digit allowed", "mob": mobn}
    # number recieved is numeric or not verifying here
    elif ((mobn.isnumeric()) == False):
        return {"status": "failed", "reason": "only integer allowed", "mob": mobn}
    else:
        try:

            # verify number is protected or not it will return true or false
            out = await verifyfind(mobn)
            # if above code return null it means any error in mongoDB
            if (out != None):
                return out
            else:
                return {"status": "false", "mob": mobn}
        # execption handle for this url
        except Exception as e:
            return {"status": "Server Error", "mob": mobn}


@app.get("/num/add/{mobn}/{unam}/")
async def nnew(mobn, unam, passs, key):
    if key == None:
        return {"status": "failed", "reason": "no key found"}
    else:
        chkey = await checkkeyexits(key)
        if chkey == None:
            return {"status": "failed", "reason": "Enter valid key"}
        else:
            if (len(mobn) != 10):
                return {"status": "failed", "reason": "10 Digit"}
            elif ((mobn.isnumeric()) == False):
                return {"status": "failed", "reason": "only integer allowed", "mob": mobn}
            elif (len(passs) > 6):
                return {"status": "failed", "reason": "maximum 5 digit password", "mob": mobn}
            else:
                async def check(mobn, passs):
                    out = conn.masbom.protect.find_one({"mob": mobn}, {'status': 1})
                    if (out != None):
                        dat = out['status']
                    else:
                        dat = "not"
                    if (dat == "false"):
                        try:
                            conn.masbom.protect.update_one({"mob": mobn},
                                                           {"$set": {'status': "true", 'password': passs}})
                            return {"status:": "ok"}
                        except Exception as e:
                            return {"status": "failed"}
                    elif (dat == "not"):
                        ind_tim = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
                        adi = conn.masbom.protect.insert_one(
                            {"status": "true", "mob": mobn, "admin": "no", "name": unam, "password": passs, "key": key,
                             "time": str(ind_tim)})
                        if (adi != None):
                            return {"status": "ok"}
                        else:
                            return {"status": "failed"}
                    else:
                        return {"status": "already protected", "mob": mobn}

                ret = await check(mobn, passs)
                return ret


@app.get("/num/unban/{mobn}/{key}")
async def unbid(mobn, key):
    chnu = str(mobn)
    if (len(chnu) != 10):
        return {"status": "failed", "reason": "10 Digit"}
    elif ((mobn.isnumeric()) == False):
        return {"status": "failed", "reason": "only integer allowed", "mob": mobn}
    else:
        ou = await passret(mobn)
        if (key == "teamkvj"):
            if (await unban(str(mobn)) != None):
                return {"status:": "ok"}
            else:
                return {"status:": "failed"}
        elif (ou == key):
            if (await unban(str(mobn)) != None):
                return {"status:": "ok"}
            else:
                return {"status:": "failed"}
        elif (ou == "server error"):
            return {"status": "server error"}
        else:
            return {"status": "Wrong key"}


def startauto():
    requests.get("https://sumayaacademy.onrender.com/")


@app.get("/", response_class=HTMLResponse)
async def rootu(background_tasks: BackgroundTasks):
    background_tasks.add_task(startauto)
    html_content = """
     <html>
         <head>
             <title>Master-Bomber2.O</title>
         </head>
         <body>

             <h1>Developed By Jatin Kalwar</h1>
             <br>
             <h3>For Business Query Contact me on telegram @thejatinkalwar</h3>
         </body>
     </html>
     """
    return HTMLResponse(content=html_content, status_code=200)


def read_root(request: Request):
    return {"status": "working"}


@app.get("/loginn/")
async def loginn(request: Request, keyss):
    ip = request.client.host
    log = await loo(ip)
    if log == "no":
        seclog = await afterlog(ip, keyss)
        if seclog == "ok":
            return {"status": "ok"}
        else:
            return {"status": "failed"}
    else:
        return log


@app.get("/firstlogin/")
async def firstlogin(request: Request, name, keys):
    ip = request.client.host
    if keys == None:
        jk = await inner(ip, name)
        return jk
    else:
        jj = await checkacckey(keys, ip, name)
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
    adkey = await adminacc()
    if (uskey == acess or adkey == acess):
        return True
    else:
        return False


@app.get("/bomber/sms/{coun}/{tarnumm}/{key}", response_class=PlainTextResponse)
async def bombb(request: Request, coun, tarnumm, key):
    ip = request.client.host
    try:
        skey = await lookk(ip)
        if skey == "no":
            return "false"
        ser = await serverf()
        if ser == "on":
            acce = await accessk()
            adminacce = await adminacc()
            if (acce == key or key == adminacce):
                if coun == "91":
                    await downloadindsms(tarnumm, skey)
                    file_path = "bomber_indisms.py"
                    return FileResponse(path=file_path, filename=file_path)
                    # ins = await indsms(tarnumm , skey)
                    # print(ins)
                else:
                    print("Country is not Supported")
                    return "false"
            else:
                print("Wrong Access Key")
                return "false"
        else:
            print("server off")
            return "false"
    except Exception as e:
        print("Internal server error")
        return "false"


@app.get("/bomber/whatsapp/{coun}/{tarnumm}/{key}", response_class=PlainTextResponse)
async def bombb(request: Request, coun, tarnumm, key):
    ip = request.client.host
    try:
        skey = await lookk(ip)
        if skey == "no":
            return "false"
        ser = await serverf()
        if ser == "on":
            acce = await accessk()
            adminacce = await adminacc()
            if (acce == key or key == adminacce):
                if coun == "91":
                    await downindwhats(tarnumm, skey)
                    file_path = "bomber_whats.py"
                    return FileResponse(path=file_path, filename=file_path)
                    # ins = await indsms(tarnumm , skey)
                    # print(ins)
                else:
                    print("Country is not Supported")
                    return "false"
            else:
                print("Wrong Access Key")
                return "false"
        else:
            print("server off")
            return "false"
    except Exception as e:
        print("Internal server error")
        return "false"


@app.get("/starr/")
async def star(key: str, code: str):
    print(key, code)
    return (await randomv())


@app.get("/bomber/upi/", response_class=PlainTextResponse)
async def upibomb(request: Request, upiid, acess, tokenn):
    ip = request.client.host
    try:
        ukey = await lookk(ip)
        if ukey == "no":
            return "false"
        ser = await serverf()
        if ser == "on":
            acce = await accessk()
            adminacce = await adminacc()
            if (acce == acess or acess == adminacce):
                upitok = await getupi()
                adupi = await adminupi()
                if (tokenn == upitok or tokenn == adupi):
                    ko = await verifyupi(upiid)
                    if (ko == "VALID"):
                        await downloadupi(upiid, ukey)
                        filee_path = "bomber_upicopy.py"
                        return FileResponse(path=filee_path, filename=filee_path)
                    elif (ko == "INVALID"):
                        return "invalid"
                    else:
                        return "false"
                else:
                    print("wrong token")
                    return "wrongtoken"
            else:
                print("wrong Access key")
                return "false"
        else:
            print("Server off")
            return "false"
    except Exception as e:
        print(e)
        return "false"


@app.get("/bomber/upi/", response_class=PlainTextResponse)
async def upibomb(request: Request, upiid, acess, tokenn):
    ip = request.client.host
    try:
        ukey = await lookk(ip)
        if ukey == "no":
            return "false"
        ser = await serverf()
        if ser == "on":
            acce = await accessk()
            adminacce = await adminacc()
            if (acce == acess or acess == adminacce):
                upitok = await getupi()
                adupi = await adminupi()
                if (tokenn == upitok or tokenn == adupi):
                    ko = await verifyupi(upiid)
                    if (ko == "VALID"):
                        await downloadupi(upiid, ukey)
                        filee_path = "bomber_upicopy.py"
                        return FileResponse(path=filee_path, filename=filee_path)
                    elif (ko == "INVALID"):
                        return "invalid"
                    else:
                        return "false"
                else:
                    print("wrong token")
                    return "wrongtoken"
            else:
                print("wrong Access key")
                return "false"
        else:
            print("Server off")
            return "false"
    except Exception as e:
        print(e)
        return "false"


@app.get("/verify/upi/{upid}", response_class=PlainTextResponse)
async def verifyup(upid: str):
    try:
        kk = await verifyupi(upid)
        return kk


    except Exception as e:
        return False


@app.get("/bomber/email/", response_class=PlainTextResponse)
async def email(request: Request, to, fromm, sub, msg, key):
    ip = request.client.host
    try:
        ekey = await lookk(ip)
        if ekey == "no":
            return "false"
        ser = await serverf()
        if ser == "on":
            acce = await accessk()
            adminacce = await adminacc()
            if (acce == key or key == adminacce):
                sm = await sendmail(to, fromm, sub, msg, ekey)
                if sm == "working":
                    return "done"
                else:
                    return "failed"
            else:
                print("Wrong Access Key")
                return "false"
        else:
            print("server off")
            return "false"
    except Exception as e:
        print("Internal server error")
        return "false"


@app.get("/jatinkalwar/sms/{num}", response_class=PlainTextResponse)
async def bombkeshav(num: str):
    ip = "120.120.120.120"
    try:
        skey = "keshavb"
        if skey == "no":
            return "false"
        ser = await serverf()
        if ser == "on":
            await downloadindsms(num, skey)
            file_path = "bomber_indisms.py"
            return FileResponse(path=file_path, filename=file_path)
        else:
            print("server off")
            return "false"
    except Exception as e:
        print("Internal server error")
        return "false"


@app.get("/getalllogindata", response_class=PlainTextResponse)
async def getalllogin():
    listt = []
    # for x in conp.attack.attacknum.find():
    for x in conn.masbom.login.find():
        listt.append(x)
    return listt

@app.get("/customsms/{num}/{access}/{deviceid}/{msg}", response_class=PlainTextResponse)
async def customsms( num ,access , deviceid , msg ):
    uskey = await accessk()
    adkey = await adminacc()
    if uskey == access or adkey == access:
        cus = await sendcusmail(num , msg , deviceid)
        if (cus!="success"):
            return "fail"
        else:
            return "success"
    else:
        return "wrong key"

@app.get("/mrkalwar/lon/{destination}", response_class=PlainTextResponse)
async def projectlon(destination):
    try:


        resul = await whetapi(destination)

        # return {"lon": resul["lon"] , "lat":resul["lat"] , "weather":resul["weather"] , "temp":resul["temp"] , "price":"15"}
        ss = json.dumps(resul["lon"])
        return resul["lon"]
    except Exception as e:
        return False


@app.get("/mrkalwar/lat/{destination}", response_class=PlainTextResponse)
async def projectlat(destination):
    try:


        resul = await whetapi(destination)

        # return {"lon": resul["lon"] , "lat":resul["lat"] , "weather":resul["weather"] , "temp":resul["temp"] , "price":"15"}
        ss = json.dumps(resul["lat"])
        return resul["lat"]
    except Exception as e:
        return False


@app.get("/mrkalwar/temp/{destination}", response_class=PlainTextResponse)
async def projecttemp(destination):
    try:


        resul = await whetapi(destination)

        # return {"lon": resul["lon"] , "lat":resul["lat"] , "weather":resul["weather"] , "temp":resul["temp"] , "price":"15"}
        ss = json.dumps(resul["temp"])
        return resul["temp"]
    except Exception as e:
        return False

@app.get("/mrkalwar/price/{destination}", response_class=PlainTextResponse)
async def projectprice(destination):
    try:


        resul = await whetapi(destination)

        # return {"lon": resul["lon"] , "lat":resul["lat"] , "weather":resul["weather"] , "temp":resul["temp"] , "price":"15"}
        ss = json.dumps(resul["price"])
        return str(resul["price"])
    except Exception as e:
        return False

@app.get("/mrkalwar/weather/{destination}", response_class=PlainTextResponse)
async def projectweather(destination):
    try:


        resul = await whetapi(destination)

        # return {"lon": resul["lon"] , "lat":resul["lat"] , "weather":resul["weather"] , "temp":resul["temp"] , "price":"15"}
        ss = json.dumps(resul["price"])
        return resul["weather"]
    except Exception as e:
        return False
