import argparse
import requests
from bs4 import BeautifulSoup
from datetime import date


MONTHS = {1: ('January', 31),
          2: ('February', 29),
          3: ('March', 31),
          4: ('April', 30),
          5: ('May', 31),
          6: ('June', 30),
          7: ('July', 31),
          8: ('August', 31),
          9: ('September', 30),
          10: ('October', 31),
          11: ('November', 30),
          12: ('December', 31)}


def find(search_param, occurrence):
    response = requests.get(
        f'https://en.wikipedia.org/wiki/{search_param}')
    soup = BeautifulSoup(response.text, 'html.parser')
    heading = soup.find(id=occurrence)
    data_list = heading.find_next('ul')
    for data in data_list.find_all('li'):
        print(data.text)


def main():
    parser = argparse.ArgumentParser(prog='What Happened On This Day',
                                     description='Find out what happened on a particular day in history')
    parser.add_argument('occurrence', nargs='?', default='Holidays_and_observances', type=str,
                        choices=['Events', 'Births', 'Deaths',
                                 'Holidays_and_observances'],
                        help='Name of the occurrence')
    parser.add_argument('-m', '--month', type=int,
                        default=date.today().month, choices=range(1, 13), help='Month to be looked')
    parser.add_argument('-d', '--day', type=int,
                        default=date.today().day, help='Day to be looked')
    args = parser.parse_args()
    month_day_tuple = MONTHS[args.month]
    if not 1 <= args.day <= month_day_tuple[1]:
        parser.error(
            f"argument -d/--day: invalid choice: {args.day} (choose from {', '.join(map(repr, range(1, month_day_tuple[1]+1)))})")
    else:
        search_param = f'{month_day_tuple[0]}_{args.day}'
    find(search_param, args.occurrence)


if __name__ == "__main__":
    main()
