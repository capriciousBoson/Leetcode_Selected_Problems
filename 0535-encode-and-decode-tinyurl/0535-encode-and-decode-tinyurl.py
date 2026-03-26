import hashlib
class Codec:
    def __init__(self):
        self.urls = {}
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        md5 = hashlib.md5()
        md5.update(longUrl.encode())
        key = md5.hexdigest()
        self.urls[key] = longUrl
        return key

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.urls[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))