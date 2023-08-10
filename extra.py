from pymongo.mongo_client import MongoClient
from encryption import *
import random
import string
from pytz import timezone
from datetime import datetime
import os
from shutil import copyfile
conp = MongoClient("mongodb+srv://thejatin:jatinkalwar@attacknum.nmuaiq8.mongodb.net/?retryWrites=true&w=majority")
conn = MongoClient("mongodb+srv://jatinkalwar:shifaanam@mbomb.ghtntua.mongodb.net")


async def htmll():
    return """
                    <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>MASTER-BOMBER2.O</title>
            </head>
            <body>
                <h1>Hello</h1>

            </body>
            </html>
                """


async def loo(ip):
    for i in conn.masbom.login.find():
        no = i['no']
        for x in range(1, int(no)):
            ipp = i[f'ip{x}']
            if ip == ipp:
                return {"status": "key", "sec": i['key'], "no": i['no']}
    return "no"


async def randomv():
    try:
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(7))
        return result_str
    except Exception as e:
        return "error"


async def newlogin(ip, name):
    try:
        ind_time = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
        keyy = await randomv()
        if keyy == "error":
            return {"status": "Key Error"}
        else:
            adi = conn.masbom.login.insert_one({"ip1": ip, "key": keyy, "name": name, "no": "2", "time": str(ind_time)})
            if adi != None:
                return {"status": "ok", "key": keyy}
            else:
                return {"status": "failed to login"}
    except Exception as e:
        return {"status": "failed"}


async def addmoreip(ip, key):
    pass


async def adnewip(ip, skey, no):
    try:
        intn = int(no)
        newno = intn + 1

        for i in range(intn, newno):
            conn.masbom.login.update_one({"key": skey}, {'$set': {f'ip{str(intn)}': ip, "no": str(newno)}})
            return "ok"
    except Exception as a:
        return "failed"


async def keyip(ip, nno, key):
    try:
        jo = await loo(ip)
        if jo == "no":
            kno = int(nno) + 1
            conn.masbom.login.update_one({"key": str(key)}, {'$set': {f'ip{str(nno)}': ip, "no": str(kno)}})
            return {"status": "ok"}
        else:
            return {"status": "ok"}
    except Exception as e:
        return {"status": "failed"}


async def checkacckey(keys, ip, name):
    try:
        for i in conn.masbom.login.find():
            dkey = i['key']
            if keys == dkey:
                nno = i['no']
                o = await keyip(ip, nno, keys)
                return o

        else:
            kk = await inner(ip, name)
            return kk
    except Exception as e:
        return {"status": "failed"}


async def inner(ip, name):
    chec = await loo(ip)
    if chec == "no":
        newl = await newlogin(ip, name)
        if "ok" == newl['status']:
            return {"status": "key", "key": newl['key']}
        else:
            return {"status": "failed"}
    else:
        return {"status": "key", "key": chec['sec']}


async def afterlog(ip, keyss):
    try:
        pas = conn.masbom.login.find_one({"key": keyss}, {'no': 1, '_id': 0})
        newno = pas['no']
        nnewno = int(newno) + 1
        conn.masbom.login.update_one({"key": str(keyss)}, {'$set': {f'ip{newno}': ip, "no": str(nnewno)}})
        return "ok"
    except Exception as e:
        return "failed"


async def checkkeyexits(key):
    pas = conn.masbom.login.find_one({"key": key}, {'no': 1, '_id': 0})
    return pas


async def downloadindsms(tarnum, skey):
    ind_time = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
    conp.attack.attacknum.insert_one(
        {"key": skey, "on": tarnum, "type": "sms", "count": "india", "when": str(ind_time)})
    os.system("rm indisms.py bomber_indisms.py")
    copyfile("indiaa.py", "indisms.py")
    file = "indisms.py"
    os.system(f"sed -i s/€tor/{tarnum}/g indisms.py")
    await setup(file)
    return "ok"


async def lookk(ip):
    for i in conn.masbom.login.find():
        no = i['no']
        for x in range(1, int(no)):
            ipp = i[f'ip{x}']
            if ip == ipp:
                return i['key']
    return "no"

async def downloadupi(upiid , ukey):
    ind_time = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
    conp.attack.upidata.insert_one({"key": ukey, "on": str(upiid), "when": str(ind_time)})
    os.system("rm upicopy.py bomber_upicopy.py")
    copyfile("upi.py", "upicopy.py")
    ufile = "upicopy.py"
    os.system(f"sed -i s/€tor/{upiid}/g upicopy.py")
    await setup(ufile)
    return "ok"

