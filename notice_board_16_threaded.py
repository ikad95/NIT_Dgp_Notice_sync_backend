import urllib2,os,thread,Queue,time
from BeautifulSoup import BeautifulSoup

q=Queue.Queue()

def dwld():
	os.system(q.get()+" >> xx.log")
def open(link):
	while True:
		i=0
		page=urllib2.urlopen(link).read()
		soup=BeautifulSoup(page)
		for a in soup.findAll('a',href=True):
			if(a['href'][-3:]=="pdf"):			
				if(a['href'][:len("all_pdf16")]=="all_pdf16"):		
					print a['href']
					q.put("wget -nc -q nitdgp.ac.in/"+"\""+a['href']+"\""+" -P 16pdfs/ >> xx.log")
					i+=1
		time.sleep(5)
		print "\n" *100
		print "found " +str(i)+ " items"
		print "Wait for 1 min to refresh..."
		print "\n" *10	
		time.sleep(60)

thread.start_new_thread(open,("http://www.nitdgp.ac.in",))

while True:
	while not q.empty():
		thread.start_new_thread(dwld,())
