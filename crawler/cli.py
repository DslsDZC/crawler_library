#!/usr/bin/env python3
"""
命令行接口模块
"""
import argparse
from crawler.core.engine import RequestEngine
from crawler.core.spider import Crawler
from crawler.utils.validator import validate_url, validate_proxy

def main():
    parser = argparse.ArgumentParser(description="高级网络爬虫工具 v2.0")
    parser.add_argument('url', help='目标网站URL')
    parser.add_argument('-m', '--mode', choices=['normal', 'concurrent'], default='normal')
    parser.add_argument('--proxy', help='代理服务器地址')
    parser.add_argument('--proxy-auth', help='代理认证信息')
    parser.add_argument('-c', '--concurrency', type=int, default=5)
    parser.add_argument('-w', '--wait', type=float, default=1.0)
    parser.add_argument('-t', '--timeout', type=float, default=10.0)
    
    args = parser.parse_args()
    
    if not validate_url(args.url):
        raise ValueError("无效的URL格式")
    if args.proxy and not validate_proxy(args.proxy):
        raise ValueError("无效的代理格式")
        
    engine = RequestEngine(max_workers=args.concurrency)
    crawler = Crawler(
        target_url=args.url,
        mode=args.mode,
        proxy=args.proxy,
        proxy_auth=args.proxy_auth,
        timeout=args.timeout
    )
    
    try:
        engine.start()
        crawler.start()
    except Exception as e:
        print(f"程序运行失败: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()
    