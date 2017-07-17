uryvek = "Má kresba ovšem není zdaleka tak půvabná jako model.Ale za to já nemohu. " \
         "Dospělí mě odradili od malířské kariéry,když mi bylo šest let, " \
         "a proto jsem se nenaučil kreslit nic jiného než zavřené a otevřené hroznýše. " \
         "Udiveně jsem se díval na ten zjev. Považte jen, že jsem byl na tisíc mil od jakéhokoliv obydleného kraje. " \
         "A můj človíček nevypadal, jako by zabloudil ani jako by byl na smrt unavený nebo vyhladovělý, " \
         "polomrtvý žízní nebo na smrt vylekán."


# Vypis pocet znaku uryvku.
def string_length():
    print(len(uryvek))
    pass


# Premen vsechna pismena v uryvku na velka pismena (upper case) a vypis ho.
def upper_case():
    print(uryvek.upper())
    pass


# Vypis 127. znak uryvku pomoci indexu
def char_127th():
    print(uryvek[126])
    pass


# Vypis 1. znak uryvku pomoci indexu
def char_1st():
    print(uryvek[0])
    pass


# Vypis posledni znak uryvku pomoci indexu
def char_last():
    print(uryvek[-1])
    pass


# Vypis 100. znak od konce uryvku pomoci indexu
def char_100th_last():
    print(uryvek[-100])
    pass


# Vypis prvnich 52 znaku z uryvku
def char_first_52():
    print(uryvek[:52])
    pass


# Vypis retezec znaku od 100. pozice az do konce retezce
def char_from_100():
    print(uryvek[99:])
    pass


# Vypis retezec znaku od 50. pozice do 100. pozice (vcetne)
def char_50_to_100():
    print(uryvek[49:99])
    pass


# --------------------------------------------

# Vypis Viet Code je nejnejnej... (100 krat nej) ...nejlepsi kurz ever!
def repeated_string():
    print("Viet Code je " + "nej" * 100 + "lepsi kurz ever!")
    pass
