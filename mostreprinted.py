import scrython
import pandas as pd

# returns a list of all known sets
sets = scrython.sets.Sets()
temp = {}

year = 1993

# prints a list of all sets. Filters out sets that do not provide black border cards or are online exclusive
for set in reversed(sets.data()):
    if set['set_type'] != 'token' and set['set_type'] != 'minigame' and set['set_type'] != 'memorabilia' and set['set_type'] != 'treasure_chest' and set['set_type'] !='alchemy':
        setCode = set['code']
        setYear = int(set['released_at'][0:4])
        setYear = int(set['released_at'][0:4])
        if setYear != year:
            # set:pust() is used so that a card always returns no matter the set. Prevents errors from returning empty searches
            temp['Earl of Squirrel'] = 2
            sortedTemp = sorted(temp.items(), key=lambda x:x[1], reverse=True)
            tempDict = dict(sortedTemp)
            df = pd.DataFrame.from_dict(tempDict, orient='index')
            df.to_csv('results/{}.csv'.format(year))
            print('{} CSV Created'.format(year))
            year += 1
        print(setCode, setYear)
        setCards = scrython.cards.Search(q='set:{},pust -is:onlyprint'.format(setCode))
        if setCards.data is not None:
            for card in setCards.data():
                if card['name'] not in temp:
                    temp[card['name']] = 1
                else:
                    temp[card['name']] += 1

