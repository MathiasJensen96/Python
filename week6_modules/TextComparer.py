import requests

class TextComparer ():
    def __init__(self, url_list):
        self.url_list = url_list

    def download(url, filename):

        r = requests.get(url)
        if (r.status_code == 200):
            with open(filename, 'w') as f:
                f.write(r.content.decode("utf-8"))
        else:
            raise Exception("Status code 404...")

    def multi_download():
        url = 'https://www.gutenberg.org/files/1342/1342-0.txt'
        r = requests.get(url)
        file_to_create = url.split("/")
        with open(file_to_create[-1], 'w') as f:
                f.write(r.content.decode("utf-8"))

    download('https://www.gutenberg.org/files/1342/1342-0.txt', 'test.txt')
    multi_download()