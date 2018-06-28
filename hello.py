import urllib2
from bs4 import BeautifulSoup
url='http://openshiksha.org/challenge/'

def go_toURL(url):
	r=urllib2.urlopen(url)
	req=r.read()
	soup = BeautifulSoup(req,"html.parser")
	t=soup.find(id="trail")
	
	while(t!=None):
		print t
		d=t.string
		flag=0
		url="http://openshiksha.org"
		c=0
		
		for i in unicode(t.string):
			if(i=='/'):
				flag=1
			if(flag==1):
				url=url+i
		print url
		r=urllib2.urlopen(url)
		req=r.read()
		soup = BeautifulSoup(req,"html.parser")
		t=soup.find(id="trail")

	
go_toURL(url)