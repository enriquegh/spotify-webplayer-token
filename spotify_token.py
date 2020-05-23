"""Utility module that helps get a webplayer access token"""
import os
import requests
from bs4 import BeautifulSoup
import json

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"

def start_session(dc=None, key=None):
    """ Starts session to get access token. """

    session = requests.Session()

    cookies = {'sp_dc': dc, 'sp_key': key}
    headers = {'user-agent': USER_AGENT}

    response = session.get("https://open.spotify.com/get_access_token?reason=transport&productType=web_player",
                           headers=headers, cookies=cookies)
    response.raise_for_status()
    data = response.content.decode("utf-8")
    config = json.loads(data)

    access_token = config['accessToken']
    expires_timestamp = config['accessTokenExpirationTimestampMs']
    expiration_date = int(expires_timestamp) // 1000
    return access_token, expiration_date