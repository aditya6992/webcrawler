from bs4 import BeautifulSoup
from urlparse import urljoin
import urllib2
import sys

visited = {}

def extractUrls(url):
	print url
	visited[url] = True
	try:
		resp = urllib2.urlopen(url)
	except:
		return []
	soup = BeautifulSoup(resp, from_encoding=resp.info().getparam('charset'))
	urls = []

	for link in soup.find_all('a', href=True):
		urls.append(link['href'])

	for i in xrange(len(urls)):
		if urls[i][0:4] != "http":
			urls[i] = urljoin(url, urls[i])
	return urls

def crawlBFS(url):
	queue = [url]
	
	while len(queue) > 0:
		url = queue.pop(0)
		while url in visited:
			url = queue.pop(0)
		newurls = extractUrls(url)
		
		for element in newurls:
			if element not in queue:
				queue.append(element.strip('/'))

if __name__ == "__main__":
	crawlBFS(sys.argv[1])