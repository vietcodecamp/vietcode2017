import json

open_database=open("film_database.json","w")
json.dump([],open_database)
open_database.close()

open_database2=open("music_database.json","w")
json.dump([],open_database2)
open_database2.close()

#vytvori "json" soubory(databaze), se kterymi program Michio pote pracuje.