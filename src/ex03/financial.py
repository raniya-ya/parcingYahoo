#!/usr/bin/env python

import sys
import time
from bs4 import BeautifulSoup
import requests


def financial_info(ticker, field_name):
    ticker = ticker.upper()
    url = f"https://finance.yahoo.com/quote/{ticker}/financials/?p={ticker}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html"
    }

    time.sleep(5)
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception("url не существует")

    soup = BeautifulSoup(response.text, "html.parser")
    rows = soup.find_all("div", class_=lambda c: c and "row" in c)


    for row in rows:
        title_div = row.find("div", class_=lambda c: c and ("column" in c or "title" in c))
        
        if not title_div:
            continue
        if title_div.text.strip().lower() == field_name.lower():
            cells = row.find_all("div", class_=lambda c: c and ("column" in c or "cell" in c))
            
            row_data = []
            for cell in cells:
                clean_text = cell.text.strip()
                if clean_text != "":
                    row_data.append(clean_text)
            
            if row_data:
                return tuple(row_data)

    raise Exception("не найдено")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("error")
        sys.exit(1)

    ticker = sys.argv[1]
    field_name = sys.argv[2]

    result = financial_info(ticker, field_name)
    print(result)