try:
    print("Vítej v mém malém kvízu!")
    pokracovat = "ano"
    hrat = "ano"
    while True:
        hrat = input("Chceš hrát? ").lower()
        if hrat in ["ano", "ne"]:
            break
        else:
            print("Prosím, zadej buď ANO nebo NE.")

    if hrat != "ano":
        print("Měj se hezky! :)")
        quit()
    print("Dobře! Tak začneme :)")

    while pokracovat == "ano":
        score = 0
        odpoved = input("Jak se jmenuje tato matematická konstanta π=3.14?\n").lower()
        if odpoved == "ludolfovo číslo" or odpoved == "ludolfovo cislo":
            print("Správně!")
            score += 1
        else:
            print("Špatná odpověď!")

        odpoved = input("\nKdo objevil polarografii?\n").lower()
        if odpoved == "jaroslav heyrovský" or odpoved == "jaroslav heyrovsky":
            print("Správně!")
            score += 1
        else:
            print("Špatná odpověď!")

        odpoved = input("\nKolik medailí získala dohromady Martina Sáblíková ve Vancouveru, Soči a Pchjongčchangu?\n").lower()
        if odpoved == "6" or odpoved == "6 medailí":
            print("Správně!")
            score += 1
        else:
            print("Špatná odpověď!")

        odpoved = input("\nJak se jmenovalo hnutí, které vzniklo jako reakce na násilné potlačení studentské demonstrace v listopadu 1989?\n").lower()
        if odpoved == "občanské fórum" or odpoved == "obcanske forum":
            print("Správně!")
            score += 1
        else:
            print("Špatná odpověď!")

        odpoved = input("\nCo znamená zkratka AI?\n").lower()
        if odpoved == "artificial intelligence":
            print("Správně!")
            score += 1
        else:
            print("Špatná odpověď!")

        percent_score = int((score / 5) * 100)

        if score == 0:
            print("\nSmůla! Nemáš ani jednu správnou odpověď!")
        elif score == 1:
            print("\nNic moc! Máš jen " + str(score) + " správnou odpověď! Což je " + str(percent_score) + "%!")
        elif score > 1 and score < 5:
            print("\nSlušný výkon! Máš celkem " + str(score) + " správné odpovědi! Což je " + str(percent_score) + "%!")
        else:
            print("\nJsi génius! Máš celkem " + str(score) + " správných odpovědí! Což je " + str(percent_score) + "%!")

        while True:
            pokracovat = input("\nChceš začít znovu? (ano/ne): ").lower()
            if pokracovat in ["ano", "ne"]:
                break
            else:
                print("\nProsím, zadej buď ANO nebo NE.")
    print("Měj se hezky! :)")

except KeyboardInterrupt:
    pass
