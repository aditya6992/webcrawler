# webcrawler
A very basic web crawler implemented using beautiful soup 4 and native python

extracts urls from any website and using breadth first search traversal, visits each url and in turn extract urls from each webpage and so on...
with slight modification this can be used to download an entire website.

usage:

```pip install -r requirements.txt```

```python crawler.py http://stanford.edu/```

replace that with any url that you'd like to crawl 
