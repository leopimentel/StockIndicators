import requests
from bs4 import BeautifulSoup

def get_ticker_vp(ticker):
    URL = "https://statusinvest.com.br/acoes/" + ticker
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    pvp = soup.select_one('#indicators-section > div.indicator-today-container > div > div:nth-child(1) > div > div:nth-child(4) > div > div > strong').text
    pl = soup.select_one('#indicators-section > div.indicator-today-container > div > div:nth-child(1) > div > div:nth-child(2) > div > div > strong').text
    ml = soup.select_one('#indicators-section > div.indicator-today-container > div > div:nth-child(3) > div > div:nth-child(4) > div > div > strong').text
    dy = soup.select_one('#indicators-section > div.indicator-today-container > div > div:nth-child(1) > div > div:nth-child(1) > div > div > strong').text
    print(pvp + '\t' + pl + '\t' + ml + '\t' + dy)


with open("p_vp_tickers.txt", "r") as f:
    tickers = f.readlines()
    for ticker in tickers:
        get_ticker_vp(ticker.strip())

