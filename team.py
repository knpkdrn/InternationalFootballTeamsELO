class Team:
    name = ""
    id = -1

    # rating
    elo = 0
    expected_outcome = -1
    real_outcome = -1
    k_factor = 0

    # data
    victories = 0
    draws = 0
    losses = 0
    all_GA = 0
    all_GF = 0

    def __init__(self, n, i):
        self.name = n
        self.id = i
        self.elo = 1000

    def calc_expected_outcome(self, other_team):
        self.expected_outcome = 1 / (1 + pow(10, (self.elo - other_team.elo) / 480))

    def update_team_after_match(self, goals_for, goals_against):
        self.all_GF += goals_for
        self.all_GA += goals_against

        if goals_for > goals_against:
            self.victories += 1
            self.real_outcome = 1
        elif goals_for < goals_against:
            self.losses += 1
            self.real_outcome = 0
        elif goals_for == goals_against:
            self.draws += 1
            self.real_outcome = 0.5

        self.calc_elo_after_match(abs(goals_for - goals_against))
        self.real_outcome = -1
        self.expected_outcome = -1

    def calc_k_factor(self):
        all_matches = self.victories + self.draws + self.losses

        if all_matches <= 10:
            self.k_factor = 15
        elif self.victories > (all_matches * 0.85) and all_matches > 10:
            self.k_factor = 25
        elif self.victories > (all_matches * 0.7) and all_matches > 10:
            self.k_factor = 21
        elif self.victories > (all_matches * 0.5) and all_matches > 10:
            self.k_factor = 18
        elif self.victories > (all_matches * 0.4) and all_matches > 10:
            self.k_factor = 15
        else:
            self.k_factor = 12

    def calc_elo_after_match(self, gd):
        if gd != 0 and gd > 1:
            self.elo = round(self.elo + self.k_factor * ((self.real_outcome - self.expected_outcome) * (gd * 0.75)))
        else:
            self.elo = round(self.elo + self.k_factor * (self.real_outcome - self.expected_outcome))
