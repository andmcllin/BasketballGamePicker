import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

firstYear = 1980
lastYear = 2022

years = np.arange(firstYear, lastYear, 1)

seasons_per_game = pd.DataFrame()

for year in years:
    base_url = 'https://www.basketball-reference.com/leagues/NBA_{}_games-october.html'

    req_url = base_url.format(year)
    req = requests.get(req_url)
    soup = BeautifulSoup(req.content, 'html.parser')
    table = soup.find('table', {'id': 'schedule'})

    if table is not None:

        df = pd.read_html(str(table))[0]
        df['Year'] = year

        del df['Date']
        del df['Attend.']
        del df['Notes']

        if 'Start (ET)' in df.columns:
            del df['Start (ET']
        if 'Unnamed: 5' in df.columns:
            del df['Unnamed: 5']
        if 'Unnamed: 6' in df.columns:
            del df['Unnamed: 6']
        if 'Unnamed: 7' in df.columns:
            del df['Unnamed: 7']

        seasons_per_game = seasons_per_game.append(df)
        if year is firstYear:
            df.to_csv('schedule.csv')
        else:
            df.to_csv('schedule.csv', header=False, mode='a')

    else:
        print(str(year) + ' october')

    base_url = 'https://www.basketball-reference.com/leagues/NBA_{}_games-november.html'

    req_url = base_url.format(year)
    req = requests.get(req_url)
    soup = BeautifulSoup(req.content, 'html.parser')
    table = soup.find('table', {'id': 'schedule'})

    if table is not None:

        df = pd.read_html(str(table))[0]
        df['Year'] = year

        del df['Date']
        del df['Attend.']
        del df['Notes']

        if 'Start (ET)' in df.columns:
            del df['Start (ET']
        if 'Unnamed: 5' in df.columns:
            del df['Unnamed: 5']
        if 'Unnamed: 6' in df.columns:
            del df['Unnamed: 6']
        if 'Unnamed: 7' in df.columns:
            del df['Unnamed: 7']

        seasons_per_game = seasons_per_game.append(df)
        if year is firstYear:
            df.to_csv('schedule.csv')
        else:
            df.to_csv('schedule.csv', header=False, mode='a')

    else:
        print(str(year) + ' november')

    base_url = 'https://www.basketball-reference.com/leagues/NBA_{}_games-december.html'

    req_url = base_url.format(year)
    req = requests.get(req_url)
    soup = BeautifulSoup(req.content, 'html.parser')
    table = soup.find('table', {'id': 'schedule'})

    if table is not None:

        df = pd.read_html(str(table))[0]
        df['Year'] = year

        del df['Date']
        del df['Attend.']
        del df['Notes']

        if 'Start (ET)' in df.columns:
            del df['Start (ET']
        if 'Unnamed: 5' in df.columns:
            del df['Unnamed: 5']
        if 'Unnamed: 6' in df.columns:
            del df['Unnamed: 6']
        if 'Unnamed: 7' in df.columns:
            del df['Unnamed: 7']

        seasons_per_game = seasons_per_game.append(df)
        if year is firstYear:
            df.to_csv('schedule.csv')
        else:
            df.to_csv('schedule.csv', header=False, mode='a')

    else:
        print(str(year) + ' december')

    base_url = 'https://www.basketball-reference.com/leagues/NBA_{}_games-january.html'

    req_url = base_url.format(year)
    req = requests.get(req_url)
    soup = BeautifulSoup(req.content, 'html.parser')
    table = soup.find('table', {'id': 'schedule'})

    if table is not None:

        df = pd.read_html(str(table))[0]
        df['Year'] = year

        del df['Date']
        del df['Attend.']
        del df['Notes']

        if 'Start (ET)' in df.columns:
            del df['Start (ET']
        if 'Unnamed: 5' in df.columns:
            del df['Unnamed: 5']
        if 'Unnamed: 6' in df.columns:
            del df['Unnamed: 6']
        if 'Unnamed: 7' in df.columns:
            del df['Unnamed: 7']

        seasons_per_game = seasons_per_game.append(df)
        if year is firstYear:
            df.to_csv('schedule.csv')
        else:
            df.to_csv('schedule.csv', header=False, mode='a')

    else:
        print(str(year) + ' january')

    base_url = 'https://www.basketball-reference.com/leagues/NBA_{}_games-february.html'

    req_url = base_url.format(year)
    req = requests.get(req_url)
    soup = BeautifulSoup(req.content, 'html.parser')
    table = soup.find('table', {'id': 'schedule'})

    if table is not None:

        df = pd.read_html(str(table))[0]
        df['Year'] = year

        del df['Date']
        del df['Attend.']
        del df['Notes']

        if 'Start (ET)' in df.columns:
            del df['Start (ET']
        if 'Unnamed: 5' in df.columns:
            del df['Unnamed: 5']
        if 'Unnamed: 6' in df.columns:
            del df['Unnamed: 6']
        if 'Unnamed: 7' in df.columns:
            del df['Unnamed: 7']

        seasons_per_game = seasons_per_game.append(df)
        if year is firstYear:
            df.to_csv('schedule.csv')
        else:
            df.to_csv('schedule.csv', header=False, mode='a')

    else:
        print(str(year) + ' february')

    base_url = 'https://www.basketball-reference.com/leagues/NBA_{}_games-march.html'

    req_url = base_url.format(year)
    req = requests.get(req_url)
    soup = BeautifulSoup(req.content, 'html.parser')
    table = soup.find('table', {'id': 'schedule'})

    if table is not None:

        df = pd.read_html(str(table))[0]
        df['Year'] = year

        del df['Date']
        del df['Attend.']
        del df['Notes']

        if 'Start (ET)' in df.columns:
            del df['Start (ET']
        if 'Unnamed: 5' in df.columns:
            del df['Unnamed: 5']
        if 'Unnamed: 6' in df.columns:
            del df['Unnamed: 6']
        if 'Unnamed: 7' in df.columns:
            del df['Unnamed: 7']

        seasons_per_game = seasons_per_game.append(df)
        if year is firstYear:
            df.to_csv('schedule.csv')
        else:
            df.to_csv('schedule.csv', header=False, mode='a')

    else:
        print(str(year) + ' march')

    base_url = 'https://www.basketball-reference.com/leagues/NBA_{}_games-april.html'

    req_url = base_url.format(year)
    req = requests.get(req_url)
    soup = BeautifulSoup(req.content, 'html.parser')
    table = soup.find('table', {'id': 'schedule'})

    if table is not None:

        df = pd.read_html(str(table))[0]
        df['Year'] = year

        del df['Date']
        del df['Attend.']
        del df['Notes']

        if 'Start (ET)' in df.columns:
            del df['Start (ET']
        if 'Unnamed: 5' in df.columns:
            del df['Unnamed: 5']
        if 'Unnamed: 6' in df.columns:
            del df['Unnamed: 6']
        if 'Unnamed: 7' in df.columns:
            del df['Unnamed: 7']

        seasons_per_game = seasons_per_game.append(df)
        if year is firstYear:
            df.to_csv('schedule.csv')
        else:
            df.to_csv('schedule.csv', header=False, mode='a')

    else:
        print(str(year) + ' april')
