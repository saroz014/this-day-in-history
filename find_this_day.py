import argparse
import requests
from bs4 import BeautifulSoup

month_dict = {1: 'January',
              2: 'February',
              3: 'March',
              4: 'April',
              5: 'May',
              6: 'June',
              7: 'July',
              8: 'August',
              9: 'September',
              10: 'October',
              11: 'November',
              12: 'December'}


def get_data(soup, search_param):
    heading = soup.find(id=search_param)
    data_list = heading.find_next('ul')
    for data in data_list.find_all('li'):
        print(data.text)


def find(month, day):
    response = requests.get(
        f'https://en.wikipedia.org/wiki/{month}_{day}')
    soup = BeautifulSoup(response.text, 'html.parser')

    # get_data('Events')
    # get_data('Births')
    # get_data('Deaths')
    get_data(soup, 'Holidays_and_observances')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--month', type=int, help='month argument')
    parser.add_argument('-d', '--day', type=str, help='day argument')
    args = parser.parse_args()
    month = month_dict[args.month]
    find(month, args.day)


if __name__ == "__main__":
    main()
