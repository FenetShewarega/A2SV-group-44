 
class Codec:
    def __init__(self):
        self.url_to_code = {}
        self.code_to_url = {}
        self.base_url = "http://tinyurl.com/"
        self.counter = 0

    def encode(self, longUrl):
        if longUrl in self.url_to_code:
            return self.url_to_code[longUrl]

        code = self.base_url + str(self.counter)
        self.url_to_code[longUrl] = code
        self.code_to_url[code] = longUrl
        self.counter += 1

        return code

    def decode(self, shortUrl):
        return self.code_to_url[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))