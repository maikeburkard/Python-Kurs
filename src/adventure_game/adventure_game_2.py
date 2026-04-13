destiny = input("Möchtest du in den Wald oder in die Stadt gehen? ")

if (destiny == "Wald"):
    print("Du gehst in den Wald.")
    
    player_decision = input("Möchtest du dem Geräusch folgen oder wegrennen? ")

    if (player_decision == "folgen"):
        print("Du findest einen Schatz")

    elif(player_decision == "wegrennen"):
        print("Du stolperst und gehst nach Hause")

    else:
        print("Das habe ich nicht verstanden")

elif (destiny == "Stadt"):
    print("Du gehst in die Stadt.")

else:
    print("Bitte schreibe Wald oder Stadt.")
