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
    if not month_day_tuple:
        print('Invalid month. Please enter a value between 1 and 12.')
        exit()
    elif not 1 <= day <= month_day_tuple[1]:
        print(
            f'Invalid day. Enter a value between 1 and {month_day_tuple[1]} for the month of {month_day_tuple[0]}.')
        exit()
    else:
        return f'{month_day_tuple[0]}_{day}'


def get_data(soup, search_param):
    heading = soup.find(id=search_param)
    data_list = heading.find_next('ul')
    for data in data_list.find_all('li'):
        print(data.text)


def find(date_value):
    response = requests.get(
        f'https://en.wikipedia.org/wiki/{date_value}')
    soup = BeautifulSoup(response.text, 'html.parser')

    # get_data('Events')
    # get_data('Births')
    # get_data('Deaths')
    get_data(soup, 'Holidays_and_observances')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--month', type=int, help='month argument')
    parser.add_argument('-d', '--day', type=int, help='day argument')
    args = parser.parse_args()
    month = args.month
    day = args.day
    today = date.today()
    if not month:
        month = today.month
    if not day:
        day = today.day
    date_value = month_day(month, day)
    find(date_value)


if __name__ == "__main__":
    main()
