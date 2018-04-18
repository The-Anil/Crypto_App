from django.http import HttpResponse
from django.shortcuts import render
############## crypto dictionary ############################
## ======================================================= ##
import bs4 as bs
import urllib.request
import numpy as np

def index(request):
	return render(request, 'crypto_app/index.html')

def bitcoin(request):
	return render(request, 'crypto_app/bitcoin.html')

def ethereum(request):
	return render(request, 'crypto_app/ethereum.html')

def ripple(request):
	return render(request, 'crypto_app/ripple.html')

def litecoin(request):
	return render(request, 'crypto_app/litecoin.html')


def monero(request):
	return render(request, 'crypto_app/monero.html')

def iota(request):
	return render(request, 'crypto_app/iota.html')

def steem(request):
	return render(request, 'crypto_app/steem.html')

def maidsafe(request):
	return render(request, 'crypto_app/maidsafe.html')

def predictions(request):
	return render(request, 'crypto_app/predictions.html')

def rankwise(request):
    ############## crypto dictionary ############################
    ## ======================================================= ##


    coinmarketcap = urllib.request.urlopen('https://coinmarketcap.com/').read()
    coinwarz = urllib.request.urlopen('https://www.coinwarz.com/cryptocurrency').read()

    soup = bs.BeautifulSoup(coinmarketcap, 'lxml')
    soup_1 = bs.BeautifulSoup(coinwarz, 'lxml')
    ######================================================================================########
    global table_p, table_d
    a = []
    b = []
    c = []
    d = []

    for t_data in soup.find_all('td'):
        # print(t_data)
        for table_p in t_data.find_all('a', class_='currency-name-container'):
            # print(table.text+" : \t",end="")
            a.append(table_p.text)

        for table_p in t_data.find_all('a', class_='price'):
            # print(table.text)
            b.append(float(table_p.text.replace('$', '').replace(',', '')))
    ######===============================================================================#########

    for t_data in soup_1.find_all('td'):
        # print(t_data)
        for table_d in t_data.find_all('div', attrs={'style': 'float: left; min-width: 160px; margin:-3px;'}):
            for table_name in table_d.find_all('a', class_='link'):
                # print(table_name.text.split()[0]+"\t",end="")
                c.append(table_name.text.split()[0])

        for table_d in t_data.find_all('div', attrs={'style': 'width: 140px; text-align: center;'}):
            # print(table_d)
            for table_difficulty in table_d.find_all('span', class_='bold'):
                # print(table_difficulty.text)
                d.append(float(table_difficulty.text.replace(',', '')))

    e = dict(zip(a, b))
    #print(e)

    f = dict(zip(c, d))
    #print(f)

    keys_a = set(e.keys())
    keys_b = set(f.keys())

    common = sorted(keys_a.intersection(keys_b), key=lambda x: c.index(x))
    # print(common)

    z = np.zeros((len(common), 2))

    for k, v in e.items():
        for i in range(len(common)):
            if k == common[i]:
                z[i][0] = v

    for k1, v1 in f.items():
        for i in range(len(common)):
            if k1 == common[i]:
                z[i][1] = v1

    g = dict(zip(common, z))

    ## ======================================================= ##
    ########### Python ends here for crypto dictionary ##########
    return render(request, 'crypto_app/rankwise.html', {'dictionary': g})