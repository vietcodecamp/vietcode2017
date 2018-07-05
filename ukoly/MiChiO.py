import random
#import randomu z knihovny
import json
#import souboru json z knihovny

#----------------------------------------------DATABAZE PRO HUDBU-------------------------------------------------

def load_list():
    help_var=open("music_database.json","r")
    list=json.load(help_var)
    help_var.close()
    return(list)
#nacitame databazy ze souboru music_database.json
#vraci nam zpracovatelnou databazy list

def add_song():
    name = input("What's the name of the song? ")
    genre = input("What genre is it? ")
    mood = input("What mood does the song have? ")
    era = input("When was the song released? ")
    interpret = input("Who's the interpret? ")
    added_song=[name,genre,mood,era,interpret]
    list.append(added_song)
    return(list)
#pridava urcitou pisnicku s parametry do zpracovatelne databaze list
#vraci databazy list i s pridanou pisnickou

def save_song():
    python_database=open("music_database.json","w")
    json.dump(save_list,python_database)
    python_database.close()
#zapisuje upravenou databazy zpet do souboru music_database.json

#----------------------------------------------DATABAZE PRO FILMY------------------------------------------------

def load_seznam():
    help_var=open("film_database.json","r")
    seznam=json.load(help_var)
    help_var.close()
    return(seznam)
#nacitame databazy ze souboru music_database.json
#vraci nam zpracovatelnou databazy list

def add_film():
    name = input("What's the name of the movie? ")
    genre = input("What genre is it? ")
    added_film=[name,genre]
    seznam.append(added_film)
    return(seznam)
#pridava urcitou pisnicku s parametry do zpracovatelne databaze list
#vraci databazy list i s pridanou pisnickou

def save_film():
    python_database=open("film_database.json","w")
    json.dump(save_seznam,python_database)
    python_database.close()
#zapisuje upravenou databazy zpet do souboru music_database.json

#----------------------------------------------FUNKCE PRO PISNICKY-----------------------------------------------
def filtr_genre(list):
    zanry=[]
    zanry_tisk=[]
    print("Available genres:")
    for zanr in list:
        zanry.append(zanr[1])
    zanry_filtr=set(zanry)
    for zanr_tisk in zanry_filtr:
        print(zanr_tisk)
    genre=input("What genre do you feel like listening to? ")
    if genre!="":
        list_genre_lok = []
        for song in list:
            if song[1]==genre:
                list_genre_lok.append(song)
        random.shuffle(list_genre_lok)
        return(list_genre_lok)
    elif genre=="":
        list_genre_lok = []
        for song in list:
            list_genre_lok.append(song)
        random.shuffle(list_genre_lok)
        return(list_genre_lok)

#nahodne seradi pisnicky v databazy
#funkcni fce pro filtrovani pisnicek
#returnuje seznam jiz se stejnym zanrem do dalsi fce

def filtr_mood(list_genre):
    nalady = []
    nalady_tisk = []
    print("Available playlist moods: ")
    for nalada in list_genre:
        nalady.append(nalada[2])
    nalady_filtr = set(nalady)
    for nalada_tisk in nalady_filtr:
        print(nalada_tisk)
    mood=input("How are you feeling right now? ")
    if mood!="":
        list_genre_mood_lok=[]
        for song in list_genre:
            if song[2]==mood:
                list_genre_mood_lok.append(song)
        return(list_genre_mood_lok)
    else:
        list_genre_mood_lok=[]
        for song in list_genre:
            list_genre_mood_lok.append(song)
        return(list_genre_mood_lok)
#funkcni fce pro filtrovani pisnicek
#returnuje seznam(stejny zanr i mood) ze seznamu(stejny zanr) do dalsi fce

def filtr_era(list_genre_mood):
    ery = []
    ery_tisk = []
    print("Available eras: ")
    for era in list_genre_mood:
        ery.append(era[3])
    ery_filtr = set(ery)
    for era_tisk in ery_filtr:
        print(era_tisk)
    era=input("Which era? ")
    if era!="":
        list_genre_mood_era_lok=[]
        for song in list_genre_mood:
            if song[3]==era:
                list_genre_mood_era_lok.append(song)
        return(list_genre_mood_era_lok)
    else:
        list_genre_mood_era_lok=[]
        for song in list_genre_mood:
            list_genre_mood_era_lok.append(song)
        return(list_genre_mood_era_lok)
# funkcni fce pro filtrovani pisnicek
# printuje nazev pisnicky ze seznamu (stejny zanr, mood i eru) ze seznamu(stejny zanr i mood)

def filtr_interpret(list_genre_mood_era):
    interpreti = []
    interpreti_tisk = []
    print("Interprets in the database: ")
    for interpret in list_genre_mood_era:
        interpreti.append(interpret[4])
    interpreti_filtr = set(interpreti)
    for interpret_tisk in interpreti_filtr:
        print(interpret_tisk)
    interpret=input("Is there anyone in particular you would like to listen to? ")
    if interpret!="":
        list_genre_mood_era_interpret=[]
        for song in list_genre_mood_era:
            if song[4]==interpret:
                list_genre_mood_era_interpret.append(song)
        pole_tisk=[]
        pole_tisk=list_genre_mood_era_interpret[0:(random.randint(11,16))]
        for song_tisk in pole_tisk:
            print(song_tisk[4] + " - " + song_tisk[0])
    else:
        list_genre_mood_era_interpret=[]
        for song in list_genre_mood_era:
            list_genre_mood_era_interpret.append(song)
        pole_tisk=[]
        pole_tisk=list_genre_mood_era_interpret[0:(random.randint(11,16))]
        for song_tisk in pole_tisk:
            print(song_tisk[4] + " - " + song_tisk[0])
#
#profiltruje jeste podle interpreta
#vybere prvnich 10 az 15 pisnicek ze seznamu(nahodne)
#vytiskne "jmeno interpreta"-"nazev pisnicky"

#----------------------------------------------FUNKCE PRO FILMY--------------------------------------------------

def filtr_zanr(seznam):
    genres = []
    genres_tisk = []
    print("Available genres:")
    for genre in seznam:
        genres.append(genre[1])
    genres_filtr = set(genres)
    for genres_tisk in genres_filtr:
        print(genres_tisk)
    zanr=input("What genre do you feel like watching? ")
    seznam_zanr_lok=[]
    for film in seznam:
        if film[1]==zanr:
            seznam_zanr_lok.append(film)
    random.shuffle(seznam_zanr_lok)
    seznam_zanr_lok_tisk=seznam_zanr_lok[0:random.randint(6,8)]
    for film_tisk in seznam_zanr_lok_tisk:
        print(film_tisk[0])
#profiltruje seznam podle druhu zanru a vytiskne "nazev filmu"
#nahodne vybere prvnich 5 az 7 filmu ze seznamu

#----------------------------------------------SAMOTNY KOD NA PROGRAM--------------------------------------------

list=load_list()
seznam=load_seznam()


choice=input("Music or films? ")

if choice == "music":
    add_search = input("Add or search? ")
    if add_search == "search":
        list_genre = filtr_genre(list)
        list_genre_mood = filtr_mood(list_genre)
        list_genre_mood_era = filtr_era(list_genre_mood)
        list_genre_mood_era_interpret = filtr_interpret(list_genre_mood_era)
    elif add_search=="add":
        load_list()
        list = load_list()
        save_list = add_song()
        save_song()
        print("New song was added to the database.")

elif choice == "films":
    add_search_films = input("Add or search? ")
    if add_search_films == "search":
        filtr_zanr(seznam)
    elif add_search_films=="add":
        load_seznam()
        seznam=load_seznam()
        save_seznam=add_film()
        save_film()
        print("You have succesfully added a new film to the database.")





