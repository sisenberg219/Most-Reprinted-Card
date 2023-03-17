import scrython
from datetime import date
import pandas as pd

year = date.today().year

# returns a list of all known sets
sets = scrython.sets.Sets()
temp = {}

# prints a list of all sets. Filters out sets that do not provide black border cards or are online exclusive
for set in sets.data():
    if set['set_type'] != 'token' and set['set_type'] != 'minigame' and set['set_type'] != 'memorabilia' and set['set_type'] != 'treasure_chest' and set['set_type'] !='alchemy':
        setCode = set['code']
        print(setCode)
        setCards = scrython.cards.Search(q='set:{},pust -is:onlyprint'.format(setCode))
        if setCards.data is not None:
            for card in setCards.data():
                if card['name'] not in temp:
                    temp[card['name']] = 1
                else:
                    temp[card['name']] += 1

# set:pust() is used so that a card always returns no matter the set. Prevents errors from returning empty searches
temp['Earl of Squirrel'] = 1
print(temp)
