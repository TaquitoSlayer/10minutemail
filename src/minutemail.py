import requests
from endpoints import NEW_EMAIL, MESSAGE_AFTER, MESSAGE_COUNT
from fake_useragent import UserAgent


class Mail(object):
    """
    Python wrapper for 10minutemail.com
    """

    def __init__(self):
        self.session = requests.session()
        self.session.headers = {
            'authority': '10minutemail.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-CA,en-US;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'dnt': '1',
            'pragma': 'no-cache',
            'referer': 'https://www.bing.com/',
            'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
        }
        self.message_count = 0
        self.messages = []
        self.mail = self.session.get(NEW_EMAIL).json()['address']

    def get_mail(self):
        """
        :return: Mail of the current instance
        """
        return self.mail

    def get_message(self):
        """
        :return: list of messages stored in this instance
        """
        return self.messages

    def fetch_message(self):
        """
        Fetches for new messages which are not present in the instance
        :return: List of messages stored in the instance
        """
        res = self.session.get(MESSAGE_AFTER + str(self.message_count)).json()
        self.message_count += len(res)
        self.messages += res
        return self.messages

    def new_message(self):
        """
        Check whether there are new messages or not
        :return: bool
        """
        return self.session.get(MESSAGE_COUNT).json()['messageCount'] != self.message_count

    def __str__(self):
        return self.mail


if __name__ == "__main__":
    import time
    mail = Mail()
    print(mail.get_mail())
    while True:
        time.sleep(2)
