import requests
import os
from urllib.parse import urlparse
from dotenv import load_dotenv
import argparse


def shorten_link(headers, link):
    url = "https://api-ssl.bitly.com/v4/bitlinks"
    params = {"long_url": link}
    response = requests.post(url, headers=headers, json=params)
    response.raise_for_status()
    return response.json()['id']


def count_clicks(headers, bitlink):
    url_clicks = f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary"
    params = {"unit": "month", 'units': -1}
    response = requests.get(url_clicks, headers=headers, params=params)
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(headers, bitlink):
    url_check = f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}"
    response = requests.get(url_check, headers=headers)
    return response.ok


if __name__ == '__main__':
    load_dotenv()
    token = os.environ['BITLY_TOKEN']
    authorization_header = {"Authorization": f"Bearer {token}" }
    parser = argparse.ArgumentParser(description='Сокращение ссылок, статистика переходов по ссылке')
    parser.add_argument('--url', help='вставьте ссылку')
    args = parser.parse_args()
    parsed_link = urlparse(args.url)
    parsed_link = f"{parsed_link.netloc}{parsed_link.path}"
    try:
        if is_bitlink(authorization_header, parsed_link):
            print(count_clicks(authorization_header, parsed_link))
        else:
            print('Битлинк', shorten_link(authorization_header, args.url))

    except requests.exceptions.HTTPError:
        print("Неверный формат ссылки")
