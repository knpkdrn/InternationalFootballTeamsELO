import csv_handler as csh
from pandas import DataFrame
from team import Team


def play_game(match: list):
    print(match)
    home_team = None
    away_team = None

    for x in all_teams:
        if home_team is not None and away_team is not None:
            break

        if match[1] == x.name:
            home_team = x
        elif match[2] == x.name:
            away_team = x

    if home_team is None or away_team is None:
        print("error in play_game() for loop")
        exit()

    home_team.calc_expected_outcome(away_team)
    away_team.calc_expected_outcome(home_team)

    home_team.calc_k_factor()
    away_team.calc_k_factor()

    home_team.update_team_after_match(match[3], match[4])
    away_team.update_team_after_match(match[4], match[3])


def find_highest_elos():
    best_teams = []
    for x in all_teams:

        if len(best_teams) < 10:
            best_teams.append(x)
        else:
            lowest_in_list = min(best_teams, key=lambda t: t.elo)
            if x.elo > lowest_in_list.elo:
                best_teams.remove(lowest_in_list)
                best_teams.append(x)

    return best_teams


# load all teams into a list
data = csh.load_from_csv()
all_teams = csh.create_teams()


csh.list_all_teams(all_teams)

i = 0
while i < len(data):
    new_match = data.loc[i, :].values.flatten().tolist()
    play_game(new_match)
    i += 1
print("DONE")

print("Ten Highest ELOs: ")
b_teams = find_highest_elos()
b_teams.sort(key=lambda t: t.elo, reverse=True)
for e in b_teams:
    print(f"{e.name}: {e.elo} point; Wins: {e.victories}, Draws: {e.draws}, Losses: {e.losses}")

