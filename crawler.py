from bs4 import BeautifulSoup
import urllib2
import sys

def extractUrls(url):
	resp = urllib2.urlopen("http://www.gpsbasecamp.com/national-parks")
	soup = BeautifulSoup(resp, from_encoding=resp.info().getparam('charset'))
	urls = []

	for link in soup.find_all('a', href=True):
		urls.append(link['href'])
	return urls

def crawlBFS(url):
	queue = [url]
	while len(queue) > 0:
		url = queue.pop(0)
		newurls = extractUrls(url)
		for element in newurls:
			if element not in queue:
				queue.append(element)
		print url

if __name__ == "__main__":
	crawlBFS(sys.argv[1])