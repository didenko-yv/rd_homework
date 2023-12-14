import os
import re
import requests




def main():

    response = requests.get(
        url='https://fake-api-vycpfa6oca-uc.a.run.app/sales',
        params={'date': '2022-08-09', "page": 1},
        headers={'Authorization': "2b8d97ce57d401abd89f45b0079d8790edd940e6"},
    )

    print("Response status code:", response.status_code)
    print("Response JSON", response.json())


if __name__ == '__main__':
    main()
