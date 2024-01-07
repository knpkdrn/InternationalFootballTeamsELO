import pandas as pd
from pandas import DataFrame
from team import Team


data = DataFrame()


def load_from_csv():
    global data
    columns = ["date", "home_team", "away_team", "home_score", "away_score"]
    data = pd.read_csv("file/results.csv", usecols=columns)
    print(data.head())
    return data


def get_unique_teams():
    unique_teams = []
    u_away_teams = data.away_team.unique()
    u_home_teams = data.home_team.unique()

    for x in u_home_teams:
        if x in unique_teams:
            continue
        elif x not in unique_teams:
            unique_teams.append(x)

    for x in u_away_teams:
        if x in unique_teams:
            continue
        elif x not in unique_teams:
            unique_teams.append(x)

    return unique_teams


def create_teams():
    team_names = get_unique_teams()
    all_teams = []
    i = 0
    for x in team_names:
        new_team = Team(x, i)
        i += 1
        all_teams.append(new_team)

    return all_teams


def list_all_teams(teams: list):
    for x in teams:
        print(f"{x.id} | {x.name}")
