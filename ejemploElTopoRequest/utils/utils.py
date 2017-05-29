from urllib.parse import urljoin
from urllib.parse import urlparse


class utils:
    def isOnionURL(url):
        if url.endswith(".onion") or url.endswith(".onion/"):
            return True
        else:
            return False

    def is_absolute(url):
        return bool(urlparse(url).netloc)

    def get_absolute_url(base_url, url):
        return urljoin(base_url, url)
