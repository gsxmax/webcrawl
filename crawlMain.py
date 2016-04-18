# -*-  coding=utf8  -*-
import  requests,sys
from bs4 import BeautifulSoup
from PIL import Image 
from StringIO import StringIO
import time


def  getHtmlResponse(url):
    try:
        rel = requests.get(url)
    except requests.exceptions.ConnectionError:
         r.status_code = "Connection refused"
         return None
    return rel

def  writeContentToFile(filename,data,mode='w'):
    m_mode = mode
    with open(filename,m_mode) as f:
        f.write(data)
    return True

def createImageFromUrl(url,path):
    import re
    filename = re.split("/|//", url)
    m_len = len(filename)
    m = re.match(".*\.jpg|.*\.gif",filename[m_len-1])
    if m is not None:
        time.sleep(0.1)
        res = requests.get(url)
        if res is not None:
            try:
                im = Image.open(StringIO(res.content))
                osfile =  path + filename[m_len-1]
                im.save(osfile)
            except IOError:
                print 'IOerror image, the current url is %s .',url
                pass

def  createImageFromUrls(urls,path):
    while  urls:
        url = urls.pop()
        import re
        filename = re.split("/|//", url)
        m_len = len(filename)
        m = re.match(".*\.jpg|.*\.gif",filename[m_len-1])
        if m is not None:
            time.sleep(0.1)
            print url
            m_data = url +'\n'
            writeContentToFile('imageUrls.txt',m_data,'a')
            res = getHtmlResponse(url)
            if res is not None:
                try:
                    im = Image.open(StringIO(res.content))
                    osfile =  path + filename[m_len-1]
                    im.save(osfile)
                except IOError:
                    print 'IOerror image, the current url is %s .',url
                    pass
        else:
            continue
    return True
    

if __name__  ==  '__main__':
    print "hello webCrawl."
    reload(sys)
    sys.setdefaultencoding('utf-8')
    
    url = 'http://cl.clus.pw/htm_data/7/1512/1774220.html'
    urlcoding = 'gbk'
    r = getHtmlResponse(url)
    r.encoding = urlcoding

    writeContentToFile("study.html",r.text.encode('gbk'))
    img_path =  '/home/beyondkoma/work/gitProject/webCrawl/images/'

    # createImageFromUrl('http://i4.tietuku.com/408da328c806fa52.jpg',img_path)
    soup_html = BeautifulSoup(r.text,'html.parser')
    img_urls = []
    soup_html.find_all('img')
    for img_src in   soup_html.find_all('img'):
        img_urls.append(img_src['src'])
        
    createImageFromUrls(img_urls,img_path)
        # i = Image.open(StringIO(r.content)) # image
    # r.json()                    # json


