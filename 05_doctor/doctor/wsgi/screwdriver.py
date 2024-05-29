import requests
import sys


def upload_file(filename):
    with open(filename, 'rb') as f:
        requests.post('http://localhost:8888/', files={'file': f})


def list_files():
    response = requests.get('http://localhost:8888/all')
    print(response.text)


if __name__ == '__main__':
    if sys.argv[1] == 'upload':
        upload_file(sys.argv[2])
    elif sys.argv[1] == 'list':
        list_files()
