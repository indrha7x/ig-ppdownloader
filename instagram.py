#!/usr/bin/python
# HD Instagram Profile Picture Downloader
# Coded by Kirnath Morscheck

import argparse
import json
import re
import requests

from bs4 import BeautifulSoup
class bcolors:
    HIJAU='\033[0;32m'
    MERAH='\033[01;31m'

BASE_URL = 'https://www.instagram.com/'

def main(username):
    url = BASE_URL + username
    source_code = requests.get(url).text.encode('ascii', 'ignore')
    soup = BeautifulSoup(source_code, 'html.parser')
    try:
        id = soup.find_all('script')
        id = re.search('''"id":"(.*)","is_business_account''', str(id)).group(1)
    except:
        print bcolors.MERAH
        print('Gagal!')
        return
    user_info = json.loads(requests.get('https://i.instagram.com/api/v1/users/{}/info/'.format(id)).text)
    profile_picture_url = user_info['user'].get('hd_profile_pic_url_info').get('url')
    profile_picture = requests.get(profile_picture_url).content
    with open('{}.jpg'.format(username), 'wb') as f:
        f.write(profile_picture)
    print bcolors.HIJAU
    print'Berhasil Download ! saved from',username
    return profile_picture

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Download HD Instagram Profile Picture')
    parser.add_argument('username', help='Username of Instagram in lower-case letters')
    args = parser.parse_args()
    main(args.username)
