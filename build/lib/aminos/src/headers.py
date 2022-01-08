headers = None


class Headers:
    def __init__(self, sid: str = None):
        self.headers = {
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 9; Redmi Note 8 Build/PKQ1.190616.001; com.narvii.amino.master/3.4.33578)",
            "AUID": "dfec1b8a-92f7-4cf0-928c-3b60aa33429a",
            "SMDEVICEID": "6e28d4c5-2d25-4977-93ec-9a4ce077fb7b",
            "Host": "service.narvii.com",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
        }

        if sid:
            self.web_headers = {
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "ar,en-US;q=0.9,en;q=0.8",
                "content-type": "application/json",
                "cookie": sid,
                "sec-ch-ua": '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
                "x-requested-with": "xmlhttprequest",
            }
