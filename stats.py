import pandas as pd
import values

def loadStats(path):
    players = pd.read_excel(path)

    playersList = {}
    stats = {}

    roles = ["P", "D", "C", "A"]
    tiers = ["LOW", "MID", "TOP"]

    indexes = values.buildAllIndexes()

    for role in roles:
        stats[role] = {}
        for tier in tiers:
            stats[role][tier] = []

    for row in players.iterrows():

        if row[1][1] not in list(indexes.keys()):
            value = 0
        else:
            value = indexes[row[1][1]]

        if "P" in row[1][0]:
            if value >= 87:
                stats["P"]["TOP"].append([row[1][1], row[1][2], value, row[1][4] * 2, value/row[1][4] / 2])
                band = "TOP"
            elif value >= 65:
                stats["P"]["MID"].append([row[1][1], row[1][2], value, row[1][4], value/row[1][4]])
                band = "MID"
            else:
                stats["P"]["LOW"].append([row[1][1], row[1][2], value, 1, value])
                band = "LOW"
        elif "D" in row[1][0]:
            if value >= 85:
                stats["D"]["TOP"].append([row[1][1], row[1][2], value, int(row[1][4] * 1.5), value/ int(row[1][4] * 1.5)])
                band = "TOP"
            elif value >= 75:
                stats["D"]["MID"].append([row[1][1], row[1][2], value, row[1][4], value/row[1][4]])
                band = "MID"
            else:
                stats["D"]["LOW"].append([row[1][1], row[1][2], value, 1, value])
                band = "LOW"
        elif "C" in row[1][0]:
            if value >= 91:
                stats["C"]["TOP"].append([row[1][1], row[1][2], value, row[1][4] * 3, value/row[1][4] / 3])
                band = "TOP"
            elif value >= 75:
                stats["C"]["MID"].append([row[1][1], row[1][2], value, row[1][4], value/row[1][4]])
                band = "MID"
            else:
                stats["C"]["LOW"].append([row[1][1], row[1][2], value, 1, value])
                band = "LOW"
        else:
            if value >= 85:
                stats["A"]["TOP"].append([row[1][1], row[1][2], value, row[1][4] * 4, value/row[1][4] / 4])
                band = "TOP"
            elif value >= 70:
                stats["A"]["MID"].append([row[1][1], row[1][2], value, row[1][4], value/row[1][4]])
                band = "MID"
            else:
                stats["A"]["LOW"].append([row[1][1], row[1][2], value, 1, value])
                band = "LOW"

        playersList[row[1][1]] = [row[1][0], band]

    avgs = {}

    avgs["P"] = 0
    number = 0
    for elem in stats["P"]["MID"]:
        avgs["P"] += elem[3]
        number += 1
    for elem in stats["P"]["LOW"]:
        avgs["P"] += elem[3]
        number += 1
    avgs["P"] = avgs["P"] / number

    avgs["D"] = 0
    number = 0
    for elem in stats["D"]["MID"]:
        avgs["D"] += elem[3]
        number += 1
    for elem in stats["D"]["LOW"]:
        avgs["D"] += elem[3]
        number += 1
    avgs["D"] = avgs["D"] / number

    avgs["C"] = 0
    number = 0
    for elem in stats["C"]["MID"]:
        avgs["C"] += elem[3]
        number += 1
    for elem in stats["C"]["LOW"]:
        avgs["C"] += elem[3]
        number += 1
    avgs["C"] = avgs["C"] / number

    avgs["A"] = 0
    number = 0
    for elem in stats["A"]["MID"]:
        avgs["A"] += elem[3]
        number += 1
    for elem in stats["A"]["LOW"]:
        avgs["A"] += elem[3]
        number += 1
    avgs["A"] = avgs["A"] / number

    return playersList, stats, avgs

def removePlayer(players, role, band, name):
    section = players[role][band]
    for player in section:
        if player[0] == name:
            section.remove(player)
