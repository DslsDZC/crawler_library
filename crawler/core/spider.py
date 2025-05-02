#!/usr/bin/env python3
"""
爬虫核心逻辑
"""
import time
import logging
import requests
from concurrent.futures import ThreadPoolExecutor
from crawler.utils.config import ConfigManager
from crawler.utils.validator import validate_url

class Crawler:
    def __init__(self, target_url, mode="normal", proxy=None, proxy_auth=None, timeout=10.0):
        self.target_url = target_url
        self.mode = mode
        self.proxy = proxy
        self.proxy_auth = proxy_auth
        self.timeout = timeout
        self.config_manager = ConfigManager()
        self.default_config = self.config_manager.get_config()
        self.logger = self._init_logger()
        self.session = self._init_session()

    def _init_logger(self):
        logger = logging.getLogger("CrawlerLibrary")
        logger.setLevel(self.default_config['logging']['level'])
        handler = logging.FileHandler(self.default_config['logging']['file'])
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    def _init_session(self):
        session = requests.Session()
        session.headers.update(self.default_config['request']['headers'])
        if self.proxy: 
            session.proxies = {'http': self.proxy, 'https': self.proxy}
        session.timeout = self.default_config['request']['timeout']
        return session

    def fetch(self, url):
        try: 
            response = self.session.get(url)
            response.raise_for_status()
            self.logger.info(f"成功获取: {url}")
            return response.text
        except Exception as e: 
            self.logger.error(f"请求失败 [{url}]: {str(e)}")
        return ""

    def start(self):
        if self.mode == "concurrent":
            with ThreadPoolExecutor(max_workers=self.default_config['request'].get('concurrency', 5)) as executor:
                [executor.submit(self._worker) for _ in range(self.default_config['request'].get('concurrency', 5))]
        else: 
            self._worker()

    def _worker(self):
        html = self.fetch(self.target_url)
        if html: 
            self.save(self.parse(html))

    def parse(self, html):
        from bs4 import BeautifulSoup
        return [a.get('href') for a in BeautifulSoup(html, 'html.parser').find_all('a', href=True)]

    def save(self, data):
        with open('output.txt', 'a') as f: 
            f.write('\n'.join(data))
            