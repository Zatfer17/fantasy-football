import pandas as pd

def loadStats(path):
    return pd.read_excel(path)

RANKINGS = {
    "JUVENTUS": 1,
    "LAZIO": 1,
    "INTER": 1,
    "ATALANTA": 1,
    "ROMA": 2,
    "MILAN": 3,
    "NAPOLI": 4,
    "PARMA": 5,
    "VERONA": 6,
    "FIORENTINA": 7,
    "SASSUOLO": 8
}

def buildPlayersIndexes(stats, type):
    indexes = {}
    for row in stats.iterrows():
        name = row[1][0]
        team = row[1][1]
        appearances = row[1][2]
        avg_fantascore = row[1][4]
        scored_goals = row[1][5] + row[1][9]
        assists = row[1][11] + row[1][12]
        yellow_cards = row[1][13]
        red_cards = row[1][14]
        conceded_goals = row[1][6]
        saved_penalties = row[1][7]

        #TODO LATER
        is_freekicker = 0
        is_penalty_shooter = 0
        #TODO add difference between normal score and fantascore to measure how much a fantasy football player it is

        index = 0

        if appearances > 15:
            if type == "P":
                index += appearances * 60 / 38
                param_a = 1
                param_b = 1
                param_c = 3 * param_b
                denom = 6 * param_a - 32 / 38 * param_b + 4 / 38 * param_c
                toAdd = avg_fantascore * param_a - conceded_goals / appearances * param_b + saved_penalties / appearances * param_c
                index += toAdd * 40 / denom
            elif type == "D":
                index += appearances * 40 / 38
                param_a = 1
                param_b = param_a
                param_c = 3 * param_b
                param_d = param_a
                param_e = 2 * param_d
                denom = 7.5 * param_a + 7 / 38 * param_b + 7 / 38 * param_c
                toAdd = avg_fantascore * param_a + assists/appearances * param_b + scored_goals/appearances * param_c - yellow_cards/appearances * param_d - red_cards/appearances * param_e
                index += toAdd * 60 / denom
                if team.upper() in list(RANKINGS.keys()):
                    index += 3 / RANKINGS[team.upper()]
                if index >= 100:
                    index = 100
            elif type == "C":
                index += appearances * 30 / 38
                param_a = 1
                param_b = param_a
                param_c = 3 * param_b
                param_d = param_a
                param_e = 2 * param_d
                denom = 7.5 * param_a + 15 / 38 * param_b + 10 / 38 * param_c
                toAdd = avg_fantascore * param_a + assists / appearances * param_b + scored_goals / appearances * param_c - yellow_cards / appearances * param_d - red_cards / appearances * param_e
                index += toAdd * 70 / denom
                if team.upper() in list(RANKINGS.keys()):
                    index += 3 / RANKINGS[team.upper()]
                if index >= 100:
                    index = 100
            else:
                index += appearances * 30 / 38
                param_a = 1
                param_b = param_a
                param_c = 4 * param_b
                param_d = param_a
                param_e = 2 * param_d
                denom = 10 * param_a + 8 / 38 * param_b + 36 / 38 * param_c
                toAdd = avg_fantascore * param_a + assists / appearances * param_b + scored_goals / appearances * param_c - yellow_cards / appearances * param_d - red_cards / appearances * param_e
                index += toAdd * 70 / denom
                if team.upper() in list(RANKINGS.keys()):
                    index += 3 / RANKINGS[team.upper()]
                if index >= 100:
                    index = 100

        indexes[name] = index
    #print(sorted(list(indexes.values()), reverse=True))
    return indexes

def buildAllIndexes():

    P = buildPlayersIndexes(loadStats("data/keepers.xlsx"), "P")
    D = buildPlayersIndexes(loadStats("data/defenders.xlsx"), "D")
    C = buildPlayersIndexes(loadStats("data/midfielders.xlsx"), "C")
    A = buildPlayersIndexes(loadStats("data/strikers.xlsx"), "A")

    return dict(list(P.items()) + list(D.items()) + list(C.items()) + list(A.items()))