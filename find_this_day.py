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


def month_day(month, day):
    month_day_tuple = MONTHS.get(month, None)
    if month_day_tuple is None:
        print('Invalid month. Enter a value between 1 and 12.')
        exit()
    elif not 1 <= day <= month_day_tuple[1]:
        print(
            f'Invalid day. Enter a value between 1 and {month_day_tuple[1]} for the month of {month_day_tuple[0]}.')
        exit()
    else:
        return f'{month_day_tuple[0]}_{day}'


def find(date_value, occurrence):
    response = requests.get(
        f'https://en.wikipedia.org/wiki/{date_value}')
    soup = BeautifulSoup(response.text, 'html.parser')
    heading = soup.find(id=occurrence)
    data_list = heading.find_next('ul')
    for data in data_list.find_all('li'):
        print(data.text)


def main():
    parser = argparse.ArgumentParser(prog='What Happened On This Day.',
                                     description='Find out what happened on a particular day in history.')
    parser.add_argument('occurrence', nargs='?', default='Holidays_and_observances', type=str,
                        choices=['Events', 'Births', 'Deaths',
                                 'Holidays_and_observances'],
                        help='occurrence argument')
    parser.add_argument('-m', '--month', type=int,
                        default=date.today().month, help='month argument')
    parser.add_argument('-d', '--day', type=int,
                        default=date.today().day, help='day argument')
    args = parser.parse_args()
    date_value = month_day(args.month, args.day)
    find(date_value, args.occurrence)


if __name__ == "__main__":
    main()
