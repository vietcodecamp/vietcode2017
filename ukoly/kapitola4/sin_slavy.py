# Pridej sve jmeno do sine slavy s pomoci funkce append
def pole_pridej():
    sin_slavy = ["Einstein", "Newton", "Dacos", "Napoleon", "Caesar", "Musk", "Gates", "Jobs"]
    sin_slavy.append("Viet Code")
    return sin_slavy


# Smaz 5. prvek pole
def pole_smaz():
    sin_slavy = ["Einstein", "Newton", "Dacos", "Napoleon", "Caesar", "Musk", "Gates", "Jobs"]
    sin_slavy.remove(sin_slavy[4])
    return sin_slavy


# Obrat vsechny prvky pole
def pole_obrat():
    sin_slavy = ["Einstein", "Newton", "Dacos", "Napoleon", "Caesar", "Musk", "Gates", "Jobs"]
    sin_slavy.reverse()
    return sin_slavy


# Z pole nemusis jenom cist, lze do nej i zapisovat.
# Prepis 4. osobu v sini slavy na "Roman"
def pole_prepis():
    sin_slavy = ["Einstein", "Newton", "Dacos", "Napoleon", "Caesar", "Musk", "Gates", "Jobs"]
    sin_slavy[3] = "Roman"
    return sin_slavy
