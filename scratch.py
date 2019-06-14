import numpy as np
import pandas as pd
import csv
import os


df = pd.read_excel (r'/Users/Kevin/PycharmProjects/pandazz/FlashX.xls')


def countLyra(n):
    '''
    :param n: is the player number and team (e.g. A1)
    :return: number of times Flash X played lyra
    '''

    m = 0

    df_new = df[df['Player ' + str(n)].str.match('FlashX')]
    for a in df_new['Player ' + str(n) + ' Hero'].str.match('Lyra'):
        if a is True:
            m += 1
    return m


# print (countLyra('A2'))
#
#
# total = countLyra('A1') + countLyra('A2') + countLyra('A3') + countLyra('B1') + countLyra('B2') + countLyra('B3')
# print (total)


def countHero(player):
    '''

    :param player: player name
    :return: a dictionary, x, of the heroes that player has played
    '''

    x = {}

    df_new = df[df['Player A1'].str.contains(player)]
    for index, row in df_new.iterrows():
        a = row['Player A1 Hero']
        if a in x:
            x[a] += 1
        else:
            x[a] = 1

    df_new = df[df['Player A2'].str.contains(player)]
    for index, row in df_new.iterrows():
        a = row['Player A2 Hero']
        if a in x:
            x[a] += 1
        else:
            x[a] = 1


    df_new = df[df['Player A3'].str.contains(player)]
    for index, row in df_new.iterrows():
        a = row['Player A3 Hero']
        if a in x:
            x[a] += 1
        else:
            x[a] = 1


    df_new = df[df['Player B1'].str.contains(player)]
    for index, row in df_new.iterrows():
        a = row['Player B1 Hero']
        if a in x:
            x[a] += 1
        else:
            x[a] = 1

    df_new = df[df['Player B2'].str.contains(player)]
    for index, row in df_new.iterrows():
        a = row['Player B2 Hero']
        if a in x:
            x[a] += 1
        else:
            x[a] = 1


    df_new = df[df['Player B3'].str.contains(player)]
    for index, row in df_new.iterrows():
        a = row['Player B3 Hero']
        if a in x:
            x[a] += 1
        else:
            x[a] = 1

    return x


def exportHero(player):
    '''

    :param player: The player that you would like to export the data for
    :return: Nothing
    Creates a csv with the player name
    '''
    data = countHero(player)
    csv_file = "playername.csv"

    print(data)

    heroes = pd.DataFrame(data, index = [0])

    print(heroes)

    heroes_transposed = heroes.transpose()
    heroes_transposed.columns = ['Number']

    print (heroes_transposed)

    heroes_transposed.to_csv('playername.csv')

    # with open('playername.csv','w') as csvFile:
    #     w = csv.DictWriter(csvFile, data)
    #     w.writeheader()
    #     w.writerow(data)
    # csvFile.close()
    #
    os.rename ('playername.csv', str(player) + '.csv')



exportHero('FlashX')

# x = df['Player A1']
# y = df.loc[:,["Player A1" , "Player A2"]]
# z = df.iloc[:,1:5]
#
# print (z.head())