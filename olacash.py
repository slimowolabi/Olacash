#AUTHOR : SLIM
#OPEN SOURCE BY SLIM
#ENJOY

import os,sys,re,time,requests,rich,random,string,json,platform,subprocess,logging,pyotp,pycountry
from typing import Set,Optional
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from faker import Faker
from os import path
from urllib.request import Request,urlopen
from time import sleep as sp
from os import system as sm
from sys import platform as pf
from random import choice as ch
from random import randint as rand
from rich import print as rprint
from rich.panel import Panel as pan
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from rich.console import Console
from rich.table import Table
from rich.live import Live
from rich.text import Text
from datetime import datetime
from time import sleep
from time import sleep as jeda
from time import strftime

console=Console()

W = "\033[1;37m"  # White
G = "\033[1;32m"  # Green
R = "\033[1;31m"  # Red
C = "\033[1;36m"  # Cyan
Y = "\033[1;33m"  # Yellow
X = "\033[0m"     # Reset

def install_dependencies():
    packages=["requests","rich","bs4","httpx","faker","fake_useragent","pyotp","pycurl"]
    print(f" INSTALLING DEPENDENCIES...\n")
    for package in packages:
        os.system(f"{sys.executable} -m pip install {package}")
    print(f" INSTALLATION COMPLETE!")

sd_folder="/sdcard/AUTO-XD"
slim_folders=("AUTO",)
os.makedirs(sd_folder,exist_ok=True)
for folder in slim_folders:
    os.makedirs(os.path.join(sd_folder,folder),exist_ok=True)

def clear_screen():
    os.system('cls' if platform.system().lower() == 'windows' else 'clear')

try:
    android_version=subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').strip()
    model=subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').strip()
    build=subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').strip()
    fbmf=subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').strip()
    fbbd=subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').strip()
    fbca=subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').strip()
    fbdm=f"{{density=2.25,height={subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').strip()},width={subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').strip()}}}"
    try:
        fbcr=subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].strip()
    except:
        fbcr='ZONG'
except:
    android_version,model,build,fbmf,fbbd,fbca,fbdm,fbcr='10','Unknown','Unknown','Unknown','Unknown','arm64-v8a','{density=2.25,height=720,width=1280}','ZONG'
device={'android_version': android_version,'model': model,'build': build,'fblc': 'en_US','fbmf': fbmf,'fbbd': fbbd,'fbdv': model,'fbsv': android_version,'fbca': fbca,'fbdm': fbdm}

ua=UserAgent()
ugen=[]

def auto_error_ua1():
    ualist=[ua.random for _ in range(50)]
    return str(random.choice(ualist))

def auto_error_ua2():
    android_versions=["10","11","12","13","14","15"]
    devices=["SM-S928B","SM-S926B","SM-S921B","SM-S938B","Pixel 8","Pixel 8 Pro","Pixel 9","Pixel 9 Pro","CPH2665","CPH2525","CPH2557","CPH2613","CPH2625","CPH2639","V2318","V2332","RMX3851","RMX3999","2201117TG","23127PN0CG","Redmi Note 13 Pro 5G","Redmi Note 14 Pro","Infinix X6853","Infinix X6871",]
    builds=["UP1A.231005.007","AP2A.240905.003","BP1A.250305.019","TP1A.220624.014","UKQ1.230804.001",]
    chrome_major=random.randint(130,137)
    chrome_build=random.randint(6000,7999)
    chrome_patch=random.randint(50,250)
    return (f"Mozilla/5.0 (Linux; Android {random.choice(android_versions)}; "
        f"{random.choice(devices)} Build/{random.choice(builds)}; wv) "
        f"AppleWebKit/537.36 (KHTML, like Gecko) "
        f"Version/4.0 Chrome/{chrome_major}.0.{chrome_build}.{chrome_patch} "
        f"Mobile Safari/537.36")

for x in range(5000):
    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='K)'
    d=random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
    e=random.randrange(1,999)
    f=random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']) 
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)

FB_LITE_UA=("Mozilla/5.0 (Linux; Android 12; 2201117TY Build/SKQ1.211006.001; wv) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.86 "
    "Mobile Safari/537.36 [FBAN/FB4A;FBAV/439.0.0.0.8;FBBV/443200018;"
    "FBDM/{density=2.75,width=1080,height=2280};FBLC/en_US;FBRV/0;FBCR/;"
    "FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.lite;FBDV/2201117TY;"
    "FBSV/12;FBOP/1;FBCA/armeabi-v7a:armeabi;]")

_DEVICE_POOL=[('Xiaomi','Redmi','2201117TY','12','armeabi-v7a:armeabi','2.75',1080,2280,'SKQ1'),('Xiaomi','Redmi','M2004J19C','10','armeabi-v7a:armeabi','2.0',720,1600,'QKQ1'),('Xiaomi','Redmi','22041219I','12','arm64-v8a:armeabi-v7a','2.4',1080,2400,'SKQ1'),('Xiaomi','Redmi','M2012K11G','11','arm64-v8a:armeabi-v7a','2.75',1080,2400,'RKQ1'),('Xiaomi','Redmi','2109119DG','11','arm64-v8a:armeabi-v7a','2.75',1080,2400,'RKQ1'),('Xiaomi','Redmi','2201116SR','12','arm64-v8a:armeabi-v7a','3.0',1080,2340,'SKQ1'),('Xiaomi','Redmi','22101316UG','12','arm64-v8a:armeabi-v7a','2.0',720,1600,'SKQ1'),('Xiaomi','Redmi','M2010J19SY','10','armeabi-v7a:armeabi','2.0',720,1600,'QKQ1'),('Xiaomi','Redmi','2207117BPG','12','arm64-v8a:armeabi-v7a','2.4',1080,2400,'SKQ1'),('Xiaomi','Redmi','2209116AG','12','arm64-v8a:armeabi-v7a','2.75',1080,2400,'SKQ1'),('Xiaomi','Redmi','22111317I','12','arm64-v8a:armeabi-v7a','2.4',1080,2400,'SKQ1'),('Xiaomi','Redmi','23021RAA2Y','12','arm64-v8a:armeabi-v7a','2.75',1080,2400,'SKQ1'),('Xiaomi','Redmi','21061110AG','11','arm64-v8a:armeabi-v7a','2.75',1080,2400,'RKQ1'),('Xiaomi','Redmi','2106118C','11','arm64-v8a:armeabi-v7a','3.0',1080,2400,'RKQ1'),('Xiaomi','Redmi','M2007J20CG','10','arm64-v8a:armeabi-v7a','2.75',1080,2340,'QKQ1'),('Xiaomi','Redmi','22120RN86G','12','arm64-v8a:armeabi-v7a','2.0',720,1640,'SKQ1'),('Xiaomi','Redmi','23028RN4DI','13','arm64-v8a:armeabi-v7a','2.4',1080,2400,'TKQ1'),('Xiaomi','Redmi','23106RN0DA','13','arm64-v8a:armeabi-v7a','2.0',720,1640,'TKQ1'),('Xiaomi','POCO','M2105K81AC','11','arm64-v8a:armeabi-v7a','2.75',1080,2400,'RKQ1'),('Xiaomi','POCO','22031116BG','12','arm64-v8a:armeabi-v7a','2.4',1080,2400,'SKQ1'),('Xiaomi','POCO','21091116I','11','arm64-v8a:armeabi-v7a','2.4',1080,2400,'RKQ1'),('Xiaomi','POCO','2107113SG','10','arm64-v8a:armeabi-v7a','2.0',720,1640,'QKQ1'),('Xiaomi','POCO','22111317PI','12','arm64-v8a:armeabi-v7a','2.4',1080,2400,'SKQ1'),('Samsung','Samsung','SM-A125F','11','arm64-v8a:armeabi-v7a','2.0',720,1600,'RP1A'),('Samsung','Samsung','SM-A235F','12','arm64-v8a:armeabi-v7a','2.4',1080,2408,'SP1A'),('Samsung','Samsung','SM-A536B','12','arm64-v8a:armeabi-v7a','2.4',1080,2408,'SP1A'),('Samsung','Samsung','SM-A325F','11','arm64-v8a:armeabi-v7a','2.0',720,1600,'RP1A'),('Samsung','Samsung','SM-A515F','12','arm64-v8a:armeabi-v7a','2.625',1080,2400,'SP1A'),('Samsung','Samsung','SM-A135F','12','arm64-v8a:armeabi-v7a','2.0',720,1600,'SP1A'),('Samsung','Samsung','SM-A037F','11','arm64-v8a:armeabi-v7a','2.0',720,1600,'RP1A'),('Samsung','Samsung','SM-A025F','10','arm64-v8a:armeabi-v7a','2.0',720,1600,'QP1A'),('Samsung','Samsung','SM-A035F','11','arm64-v8a:armeabi-v7a','2.0',720,1600,'RP1A'),('Samsung','Samsung','SM-A055F','13','arm64-v8a:armeabi-v7a','2.4',1080,2408,'TP1A'),('Samsung','Samsung','SM-A155F','14','arm64-v8a:armeabi-v7a','2.4',1080,2340,'UP1A'),('Samsung','Samsung','SM-A245F','13','arm64-v8a:armeabi-v7a','2.4',1080,2340,'TP1A'),('Samsung','Samsung','SM-A346B','13','arm64-v8a:armeabi-v7a','2.4',1080,2340,'TP1A'),('Samsung','Samsung','SM-A526B','12','arm64-v8a:armeabi-v7a','2.4',1080,2400,'SP1A'),('Samsung','Samsung','SM-A725F','11','arm64-v8a:armeabi-v7a','2.625',1080,2400,'RP1A'),('Samsung','Samsung','SM-M325F','11','arm64-v8a:armeabi-v7a','2.4',1080,2408,'RP1A'),('Samsung','Samsung','SM-M335F','12','arm64-v8a:armeabi-v7a','2.4',1080,2408,'SP1A'),('Samsung','Samsung','SM-M525F','11','arm64-v8a:armeabi-v7a','2.625',1080,2400,'RP1A'),('Samsung','Samsung','SM-A736B','12','arm64-v8a:armeabi-v7a','2.4',1080,2408,'SP1A'),('Samsung','Samsung','SM-A035M','11','arm64-v8a:armeabi-v7a','2.0',720,1600,'RP1A'),('Samsung','Samsung','SM-A145F','12','arm64-v8a:armeabi-v7a','2.0',720,1600,'SP1A'),('Samsung','Samsung','SM-A236B','13','arm64-v8a:armeabi-v7a','2.4',1080,2408,'TP1A'),('Samsung','Samsung','SM-M146B','13','arm64-v8a:armeabi-v7a','2.4',1080,2408,'TP1A'),('OPPO','OPPO','CPH2461','12','arm64-v8a:armeabi-v7a','2.4',1080,2412,'SP1A'),('OPPO','OPPO','CPH2373','11','arm64-v8a:armeabi-v7a','2.0',720,1612,'RP1A'),('OPPO','OPPO','CPH2389','11','arm64-v8a:armeabi-v7a','2.4',1080,2412,'RP1A'),('OPPO','OPPO','CPH2451','12','arm64-v8a:armeabi-v7a','2.4',1080,2412,'SP1A'),('OPPO','OPPO','CPH2269','11','arm64-v8a:armeabi-v7a','2.0',720,1612,'RP1A'),('OPPO','OPPO','CPH2325','11','arm64-v8a:armeabi-v7a','2.4',1080,2412,'RP1A'),('OPPO','OPPO','CPH2357','12','arm64-v8a:armeabi-v7a','2.0',720,1612,'SP1A'),('OPPO','OPPO','CPH2471','12','arm64-v8a:armeabi-v7a','2.0',720,1612,'SP1A'),('OPPO','OPPO','CPH2505','12','arm64-v8a:armeabi-v7a','2.4',1080,2412,'SP1A'),('OPPO','OPPO','CPH2339','12','arm64-v8a:armeabi-v7a','2.4',1080,2400,'SP1A'),('OPPO','OPPO','CPH2363','12','arm64-v8a:armeabi-v7a','2.4',1080,2400,'SP1A'),('OPPO','OPPO','CPH2523','13','arm64-v8a:armeabi-v7a','2.0',720,1612,'TP1A'),('OPPO','OPPO','CPH2333','11','arm64-v8a:armeabi-v7a','2.4',1080,2412,'RP1A'),('OPPO','OPPO','CPH2219','11','arm64-v8a:armeabi-v7a','2.4',1080,2412,'RP1A'),('OPPO','OPPO','CPH2579','13','arm64-v8a:armeabi-v7a','2.4',1080,2412,'TP1A'),('realme','realme','RMX3516','12','arm64-v8a:armeabi-v7a','2.4',1080,2412,'SP1A'),('realme','realme','RMX3371','11','arm64-v8a:armeabi-v7a','2.4',1080,2412,'RP1A'),('realme','realme','RMX3241','11','arm64-v8a:armeabi-v7a','2.0',720,1612,'RP1A'),('realme','realme','RMX3461','12','arm64-v8a:armeabi-v7a','2.4',1080,2412,'SP1A'),('realme','realme','RMX3686','12','arm64-v8a:armeabi-v7a','2.4',1080,2412,'SP1A'),('realme','realme','RMX3785','13','arm64-v8a:armeabi-v7a','2.4',1080,2412,'TP1A'),('realme','realme','RMX3830','13','arm64-v8a:armeabi-v7a','2.4',1080,2412,'TP1A'),('realme','realme','RMX3710','12','arm64-v8a:armeabi-v7a','2.4',1080,2412,'SP1A'),('realme','realme','RMX3195','11','arm64-v8a:armeabi-v7a','2.4',1080,2412,'RP1A'),('realme','realme','RMX3081','11','arm64-v8a:armeabi-v7a','2.0',720,1612,'RP1A'),('realme','realme','RMX3261','11','arm64-v8a:armeabi-v7a','2.0',720,1612,'RP1A'),('realme','realme','RMX3430','12','arm64-v8a:armeabi-v7a','2.4',1080,2412,'SP1A'),('realme','realme','RMX3392','12','arm64-v8a:armeabi-v7a','2.4',1080,2412,'SP1A'),('realme','realme','RMX3311','12','arm64-v8a:armeabi-v7a','2.0',720,1612,'SP1A'),('realme','realme','RMX3888','13','arm64-v8a:armeabi-v7a','2.4',1080,2412,'TP1A'),('Infinix','Infinix','X6823','12','arm64-v8a:armeabi-v7a','2.0',720,1612,'SP1A'),('Infinix','Infinix','X669C','11','arm64-v8a:armeabi-v7a','2.0',720,1612,'RP1A'),('Infinix','Infinix','X683','11','arm64-v8a:armeabi-v7a','2.0',720,1560,'RP1A'),('Infinix','Infinix','X6811','12','arm64-v8a:armeabi-v7a','2.0',720,1612,'SP1A'),('Infinix','Infinix','X6816','12','arm64-v8a:armeabi-v7a','2.0',720,1612,'SP1A'),('Infinix','Infinix','X6819','12','arm64-v8a:armeabi-v7a','2.0',720,1612,'SP1A'),('Infinix','Infinix','X678B','11','arm64-v8a:armeabi-v7a','2.0',720,1612,'RP1A'),('Infinix','Infinix','X6833B','13','arm64-v8a:armeabi-v7a','2.0',720,1612,'TP1A'),('Infinix','Infinix','X669','11','arm64-v8a:armeabi-v7a','2.0',720,1612,'RP1A'),('Infinix','Infinix','X6525','12','arm64-v8a:armeabi-v7a','2.4',1080,2460,'SP1A'),('Infinix','Infinix','X6739','12','arm64-v8a:armeabi-v7a','2.4',1080,2460,'SP1A'),('Infinix','Infinix','X655','10','arm64-v8a:armeabi-v7a','2.0',720,1612,'QP1A'),('Infinix','Infinix','X6526','12','arm64-v8a:armeabi-v7a','2.4',1080,2460,'SP1A'),('Infinix','Infinix','X6835','13','arm64-v8a:armeabi-v7a','2.0',720,1612,'TP1A'),('Infinix','Infinix','X6831','12','arm64-v8a:armeabi-v7a','2.0',720,1612,'SP1A'),('Infinix','Infinix','X6858','13','arm64-v8a:armeabi-v7a','2.4',1080,2460,'TP1A'),('vivo','vivo','V2109','11','arm64-v8a:armeabi-v7a','2.625',1080,2408,'RP1A'),('vivo','vivo','V2207','12','arm64-v8a:armeabi-v7a','2.625',1080,2408,'SP1A'),('vivo','vivo','V2041','11','arm64-v8a:armeabi-v7a','2.0',720,1600,'RP1A'),('vivo','vivo','V2129','11','arm64-v8a:armeabi-v7a','2.0',720,1600,'RP1A'),('vivo','vivo','V2130','11','arm64-v8a:armeabi-v7a','2.625',1080,2408,'RP1A'),('vivo','vivo','V2219','12','arm64-v8a:armeabi-v7a','2.625',1080,2408,'SP1A'),('vivo','vivo','V2203','12','arm64-v8a:armeabi-v7a','2.0',720,1600,'SP1A'),('vivo','vivo','V2166','12','arm64-v8a:armeabi-v7a','2.0',720,1600,'SP1A'),('vivo','vivo','V2147','12','arm64-v8a:armeabi-v7a','2.0',720,1600,'SP1A'),('vivo','vivo','V2208','12','arm64-v8a:armeabi-v7a','2.625',1080,2408,'SP1A'),('vivo','vivo','V2250','12','arm64-v8a:armeabi-v7a','2.0',720,1600,'SP1A'),('vivo','vivo','V2253','12','arm64-v8a:armeabi-v7a','2.625',1080,2408,'SP1A'),('vivo','vivo','V2258','12','arm64-v8a:armeabi-v7a','2.0',720,1600,'SP1A'),('vivo','vivo','V2317','13','arm64-v8a:armeabi-v7a','2.0',720,1600,'TP1A'),('vivo','vivo','V2349','13','arm64-v8a:armeabi-v7a','2.625',1080,2408,'TP1A'),('Tecno','Tecno','LE7','12','arm64-v8a:armeabi-v7a','2.0',720,1612,'SP1A'),('Tecno','Tecno','KH7','11','arm64-v8a:armeabi-v7a','2.0',720,1612,'RP1A'),('Tecno','Tecno','LG6','12','arm64-v8a:armeabi-v7a','2.0',720,1612,'SP1A'),('Tecno','Tecno','KF8','11','arm64-v8a:armeabi-v7a','2.0',720,1612,'RP1A'),('Tecno','Tecno','KI5k','11','arm64-v8a:armeabi-v7a','2.0',720,1612,'RP1A'),('Tecno','Tecno','BG8','12','arm64-v8a:armeabi-v7a','2.4',1080,2460,'SP1A'),('Tecno','Tecno','CD8','13','arm64-v8a:armeabi-v7a','2.4',1080,2460,'TP1A'),('Tecno','Tecno','LE6n','12','arm64-v8a:armeabi-v7a','2.0',720,1612,'SP1A'),('Tecno','Tecno','PH7n','12','arm64-v8a:armeabi-v7a','2.0',720,1612,'SP1A'),('Tecno','Tecno','LH8n','13','arm64-v8a:armeabi-v7a','2.0',720,1612,'TP1A'),('Tecno','Tecno','CK6','11','arm64-v8a:armeabi-v7a','2.4',1080,2460,'RP1A'),('Tecno','Tecno','LG7n','13','arm64-v8a:armeabi-v7a','2.0',720,1612,'TP1A'),('motorola','motorola','motog22','12','arm64-v8a:armeabi-v7a','2.0',720,1600,'SP1A'),('motorola','motorola','motog42','12','arm64-v8a:armeabi-v7a','2.75',1080,2400,'SP1A'),('motorola','motorola','motog52','12','arm64-v8a:armeabi-v7a','2.75',1080,2400,'SP1A'),('motorola','motorola','motog625G','12','arm64-v8a:armeabi-v7a','2.4',1080,2400,'SP1A'),('motorola','motorola','motoe32','11','arm64-v8a:armeabi-v7a','2.0',720,1600,'RP1A'),('motorola','motorola','motog31','11','arm64-v8a:armeabi-v7a','2.0',720,1560,'RP1A'),('motorola','motorola','motog825G','12','arm64-v8a:armeabi-v7a','2.75',1080,2400,'SP1A'),('motorola','motorola','motog735G','13','arm64-v8a:armeabi-v7a','2.75',1080,2400,'TP1A'),('motorola','motorola','motorolaedge40neo','13','arm64-v8a:armeabi-v7a','2.75',1080,2400,'TP1A'),('motorola','motorola','motog14','13','arm64-v8a:armeabi-v7a','2.0',720,1600,'TP1A'),('Nokia','Nokia','NokiaG21','12','arm64-v8a:armeabi-v7a','2.0',720,1600,'SP1A'),('Nokia','Nokia','NokiaG11','11','arm64-v8a:armeabi-v7a','2.0',720,1600,'RP1A'),('Nokia','Nokia','NokiaC21','11','arm64-v8a:armeabi-v7a','2.0',720,1600,'RP1A'),('Nokia','Nokia','NokiaG22','12','arm64-v8a:armeabi-v7a','2.0',720,1600,'SP1A'),('Nokia','Nokia','NokiaC32','13','arm64-v8a:armeabi-v7a','2.0',720,1600,'TP1A'),('Nokia','Nokia','NokiaG425G','13','arm64-v8a:armeabi-v7a','2.0',720,1600,'TP1A'),]
_CHROME_VERSIONS=[('109','5414','86','443200018','439.0.0.0.8'),('111','5563','58','460030614','451.0.0.0.14'),('112','5615','63','468206716','458.0.0.0.12'),('114','5735','154','478200230','466.0.0.0.30'),('116','5845','65','494036218','477.0.0.0.6'),('117','5938','183','502141314','483.0.0.0.24'),('119','6045','66','516039218','493.0.0.0.18'),('120','6099','117','526141914','498.0.0.0.22'),('121','6167','58','533011314','506.0.0.0.8'),('122','6261','39','542050618','513.0.0.0.16'),('123','6312','49','549004226','519.0.0.0.22'),('124','6367','113','558221414','527.0.0.0.14'),]
_BUILD_SUFFIXES=['001','002','003','004','005','011','012','013','014','020','021','022','023','030','031','032',]
ALL_LOCALES=["af-ZA,af;q=0.9,en-US;q=0.8","am-ET,am;q=0.9,en-US;q=0.8","ar-SA,ar;q=0.9,en-US;q=0.8,en;q=0.7","az-AZ,az;q=0.9,en-US;q=0.8","be-BY,be;q=0.9,en-US;q=0.8","bg-BG,bg;q=0.9,en-US;q=0.8","bn-IN,bn;q=0.9,en-US;q=0.8","ca-ES,ca;q=0.9,en-US;q=0.8","cs-CZ,cs;q=0.9,en-US;q=0.8","da-DK,da;q=0.9,en-US;q=0.8","de-DE,de;q=0.9,en-US;q=0.8","el-GR,el;q=0.9,en-US;q=0.8","en-US,en;q=0.9","en-GB,en;q=0.9","en-PH,en;q=0.9","en-IN,hi;q=0.9,en;q=0.8","en-NG,en;q=0.9","en-KE,en;q=0.9","en-ZA,en;q=0.9","es-ES,es;q=0.9,en-US;q=0.8","es-MX,es;q=0.9,en-US;q=0.8","et-EE,et;q=0.9,en-US;q=0.8","fa-IR,fa;q=0.9,en-US;q=0.8","fi-FI,fi;q=0.9,en-US;q=0.8","fil-PH,fil;q=0.9,en-US;q=0.8","fr-FR,fr;q=0.9,en-US;q=0.8","fr-CA,fr;q=0.9,en-US;q=0.8","fr-CI,fr;q=0.9,en-US;q=0.8","gu-IN,gu;q=0.9,en-US;q=0.8","he-IL,he;q=0.9,en-US;q=0.8","hi-IN,hi;q=0.9,en-US;q=0.8","hr-HR,hr;q=0.9,en-US;q=0.8","hu-HU,hu;q=0.9,en-US;q=0.8","id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","is-IS,is;q=0.9,en-US;q=0.8","it-IT,it;q=0.9,en-US;q=0.8","ja-JP,ja;q=0.9,en-US;q=0.8","ka-GE,ka;q=0.9,en-US;q=0.8","kk-KZ,kk;q=0.9,en-US;q=0.8","km-KH,km;q=0.9,en-US;q=0.8","ko-KR,ko;q=0.9,en-US;q=0.8","lo-LA,lo;q=0.9,en-US;q=0.8","lt-LT,lt;q=0.9,en-US;q=0.8","lv-LV,lv;q=0.9,en-US;q=0.8","mk-MK,mk;q=0.9,en-US;q=0.8","ml-IN,ml;q=0.9,en-US;q=0.8","mn-MN,mn;q=0.9,en-US;q=0.8","mr-IN,mr;q=0.9,en-US;q=0.8","ms-MY,ms;q=0.9,en-US;q=0.8","my-MM,my;q=0.9,en-US;q=0.8","ne-NP,ne;q=0.9,en-US;q=0.8","nl-NL,nl;q=0.9,en-US;q=0.8","no-NO,no;q=0.9,en-US;q=0.8","pa-IN,pa;q=0.9,en-US;q=0.8","pl-PL,pl;q=0.9,en-US;q=0.8","pt-BR,pt;q=0.9,en-US;q=0.8","pt-PT,pt;q=0.9,en-US;q=0.8","ro-RO,ro;q=0.9,en-US;q=0.8","ru-RU,ru;q=0.9,en-US;q=0.8","si-LK,si;q=0.9,en-US;q=0.8","sk-SK,sk;q=0.9,en-US;q=0.8","sl-SI,sl;q=0.9,en-US;q=0.8","sq-AL,sq;q=0.9,en-US;q=0.8","sr-RS,sr;q=0.9,en-US;q=0.8","sv-SE,sv;q=0.9,en-US;q=0.8","sw-KE,sw;q=0.9,en-US;q=0.8","ta-IN,ta;q=0.9,en-US;q=0.8","te-IN,te;q=0.9,en-US;q=0.8","th-TH,th;q=0.9,en-US;q=0.8","tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7","uk-UA,uk;q=0.9,en-US;q=0.8","ur-PK,ur;q=0.9,en-US;q=0.8","uz-UZ,uz;q=0.9,en-US;q=0.8","vi-VN,vi;q=0.9,en-US;q=0.8","zh-CN,zh;q=0.9,en-US;q=0.8","zh-HK,zh;q=0.9,en-US;q=0.8","zh-TW,zh;q=0.9,en-US;q=0.8"]
_LOCALE_BY_MFR={"Xiaomi": ALL_LOCALES,"Samsung": ALL_LOCALES,"OPPO": ALL_LOCALES,"realme": ALL_LOCALES,"Infinix": ALL_LOCALES,"vivo": ALL_LOCALES,"Tecno": ALL_LOCALES,"motorola": ALL_LOCALES,"Nokia": ALL_LOCALES,}
_FBLC_MAP={"af": "af_ZA","am": "am_ET","ar": "ar_AR","az": "az_AZ","be": "be_BY","bg": "bg_BG","bn": "bn_IN","bs": "bs_BA","ca": "ca_ES","cs": "cs_CZ","cy": "cy_GB","da": "da_DK","de": "de_DE","el": "el_GR","en": "en_US","es": "es_ES","et": "et_EE","eu": "eu_ES","fa": "fa_IR","fi": "fi_FI","fil": "fil_PH","fr": "fr_FR","ga": "ga_IE","gl": "gl_ES","gu": "gu_IN","he": "he_IL","hi": "hi_IN","hr": "hr_HR","hu": "hu_HU","hy": "hy_AM","id": "id_ID","is": "is_IS","it": "it_IT","ja": "ja_JP","ka": "ka_GE","kk": "kk_KZ","km": "km_KH","kn": "kn_IN","ko": "ko_KR","lo": "lo_LA","lt": "lt_LT","lv": "lv_LV","mk": "mk_MK","ml": "ml_IN","mn": "mn_MN","mr": "mr_IN","ms": "ms_MY","my": "my_MM","ne": "ne_NP","nl": "nl_NL","no": "nb_NO","pa": "pa_IN","pl": "pl_PL","ps": "ps_AF","pt": "pt_BR","ro": "ro_RO","ru": "ru_RU","si": "si_LK","sk": "sk_SK","sl": "sl_SI","sq": "sq_AL","sr": "sr_RS","sv": "sv_SE","sw": "sw_KE","ta": "ta_IN","te": "te_IN","tg": "tg_TJ","th": "th_TH","tk": "tk_TM","tr": "tr_TR","tt": "tt_RU","uk": "uk_UA","ur": "ur_PK","uz": "uz_UZ","vi": "vi_VN","xh": "xh_ZA","yo": "yo_NG","zh": "zh_CN","zh_cn": "zh_CN","zh_hk": "zh_HK","zh_tw": "zh_TW","zu": "zu_ZA"}
_CARRIERS_BY_LOCALE={"id": ["Telkomsel","Indosat","IM3","XL Axiata","AXIS","Smartfren","Tri","by.U"],"ph": ["GLOBE","SMART","TM","TNT","DITO"],"ms": ["CelcomDigi","Maxis","U Mobile","Unifi Mobile","Yes"],"sg": ["Singtel","StarHub","M1","GOMO","SIMBA","Circles.Life"],"th": ["AIS","DTAC","TrueMove H"],"vi": ["Viettel","Vinaphone","Mobifone"],"my": ["MPT","Ooredoo","Atom","Mytel"],"km": ["Smart","Cellcard","Metfone","Seatel"],"lo": ["Lao Telecom","Unitel","ETL"],"hi": ["Jio","Airtel","Vi","BSNL"],"bn": ["Grameenphone","Robi","Banglalink","Teletalk"],"ur": ["Jazz", "Zong","Telenor PK","Ufone"],"si": ["Dialog","Mobitel","Hutch","Airtel LK"],"zh": ["China Mobile","China Unicom","China Telecom"],"tw": ["Chunghwa Telecom","Taiwan Mobile","Far EasTone"],"hk": ["CSL","3HK","China Mobile HK","SmarTone"],"ja": ["NTT Docomo","SoftBank","au","Rakuten Mobile"],"ko": ["SK Telecom","KT","LG U+"],"tr": ["Turkcell","Vodafone TR","Turk Telekom"],"ar": ["STC","Mobily","Zain"],"ae": ["Etisalat","du"],"eg": ["Vodafone EG","Orange EG","Etisalat Misr", "WE"],"ng": ["MTN","Airtel","Glo","9mobile"],"sw": ["Safaricom","Airtel KE","Telkom KE"],"za": ["Vodacom","MTN SA","Cell C","Telkom Mobile"],"fr": ["Orange","SFR","Bouygues Telecom""Free Mobile"],"de": ["Telekom","Vodafone DE","O2 DE"],"it": ["TIM","Vodafone IT","WindTre","Iliad"],"es": ["Movistar","Vodafone ES","Orange ES","Yoigo"],"uk": ["EE","O2 UK","Vodafone UK","Three UK"],"en": ["T-Mobile","AT&T","Verizon","US Cellular","Boost Mobile","Metro"],"ca": ["Rogers","Bell","Telus","Freedom Mobile"],"au": ["Telstra","Optus","Vodafone AU"],"nz": ["Spark","One NZ","2degrees"],"pt": ["Vivo","Claro BR","TIM BR","Oi"],"mx": ["Telcel","AT&T MX","Movistar MX"],"ru": ["MTS","Beeline","MegaFon","Tele2"]}
_CONNECTION_TYPES=['WIFI','WIFI','WIFI','MOBILE_LTE','MOBILE_LTE','MOBILE_4G','MOBILE_3G',]

def make_device_profile():
    mfr,board,model,android_ver,abi,density,width,height,build_pfx=random.choice(_DEVICE_POOL)
    chrome_ver,chrome_build,chrome_patch,fb_bv,fb_av=random.choice(_CHROME_VERSIONS)
    build_date=random.randint(200000,240000)
    build_suffix=random.choice(_BUILD_SUFFIXES)
    build_str=f"{build_pfx}.{build_date}.{build_suffix}"
    locale='en-PH,en;q=0.9'
    fb_locale='en_US'
    carrier=random.choice(['GLOBE','SMART','TM','DITO','TNT','Sun Cellular'])
    conn_type=random.choice(_CONNECTION_TYPES)
    ua=(f"Mozilla/5.0 (Linux; Android {android_ver}; {model} Build/{build_str}; wv) "
        f"AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 "
        f"Chrome/{chrome_ver}.0.{chrome_build}.{chrome_patch} Mobile Safari/537.36 "
        f"[FBAN/FB4A;FBAV/{fb_av};FBBV/{fb_bv};"
        f"FBDM/{{density={density},width={width},height={height}}};"
        f"FBLC/{fb_locale};FBRV/0;FBCR/{carrier};"
        f"FBMF/{mfr};FBBD/{board};FBPN/com.facebook.lite;"
        f"FBDV/{model};FBSV/{android_ver};FBOP/1;FBCA/{abi};]")
    sec_ch_ua=(f'"Android WebView";v="{chrome_ver}", '
        f'"Chromium";v="{chrome_ver}", '
        f'"Not_A Brand";v="24"')
    return {'ua': ua,'locale': locale,'fb_locale': fb_locale,'carrier': carrier,'connection_type': conn_type,'android_ver': android_ver,'model': model,'chrome_ver': chrome_ver,'manufacturer': mfr,'board': board,'abi': abi,'density': density,'width': width,'height': height,'sec_ch_ua': sec_ch_ua,'viewport_width': str(width),}

_name_pools={'filipino_male_first': [],'filipino_female_first': [],'filipino_last': [],'rpw_male_first': [],'rpw_female_first': [],'rpw_last': []}

first_names_ph = ["Maria","Mary","Mae","Anne","Ann","Rose","Joy","Grace","Angel","Princess",
    "Nicole","Angela","Jenny","Lovely","Irish","Kate","Faith","Claire","Bea","Danica",
    "Alyssa","Trisha","Andrea","Camille","Bianca","Katrina","Sophia","Mika","Sheila",
    "Kristine","Jonalyn","Maricel","Cherry","Cristina","Shaina","Jessa","Rochelle",
    "Aira","Patricia","Louise","Megan","Catherine","Janine","Nadine","Hazel","Heart",
    "Cheska","Aubrey","Mica","Lea","Sheryl","Paula","Donna","Carla","Liza","Aileen",
    "Vanessa","Abigail","Karen","Michelle","Angelica","Bernadette","Marlene","Joan",
    "Riza","Cindy","April","Lyn","Julia","Kimberly","Rhea","Tina","Marjorie","Alexa",
    "Samantha","Ariane","Monica","Celine","Belle","Maureen","Denise","Charlene",
    "Clarisse","Therese","Marissa","Precious","Heidi","Christine","Joanna","Melissa",
    "Angelique","Yasmin","Roxanne","Mariel","Eunice","Jillian","Kyla","Ariana",
    "Isabel","Olivia","Mia","Charlotte","Amelia","Harper","Emily","Elizabeth",
    "Victoria","Luna","Chloe","Bella","Anna","Caroline","Sarah","Gabriella",
    "Alice","Ruby","Eva","Hailey","Gianna","Valentina","Ivy","Julia","Vivian",
    "Sophie","Jade","Natalia","Athena","Ashley","Brianna","Melody","Valerie",
    "Anastasia","Harmony","Juliana","Vanessa","Hope","Nicole","Camila","Daniela",
    "Veronica","Diana","Angela","Selena","Leslie","Miranda","Erin","Helena",
    "Francesca","Jocelyn","Bianca","Miriam","Alison","Amina","Fatima","Yvonne",
    "Nina","Carmen","Celeste","Gloria","Joyce","Martha","Pauline","Teresa",
    "Evelyn","Ruth","Esther","Deborah","Sharon","Janice","Connie","Regina",
    "Lorraine","Darlene","Janet","Joanne","Rosalie","Lucille","Annabelle",
    "Bethany","Cassandra","Crystal","Elise","Felicity","Gabrielle","Janelle",
    "Kendra","Larissa","Mallory","Noelle","Priscilla","Raven","Sabrina",
    "Tabitha","Whitney","Zaria","Brenda","Corazon","Divina","Erlinda","Fe",
    "Gina","Hilda","Imelda","Jean","Marites","Nenita","Ofelia","Perla",
    "Rosanna","Vilma","Wendy","Yolanda","Zenaida","Belen","Carissa","Dianne",
    "Flor","Gretchen","Honey","Irene","Karla","Lani","Maribel","Odessa",
    "Patrice","Sharmaine","Vienna","Zyra"]

first_names_thai = ["Ploy","Praew","Pim","Mint","Nam","Fah","Fern","Fon","Ying","Ning",
    "Wanida","Sudarat","Supatra","Siriporn","Thanyarat","Natnicha","Pimchanok",
    "Phailin","Kanchana","Sukanya","Rinrada","Waranya","Sasithorn","Narumol",
    "Busaba","Lalita","Jintana","Saowanee","Malee","Kannika","Araya","Chalida",
    "Chanida","Daranee","Duangkamol","Jariya","Kamonwan","Kasalong","Ketsara",
    "Mananya","Nicha","Nichada","Nisara","Nonglak","Orathai","Panadda",
    "Pensri","Phatchara","Pimdao","Pimnara","Preeya","Rachanee","Ratree",
    "Sunisa","Supaporn","Suwanna","Tanyarat","Thida","Tipawan","Wanwisa",
    "Wilai","Yada","Anchalee","Benjamas","Chompoo","Duangjai","Intira",
    "Kalaya","Ladda","Lawan","Maleewan","Monthira","Petchara","Sineenat",
    "Sopa","Thanaporn","Thidarat","Urai","Wassana","Yuwadee","Anong",
    "Busarakham","Patcharaporn","Chanoknan","Pattarawadee","Kanyarat",
    "Napassorn","Kornkanok","Sirinya","Thanida","Natcha","Piyaporn",
    "Chutima","Kewalin","Apsara","Aree","Areeya","Atchara","Benya",
    "Buppha","Chaba","Chailai","Chanthira","Charinrat","Chotika","Darika",
    "Dawan","Duangdao","Duangporn","Janjira","Jarunee","Jirapa","Jiraporn",
    "Jutharat","Kaewta","Kamolchanok","Kamonrat","Kanlaya","Kanokwan",
    "Karuna","Kasama","Khemika","Khwanjai","Kittiya","Kulaya","Kulchaya",
    "Lakkhana","Malinee","Manee","Methinee","Napaporn","Naphatsorn",
    "Natthaya","Nattida","Nawarat","Noina","Nuanchan","Onuma","Orasa",
    "Papatsorn","Parichat","Pensuda","Petchpailin","Phensri","Phimlada",
    "Phitchaya","Phornphan","Pikul","Pinthip","Piyawan","Porntip",
    "Pranisa","Prapha","Rapeeporn","Rattanaporn","Renu","Rojjana",
    "Romyen","Rungnapa","Rungthip","Saengdao","Saowalak","Saranya",
    "Sasima","Sasiwimon","Sirikanya","Sirikwan","Sirinapa","Sirirat",
    "Siriwan","Somporn","Somsri","Suchada","Sudaporn","Sujitra",
    "Sukanda","Sunee","Sunantha","Supansa","Sureeporn","Suthida",
    "Tassanee","Thanchanok","Thanyalak","Thanyaporn","Thipphawan",
    "Thongbai","Ubonrat","Usa","Wanpen","Waraporn","Wilawan","Yanin",
    "Yupa","Yupin","Aom","Aye","Bam","Beam","Belle","Bow","Cake",
    "Dream","Gift","Grace","Ice","Jam","Jane","Jib","Jin","Joy",
    "Kaew","Kaimook","Kwan","May","Meen","Mew","Mind","Mook","Nan",
    "Nana","New","Noey","Nook","Nui","Oil","Pang","Pear","Prae",
    "Proud","Sai","Sand","Som","Tarn","Toey","View","Yui","Zani"]

first_names_id = ["Robert", "James", "John", "William", "Charles", "George", "Joseph",
    "Thomas", "Richard", "Edward", "Donald", "Frank", "Harold", "Raymond",
    "Walter", "Arthur", "Albert", "Henry", "Carl", "Roy", "Ralph",
    "Earl", "Fred", "Howard", "Ernest", "Clarence", "Willie", "Louis",
    "Kenneth", "Gerald", "Ronald", "Donald", "Dennis", "Douglas", "Roger",
    "Larry", "Lawrence", "Russell", "Jack", "Bruce", "Wayne", "Norman",
    "Leonard", "Melvin", "Leroy", "Herbert", "Marvin", "Bernard", "Clifford",
    "Dorothy", "Mary", "Patricia", "Barbara", "Betty", "Carol", "Shirley",
    "Margaret", "Ruth", "Helen", "Elizabeth", "Frances", "Virginia",
    "Mildred", "Evelyn", "Florence", "Alice", "Edna", "Edith", "Gladys",
    "Hazel", "Irene", "Louise", "Marjorie", "Doris", "Jean", "Marilyn",
    "Joan", "Phyllis", "Norma", "Lois", "Gloria", "Beverly", "Sharon",
    "Joyce", "Rose", "Theresa", "Ann", "Jeanette", "Clara", "Beatrice",
    "Lillian", "Pearl", "Agnes", "Gertrude", "Catherine", "Martha",
    "Esther", "Pauline", "Eleanor", "Lucille", "Maxine", "Wilma"]

def generate_phone_number():
    countries={'BD': {'code': '+880', 'prefixes': ['17', '18', '19', '16'], 'length': 8},
        'IN': {'code': '+91', 'prefixes': ['98', '99', '97', '96'], 'length': 8},
        'PK': {'code': '+92', 'prefixes': ['300', '301', '302'], 'length': 7},
        'NP': {'code': '+977', 'prefixes': ['98', '97'], 'length': 8},
        'LK': {'code': '+94', 'prefixes': ['70', '71', '72'], 'length': 7},
        'PH': {'code': '+63', 'prefixes': ['917', '918', '919'], 'length': 7},
        'ID': {'code': '+62', 'prefixes': ['813', '815', '816'], 'length': 7},
        'MY': {'code': '+60', 'prefixes': ['11', '12', '13'], 'length': 7},
        'TH': {'code': '+66', 'prefixes': ['81', '82', '84'], 'length': 7},
        'VN': {'code': '+84', 'prefixes': ['32', '33', '34'], 'length': 7},
        'KH': {'code': '+855', 'prefixes': ['10', '11', '12'], 'length': 6},
        'CN': {'code': '+86', 'prefixes': ['130', '131', '132'], 'length': 8},
        'JP': {'code': '+81', 'prefixes': ['70', '80', '90'], 'length': 8},
        'KR': {'code': '+82', 'prefixes': ['10'], 'length': 8},
        'SG': {'code': '+65', 'prefixes': ['8', '9'], 'length': 7},
        'SA': {'code': '+966', 'prefixes': ['50', '53', '55'], 'length': 7},
        'AE': {'code': '+971', 'prefixes': ['50', '52', '54'], 'length': 7},
        'OM': {'code': '+968', 'prefixes': ['71', '72', '73'], 'length': 6},
        'QA': {'code': '+974', 'prefixes': ['30', '33', '55'], 'length': 6},
        'KW': {'code': '+965', 'prefixes': ['5', '6', '9'], 'length': 7},
        'UK': {'code': '+44', 'prefixes': ['7400', '7500'], 'length': 6},
        'FR': {'code': '+33', 'prefixes': ['6', '7'], 'length': 8},
        'DE': {'code': '+49', 'prefixes': ['15', '16', '17'], 'length': 8},
        'IT': {'code': '+39', 'prefixes': ['31', '32', '33'], 'length': 7},
        'ES': {'code': '+34', 'prefixes': ['6', '7'], 'length': 8},
        'RU': {'code': '+7', 'prefixes': ['91', '92', '93'], 'length': 8},
        'NG': {'code': '+234', 'prefixes': ['701', '703', '705'], 'length': 7},
        'ZA': {'code': '+27', 'prefixes': ['60', '61', '71'], 'length': 7},
        'EG': {'code': '+20', 'prefixes': ['10', '11', '12'], 'length': 8},
        'KE': {'code': '+254', 'prefixes': ['70', '71', '72'], 'length': 7},
        'US': {'code': '+1', 'prefixes': ['201', '202', '303'], 'length': 7},
        'CA': {'code': '+1', 'prefixes': ['204', '236', '249'], 'length': 7},
        'MX': {'code': '+52', 'prefixes': ['55', '81', '33'], 'length': 8},
        'BR': {'code': '+55', 'prefixes': ['11', '21', '31'], 'length': 8},
        'AR': {'code': '+54', 'prefixes': ['11', '221', '261'], 'length': 7},
        'CO': {'code': '+57', 'prefixes': ['300', '301', '302'], 'length': 7},
        'AU': {'code': '+61', 'prefixes': ['4'], 'length': 8},
        'NZ': {'code': '+64', 'prefixes': ['20', '21', '22'], 'length': 7},
        'CI': {'code': '+225', 'prefixes': ['01', '05', '07'], 'length': 8},
        'AD': {'code': '+376', 'prefixes': ['3', '4', '6'], 'length': 6},
        'AX': {'code': '+358', 'prefixes': ['40', '41', '45', '50'], 'length': 7},
        'TJ': {'code': '+992', 'prefixes': ['90', '91', '92', '93'], 'length': 7},
        'TK': {'code': '+690', 'prefixes': ['2', '3', '5'], 'length': 4},
        'TL': {'code': '+670', 'prefixes': ['77', '78'], 'length': 6}}
    country=random.choice(list(countries.keys()))
    info=countries[country]
    prefix=random.choice(info['prefixes'])
    number=''.join(random.choices(string.digits,k=info['length']))
    full_number=f"{info['code']}{prefix}{number}"
    return full_number

def fake_gmail():
    name=''.join(random.choices(string.ascii_lowercase+string.digits,k=10))
    num=''.join(random.choices(string.digits,k=random.randint(3,6)))
    return f"{name}{num}@gmail.com"

def fake_hotmail():
    name=''.join(random.choices(string.ascii_lowercase+string.digits,k=10))
    num=''.join(random.choices(string.digits,k=random.randint(3,6)))
    domains=["hotmail.com","hotmail.org","hotmail.ph"]
    return f"{name}{num}@{random.choice(domains)}"

def auto_pass():
    names=["Ethan","EthanPogi"]
    symbols=["@","#","$","&","_"]
    name=random.choice(names)
    symbol=random.choice(symbols)
    number=''.join(random.choices(string.digits,k=random.randint(3,6)))
    password=f"{name}{symbol}{number}"
    return password

def get_ph_name():
    first=random.choice(first_names_ph)
    return first

def get_thai_name():
    first=random.choice(first_names_thai)
    return first

def get_id_name():
    first=random.choice(first_names_id)
    return first

console=Console()
oks=[]
cps=[]
alive=[]
dead=[]
ok_count=0
cp_count=0
alive_count=0
dead_count=0

def extractor(data):
    soup=BeautifulSoup(data,"html.parser")
    data={}
    for inputs in soup.find_all("input"):
        name=inputs.get("name")
        value=inputs.get("value")
        if name:
            data[name]=value
    return data

ip=requests.get("https://api.ipify.org").text
ip_info=requests.post(f"http://ip-api.com/json/{ip}")
af=json.loads(ip_info.text)
negara=af['country'].upper()

bulan={'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10': 'October', '11': 'November', '12': 'December'}
tgl=datetime.now().day
bln=bulan[(str(datetime.now().month))]
thn=datetime.now().year
tanggal=(str(tgl)+' '+str(bln)+' '+str(thn))
waktu=strftime('%H:%M:%S')
hari=datetime.now().strftime("%A")

logo=("""   [green1]███████╗██╗     ██╗███╗   ███╗
   [spring_green2]██╔════╝██║     ██║████╗ ████║
   [medium_spring_green]███████╗██║     ██║██╔████╔██║
   [cyan2]╚════██║██║     ██║██║╚██╔╝██║
   [cyan1]███████║███████╗██║██║ ╚═╝ ██║
   [cyan1]╚══════╝╚══════╝╚═╝╚═╝     ╚═╝
          [cyan][bold]VERSION/0.9
   [green_yellow]MY [dark_olive_gre]SYSTEM[pale_green1] IS[dark_sea_green] DIFFERENT BROTHER""")
ll=str([hari,tanggal])
access_key = "TEST"
hx = f"""  [bold green1]AUTHOR[bold white]      ▶︎ [cyan][bold]SLIM
  [bold green1]FACEBOOK[bold white]    ▶︎ [cyan][bold]ETHAN KLEIN HUILEN
  [bold green1]STATUS[bold white]      ▶︎ [cyan][bold]PAID
  [bold green1]BESTFRIEND[bold white]  ▶︎ [cyan][bold]ASIM CHUZA ARNOLD MUJIB SYED SHANU
  [bold green1]TYPE[bold white]        ▶︎ [cyan][bold]AUTO CREATE FACEBOOK
  [bold green1]GITHUB[bold white]      ▶︎ [cyan][bold]MR-ERROR-807
  [bold green1]COUNTRY[bold white]     ▶︎ [cyan][bold]{negara}
  [bold green1]TODAY DATE[bold white]  ▶︎ [green]{ll}
  [bold green1]ACCESS KEY[bold white]  ▶︎ [green]{access_key}"""
def clear():
    os.system('cls' if platform.system().lower() == 'windows' else 'clear')
    rprint(pan(logo,subtitle="[bold red]● [bright_yellow]● [green1]●",subtitle_align='left',title="[bold red]● [bright_yellow]● [green1]●",title_align='right',width=102,padding=0,style="bold cyan1"))
    rprint(pan(hx,subtitle="[bold red]● [bright_yellow]● [green1]●",subtitle_align='left',title="[bold red]● [bright_yellow]● [green1]●",title_align='right',width=102,padding=0,style="bold cyan1"))

def main():
    clear()
    rprint(pan(f"""[bold white][[bold green1]01[bold white]][bold green1] START AUTO CREATE FACEBOOK\n[bold white][[bold red]00[bold white]][bold red] EXIT TOOLS""",width=102,border_style=f"bold cyan1"))
    Error=input(f" \033[1;37mChoose Number \033[1;37m▶︎ \033[1;32m")
    if Error in ["1","01"]:
        auto_method()
    elif Error in ["0","00"]:
        exit()
    else:
        main()

def auto_method():
    clear()
    rprint(pan(f"""[bold white][[bold green1]01[bold white]][bold green1] METHOD (x.facebook.com)\n[bold white][[bold green1]02[bold white]][bold green1] METHOD (p.facebook.com)\n[bold white][[bold green1]03[bold white]][bold green1] METHOD (mbasic.facebook.com)\n[bold white][[bold green1]04[bold white]][bold green1] METHOD (touch.facebook.com)\n[bold white][[bold green1]05[bold white]][bold green1] METHOD (m.alpha.facebook.com)\n[bold white][[bold green1]06[bold white]][bold green1] METHOD (m.beta.facebook.com)""",width=102,border_style=f"bold cyan1"))
    Error=input(f" \033[1;37mChoose Method Number \033[1;37m▶︎ \033[1;32m")
    if Error in ["1","01"]:
        auto_create_method_1()
    elif Error in ["2","02"]:
        auto_create_method_2()
    elif Error in ["3","03"]:
        auto_create_method_3()
    elif Error in ["4","04"]:
        auto_create_method_4()
    elif Error in ["5","05"]:
        auto_create_method_5()
    elif Error in ["6","06"]:
        auto_create_method_6()
    else:
        auto_method()

def check_facebook_profile_picture(uid):
    pic_url=f"https://graph.facebook.com/{uid}/picture?type=normal"
    headers={"User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36"}
    try:
        response=requests.get(pic_url,headers=headers,allow_redirects=False)
        if response.status_code==302:
            redirect_url=response.headers.get("Location","")
            if "scontent" in redirect_url:
                return "live"
            else:
                return "not_live"
        else:
            return
    except requests.RequestException as e:
        return

def progres(current,num,delay):
    for sleep in range(int(delay),0,-1):
        print(f'''\r {W}ETHAN-CREATE{W} {G}ALIVE:{G}{len(alive)}{W} {W}▶︎ {R}DEAD:{R}{len(dead)}''',end='\x1b[1;37m')
        time.sleep(1)
        if not current==num:
            pass

def auto_create_method_1():
    clear()
    names=[("01","RANDOM NAME PHILIPPINES"),("02","RANDOM NAME THAILAND"),("03","RANDOM NAME INDONESIA")]
    menu="\n".join(f"[bold white][[bold green1]{num}[bold white]] [bold green1]{name}"for num,name in names)
    rprint(pan(menu,width=102,border_style=f"bold cyan1"))
    name_error=input(f" \033[1;37mChoose Name Number \033[1;37m▶︎ \033[1;32m")
    clear()
    emails=[("01","TEMP MIX NUMBER COUNTRY 1"),("02","TEMP GMAIL MAIL 2"),("03","TEMP HOMAIL MAIL 3")]
    menu="\n".join(f"[bold white][[bold green1]{num}[bold white]] [bold green1]{name}"for num,name in emails)
    rprint(pan(menu,width=102,border_style=f"bold cyan1"))
    email_number_error=input(f" \033[1;37mChoose Number/Email Number \033[1;37m▶︎ \033[1;32m")
    clear()
    try:
        num=int(input(f" \033[1;37mHow Many Create Account Limit \033[1;37m▶︎ \033[1;32m"))
    except ValueError:
        num=9
    clear()
    rprint(pan(f"""[bold white][[bold green1]01[bold white]][bold green1] AUTO PASSWORD\n[bold white][[bold green1]02[bold white]][bold green1] CUSTOM PASSWORD""",width=102,border_style=f"bold cyan1"))
    pasw=input(f" \033[1;37mChoose Password Number \033[1;37m▶︎ \033[1;32m")
    if pasw in ["2","02"]:
      pww=input(f" \033[1;37mEnter Customer Password \033[1;37m▶︎ \033[1;32m")
    clear()
    try:
        delay=int(input(f" \033[1;37mEnter Between Time \033[1;37m▶︎ \033[1;32m"))
    except ValueError:
        delay=2
    clear()
    rprint(pan(f""" [bold white]TOTAL ID [bold white]▶︎ [bold  green]{num}\n [bold cyan]ACCOUNT CREATING STARTED\n [bold white]USE VPN 1.1.1.1 OR USE AIRPLANE MODE ON/OFF 5 MINUTE""",width=102,border_style=f"bold cyan1"))
    for i in range(num):
        try:
            global alive,dead
            progres(i+1,num,delay)
            ses=requests.Session()
            response=ses.get("https://x.facebook.com/reg")
            form=extractor(response.text)
            if name_error in ["1","01"]:
               firstname=get_ph_name()
            elif name_error in ["2","02"]:
               firstname=get_thai_name()
            elif name_error in ["3","03"]:
               firstname=get_id_name()
            if email_number_error in ["1","01"]:
               phone=generate_phone_number()
            elif email_number_error in ["2","02"]:
               phone=fake_gmail()
            elif email_number_error in ["3","03"]:
               phone=fake_hotmail() 
            if pasw in ["1","01"]:
               pww=auto_pass()
            label="NUMBER" if email_number_error in ["1","01"] else "EMAIL"
            payload={'ccp': "2",
            'reg_instance': form.get("reg_instance",""),
            'submission_request': "true",
            'reg_impression_id': form.get("reg_impression_id",""),
            'ns': "1",
            'logger_id': form.get("logger_id",""),
            'firstname': firstname,
            'birthday_day': str(random.randint(15,25)),
            'birthday_month': str(random.randint(5,10)),
            'birthday_year': str(random.randint(1946,1960)),
            'reg_email__': phone,
            'sex': "1",
            'encpass': f'#PWD_BROWSER:0:{int(time.time())}:{pww}',
            'submit': "Sign Up",
            'fb_dtsg': form.get("fb_dtsg",""),
            'jazoest': form.get("jazoest",""),
            'lsd': form.get("lsd","")}
            headers={"Host": "m.facebook.com",
            "Connection": "keep-alive",
            "User-Agent": auto_error_ua1(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9"}
            head1={'accept-encoding': 'gzip, deflate',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'referer': 'https://mbasic.facebook.com/reg/',
            'sec-ch-ua': '',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': 'Android',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': auto_error_ua1()}
            merged_headers={**headers,**head1}
            reg_url="https://www.facebook.com/reg/submit/"
            reg_submit=ses.post(reg_url,data=payload,headers=merged_headers)
            login_coki=ses.cookies.get_dict()
            if "c_user" in login_coki:
               coki=";".join([f"{key}={value}" for key, value in login_coki.items()])
               uid=login_coki["c_user"]
               status=check_facebook_profile_picture(uid)
               if status=="live":
                  print("\n")
                  info={"NAME": firstname,label: phone,"GENDER": "Female","BIRTHDAY": f"{payload['birthday_day']}-{payload['birthday_month']}-{payload['birthday_year']}","UID": uid,"PASS": pww,"COOKIE": coki,"FBLINK": f"facebook.com/{uid}",}
                  for k,v in info.items():
                      print(f'''\r {W}{k:<10}▶︎ {G}{v}{X}''')
                  print()
                  try:
                      with open('/sdcard/AUTO-XD/AUTO/AUTO_CREATE_M1.txt','a') as f:
                            f.write(f"{uid}|{pww}\n")
                      alive.append(uid)
                  except IOError:
                      continue
               else:
                  dead.append(uid)
            elif "checkpoint" in login_coki:
               uid=login_coki.get("c_user","unknown")
               dead.append(uid)
               time.sleep(1)
        except Exception as e:
            time.sleep(5)
            continue

def auto_create_method_2():
    clear()
    names=[("01","RANDOM NAME PHILIPPINES"),("02","RANDOM NAME THAILAND"),("03","RANDOM NAME INDONESIA")]
    menu="\n".join(f"[bold white][[bold green1]{num}[bold white]] [bold green1]{name}"for num,name in names)
    rprint(pan(menu,width=102,border_style=f"bold cyan1"))
    name_error=input(f" \033[1;37mChoose Name Number \033[1;37m▶︎ \033[1;32m")
    clear()
    emails=[("01","TEMP MIX NUMBER COUNTRY 1"),("02","TEMP GMAIL MAIL 2"),("03","TEMP HOMAIL MAIL 3")]
    menu="\n".join(f"[bold white][[bold green1]{num}[bold white]] [bold green1]{name}"for num,name in emails)
    rprint(pan(menu,width=102,border_style=f"bold cyan1"))
    email_number_error=input(f" \033[1;37mChoose Number/Email Number \033[1;37m▶︎ \033[1;32m")
    clear()
    try:
        num=int(input(f" \033[1;37mHow Many Create Account Limit \033[1;37m▶︎ \033[1;32m"))
    except ValueError:
        num=9
    clear()
    rprint(pan(f"""[bold white][[bold green1]01[bold white]][bold green1] AUTO PASSWORD\n[bold white][[bold green1]02[bold white]][bold green1] CUSTOM PASSWORD""",width=102,border_style=f"bold cyan1"))
    pasw=input(f" \033[1;37mChoose Password Number \033[1;37m▶︎ \033[1;32m")
    if pasw in ["2","02"]:
      pww=input(f" \033[1;37mEnter Customer Password \033[1;37m▶︎ \033[1;32m")
    clear()
    try:
        delay=int(input(f" \033[1;37mEnter Between Time \033[1;37m▶︎ \033[1;32m"))
    except ValueError:
        delay=2
    clear()
    rprint(pan(f""" [bold white]TOTAL ID [bold white]▶︎ [bold  green]{num}\n [bold cyan]ACCOUNT CREATING STARTED\n [bold white]USE VPN 1.1.1.1 OR USE AIRPLANE MODE ON/OFF 5 MINUTE""",width=102,border_style=f"bold cyan1"))
    for i in range(num):
        try:
            global alive,dead
            progres(i+1,num,delay)
            ses=requests.Session()
            response=ses.get("https://p.facebook.com/reg")
            form=extractor(response.text)
            if name_error in ["1","01"]:
               firstname=get_ph_name()
            elif name_error in ["2","02"]:
               firstname=get_thai_name()
            elif name_error in ["3","03"]:
               firstname=get_id_name()
            if email_number_error in ["1","01"]:
               phone=generate_phone_number()
            elif email_number_error in ["2","02"]:
               phone=fake_gmail()
            elif email_number_error in ["3","03"]:
               phone=fake_hotmail() 
            if pasw in ["1","01"]:
               pww=auto_pass()
            label="NUMBER" if email_number_error in ["1","01"] else "EMAIL"
            payload={'ccp': "2",
            'reg_instance': form.get("reg_instance",""),
            'submission_request': "true",
            'reg_impression_id': form.get("reg_impression_id",""),
            'ns': "1",
            'logger_id': form.get("logger_id",""),
            'firstname': firstname,
            'birthday_day': str(random.randint(15,25)),
            'birthday_month': str(random.randint(5,10)),
            'birthday_year': str(random.randint(1985,1995)),
            'reg_email__': phone,
            'sex': "1",
            'encpass': f'#PWD_BROWSER:0:{int(time.time())}:{pww}',
            'submit': "Sign Up",
            'fb_dtsg': form.get("fb_dtsg",""),
            'jazoest': form.get("jazoest",""),
            'lsd': form.get("lsd","")}
            headers={"Host": "m.facebook.com",
            "Connection": "keep-alive",
            "User-Agent": auto_error_ua1(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9"}
            head1={'accept-encoding': 'gzip, deflate',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'referer': 'https://mbasic.facebook.com/reg/',
            'sec-ch-ua': '',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': 'Android',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': auto_error_ua1()}
            merged_headers={**headers,**head1}
            reg_url="https://www.facebook.com/reg/submit/"
            reg_submit=ses.post(reg_url,data=payload,headers=merged_headers)
            login_coki=ses.cookies.get_dict()
            if "c_user" in login_coki:
               coki=";".join([f"{key}={value}" for key, value in login_coki.items()])
               uid=login_coki["c_user"]
               status=check_facebook_profile_picture(uid)
               if status=="live":
                  print("\n")
                  info={"NAME": firstname,label: phone,"GENDER": "Female","BIRTHDAY": f"{payload['birthday_day']}-{payload['birthday_month']}-{payload['birthday_year']}","UID": uid,"PASS": pww,"COOKIE": coki,"FBLINK": f"facebook.com/{uid}",}
                  for k,v in info.items():
                      print(f'''\r {W}{k:<10}▶︎ {G}{v}{X}''')
                  print()
                  try:
                      with open('/sdcard/AUTO-XD/AUTO/AUTO_CREATE_M2.txt','a') as f:
                            f.write(f"{uid}|{pww}\n")
                      alive.append(uid)
                  except IOError:
                      continue
               else:
                  dead.append(uid)
            elif "checkpoint" in login_coki:
               uid=login_coki.get("c_user","unknown")
               dead.append(uid)
               time.sleep(1)
        except Exception as e:
            time.sleep(5)
            continue

def auto_create_method_3():
    clear()
    names=[("01","RANDOM NAME PHILIPPINES"),("02","RANDOM NAME THAILAND"),("03","RANDOM NAME INDONESIA")]
    menu="\n".join(f"[bold white][[bold green1]{num}[bold white]] [bold green1]{name}"for num,name in names)
    rprint(pan(menu,width=102,border_style=f"bold cyan1"))
    name_error=input(f" \033[1;37mChoose Name Number \033[1;37m▶︎ \033[1;32m")
    clear()
    emails=[("01","TEMP MIX NUMBER COUNTRY 1"),("02","TEMP GMAIL MAIL 2"),("03","TEMP HOMAIL MAIL 3")]
    menu="\n".join(f"[bold white][[bold green1]{num}[bold white]] [bold green1]{name}"for num,name in emails)
    rprint(pan(menu,width=102,border_style=f"bold cyan1"))
    email_number_error=input(f" \033[1;37mChoose Number/Email Number \033[1;37m▶︎ \033[1;32m")
    clear()
    try:
        num=int(input(f" \033[1;37mHow Many Create Account Limit \033[1;37m▶︎ \033[1;32m"))
    except ValueError:
        num=9
    clear()
    rprint(pan(f"""[bold white][[bold green1]01[bold white]][bold green1] AUTO PASSWORD\n[bold white][[bold green1]02[bold white]][bold green1] CUSTOM PASSWORD""",width=102,border_style=f"bold cyan1"))
    pasw=input(f" \033[1;37mChoose Password Number \033[1;37m▶︎ \033[1;32m")
    if pasw in ["2","02"]:
      pww=input(f" \033[1;37mEnter Customer Password \033[1;37m▶︎ \033[1;32m")
    clear()
    try:
        delay=int(input(f" \033[1;37mEnter Between Time \033[1;37m▶︎ \033[1;32m"))
    except ValueError:
        delay=2
    clear()
    rprint(pan(f""" [bold white]TOTAL ID [bold white]▶︎ [bold  green]{num}\n [bold cyan]ACCOUNT CREATING STARTED\n [bold white]USE VPN 1.1.1.1 OR USE AIRPLANE MODE ON/OFF 5 MINUTE""",width=102,border_style=f"bold cyan1"))
    for i in range(num):
        try:
            global alive,dead
            progres(i+1,num,delay)
            ses=requests.Session()
            response=ses.get("https://mbasic.facebook.com/reg")
            form=extractor(response.text)
            if name_error in ["1","01"]:
               firstname=get_ph_name()
            elif name_error in ["2","02"]:
               firstname=get_thai_name()
            elif name_error in ["3","03"]:
               firstname=get_id_name()
            if email_number_error in ["1","01"]:
               phone=generate_phone_number()
            elif email_number_error in ["2","02"]:
               phone=fake_gmail()
            elif email_number_error in ["3","03"]:
               phone=fake_hotmail() 
            if pasw in ["1","01"]:
               pww=auto_pass()
            label="NUMBER" if email_number_error in ["1","01"] else "EMAIL"
            payload={'ccp': "2",
            'reg_instance': form.get("reg_instance",""),
            'submission_request': "true",
            'reg_impression_id': form.get("reg_impression_id",""),
            'ns': "1",
            'logger_id': form.get("logger_id",""),
            'firstname': firstname,
            'birthday_day': str(random.randint(15,25)),
            'birthday_month': str(random.randint(5,10)),
            'birthday_year': str(random.randint(1985,1995)),
            'reg_email__': phone,
            'sex': "1",
            'encpass': f'#PWD_BROWSER:0:{int(time.time())}:{pww}',
            'submit': "Sign Up",
            'fb_dtsg': form.get("fb_dtsg",""),
            'jazoest': form.get("jazoest",""),
            'lsd': form.get("lsd","")}
            headers={"Host": "m.facebook.com",
            "Connection": "keep-alive",
            "User-Agent": auto_error_ua1(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9"}
            head1={'accept-encoding': 'gzip, deflate',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'referer': 'https://mbasic.facebook.com/reg/',
            'sec-ch-ua': '',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': 'Android',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': auto_error_ua1()}
            merged_headers={**headers,**head1}
            reg_url="https://www.facebook.com/reg/submit/"
            reg_submit=ses.post(reg_url,data=payload,headers=merged_headers)
            login_coki=ses.cookies.get_dict()
            if "c_user" in login_coki:
               coki=";".join([f"{key}={value}" for key, value in login_coki.items()])
               uid=login_coki["c_user"]
               status=check_facebook_profile_picture(uid)
               if status=="live":
                  print("\n")
                  info={"NAME": firstname,label: phone,"GENDER": "Female","BIRTHDAY": f"{payload['birthday_day']}-{payload['birthday_month']}-{payload['birthday_year']}","UID": uid,"PASS": pww,"COOKIE": coki,"FBLINK": f"facebook.com/{uid}",}
                  for k,v in info.items():
                      print(f'''\r {W}{k:<10}▶︎ {G}{v}{X}''')
                  print()
                  try:
                      with open('/sdcard/AUTO-XD/AUTO/AUTO_CREATE_M3.txt','a') as f:
                            f.write(f"{uid}|{pww}\n")
                      alive.append(uid)
                  except IOError:
                      continue
               else:
                  dead.append(uid)
            elif "checkpoint" in login_coki:
               uid=login_coki.get("c_user","unknown")
               dead.append(uid)
               time.sleep(1)
        except Exception as e:
            time.sleep(5)
            continue

def auto_create_method_4():
    clear()
    names=[("01","RANDOM NAME PHILIPPINES"),("02","RANDOM NAME THAILAND"),("03","RANDOM NAME INDONESIA")]
    menu="\n".join(f"[bold white][[bold green1]{num}[bold white]] [bold green1]{name}"for num,name in names)
    rprint(pan(menu,width=102,border_style=f"bold cyan1"))
    name_error=input(f" \033[1;37mChoose Name Number \033[1;37m▶︎ \033[1;32m")
    clear()
    emails=[("01","TEMP MIX NUMBER COUNTRY 1"),("02","TEMP GMAIL MAIL 2"),("03","TEMP HOMAIL MAIL 3")]
    menu="\n".join(f"[bold white][[bold green1]{num}[bold white]] [bold green1]{name}"for num,name in emails)
    rprint(pan(menu,width=102,border_style=f"bold cyan1"))
    email_number_error=input(f" \033[1;37mChoose Number/Email Number \033[1;37m▶︎ \033[1;32m")
    clear()
    try:
        num=int(input(f" \033[1;37mHow Many Create Account Limit \033[1;37m▶︎ \033[1;32m"))
    except ValueError:
        num=9
    clear()
    rprint(pan(f"""[bold white][[bold green1]01[bold white]][bold green1] AUTO PASSWORD\n[bold white][[bold green1]02[bold white]][bold green1] CUSTOM PASSWORD""",width=102,border_style=f"bold cyan1"))
    pasw=input(f" \033[1;37mChoose Password Number \033[1;37m▶︎ \033[1;32m")
    if pasw in ["2","02"]:
      pww=input(f" \033[1;37mEnter Customer Password \033[1;37m▶︎ \033[1;32m")
    clear()
    try:
        delay=int(input(f" \033[1;37mEnter Between Time \033[1;37m▶︎ \033[1;32m"))
    except ValueError:
        delay=2
    clear()
    rprint(pan(f""" [bold white]TOTAL ID [bold white]▶︎ [bold  green]{num}\n [bold cyan]ACCOUNT CREATING STARTED\n [bold white]USE VPN 1.1.1.1 OR USE AIRPLANE MODE ON/OFF 5 MINUTE""",width=102,border_style=f"bold cyan1"))
    for i in range(num):
        try:
            global alive,dead
            progres(i+1,num,delay)
            ses=requests.Session()
            response=ses.get("https://touch.facebook.com/reg")
            form=extractor(response.text)
            if name_error in ["1","01"]:
               firstname=get_ph_name()
            elif name_error in ["2","02"]:
               firstname=get_thai_name()
            elif name_error in ["3","03"]:
               firstname=get_id_name()
            if email_number_error in ["1","01"]:
               phone=generate_phone_number()
            elif email_number_error in ["2","02"]:
               phone=fake_gmail()
            elif email_number_error in ["3","03"]:
               phone=fake_hotmail() 
            if pasw in ["1","01"]:
               pww=auto_pass()
            label="NUMBER" if email_number_error in ["1","01"] else "EMAIL"
            payload={'ccp': "2",
            'reg_instance': form.get("reg_instance",""),
            'submission_request': "true",
            'reg_impression_id': form.get("reg_impression_id",""),
            'ns': "1",
            'logger_id': form.get("logger_id",""),
            'firstname': firstname,
            'birthday_day': str(random.randint(15,25)),
            'birthday_month': str(random.randint(5,10)),
            'birthday_year': str(random.randint(1985,1995)),
            'reg_email__': phone,
            'sex': "1",
            'encpass': f'#PWD_BROWSER:0:{int(time.time())}:{pww}',
            'submit': "Sign Up",
            'fb_dtsg': form.get("fb_dtsg",""),
            'jazoest': form.get("jazoest",""),
            'lsd': form.get("lsd","")}
            headers={"Host": "m.facebook.com",
            "Connection": "keep-alive",
            "User-Agent": auto_error_ua1(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9"}
            head1={'accept-encoding': 'gzip, deflate',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'referer': 'https://mbasic.facebook.com/reg/',
            'sec-ch-ua': '',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': 'Android',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': auto_error_ua1()}
            merged_headers={**headers,**head1}
            reg_url="https://www.facebook.com/reg/submit/"
            reg_submit=ses.post(reg_url,data=payload,headers=merged_headers)
            login_coki=ses.cookies.get_dict()
            if "c_user" in login_coki:
               coki=";".join([f"{key}={value}" for key, value in login_coki.items()])
               uid=login_coki["c_user"]
               status=check_facebook_profile_picture(uid)
               if status=="live":
                  print("\n")
                  info={"NAME": firstname,label: phone,"GENDER": "Female","BIRTHDAY": f"{payload['birthday_day']}-{payload['birthday_month']}-{payload['birthday_year']}","UID": uid,"PASS": pww,"COOKIE": coki,"FBLINK": f"facebook.com/{uid}",}
                  for k,v in info.items():
                      print(f'''\r {W}{k:<10}▶︎ {G}{v}{X}''')
                  print()
                  try:
                      with open('/sdcard/AUTO-XD/AUTO/AUTO_CREATE_M4.txt','a') as f:
                            f.write(f"{uid}|{pww}\n")
                      alive.append(uid)
                  except IOError:
                      continue
               else:
                  dead.append(uid)
            elif "checkpoint" in login_coki:
               uid=login_coki.get("c_user","unknown")
               dead.append(uid)
               time.sleep(1)
        except Exception as e:
            time.sleep(5)
            continue

def auto_create_method_5():
    clear()
    names=[("01","RANDOM NAME PHILIPPINES"),("02","RANDOM NAME THAILAND"),("03","RANDOM NAME INDONESIA")]
    menu="\n".join(f"[bold white][[bold green1]{num}[bold white]] [bold green1]{name}"for num,name in names)
    rprint(pan(menu,width=102,border_style=f"bold cyan1"))
    name_error=input(f" \033[1;37mChoose Name Number \033[1;37m▶︎ \033[1;32m")
    clear()
    emails=[("01","TEMP MIX NUMBER COUNTRY 1"),("02","TEMP GMAIL MAIL 2"),("03","TEMP HOMAIL MAIL 3")]
    menu="\n".join(f"[bold white][[bold green1]{num}[bold white]] [bold green1]{name}"for num,name in emails)
    rprint(pan(menu,width=102,border_style=f"bold cyan1"))
    email_number_error=input(f" \033[1;37mChoose Number/Email Number \033[1;37m▶︎ \033[1;32m")
    clear()
    try:
        num=int(input(f" \033[1;37mHow Many Create Account Limit \033[1;37m▶︎ \033[1;32m"))
    except ValueError:
        num=9
    clear()
    rprint(pan(f"""[bold white][[bold green1]01[bold white]][bold green1] AUTO PASSWORD\n[bold white][[bold green1]02[bold white]][bold green1] CUSTOM PASSWORD""",width=102,border_style=f"bold cyan1"))
    pasw=input(f" \033[1;37mChoose Password Number \033[1;37m▶︎ \033[1;32m")
    if pasw in ["2","02"]:
      pww=input(f" \033[1;37mEnter Customer Password \033[1;37m▶︎ \033[1;32m")
    clear()
    try:
        delay=int(input(f" \033[1;37mEnter Between Time \033[1;37m▶︎ \033[1;32m"))
    except ValueError:
        delay=2
    clear()
    rprint(pan(f""" [bold white]TOTAL ID [bold white]▶︎ [bold  green]{num}\n [bold cyan]ACCOUNT CREATING STARTED\n [bold white]USE VPN 1.1.1.1 OR USE AIRPLANE MODE ON/OFF 5 MINUTE""",width=102,border_style=f"bold cyan1"))
    for i in range(num):
        try:
            global alive,dead
            progres(i+1,num,delay)
            ses=requests.Session()
            response=ses.get("https://m.alpha.facebook.com/reg")
            form=extractor(response.text)
            if name_error in ["1","01"]:
               firstname=get_ph_name()
            elif name_error in ["2","02"]:
               firstname=get_thai_name()
            elif name_error in ["3","03"]:
               firstname=get_id_name()
            if email_number_error in ["1","01"]:
               phone=generate_phone_number()
            elif email_number_error in ["2","02"]:
               phone=fake_gmail()
            elif email_number_error in ["3","03"]:
               phone=fake_hotmail() 
            if pasw in ["1","01"]:
               pww=auto_pass()
            label="NUMBER" if email_number_error in ["1","01"] else "EMAIL"
            payload={'ccp': "2",
            'reg_instance': form.get("reg_instance",""),
            'submission_request': "true",
            'reg_impression_id': form.get("reg_impression_id",""),
            'ns': "1",
            'logger_id': form.get("logger_id",""),
            'firstname': firstname,
            'birthday_day': str(random.randint(15,25)),
            'birthday_month': str(random.randint(5,10)),
            'birthday_year': str(random.randint(1985,1995)),
            'reg_email__': phone,
            'sex': "1",
            'encpass': f'#PWD_BROWSER:0:{int(time.time())}:{pww}',
            'submit': "Sign Up",
            'fb_dtsg': form.get("fb_dtsg",""),
            'jazoest': form.get("jazoest",""),
            'lsd': form.get("lsd","")}
            headers={"Host": "m.facebook.com",
            "Connection": "keep-alive",
            "User-Agent": auto_error_ua1(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9"}
            head1={'accept-encoding': 'gzip, deflate',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'referer': 'https://mbasic.facebook.com/reg/',
            'sec-ch-ua': '',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': 'Android',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': auto_error_ua1()}
            merged_headers={**headers,**head1}
            reg_url="https://www.facebook.com/reg/submit/"
            reg_submit=ses.post(reg_url,data=payload,headers=merged_headers)
            login_coki=ses.cookies.get_dict()
            if "c_user" in login_coki:
               coki=";".join([f"{key}={value}" for key, value in login_coki.items()])
               uid=login_coki["c_user"]
               status=check_facebook_profile_picture(uid)
               if status=="live":
                  print("\n")
                  info={"NAME": firstname,label: phone,"GENDER": "Female","BIRTHDAY": f"{payload['birthday_day']}-{payload['birthday_month']}-{payload['birthday_year']}","UID": uid,"PASS": pww,"COOKIE": coki,"FBLINK": f"facebook.com/{uid}",}
                  for k,v in info.items():
                      print(f'''\r {W}{k:<10}▶︎ {G}{v}{X}''')
                  print()
                  try:
                      with open('/sdcard/AUTO-XD/AUTO/AUTO_CREATE_M5.txt','a') as f:
                            f.write(f"{uid}|{pww}\n")
                      alive.append(uid)
                  except IOError:
                      continue
               else:
                  dead.append(uid)
            elif "checkpoint" in login_coki:
               uid=login_coki.get("c_user","unknown")
               dead.append(uid)
               time.sleep(1)
        except Exception as e:
            time.sleep(5)
            continue

def auto_create_method_6():
    clear()
    names=[("01","RANDOM NAME PHILIPPINES"),("02","RANDOM NAME THAILAND"),("03","RANDOM NAME INDONESIA")]
    menu="\n".join(f"[bold white][[bold green1]{num}[bold white]] [bold green1]{name}"for num,name in names)
    rprint(pan(menu,width=102,border_style=f"bold cyan1"))
    name_error=input(f" \033[1;37mChoose Name Number \033[1;37m▶︎ \033[1;32m")
    clear()
    emails=[("01","TEMP MIX NUMBER COUNTRY 1"),("02","TEMP GMAIL MAIL 2"),("03","TEMP HOMAIL MAIL 3")]
    menu="\n".join(f"[bold white][[bold green1]{num}[bold white]] [bold green1]{name}"for num,name in emails)
    rprint(pan(menu,width=102,border_style=f"bold cyan1"))
    email_number_error=input(f" \033[1;37mChoose Number/Email Number \033[1;37m▶︎ \033[1;32m")
    clear()
    try:
        num=int(input(f" \033[1;37mHow Many Create Account Limit \033[1;37m▶︎ \033[1;32m"))
    except ValueError:
        num=9
    clear()
    rprint(pan(f"""[bold white][[bold green1]01[bold white]][bold green1] AUTO PASSWORD\n[bold white][[bold green1]02[bold white]][bold green1] CUSTOM PASSWORD""",width=102,border_style=f"bold cyan1"))
    pasw=input(f" \033[1;37mChoose Password Number \033[1;37m▶︎ \033[1;32m")
    if pasw in ["2","02"]:
      pww=input(f" \033[1;37mEnter Customer Password \033[1;37m▶︎ \033[1;32m")
    clear()
    try:
        delay=int(input(f" \033[1;37mEnter Between Time \033[1;37m▶︎ \033[1;32m"))
    except ValueError:
        delay=2
    clear()
    rprint(pan(f""" [bold white]TOTAL ID [bold white]▶︎ [bold  green]{num}\n [bold cyan]ACCOUNT CREATING STARTED\n [bold white]USE VPN 1.1.1.1 OR USE AIRPLANE MODE ON/OFF 5 MINUTE""",width=102,border_style=f"bold cyan1"))
    for i in range(num):
        try:
            global alive,dead
            progres(i+1,num,delay)
            ses=requests.Session()
            response=ses.get("https://m.beta.facebook.com/reg")
            form=extractor(response.text)
            if name_error in ["1","01"]:
               firstname=get_ph_name()
            elif name_error in ["2","02"]:
               firstname=get_thai_name()
            elif name_error in ["3","03"]:
               firstname=get_id_name()
            if email_number_error in ["1","01"]:
               phone=generate_phone_number()
            elif email_number_error in ["2","02"]:
               phone=fake_gmail()
            elif email_number_error in ["3","03"]:
               phone=fake_hotmail() 
            if pasw in ["1","01"]:
               pww=auto_pass()
            label="NUMBER" if email_number_error in ["1","01"] else "EMAIL"
            payload={'ccp': "2",
            'reg_instance': form.get("reg_instance",""),
            'submission_request': "true",
            'reg_impression_id': form.get("reg_impression_id",""),
            'ns': "1",
            'logger_id': form.get("logger_id",""),
            'firstname': firstname,
            'birthday_day': str(random.randint(15,25)),
            'birthday_month': str(random.randint(5,10)),
            'birthday_year': str(random.randint(1985,1995)),
            'reg_email__': phone,
            'sex': "1",
            'encpass': f'#PWD_BROWSER:0:{int(time.time())}:{pww}',
            'submit': "Sign Up",
            'fb_dtsg': form.get("fb_dtsg",""),
            'jazoest': form.get("jazoest",""),
            'lsd': form.get("lsd","")}
            headers={"Host": "m.facebook.com",
            "Connection": "keep-alive",
            "User-Agent": auto_error_ua1(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9"}
            head1={'accept-encoding': 'gzip, deflate',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'referer': 'https://mbasic.facebook.com/reg/',
            'sec-ch-ua': '',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': 'Android',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': auto_error_ua1()}
            merged_headers={**headers,**head1}
            reg_url="https://www.facebook.com/reg/submit/"
            reg_submit=ses.post(reg_url,data=payload,headers=merged_headers)
            login_coki=ses.cookies.get_dict()
            if "c_user" in login_coki:
               coki=";".join([f"{key}={value}" for key, value in login_coki.items()])
               uid=login_coki["c_user"]
               status=check_facebook_profile_picture(uid)
               if status=="live":
                  print("\n")
                  info={"NAME": firstname,label: phone,"GENDER": "Female","BIRTHDAY": f"{payload['birthday_day']}-{payload['birthday_month']}-{payload['birthday_year']}","UID": uid,"PASS": pww,"COOKIE": coki,"FBLINK": f"facebook.com/{uid}",}
                  for k,v in info.items():
                      print(f'''\r {W}{k:<10}▶︎ {G}{v}{X}''')
                  print()
                  try:
                      with open('/sdcard/AUTO-XD/AUTO/AUTO_CREATE_M5.txt','a') as f:
                            f.write(f"{uid}|{pww}\n")
                      alive.append(uid)
                  except IOError:
                      continue
               else:
                  dead.append(uid)
            elif "checkpoint" in login_coki:
               uid=login_coki.get("c_user","unknown")
               dead.append(uid)
               time.sleep(1)
        except Exception as e:
            time.sleep(5)
            continue


if __name__ == "__main__":
    #clear_screen()
    #install_dependencies()
    main()

