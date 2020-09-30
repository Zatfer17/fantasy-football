import stats
import auction

def main():

    credits = 500
    names = ["TEO", "STE"]
    you = "TEO"
    budgetAllocation = {"P": 50, "D": 50, "C": 130, "A": 270}
    components = {"P": 0, "D": 1, "C": 1, "A": 1}
    numSlots = components["P"] + components["D"] + components["C"] + components["A"]
    numPlayers = len(names)
    playersList, players, avgs = stats.loadStats("data/listone.xlsx")
    gameAuction = auction.createAuction(credits, numPlayers, names, budgetAllocation, components)

    notEnded = 0

    print(players["P"]["TOP"])
    print(players["D"]["TOP"])
    print(players["C"]["TOP"])
    print(players["A"]["TOP"])

    while notEnded < (numSlots * numPlayers):
        for name in names:
            if notEnded < components["P"] * numPlayers:

                if notEnded == 0:
                    print("\n\n\n\n")
                    print(" /$$   /$$ /$$$$$$$$ /$$$$$$$$ /$$$$$$$  /$$$$$$$$ /$$$$$$$   /$$$$$$")
                    print("| $$  /$$/| $$_____/| $$_____/| $$__  $$| $$_____/| $$__  $$ /$$__  $$")
                    print("| $$ /$$/ | $$      | $$      | $$  \ $$| $$      | $$  \ $$| $$  \__/")
                    print("| $$$$$/  | $$$$$   | $$$$$   | $$$$$$$/| $$$$$   | $$$$$$$/|  $$$$$$ ")
                    print("| $$  $$  | $$__/   | $$__/   | $$____/ | $$__/   | $$__  $$ \____  $$")
                    print("| $$\  $$ | $$      | $$      | $$      | $$      | $$  \ $$ /$$  \ $$")
                    print("| $$ \  $$| $$$$$$$$| $$$$$$$$| $$      | $$$$$$$$| $$  | $$|  $$$$$$/")
                    print("|__/  \__/|________/|________/|__/      |________/|__/  |__/ \______/ ")
                    print("\n")

                print("\n\n")

                role = "P"

            elif notEnded < (components["P"] + components["D"]) * numPlayers:

                if notEnded == components["P"] * numPlayers:
                    print("\n\n\n\n")
                    print(" /$$$$$$$  /$$$$$$$$ /$$$$$$$$ /$$$$$$$$ /$$   /$$ /$$$$$$$  /$$$$$$$$ /$$$$$$$   /$$$$$$")
                    print("| $$__  $$| $$_____/| $$_____/| $$_____/| $$$ | $$| $$__  $$| $$_____/| $$__  $$ /$$__  $$")
                    print("| $$  \ $$| $$      | $$      | $$      | $$$$| $$| $$  \ $$| $$      | $$  \ $$| $$  \__/")
                    print("| $$  | $$| $$$$$   | $$$$$   | $$$$$   | $$ $$ $$| $$  | $$| $$$$$   | $$$$$$$/|  $$$$$$ ")
                    print("| $$  | $$| $$__/   | $$__/   | $$__/   | $$  $$$$| $$  | $$| $$__/   | $$__  $$ \____  $$")
                    print("| $$  | $$| $$      | $$      | $$      | $$\  $$$| $$  | $$| $$      | $$  \ $$ /$$  \ $$")
                    print("| $$$$$$$/| $$$$$$$$| $$      | $$$$$$$$| $$ \  $$| $$$$$$$/| $$$$$$$$| $$  | $$|  $$$$$$/")
                    print("|_______/ |________/|__/      |________/|__/  \__/|_______/ |________/|__/  |__/ \______/ ")

                    auction.updateSavings(gameAuction,"P")

                print("\n\n")

                role = "D"

            elif notEnded < (components["P"] + components["D"] + components["C"]) * numPlayers:

                if notEnded == (components["P"] + components["D"]) * numPlayers:
                    print("\n\n\n\n")
                    print( " /$$      /$$ /$$$$$$ /$$$$$$$  /$$$$$$$$ /$$$$$$ /$$$$$$$$ /$$       /$$$$$$$  /$$$$$$$$ /$$$$$$$   /$$$$$$")
                    print("| $$$    /$$$|_  $$_/| $$__  $$| $$_____/|_  $$_/| $$_____/| $$      | $$__  $$| $$_____/| $$__  $$ /$$__  $$")
                    print("| $$$$  /$$$$  | $$  | $$  \ $$| $$        | $$  | $$      | $$      | $$  \ $$| $$      | $$  \ $$| $$  \__/")
                    print("| $$ $$/$$ $$  | $$  | $$  | $$| $$$$$     | $$  | $$$$$   | $$      | $$  | $$| $$$$$   | $$$$$$$/|  $$$$$$")
                    print("| $$  $$$| $$  | $$  | $$  | $$| $$__/     | $$  | $$__/   | $$      | $$  | $$| $$__/   | $$__  $$ \____  $$")
                    print("| $$\  $ | $$  | $$  | $$  | $$| $$        | $$  | $$      | $$      | $$  | $$| $$      | $$  \ $$ /$$  \ $$")
                    print("| $$ \/  | $$ /$$$$$$| $$$$$$$/| $$       /$$$$$$| $$$$$$$$| $$$$$$$$| $$$$$$$/| $$$$$$$$| $$  | $$|  $$$$$$/")
                    print("|__/     |__/|______/|_______/ |__/      |______/|________/|________/|_______/ |________/|__/  |__/ \______/")

                    auction.updateSavings(gameAuction, "D")

                print("\n\n")

                role = "C"

            else:

                if notEnded == (components["P"] + components["D"] + components["C"]) * numPlayers:
                    print("\n\n\n\n")
                    print("  /$$$$$$  /$$$$$$$$ /$$$$$$$  /$$$$$$ /$$   /$$ /$$$$$$$$ /$$$$$$$   /$$$$$$")
                    print(" /$$__  $$|__  $$__/| $$__  $$|_  $$_/| $$  /$$/| $$_____/| $$__  $$ /$$__  $$")
                    print("| $$  \__/   | $$   | $$  \ $$  | $$  | $$ /$$/ | $$      | $$  \ $$| $$  \__/")
                    print("|  $$$$$$    | $$   | $$$$$$$/  | $$  | $$$$$/  | $$$$$   | $$$$$$$/|  $$$$$$")
                    print(" \____  $$   | $$   | $$__  $$  | $$  | $$  $$  | $$__/   | $$__  $$ \____  $$")
                    print(" /$$  \ $$   | $$   | $$  \ $$  | $$  | $$\  $$ | $$      | $$  \ $$ /$$  \ $$")
                    print("|  $$$$$$/   | $$   | $$  | $$ /$$$$$$| $$ \  $$| $$$$$$$$| $$  | $$|  $$$$$$/")
                    print("\______/    |__/   |__/  |__/|______/|__/  \__/|________/|__/  |__/ \______/")

                    auction.updateSavings(gameAuction, "C")

                print("\n\n")

                role = "A"

            if name == you:
                band = input(">>Tell me a band: ")
                while (band != "TOP" and band != "MID" and band != "LOW"):
                    band = input(">>Tell me a band: ")
                player = auction.suggestBest(players, role, band)
                print(">>>>Consider offering for: " + str(player))

            display = input(">>>>Do you want to see the best " + role + " still open? ")
            while (display != "YES" and display != "NO"):
                display = input(">>>>Do you want to see the best " + role + " still open? ")
            if display == "YES":
                topPlayers = sorted(players[role]["TOP"], key=lambda x: x[4], reverse=True)
                print(">>>>>>Best TOP " + role + ":")
                l = min(5, len(topPlayers))
                for i in range(l):
                    print(">>>>>>>> " + str(i) + ". " + str(topPlayers[i][0]) + " " + str(topPlayers[i][2]))

                midPlayers = sorted(players[role]["MID"], key=lambda x: x[4], reverse=True)
                print(">>>>>>Best MID " + role + ":")
                l = min(5, len(midPlayers))
                for i in range(l):
                    print(">>>>>>>> " + str(i) + ". " + str(midPlayers[i][0]) + " " + str(midPlayers[i][2]))

                lowPlayers = sorted(players[role]["MID"], key=lambda x: x[4], reverse=True)
                print(">>>>>>Best LOW " + role + ":")
                l = min(5, len(lowPlayers))
                for i in range(l):
                    print(">>>>>>>> " + str(i) + ". " + str(lowPlayers[i][0]) + " " + str(lowPlayers[i][2]))

            player = input(">>Who are you offering for? ")
            while player not in playersList.keys():
                player = input(">>Who are you offering for? ")

            maxPrice, mostConvenient, limit = auction.calculateMaxOffer(gameAuction, players, playersList, avgs, player, numPlayers)
            print(">>>>Go for " + player + ", offer no more than " + str(maxPrice))
            if mostConvenient != None:
                print(">>>>However consider that reached an offer of " + str(limit) + " " + mostConvenient + " is a better choice")

            auctionNotEnded = True
            while auctionNotEnded:
                currentOffer = input(">>>>Tell me current offer: ")
                while not currentOffer.isdigit():
                    currentOffer = input(">>>>Tell me current offer: ")
                currentOffer = int(currentOffer)
                betterPlayer, worthOffering = auction.checkIfWorthOffering(players, playersList, player, currentOffer)
                if worthOffering and currentOffer <= maxPrice:
                    print(">>>>>>You can offer that price")
                else:
                    if currentOffer > maxPrice:
                        print(">>>>>>Exceeded suggested price, stop offering")
                    if not worthOffering:
                        print(">>>>>>There are better players for that price, eg: " + betterPlayer)
                        print(">>>>>>Buy at your own risk")

                response = input(">>>>Has the auction ended? ")
                while (response != "YES" and response != "NO"):
                    response = input(">>>>Has the auction ended? ")
                if response == "YES":
                    auctionNotEnded = False

            name = input(">>>>>>Who bought the player? ")
            while name not in names:
                name = input(">>>>>>Who bought the player? ")
            cost = input(">>>>>>>>For how much ? ")
            while not cost.isdigit():
                cost = input(">>>>>>>>For how much ? ")
            cost = int(cost)
            auction.addPlayer(gameAuction, playersList, players, name, player, cost, you)

            auction.updateProbabilities(gameAuction, names, you)

            notEnded += 1

    print("Auction ended")

if __name__ == "__main__":
    main()



