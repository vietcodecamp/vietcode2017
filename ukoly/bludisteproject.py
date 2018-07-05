import random

#PROMENNE
hrac_zivoty = 3
# souradnice panaka
souradnice_x = 0
souradnice_y = 0
#pocet prekazek - pomocna promenna
prekazek = 0
#zavolan dacos
dacosed = False
#zije
nazivu = True

#pole hrace, S - start, F- finish, Unicode - kosticka
pole_hrace = [["S", "\u1AC0", "\u1AC0", "\u1AC0", "\u1AC0"],
              ["\u1AC0", "\u1AC0", "\u1AC0", "\u1AC0", "\u1AC0"],
              ["\u1AC0", "\u1AC0", "\u1AC0", "\u1AC0", "\u1AC0"],
              ["\u1AC0", "\u1AC0", "\u1AC0", "\u1AC0", "\u1AC0"],
              ["\u1AC0", "\u1AC0", "\u1AC0", "\u1AC0", "F"]]

#pole, kde budou prekazky
# 0 = prazdne pole
# 1 = pole s prekazkou
pole_backend = [["S", 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, "F"]]

# ---------------------------------------------------------------------------------------------------------------
#DEFS


#vypln min, prijma argument nejvetsi pocet prekazek
def vypln_min(max_pocet_prekazek):
    global pole_backend
    global prekazek
    #pro i od 0 do 4 -----------[0,1,2,3,4]
    for i in range(5):
        #pro j od 0 do 4 -------[0,1,2,3,4]
        for j in range(5):
            #tedy pro jedno i je 5x j - tedy vsechny kombinace souradnice od [0,0] do [4,4] coz je velikost pole
            #jestli policko v poli rovno 0, tak muzeme pridat prekazku s urcitou pravdepodobnosti
            if(pole_backend[i][j] == 0):
                #2/3  = 66%
                #if (random.randint(1, 3) == 1) or random.randint(1,3) == 2:
                #1/2 = 50%
                if (random.randint(1, 2) == 1):
                    #pokud sance vyjde, dame na pole 1 coz znamena ze je to prekazka
                    pole_backend[i][j] = 1
                    #pokazde pridame pocet prekazek
                    prekazek = prekazek + 1
            if (prekazek == max_pocet_prekazek):
                return
        #jestli bude pocet prekazek roven max poctu, tak nemusime dale pridavat prekazky



#vypis pole s parametrem pole ktere chceme vypsat
def vypis(pole):
    #odradkujeme
    print()
    #foreach vs for
    #jelikoz pouze cteme, tak pouzijeme zjednodusenou verzi
    #pro kazdy seznam v poli       [ [2,3,]. [3,4], [4,5] ]
    for seznam in pole:
        #pro kazdy prvek v seznamu     2 3 3 4 4 5
        for prvek in seznam:
            #vypiseme vsechny prvky v seznamu do jednoho radku oddelene mezerou
            print(prvek, end = " ")
        #po skonceni vypisu jednoho seznamu odradkujeme abychom dalsi seznam psali na novou radku
        #tim udelame tabulku
        print()
    #odradkujeme kvuli ostatnim funkcim
    print()

#vyber tahu s parametrem tah - "W", "S", "A", "D"
def vyber_tahu(tah):
    #global promenne abychom mohli upravovat souradnice panaka vzdycky
    global souradnice_x
    global souradnice_y
    #budeme upravovat i vizualni pole hrace
    global pole_hrace
    #zada tah a abychom se vyhli case sensitivity tak .lower()
    #pri vyberu tahu, pokud tah je dane pismeno a zaroven jeho vyber nejde do zaporneho indexu tedy mimo pole, pak:
    if (tah == "w") and (souradnice_x - 1 >= 0):
        #na soucasne pole hrace dame prazdnou kosticku
        pole_hrace[souradnice_x][souradnice_y] = "\u1AC0"
        #zmenime souradnice hrace ve smeru toho ktery zvolil
        souradnice_x = souradnice_x - 1
        #na nove souradnice hrace pridame snehulaka
        pole_hrace[souradnice_x][souradnice_y] = "\u26C4"
        # zavolame funkce pro vypis pole po kazdem tahu aby hrac videl kde stoji
        vypis(pole_hrace)
        # porovname zda li hrac nestoupl na pole s hadankou
        porovnavani()
    elif (tah == "s") and (souradnice_x + 1 <= 4):
        pole_hrace[souradnice_x][souradnice_y] = "\u1AC0"
        souradnice_x = souradnice_x + 1
        pole_hrace[souradnice_x][souradnice_y] = "\u26C4"
        vypis(pole_hrace)
        porovnavani()
    elif (tah == "d") and (souradnice_y + 1 <= 4):
        pole_hrace[souradnice_x][souradnice_y] = "\u1AC0"
        souradnice_y = souradnice_y + 1
        pole_hrace[souradnice_x][souradnice_y] = "\u26C4"
        vypis(pole_hrace)
        porovnavani()
    elif (tah == "a") and (souradnice_y - 1 >= 0):
        pole_hrace[souradnice_x][souradnice_y] = "\u1AC0"
        souradnice_y = souradnice_y - 1
        pole_hrace[souradnice_x][souradnice_y] = "\u26C4"
        vypis(pole_hrace)
        porovnavani()
    else:
        #pokud pri zmacknuti neceho jineho, zustane na miste
        print("Neplatne zadani, zadej znovu.")

#hrac ztrati zivot
def ztracis_zivot():
    #upravujeme promenou hrac_zivoty = 3
    global hrac_zivoty
    #odecteme a ulozime
    hrac_zivoty = hrac_zivoty - 1
    #vypiseme
    print("Tvuj pocet zivotu je: {}".format(hrac_zivoty))

#kontrola jestli hrac jeste neprohral x nevyhral
def kontrola():
    #globalni promenne
    global hrac_zivoty
    global souradnice_x
    global souradnice_y
    #globalni boolean, urcujici pokracovani hry
    global nazivu
    #pokud ma 0 zivotu, tak zemrel
    if hrac_zivoty <= 0:
        #zmenime pravdu na nepravdu
        nazivu = False
        #podekujeme za hru
        print("Dosli ti zivoty, prohral jsi!")
        print("Dekujeme za hru!")
    #pokud je na [4,4] - Finish
    if souradnice_x == 4 and souradnice_y == 4:
        print("Dosel jsi do cile, vyhral jsi!")
        print("Dekujeme za hru!")
        nazivu = False

#porovname jestli stoji na poli s hadankou
def porovnavani():
    #pokud je na soucasnem poli panaka v pole_backend prekazka, tedy 1
    if(pole_backend[souradnice_x][souradnice_y] == 1):
        #nahodne vybereme hadanku
        #1/8 = 12.5% pro kazdou hadanku
        volat_hadanku(random.randint(1,8))
        #volat_hadanku(6)


#vola hadanku na zaklade nahodneho cislo ktere dostane
def volat_hadanku(cislo):
    global dacosed
    if cislo == 1:
        hai_mac()
    elif cislo == 2:
        karyn()
    elif cislo == 3:
        vrat_se()
    #dacos je specialni funkce
    #jelikoz dacos pretrvava vice kol, tak abychom se vyvarovali dvojnemu zavolani stejne funkce
    #budeme overovat zda je uz "dacosnutej"
    elif (cislo == 4) and not(dacosed):
        dacos()
    elif cislo == 5:
        roman()
    elif cislo == 6:
        minh_tri()
    elif cislo == 7:
        monika()
    elif cislo == 8:
        nitka()
#---------------------------------------------------------------------------------------------------------------

#HADANKY
def minh_tri():
    #resetujeme pole_backend na "default"
    global pole_backend
    global prekazek
    prekazek = 0
    pole_backend = [[0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, "F"]]
    #vypisem co se stalo
    print("Sel jsi a potkal jsi Minh Tri Pham!")
    print("Minh Tri Pham nam hacknul kod a zvysil pocet a polohy hadanek")
    #vyplni miny pomoci funkce s nahodne vetsim poctem min a jinak
    vypln_min(random.randint(11, 13))


def nitka():
    global hrac_zivoty
    print("Potkal jsi Nitku, ktera si prave byla zabehat.")
    print("Pridal ses k ni a zlepsil sis kondici!")
    print("Health + 1")
    hrac_zivoty = hrac_zivoty + 1
    print("Tvuj pocet zivotu je: {}".format(hrac_zivoty))


def monika():
    global souradnice_x
    global souradnice_y
    global pole_hrace
    print("Omylem si vrazil do Moniky.")
    print("Monika nema slitovani.")
    print("Monika ti dava kop z otocky.")
    print("Kop je tak silny, ze letis na jakekoliv nahodne policko a ztracis zivot.")
    ztracis_zivot()
    #nejdriv dame na souradnici kde stoji kosticku
    pole_hrace[souradnice_x][souradnice_y] = "\u1AC0"
    #pote dame nahodne souradnice
    souradnice_x = random.randint(0, 4)
    souradnice_y = random.randint(0, 4)
    #a pote na tez souradnice dame pandulaka
    pole_hrace[souradnice_x][souradnice_y] = "\u26C4"
    vypis(pole_hrace)

def roman():
    print("Potkal jsi Romana, ktery ti dal ochutnat svoje cupcakes")
    print("Byl jsi otraven")
    ztracis_zivot()

def dacos():
    #global dacosed boolean
    global dacosed
    #pokud se zavola tato funkce, hrac je dacosnuty, tedy dacosed = True
    dacosed = True
    print("Wild Dacos has appeared! ")
    print("Dacos used Body slam!")
    print("It\'s super effective!")
    print("You are confused!")
    #do cyklu aby byl confused na 2 tahy
    for i in range(2):
        #zada tah, zmensime
        move = input("Move: ").lower()
        #cyklus kvuli opakovani inputu kvuli neplatnemu zadani
        while True:
            #podle move, priradime ten druhy opacny k tomu
            if(move == "w"):
                move = "s"
                #kdyz zmenime, tak zrusime cyklus while
                break
            elif(move == "s"):
                move = "w"
                break
            elif(move == "a"):
                move = "d"
                break
            elif(move == "d"):
                move = "a"
                break
            else:
                #pokud zada spatne, vypiseme a nechame opet zadat
                print("Neplatne zadani, zadej znovu.")
                move = input("Move: ").lower()
        #az zada spravne tak volame funkci vyber tahu se zmenenym tahem
        vyber_tahu(move)
        kontrola()
        #pokud je v cili, vypneme cyklus
        if not(nazivu):
            return
    #Po dvou koleh se oznami ze uz neni confused
    print("You\'re not confused anymore")
    #zmenime z dacosnuty na dacosnutelny
    dacosed = False

def vrat_se():
    global souradnice_x
    global souradnice_y
    global hrac_zivoty
    print("Prisel jsi pozde.")
    print("Vratil ses na start pro zmrzlinu, ktera ti pridala zivot.")
    #na soucasne souradnice dame kosticku
    pole_hrace[souradnice_x][souradnice_y] = "\u1AC0"
    #zmenime souradnice na pevno na start
    souradnice_x = 0
    souradnice_y = 0
    #na start dame panaka
    pole_hrace[souradnice_x][souradnice_y] = "\u26C4"
    hrac_zivoty = hrac_zivoty + 1
    print("Tvuj pocet zivotu je: {}".format(hrac_zivoty))
    vypis(pole_hrace)

def hai_mac():
    print("Narazil jsi na Hai Mac Duy!")
    print("Hai se te pta: \"Ktere cislo je na 47. desetinem miste cisla pi.\"")
    input()
    print("To je jedno, Hai zapomnel odpoved.")
    print("Ztracis zivot jen tak.")
    ztracis_zivot()

def karyn():
    global pole_hrace
    print("Ses na VietCode a vidis Karyn.")
    print("Protoze jsi spravny ajtak, neumis se pred holkami chovat.")
    print("Zrmznul jsi na miste.")
    #pro nahodny pocet cyklu
    for i in range(random.randint(3, 5)):
        input("Predved se: ")
        print("Nuda.")
    print("Jsi nudny, tak se Karyn rozhodla odejit.")
    print("Opet se umis hybat.")
    vypis(pole_hrace)

def pravidla_start():
    #vypis pravidel
    print("Ahoj, hraci!")
    print("-------------------------------------------------------")
    print("Vitej ve hre.")
    print("-------------------------------------------------------")
    print("Cilem tve hry je dojit do Finishe - F")
    print("-------------------------------------------------------")
    print("Mas 3 zivoty")
    print("-------------------------------------------------------")
    print("Necekej, ze to bude jednoduche.")
    print("-------------------------------------------------------")
    print("Toto je tve hraci pole, zacinas na S")
    vypis(pole_hrace)
    print("-------------------------------------------------------")
    print("Pohybujes se tim ze napises jedno z nasledujicich:")
    print("              W = \u2191")
    print("              S = \u2193")
    print("              A = \u2190")
    print("              D = \u2192")
    print("-------------------------------------------------------")
    print("HRA ZACINA")
    print("HODNE STESTI")
    input("Press enter to start")
    for prvek in range(50):
        print()
    pole_hrace[0][0] = "\u26C4"
    vypis(pole_hrace)

# ---------------------------------------------------------------------------------------------------------------
#vyplni pole - na 25 poli bude 10 prekazek
vypln_min(10)
pravidla_start()
while nazivu:
    tah = input("Move: ").lower()
    vyber_tahu(tah)
    if(nazivu):
        kontrola()

