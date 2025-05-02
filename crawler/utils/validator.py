import re
from urllib.parse import urlparse

URL_REGEX = re.compile(r'^(https?://)(([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}|(\d{1,3}\.){3}\d{1,3})(:\d+)?(/.*)?$')

def validate_url(url):
    if not isinstance(url, str) or len(url) > 2048: return False
    if not URL_REGEX.match(url): return False
    try: 
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except: return False

def validate_proxy(proxy):
    try:
        parsed = urlparse(proxy)
        return parsed.scheme in ('http','https') and parsed.port and 0 < parsed.port <= 65535
    except: return False
