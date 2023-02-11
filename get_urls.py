# import bs4
import argparse
import requests
from bs4 import BeautifulSoup


def get_soup(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup


def main(url, depth=1):
    data = set()

    soup = get_soup(url)
    elements = soup.select('a[href]')

    if len(elements) == 0:
        return data

    for tag in elements:
        item = tag['href']
        if not item.startswith('http'):
            # 文字列の結合の前に、もとのURLのクエリパラメータの削除処理が必要かも
            if url.endswith('/') and item.startswith('/'):# スラッシュ（/)がかぶっているとき
                item = url + item[1:]
            elif url.endswith('/') or item.startswith('/'):# スラッシュがどちらかのみのとき
                item = url + item
            else:# スラッシュがどちらもないとき
                item = url + '/' + item
        data.add(item)

    data = set(data) # 重複の削除

    print('url数', len(data))
    print(data)
    return data


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='get_urls.py',  # プログラム名
        usage='get all urls from a specified url',  # プログラムの利用方法
        description='description',  # 引数のヘルプの前に表示
        epilog='end',  # 引数のヘルプの後で表示
        add_help=True,  # -h/–help オプションの追加
    )
    parser.add_argument(
        '-u',
        '--url',
        help="Provide the url you would like to search in",
        required=True
    )
    parser.add_argument(
        '-d',
        '--depth',
        help="Provide the depth you would like to search recursively in (default 1)",
        required=False,
        default = 1,
        type=int
    )

    args = parser.parse_args()
    url = args.url # コマンドライン引数からURLを取得
    depth = args.depth

    main(url, depth)
