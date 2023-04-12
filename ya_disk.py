import requests


# token = ''

class YandexDisk:
    def __init__(self, token, name_folder):
        self.token = token
        self.name_folder = name_folder

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def create_folder(self):
        link_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {"path": self.name_folder, "url": link_url}
        response = requests.put(link_url, headers=headers, params=params)
        return response

    def link_url_get_upload_link(self, name_file, link_url):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": f'{self.name_folder}/{name_file}', "url": link_url}
        response = requests.post(upload_url, headers=headers, params=params)
        return response