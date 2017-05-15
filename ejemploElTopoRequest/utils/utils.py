class utils:
    def isOnionURL(url):
        if url.endswith(".onion") or url.endswith(".onion/"):
            return True
        else:
            return False
