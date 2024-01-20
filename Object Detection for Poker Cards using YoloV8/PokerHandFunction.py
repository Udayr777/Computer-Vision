def findPokerHand(hand):
    ranks = []
    suits = []
    possibleRanks = []

    # Dividing Rank and Suit
    for card in hand:
        if len(card) == 2:
            rank = card[0]
            suit = card[1]
        else:
            rank = card[0:2]
            suit = card[2]
        if rank == "A":
            rank = 14
        elif rank =="K":
            rank = 13
        elif rank == "Q":
            rank = 12
        elif rank == "J":
            rank = 11
        ranks.append(int(rank))
        suits.append(suit)


        # sort it to make it easier
        sortedRanks = sorted(ranks)

    # Royal Flush and Straight Flush and Flush
    if suits.count(suits[0]) == 5: # check for flush
        if 14 in sortedRanks and 13 in sortedRanks and 12 in sortedRanks and 11 in sortedRanks \
                and 10 in sortedRanks:
            possibleRanks.append(10)
            # Straight Flush
            # 10 11 12 13 14
            # 11 == 10 + 1
        elif all(sortedRanks[i] == sortedRanks[i-1]+1 for i in range(1, len(sortedRanks))):# Straight Flush
            possibleRanks.append(9)
        else:
            possibleRanks.append(6) # -- Flush

        # Straight
        # 10 11 12 13 14
        #  11 == 10 + 1
    if all(sortedRanks[i] == sortedRanks[i - 1] + 1 for i in range(1, len(sortedRanks))):
        possibleRanks.append(5)

    handUniqueVals = list(set(sortedRanks))

    # Four of the kind and Full House
    # 3 3 3 3 5 -- set -- 3 5 ---- unique values = 2 -- Four of a Kind
    # 3 3 3 5 5 -- set -- 3 5 --- -- unique values = 2 --Full House

    if len(handUniqueVals) == 2:
        for val in handUniqueVals:
            if sortedRanks.count(val) == 4: # -- Four of a Kind
                possibleRanks.append(8)
            if sortedRanks.count(val) == 3: # --Full House
                possibleRanks.append(7)

    # Three of a Kind and a Pair
    # 5 5 5 6 7 -- set --  5 6 7 -- unique values = 3 --Three of kind
    # 8 8 7 7 2 -- set -- 8 7 2 -- unique values = 3 --Two pair
    if len(handUniqueVals) == 3:
        for val in handUniqueVals:
            if sortedRanks.count(val) == 3: # --Three of kind
                possibleRanks.append(4)
            if sortedRanks.count(val) == 2: # -Two pair
                possibleRanks.append(3)

    # Pair
    # 5 5 3 6 7 -- set -- 5 3 6 7 -- unique values = 4 -- pair
    if len(handUniqueVals) == 4:
        possibleRanks.append(2)
   # print(handUniqueVals)
    # High Card
    if not possibleRanks:
        possibleRanks.append(1)

    pokerHandRanks = {10: "Royal Flush", 9: "Straight Flush", 8: "Four of a Kind", 7: "Full House", 6: "Flush",
                      5: "Straight", 4: "Three of a Kind", 3: "Two Pair", 2: "Pair", 1: "High Card"}

    output = pokerHandRanks[max(possibleRanks)]
    print(hand, output)
    return output

if __name__ == "__main__":
    # sending to the findPokerHand
    findPokerHand(["AH", "KH", "QH", "JH","10H"]) # AH -- A of Hearts, KH -- K of Hearts, QH --Q of Hearts, JK -- J of Hearts, 10H --10 of Hearts ----> Royal Flush
    findPokerHand(["QC", "JC", "10C", "9C","8C"])  # QC -- Q of Clubs, JC -- K of Clubs, 10C -- 10 of Clubs, 9C -- 9 of Clubs, 8C -- 8 of Clubs ----> Straight Flush
    findPokerHand(["5C", "5S", "5H", "5D", "QH"])  # Four of Kind
    findPokerHand(["2H", "2D", "2S", "10H", "10C"])  # Full House
    findPokerHand(["2D", "KD", "7D", "6D", "5D"])  # Flush
    findPokerHand(["JC", "10H", "9C", "8C", "7D"])  # Straight
    findPokerHand(["10H", "10C", "10D", "2D", "5S"])  # Three of a Kind
    findPokerHand(["KD", "KH", "5C", "5S", "6D"])  # Two Pair
    findPokerHand(["2D", "2S", "9C", "KD", "10C"])  # Pair
    findPokerHand(["KD", "5H", "2D", "10C", "JH"])  # High Card



