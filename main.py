#coding:utf-8
import re,requests,sys,time
from bs4 import BeautifulSoup

reload(sys)

sys.setdefaultencoding('utf-8')

url='http://cn-proxy.com/'
url2='https://www.baidu.com/favicon.ico'

page=requests.get(url=url)

soup=BeautifulSoup(page.text)

td=soup.find_all('td')

date=time.strftime('%Y-%m-%d',time.localtime(time.time()))

for id,x in enumerate(td):
	pat=re.compile(r"(\d+)\.(\d+)\.(\d+)\.(\d+)")
	if(pat.match(x.text)):
		try:
			if(requests.get(url=url2,proxies={"https":"http://%s:%s" % (x.text,td[id+1].text)},timeout=3).status_code==200):
				f=open('/root/ip_%s.txt'%(date),'a')
				f.write(x.text+'\t'+td[id+1].text+'\t'+td[id+2].text+'\n')
				f.close()
		except:
			pass

