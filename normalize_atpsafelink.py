from argparse import ArgumentParser
from urllib import parse


def normalize_atpsafelink(safelink_url):
    safelink_url = safelink_url.split("=")[1]
    safelink_url = safelink_url.split('&')[0]
    safelink_url = parse.unquote(safelink_url)

    return safelink_url


def main(url):
    print(normalize_atpsafelink(url))


if __name__ == "__main__":
    args = ArgumentParser()
    args.add_argument('-u', '--url', help="Enter the Office365 ATP SafeLinks URL", dest='url', required=True)
    args = args.parse_args()

    main(args.url)
