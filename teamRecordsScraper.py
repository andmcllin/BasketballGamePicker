import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

firstYear = 1980
lastYear = 2022

years = np.arange(firstYear, lastYear, 1)

seasons_per_game = pd.DataFrame()

for year in years:
    base_url = 'https://www.basketball-reference.com/leagues/NBA_{}_standings.html'

    req_url = base_url.format(year)
    req = requests.get(req_url)
    soup = BeautifulSoup(req.content, 'html.parser')
    table = soup.find('table', {'id': 'confs_standings_E'})

    if table is not None:
        df = pd.read_html(str(table))[0]
        df['Year'] = year

        seasons_per_game = seasons_per_game.append(df)
        if year is firstYear:
            df.to_csv('standings.csv', header=False, mode='a')
        else:
            df.to_csv('standings.csv', header=False, mode='a')

    else:
        table = soup.find('table', {'id': 'divs_standings_E'})

        df = pd.read_html(str(table))[0]
        df['Year'] = year

        seasons_per_game = seasons_per_game.append(df)
        if year is firstYear:
            df.to_csv('standings.csv', header=False, mode='a')
        else:
            df.to_csv('standings.csv', header=False, mode='a')

    base_url = 'https://www.basketball-reference.com/leagues/NBA_{}_standings.html'

    req_url = base_url.format(year)
    req = requests.get(req_url)
    soup = BeautifulSoup(req.content, 'html.parser')
    table = soup.find('table', {'id': 'confs_standings_W'})

    if table is not None:
        df = pd.read_html(str(table))[0]
        df['Year'] = year

        seasons_per_game = seasons_per_game.append(df)
        if year is firstYear:
            df.to_csv('standings.csv', header=False, mode='a')
        else:
            df.to_csv('standings.csv', header=False, mode='a')

    else:
        table = soup.find('table', {'id': 'divs_standings_W'})

        df = pd.read_html(str(table))[0]
        df['Year'] = year

        seasons_per_game = seasons_per_game.append(df)
        if year is firstYear:
            df.to_csv('standings.csv', header=False, mode='a')
        else:
            df.to_csv('standings.csv', header=False, mode='a')
