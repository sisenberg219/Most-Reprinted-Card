import scrython
import pandas as pd

# returns a list of all known sets
sets = scrython.sets.Sets()
temp = {}
year = 1993
index = 0
columnName = []
# defaultList = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
df = pd.DataFrame()
# prints a list of all sets. Filters out sets that do not provide black border cards or are online exclusive
# for set in reversed(sets.data()):
#     if set['set_type'] != 'token' and set['set_type'] != 'minigame' and set['set_type'] != 'memorabilia' and set['set_type'] != 'treasure_chest' and set['set_type'] !='alchemy':
#         setCode = set['code']
#         setYear = int(set['released_at'][0:4])
#         if setYear != year:
#             # set:pust() is used so that a card always returns no matter the set. Prevents errors from returning empty searches
#             temp['Earl of Squirrel'] = 2 # Do this last
#             sortedTemp = sorted(temp.items(), key=lambda x:x[1], reverse=True)
#             tempDict = dict(sortedTemp)
#             temp = pd.DataFrame.from_dict(tempDict, orient='index', columns=['{}'.format(year)])
#             #df.insert(temp)
#             #df.to_csv('results/{}.csv'.format(year))
#             print('{} CSV Created'.format(year))
#             year += 1
#         print(setCode, setYear)
#         setCards = scrython.cards.Search(q='set:{},pust -is:onlyprint'.format(setCode))
#         if setCards.data is not None:
#             for card in setCards.data():
#                 if card['name'] not in temp:
#                     temp[card['name']] = 1
#                 else:
#                     temp[card['name']] += 1

for set in reversed(sets.data()):
    if set['set_type'] != 'token' and set['set_type'] != 'minigame' and set['set_type'] != 'memorabilia' and set['set_type'] != 'treasure_chest' and set['set_type'] !='alchemy':
        setCode = set['code']
        setYear = int(set['released_at'][0:4])
        if setYear != year:
            columnName.append(str(year))
            index += 1
            year += 1
            for i in temp:
                temp[i][index] = temp[i][index-1]
            print('Advanced to {}'.format(year))
        print(setCode, setYear)
        setCards = scrython.cards.Search(q='set:{},pust -is:onlyprint'.format(setCode))
        if setCards.data is not None:
            for card in setCards.data():
                if card['name'] not in temp:
                    temp[card['name']] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    temp[card['name']][index] = 1
                else:
                    temp[card['name']][index] += 1
columnName.append('2023')
df = pd.DataFrame.from_dict(temp, orient='index', columns=columnName)
df.rename()
#df.insert(df)
df.to_csv('results/results.csv')