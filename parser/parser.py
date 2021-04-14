from bs4 import BeautifulSoup
import requests as req
from itertools import cycle
from fake_useragent import UserAgent
import pandas as pd
import re

# reviews = "1,736 reviews"
# rt = "#14 of 16,733 Restaurants in London"



#
# urls = "https://www.tripadvisor.com/Restaurant_Review-g190454-d12845029-Reviews-Grunstern-Vienna.html"
# # urls = "https://www.tripadvisor.com/Restaurant_Review-g186338-d10440481-Reviews-Andy_s_Greek_Taverna-London_England.html"
# # urls = "https://www.tripadvisor.com/Restaurant_Review-g186338-d8632781-Reviews-ROKA_Mayfair-London_England.html"
# # urls = "https://www.tripadvisor.ru/Restaurant_Review-g187323-d1358776-Reviews-Esplanade-Berlin.html"
# resp = req.get(urls)
# soup = BeautifulSoup(resp.text, 'lxml')
# span = soup.find("span", attrs={"class": "_13OzAOXO _34GKdBMV"})
# print(span)
# hrefs = span.find_all("a")
# print(hrefs)
# print(len(hrefs))
#
# if len(hrefs) > 0:
#     print(hrefs[0].text)
#     fc_index = 1
#     if "$" not in hrefs[0].text:
#         fc_index = 0
#     for i in range(fc_index, len(hrefs)):
#         print(hrefs[i].text)
# # img = soup.find("div", attrs={"class": "prw_rup prw_common_responsive_static_map_image map-widget"})
# # print(img)
#
# print(soup.title)
# # print(soup.title.text)
# # print(soup.title.parent)
#
# for i in range(1, 6):
#     div = soup.find("div", attrs={"class": "ui_checkbox item cx_brand_refresh_phase2", "data-value": i})
#     # print(div)
#     span = div.find("span", attrs={"class": "row_num is-shown-at-tablet"})
#     print(span.text)
#
# divM = soup.find('div', attrs={'class': '_1ud-0ITN'})
# print(divM)
# sp = divM.find('span', attrs={'class': '_3Wub8auF'})
# print(sp)
# print(sp.text)
# reviews = sp.text
# reviews = reviews.replace(',', '')
# reviews = reviews.replace(' ', '')
# reviews = reviews.replace('review', '')
# reviews = reviews.replace('s', '')
# print(reviews)
# ar = divM.find('a', attrs={'class': '_15QfMZ2L'})
# print(ar)
# print(ar.text)
# rt = ar.text
# rd = rt.split(" of ")
# print(rd[0].replace("#", ""))


# #####         GEO
# from geopy.geocoders import Nominatim
# geolocator = Nominatim(user_agent="MyApp")
# location = geolocator.geocode("Hornsgatan 66, Stockholm 118 21 Sweden")
# print(location.latitude, location.longitude)
# 59.318535,18.058828


# ## MAIN CODE

filename = 'reviews.csv'
delimiter = ";"


def parse_data(content):
    data = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        'price': 'NaN',
        'cuisines': 'NaN',
        'city_rating': 'NaN',
        'reviews': 'NaN',
    }

    soup = BeautifulSoup(content, 'lxml')
    for i in range(1, 6):
        div = soup.find("div", attrs={"class": "ui_checkbox item cx_brand_refresh_phase2", "data-value": i})
        # print(div)
        span = div.find("span", attrs={"class": "row_num is-shown-at-tablet"})
        data[i] = span.text
        # print(span.text)

    span = soup.find("span", attrs={"class": "_13OzAOXO _34GKdBMV"})
    # print(span)
    hrefs = span.find_all("a")
    # print(hrefs)
    # print(len(hrefs))

    # Price
    # Cuisines
    if len(hrefs) > 0:
        # print(hrefs[0].text)
        only_1 = False
        fc_index = 1
        if "$" in hrefs[0].text:
            data['price'] = hrefs[0].text
        else:
            only_1 = True
            fc_index = 0

        if only_1 or len(hrefs) > 1:
            cuisines = []
            for ind in range(fc_index, len(hrefs)):
                cuisines.append(hrefs[ind].text)
            if len(cuisines) > 0:
                data['cuisines'] = ','.join(cuisines)

    # Reviews
    # City rating
    divM = soup.find('div', attrs={'class': '_1ud-0ITN'})
    if divM is not None:
        # print(divM)
        sp = divM.find('span', attrs={'class': '_3Wub8auF'})
        # print(sp)
        # print(sp.text)
        reviews = 0
        if sp is not None:
            reviews = sp.text
            reviews = reviews.replace(',', '')
            reviews = reviews.replace(' ', '')
            reviews = reviews.replace('review', '')
            reviews = reviews.replace('s', '')
            # print(reviews)
        data['reviews'] = reviews

        ar = divM.find('a', attrs={'class': '_15QfMZ2L'})
        city_rating = 100000
        if ar is not None:
            # print(ar)
            # print(ar.text)
            rt = ar.text
            rd = rt.split(" of ")
            city_rating = rd[0].replace("#", "")
            city_rating = city_rating.replace(",", "")
        data['city_rating'] = city_rating
    # print(data)
    return data


df = pd.read_csv("main_task.csv")
# print(df.info())

list_proxy = [
    'socks5://95Jr8J:c8FqXs@107.152.153.145:9599',
    'socks5://5Gvjr6:SgSmoo@104.227.102.168:9157',
    'socks5://4nD5vV:o8nT4R@186.65.118.246:9416',
    'socks5://5Gvjr6:SgSmoo@104.227.102.252:9178',
    'socks5://95Jr8J:c8FqXs@104.227.102.123:9414',
    'socks5://95Jr8J:c8FqXs@138.128.19.12:9062',
    'socks5://95Jr8J:c8FqXs@104.227.96.96:9173',
    'socks5://95Jr8J:c8FqXs@107.152.153.157:9425',
    'socks5://5Gvjr6:SgSmoo@104.227.102.192:9610',
    'socks5://4nD5vV:o8nT4R@186.65.118.15:9623',
    'socks5://4nD5vV:o8nT4R@186.65.115.139:9826',
    'socks5://4nD5vV:o8nT4R@186.65.114.236:9547',
    'socks5://4nD5vV:o8nT4R@186.65.117.184:9372',
    'socks5://HQYuUS:PDEoYR@196.18.0.87:8000',
    'socks5://5Gvjr6:SgSmoo@104.227.96.127:9549',
    'socks5://5Gvjr6:SgSmoo@104.227.96.195:9733',
    'socks5://yzuMuw:bYsoxn@181.177.87.51:9627',
    'socks5://yzuMuw:bYsoxn@181.177.84.108:9256',
    'socks5://yzuMuw:bYsoxn@181.177.87.106:9839',
    'socks5://yzuMuw:bYsoxn@181.177.87.208:9201',
    'socks5://yzuMuw:bYsoxn@181.177.86.228:9298'
    ]


def get_url(url_ta):
    url = "https://www.tripadvisor.com" + str(url_ta)
    # print(url)
    return url


def get_url_data(url, cur_proxy):
    parsed_ata = None
    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    try:
        r = req.get(url=url, headers=headers, proxies=cur_proxy)
        # print(r.text)
        if r.status_code == 200:
            parsed_ata = parse_data(r.text)
    except:
        print("Error with url: ", url)

    return parsed_ata


def save_data(p_data, r):
    # print(p_data)
    if p_data is not None:
        string = r['Restaurant_id'] + delimiter + r['ID_TA'] + delimiter + \
                 str(p_data[1]) + delimiter + \
                 str(p_data[2]) + delimiter + \
                 str(p_data[3]) + delimiter + \
                 str(p_data[4]) + delimiter + \
                 str(p_data[5]) + delimiter + \
                 str(p_data['price']) + delimiter + \
                 str(p_data['city_rating']) + delimiter + \
                 str(p_data['reviews']) + delimiter + \
                 str(p_data['cuisines']) + '\n'
        with open(filename, 'a') as f:
            f.write(string)


proxy_cycle = cycle(list_proxy)
proxy = next(proxy_cycle)

d = df[:10]

for index, row in d.iterrows():
    print(row['URL_TA'])
    # print(row['Restaurant_id'])
    proxy = next(proxy_cycle)
    # print(proxy)
    proxies = {
        "http": proxy,
        "https": proxy
    }
    data = get_url_data(url=get_url(row['URL_TA']), cur_proxy=proxies)
    # print(data)
    if data is not None:
        save_data(data, row)
    # data = get_url_data(url="http://arutyunyan.ns25.ru", cur_proxy=proxies)
    print()




# # for i in range(1, 3):
#
#     proxy = next(proxy_cycle)
#     print(proxy)
#     proxies = {
#         "http": proxy,
#         "https": proxy
#     }
#     # r = req.get(url=urls, proxies=proxies)
#     # print(r.text)
#     # get_url()


# pip install pysocks
