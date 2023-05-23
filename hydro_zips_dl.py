from bs4 import BeautifulSoup
import requests
import urllib.request
import os
import zipfile

download_dir = './hydro/monthly_hydro_extracted_zips'
download_dir1 = './hydro/daily_hydro_extracted_zips'

if not os.path.exists(download_dir):
    os.mkdir(download_dir)

if not os.path.exists(download_dir1):
    os.mkdir(download_dir1)

for i in range(2000, 2022):
    url = f'https://danepubliczne.imgw.pl/data/dane_pomiarowo_obserwacyjne/dane_hydrologiczne/miesieczne/{i}/'
    url_daily = f'https://danepubliczne.imgw.pl/data/dane_pomiarowo_obserwacyjne/dane_hydrologiczne/dobowe/{i}/'

    html_page = requests.get(url)
    soup = BeautifulSoup(html_page.content, 'html.parser')

    html_page_d = requests.get(url_daily)
    soup_d = BeautifulSoup(html_page_d.content, 'html.parser')

    for link in soup.find_all('a'):
        if link.get('href').endswith('.zip'):
            
            zip_file = link.get('href')
            file_url = url + zip_file
            
            download_path = os.path.join(download_dir, zip_file)

            urllib.request.urlretrieve(file_url, download_path)

            with zipfile.ZipFile(download_path, 'r') as zip_ref:
                zip_ref.extractall(download_dir)

            os.remove(download_path)

    for link in soup_d.find_all('a'):
        if link.get('href').endswith('.zip'):
            
            zip_file = link.get('href')
            file_url = url_daily + zip_file
            
            download_path = os.path.join(download_dir1, zip_file)

            urllib.request.urlretrieve(file_url, download_path)

            with zipfile.ZipFile(download_path, 'r') as zip_ref:
                zip_ref.extractall(download_dir1)

            os.remove(download_path)