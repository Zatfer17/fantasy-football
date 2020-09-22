# GENERAL CONSIDERATIONS:
#   - 3 BANDS: TOP TIER, MID TIER, LOW TIER
#   - RANK PLAYERS PER BAND DEPENDING ON PRICE/PALATABILITY INDEX
#   - FOR EACH ROLE: 1 TOP PLAYER, 1 RISING STAR, BEST MID TIER PLAYERS
#   - PRIORITIZE PENALTY SHOOTERS DUE TO NEW SERIE A RULE
#   - ASSIGN A BUDGET TO EACH ROLE, EXCEEDING BUDGET GOES TO MIDFIELDERS AND STRIKERS
#   - 250 STRIKERS, 150 MIDFIELDERS, 50 DEFENDERS, 50 KEEPERS

#   A OGNI CHIAMATA RICALCOLO INDICE DI APPETIBILITA':
#   - IL GIOCATORE CHIAMATO MANTIENE L'INDICE DI APPETIBILITA' PRECEDENTE
#   - TUTTI GLI ALTRI GIOCATORI RICALCOLANO L'INDICE NELLO SCENARIO IN CUI IL GIOCATORE CHIAMATO E' STATO VENDUTO AD UN ALTRO PARTECIPANTE
#   STABILISCO L'OFFERTA MASSIMA SULLA BASE DELLA PROBABILITA' DI ACQUISTO, BUDGET RESIDUO E FASCIA
#   (FASCIA INFLUISCE CON MOLTIPLICATORE, BUDGET RESIDUO INFLUISCE SOTTRAENDO A OFFERTA SLOT_LIBERI * PREZZO MEDIO GIOCATORI FASCIA MEDIA RESIDUI,
#   PROBABILITA' INFLUISCE COME FRAZIONE DEL BUDGET CUSCINETTO)
#   OFFRO FINTANTO CHE INDICE DI APPETIBILITA' DEL GIOCATORE IN ASTA (APPETIBILITA'/ OFFERTA CORRENTE) E' MAGGIORE
#   DELL'INDICE DI APPETIBILITA' MIGLIORE DEI GIOCATORI NON VENDUTI E NON SFORO OFFERTA MASSIMA

import stats
import copy

def createAuction(credits, numPlayers, names, budgetAllocation, components):

    auction = {}

    for num in range(numPlayers):
        player = {}

        player["CREDITS"] = credits
        player["PLAYERS"] = {}
        player["PLAYERS"]["P"] = []
        player["PLAYERS"]["D"] = []
        player["PLAYERS"]["C"] = []
        player["PLAYERS"]["A"] = []

        auction[names[num]] = player

    auction["SAVINGS"] = 0

    auction["SLOTS"] = {}

    auction["SLOTS"]["P"] = {}
    auction["SLOTS"]["P"]["OWN"] = components["P"]
    auction["SLOTS"]["P"]["ENEMY"] = components["P"] * (numPlayers - 1)

    auction["SLOTS"]["D"] = {}
    auction["SLOTS"]["D"]["OWN"] = components["D"]
    auction["SLOTS"]["D"]["ENEMY"] = components["D"] * (numPlayers - 1)

    auction["SLOTS"]["C"] = {}
    auction["SLOTS"]["C"]["OWN"] = components["C"]
    auction["SLOTS"]["C"]["ENEMY"] = components["C"] * (numPlayers - 1)

    auction["SLOTS"]["A"] = {}
    auction["SLOTS"]["A"]["OWN"] = components["A"]
    auction["SLOTS"]["A"]["ENEMY"] = components["A"] * (numPlayers - 1)

    auction["BUDGET"] = budgetAllocation

    auction["COMPONENTS"] = copy.deepcopy(components)

    return auction

def addPlayer(gameAuction, playersList, players, name, player, cost, you):
    gameAuction[name]["PLAYERS"][playersList[player][0]].append([player, cost])
    gameAuction[name]["CREDITS"] -= cost
    role, band = playersList[player]
    if name == you:
        gameAuction["BUDGET"][role] -= cost
        gameAuction["COMPONENTS"][role] -= 1
    stats.removePlayer(players, playersList[player][0], playersList[player][1], player)

def updateProbabilities(gameAuction, names, myName):

    ownSlots = {}
    ownSlots["P"] = 0
    ownSlots["D"] = 0
    ownSlots["C"] = 0
    ownSlots["A"] = 0

    enemySlots =  {}
    enemySlots["P"] = 0
    enemySlots["D"] = 0
    enemySlots["C"] = 0
    enemySlots["A"] = 0

    for name in names:
        if name == myName:
            gameAuction["SLOTS"]["P"]["OWN"] -= len(gameAuction[name]["PLAYERS"]["P"])
            gameAuction["SLOTS"]["D"]["OWN"] -= len(gameAuction[name]["PLAYERS"]["D"])
            gameAuction["SLOTS"]["C"]["OWN"] -= len(gameAuction[name]["PLAYERS"]["C"])
            gameAuction["SLOTS"]["A"]["OWN"] -= len(gameAuction[name]["PLAYERS"]["A"])
        else:
            gameAuction["SLOTS"]["P"]["ENEMY"] -= len(gameAuction[name]["PLAYERS"]["P"])
            gameAuction["SLOTS"]["D"]["ENEMY"] -= len(gameAuction[name]["PLAYERS"]["D"])
            gameAuction["SLOTS"]["C"]["ENEMY"] -= len(gameAuction[name]["PLAYERS"]["C"])
            gameAuction["SLOTS"]["A"]["ENEMY"] -= len(gameAuction[name]["PLAYERS"]["A"])


def updateSavings(gameAuction, role):
    gameAuction["SAVINGS"] += gameAuction["BUDGET"][role]

def findPlayer(players, name, role, band):
    for elem in players[role][band]:
        if elem[0] == name:
            return elem

def calculateMaxOffer(gameAuction, players, playersList, avgs, player, numPlayers):
    role, band = playersList[player]
    myPlayer = findPlayer(players, player, role, band)
    price = myPlayer[3]

    residual = gameAuction["BUDGET"][role] - price
    yetToPay = (gameAuction["COMPONENTS"][role] - 1) * avgs[role]
    if residual < yetToPay:
        price -= (yetToPay - residual)

    if gameAuction["SLOTS"][role]["OWN"] <= gameAuction["SLOTS"][role]["ENEMY"] / (numPlayers - 1):
        if role == "P":
            multiplier = 1/10
        elif role == "D":
            multiplier = 2/10
        elif role == "C":
            multiplier = 5/10
        else:
            multiplier = 1
        price += multiplier * gameAuction["SAVINGS"]

    mostConvenient = findMostConvenient(players, playersList, player)
    bestconvenience = mostConvenient[4]

    currentOffer = 1
    currentConvenience = myPlayer[2] / currentOffer
    while currentConvenience > bestconvenience:
        currentOffer += 1
        currentConvenience = myPlayer[2] / currentOffer



    return price, mostConvenient[0], currentOffer

def findMostConvenient(players, playersList, player):
    role, band = playersList[player]
    highest = 0
    best = None
    for elem in players[role][band]:
        if elem[4] > highest and elem[0] != player:
            best = elem
    return best

def calculateCurrentConvenience(players, playersList, player, currentPrice):
    role, band = playersList[player]
    value = findPlayer(players, player, role, band)[2]
    return value/currentPrice

def checkIfWorthOffering(players, playersList, player, currentPrice):
    currentConvenience = calculateCurrentConvenience(players, playersList, player, currentPrice)
    role, band = playersList[player]
    for elem in players[role][band]:
        if elem[4] > currentConvenience and elem[0] != player:
            return elem[0], False
    return None, True

def suggestBest(players, role, band):
    highest = 0
    name = None
    for elem in players[role][band]:
        if elem[4] > highest:
            highest = elem[4]
            name = elem[0]
    return name

