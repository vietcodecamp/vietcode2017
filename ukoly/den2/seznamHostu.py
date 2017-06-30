# Spust program a zkus zadat par hrdinu na seznamu a par, kteri nejsou
# v seznamu.

heroes = ['Thor', 'Batman', 'Iron-man', 'Superman', 'Hulk', 'Spider-man']
print('Zadej superhrdinu:')
hero = input()
if hero not in heroes:
    print('Na nasem seznamu svatebnich hostu bohuzel neni ' + hero)
else:
    print(hero + ' je v seznamu nasich svatebnich hostu.')
