import json

import requests


ENCODING = 'utf-8'


def get_gitignore(filetype: str) -> str:

    url = 'https://www.toptal.com/developers/gitignore/api/list?format=json'
    response = requests.get(url)
    str_data = response.content.decode(ENCODING)
    json_ = json.loads(str_data)

    contents = json_.get(filetype, {'contents': ''}).get('contents', '')

    return contents
