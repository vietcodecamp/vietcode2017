druh = 'clovek'
jmeno = 'Boromir'
zbran = 'mec'
mise = 'ochranit nositele prstenu moci'

print('Jmenuji se ' + jmeno + ' a jsem ' + druh + '. Moji oblibenou zbrani se stal '
      + zbran + ' a muj ukol je ' + mise + '.')


# Podobne jako vyse, pouzij hodnoty promennych ke zretezeni textu s pouzitim operatoru %
def concatenate_with_percentage_operator():
    print('Jmenuji se %s a jsem %s. Moji oblibenou zbrani se stal %s a muj ukol je %s.' % (jmeno, druh, zbran, mise))
    pass


# Podobne jako vyse, pouzij hodnoty promennych ke zretezeni textu s pouzitim .format()
def concatenate_with_format():
    print('Jmenuji se {} a jsem {}. Moji oblibenou zbrani se stal {} a muj ukol je {}.'.format(jmeno, druh, zbran, mise))
    pass
