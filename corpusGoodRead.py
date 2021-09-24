# Erlina Rohmawati	    175150201111045
# Tania Malik Iryana	175150201111053
# Alvina Eka Damayanti	175150201111056
# Jeowandha Ria Wiyani	175150207111029

import requests
import sys
from bs4 import BeautifulSoup
import time

awal = time.time()

cookies = {
    'ccsid': '816-4785021-9980172',
    '__qca': 'P0-59280284-1587618929146',
    '__gads': 'ID=a25e1e146646c364:T=1587618929:S=ALNI_MaAFRKvkzlmsvqdELKnvKQ93O_4Dw',
    'never_show_interstitial': 'true',
    '__utmz': '250562704.1587631663.2.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
    'p': 'MKsFRYcLD20vI4_-JpeaUFHBW3MGE20Yjfvwb9XmJs6BjKk0',
    'locale': 'en',
    '__utmc': '250562704',
    'blocking_sign_in_interstitial': 'true',
    'u': 'VUA9pzIpUaiyEPOsT-nSW5bEtZ3aeT8evfxnCgspVZy49zzY',
    '_session_id2': '8a9750ba527499d79b8608b8a9aec6cd',
    '__utma': '250562704.625867263.1587618928.1587738336.1587748717.7',
    '__utmb': '250562704.3.10.1587748717',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Language': 'id,en-US;q=0.9,en;q=0.8',
    'If-None-Match': 'W/"ec9c265abc834a0723ced0b5db71eefa"',
}

def getSoup(search, param):
    url = 'https://www.goodreads.com'+search
    r = requests.get(url, headers=headers, params=param, cookies=cookies)
    request = r.content
    return BeautifulSoup(request, 'html.parser')

f = open("corpusGoodRead.txt", "a", encoding="utf-8")

dok = 0
for page in range(1,26):
    print('page '+str(page))
    search = '/shelf/show/indonesian-literature'
    param = (
        ('page', str(page)),
    )

    soup = getSoup(search, param)

    title = soup.find_all('a', attrs={'class' : 'bookTitle'})
    author = soup.find_all('a', attrs={'class' : 'authorName'})

    sinopsis = []
    new_tag_id = soup.new_tag('id')
    new_tag_judul = soup.new_tag('judul')
    new_tag_penulis = soup.new_tag('penulis')
    new_tag_deskripsi = soup.new_tag('deskripsi')

    for t in range(0,len(title)):
        print('t' +str(t))
        url2 = title[t]['href']
        soup2 = getSoup(url2, param)
        teks = soup2.find('span', attrs={'style' : 'display:none'})
        if(teks != None):
            dok += 1            
            new_tag_id.string = 'Book-'+ str(dok)
            new_tag_judul.string= title[t].text.strip()
            new_tag_penulis.string=author[t].text.strip()
            new_tag_deskripsi.string=teks.text.strip()

            f.write("{0}\n{1}\n{2}\n{3}\n\n".format(new_tag_id, new_tag_judul, new_tag_penulis, new_tag_deskripsi))
            if(dok == 50):
                f.close()
                akhir = time.time()
                print("")
                print ("Total Waktu Proses " + str(akhir-awal) + " Detik." )
                sys.exit(0)

        print(new_tag_judul)
        print(new_tag_penulis)
        print(new_tag_deskripsi)
        print()
        
f.close()

akhir = time.time()
print("")
print ("Total Waktu Proses " + str(akhir-awal) + " Detik." )