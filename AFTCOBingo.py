"""
Project name: AFTCOBingoPlayer
Programmed by: Jordon Lovik
Website: JordonLovik.com
Date: 3/12/17
"""
import urllib.request
import urllib.parse
import re
import os
from Email import sendemail

savelocation = 'C:\\Users\\jordon.AFTCO\\Desktop\\bingofile.txt'
bingofile = open(savelocation, 'w')
url = 'http://www.executiveadministrator.com/cgi-local/inoutPROhosted4/inoutPRO.pl?refresh=1&ID=AFTCO'
resp = urllib.request.urlopen(url) #request html data from website
respdata = resp.read() #store request data in respdata
bingodict = {

'Jordon':      ['B8,', 'I18,', 'N38,', 'G47,', 'O66,',
                'B10,','I27,', 'N44,', 'G53,', 'O71,',
                'B3,', 'I19,', 'fre,', 'G48,', 'O67,',
                'B4,', 'I25,', 'N39,', 'G56,', 'O65,',
                'B9,', 'I30,', 'N34,', 'G58,', 'O69,'],

'Freddy_b1':    ['B10,','I22,', 'N32,', 'G54,', 'O62,',
                'B5,',  'I21,', 'N41,', 'G57,', 'O65,',
                'B8,',  'I27,', 'fre,', 'G48,', 'O73,',
                'B14,', 'I25,', 'N43,', 'G55,', 'O64,',
                'B3,',  'I30,', 'N35,', 'G52,', 'O70,'],

'Freddy_b2':    ['B4,','I18,', 'N39,', 'G59,', 'O70,',
                'B13,','I21,', 'N45,', 'G57,', 'O74,',
                'B10,','I23,', 'fre,', 'G60,', 'O65,',
                'B11,','I27,', 'N31,', 'G47,', 'O73,',
                'B3,', 'I25,', 'N37,', 'G55,', 'O61,'],

'David_b1':    ['B5,', 'I20,', 'N37,', 'G50,', 'O62,',
                'B4,', 'I24,', 'N45,', 'G56,', 'O65,',
                'B14,','I19,', 'fre,', 'G47,', 'O71,',
                'B12,','I28,', 'N35,', 'G52,', 'O66,',
                'B10,','I23,', 'N43,', 'G60,', 'O74,'],

'David_b2':    ['B9,', 'I27,', 'N41,', 'G59,', 'O68,',
                'B14,','I26,', 'N43,', 'G57,', 'O70,',
                'B5,', 'I23,', 'fre,', 'G55,', 'O66,',
                'B7,', 'I30,', 'N36,', 'G56,', 'O67,',
                'B6,', 'I29,', 'N42,', 'G58,', 'O64,'],

'Yvonne_b1':    ['B7,','I27,', 'N42,', 'G49,', 'O73,',
                'B15,','I26,', 'N36,', 'G56,', 'O74,',
                'B8,', 'I17,', 'fre,', 'G52,', 'O61,',
                'B5,', 'I18,', 'N32,', 'G59,', 'O63,',
                'B6,', 'I19,', 'N31,', 'G46,', 'O65,'],

'Yvonne_b2':    ['B12,','I24,', 'N42,', 'G60,', 'O75,',
                'B15,', 'I23,', 'N34,', 'G57,', 'O70,',
                'B10,', 'I25,', 'fre,', 'G54,', 'O72,',
                'B9,',  'I30,', 'N35,', 'G53,', 'O68,',
                'B8,',  'I27,', 'N36,', 'G55,', 'O69,'],

'Sherwood':    ['B13,','I26,', 'N32,', 'G59,', 'O66,',
                'B10,','I24,', 'N43,', 'G50,', 'O65,',
                'B1,', 'I25,', 'fre,', 'G53,', 'O64,',
                'B14,','I28,', 'N41,', 'G51,', 'O68,',
                'B3,', 'I27,', 'N36,', 'G49,', 'O69,'],

'Surgio_b1':    ['B9,','I27,', 'N41,', 'G56,', 'O62,',
                'B10,','I18,', 'N31,', 'G49,', 'O69,',
                'B11,','I16,', 'fre,', 'G53,', 'O64,',
                'B7,', 'I30,', 'N42,', 'G58,', 'O75,',
                'B8,', 'I29,', 'N44,', 'G59,', 'O73,'],

'Surgio_b2':    ['B14,','I26,', 'N32,', 'G58,', 'O65,',
                'B15,','I18,', 'N42,', 'G60,', 'O71,',
                'B8,','I28,', 'fre,', 'G59,', 'O62,',
                'B2,', 'I25,', 'N43,', 'G55,', 'O68,',
                'B9,', 'I19,', 'N41,', 'G57,', 'O74,'],

'Sarah':       ['B2,', 'I23,', 'N45,', 'G53,', 'O71,',
                'B9,', 'I22,', 'N39,', 'G59,', 'O61,',
                'B14,','I27,', 'fre,', 'G52,', 'O63,',
                'B13,','I16,', 'N38,', 'G48,', 'O68,',
                'B15,','I25,', 'N32,', 'G47,', 'O70,'],

'Chris':       ['B1,','I24,', 'N42,', 'G52,', 'O69,',
                'B7,','I25,', 'N44,', 'G54,', 'O66,',
                'B3,','I17,', 'fre,', 'G53,', 'O63,',
                'B4,','I22,', 'N43,', 'G51,', 'O70,',
                'B5,','I21,', 'N45,', 'G47,', 'O67,'],

'Nick':        ['B6,', 'I26,', 'N36,', 'G53,', 'O66,',
                'B10,','I28,', 'N32,', 'G54,', 'O70,',
                'B14,','I19,', 'fre,', 'G58,', 'O71,',
                'B1,', 'I17,', 'N42,', 'G59,', 'O75,',
                'B5,', 'I20,', 'N34,', 'G48,', 'O64,'],

'MatthewQ_b1': ['B8,', 'I24,', 'N41,', 'G52,', 'O72,',
                'B2,', 'I19,', 'N45,', 'G50,', 'O62,',
                'B11,', 'I20,', 'fre,', 'G46,','O70,',
                'B13,', 'I23,', 'N39,', 'G57,','O64,',
                'B14,', 'I26,', 'N36,', 'G48,','O68,'],

'MatthewQ_b2': ['B3,', 'I17,', 'N41,', 'G53,', 'O61,',
                'B7,', 'I18,', 'N39,', 'G60,', 'O62,',
                'B1,', 'I21,', 'fre,', 'G47,', 'O73,',
                'B14,', 'I23,', 'N37,', 'G49,','O70,',
                'B15,', 'I19,', 'N43,', 'G52,','O68,'],

'Maria_b1':     ['B6,','I17,', 'N43,', 'G52,', 'O70,',
                'B4,', 'I22,', 'N37,', 'G60,', 'O68,',
                'B12,','I6,',  'fre,', 'G59,', 'O73,',
                'B8,', 'I26,', 'N32,', 'G56,', 'O72,',
                'B15,','I23,', 'N35,', 'G51,', 'O75,'],

'Maria_b2':    ['B3,', 'I29,', 'N45,', 'G59,', 'O71,',
                'B6,', 'I24,', 'N39,', 'G54,', 'O61,',
                'B2,', 'I17,', 'fre,', 'G60,', 'O74,',
                'B1,', 'I28,', 'N36,', 'G53,', 'O62,',
                'B8,', 'I18,', 'N37,', 'G58,', 'O64,'],

'Noe_b1':  ['B6,', 'I29,', 'N36,', 'G51,', 'O68,',
            'B14,','I16,', 'N32,', 'G59,', 'O66,',
            'B1,', 'I19,', 'fre,', 'G46,', 'O74,',
            'B4,', 'I21,', 'N45,', 'G53,', 'O61,',
            'B8,', 'I23,', 'N31,', 'G49,', 'O64,'],

'Noe_b2':  ['B14,','I29,', 'N44,', 'G48,', 'O61,',
            'B10,','I24,', 'N31,', 'G59,', 'O63,',
            'B15,','I26,', 'fre,', 'G53,', 'O71,',
            'B4,', 'I22,', 'N42,', 'G49,', 'O73,',
            'B12,','I17,', 'N43,', 'G54,', 'O64,'],

'MattF':   ['B5,', 'I20,', 'N34,', 'G48,', 'O10,',
            'B6,', 'I23,', 'N36,', 'G52,', 'O67,',
            'B4,', 'I16,', 'fre,', 'G54,', 'O68,',
            'B2,', 'I26,', 'N43,', 'G50,', 'O73,',
            'B1,', 'I27,', 'N33,', 'G57,', 'O72,'],

'Jay_b1': ['B6,', 'I29,', 'N32,', 'G51,', 'O75,',
           'B8,', 'I20,', 'N43,', 'G55,', 'O65,',
           'B14,', 'I30,', 'fre,', 'G48,','O66,',
           'B7,', 'I23,', 'N34,', 'G52,', 'O68,',
           'B3,', 'I19,', 'N41,', 'G59,', 'O61,'],

'jay_b2': ['B1,', 'I26,', 'N37,', 'G50,', 'O71,',
           'B3,', 'I28,', 'N33,', 'G53,', 'O73,',
           'B2,', 'I22,', 'fre,', 'G57,', 'O68,',
           'B9,', 'I21,', 'N34,', 'G46,', 'O70,',
           'B13,', 'I29,', 'N45,', 'G52,','O63,']
}

for key, value in bingodict.items():
    string = '<TEXTAREA ROWS="2" NAME="1 ANNOUNCEMENTS-return" COLS="50" WRAP=VIRTUAL>(.*?)</TEXTAREA>'#search within text area for bingo numbers
    search = re.findall(string, str(respdata)) #find all data between <b> and </b>
    searchstring = str(search) #convert search results to string
    cleanlist = searchstring.split() #split seachstring into a list object
    cleanlist.append('fre,') #add free space
    print(cleanlist) #print list taken from web

###ALL POSSIBLE SOLUTIONS FOR BINGO GAME 5x5###
    solutions = [(0,6,12,18,24),(4,8,12,16,20),(0,5,10,15,20),(1,6,11,16,21),
                  (2,7,12,17,22),(3,8,13,18,23),(4,9,14,19,24),(0,1,2,3,4),
                    (5,6,7,8,9),(10,11,12,13,14),(15,16,17,18,19),(20,21,22,23,24)]

    counter = 0 #inicialize counter variable
    hitlist = set() #inicialize hitlist variable
    print('-------------')# formating
    print(key)# print the Bingo board name
    boardprint = [] #inicialize empty list which will hold any hits found in a board

###CHECK TO SEE IF A BOARD HAS ITEM CALLED BY GAME MASTER###
    for i in value: #index into each Bingo board
        boardprint.append('O')# append O to all spaces from 0-24
        for j in cleanlist: #Index into cleanlist i.e item called
            if i == j: #check to see if someones board item matches an item called by game master
                hitlist.add(counter)#When hit occurs add it to our hitlist which holds all items
                #print('Hit: {} '.format(i)) #debuging
                boardprint.pop()# removes the last item in list which will always be an 'O'
                boardprint.append('X')# adds 'X' in place of said 'O'
        counter += 1 #add one to counter

###CHECK HITLIST AGAINS POSSIBLE SOLUTIONS###
    for each in solutions: #for each item in solutions
        if hitlist.issuperset(each):
            #if collections.Counter(hitlist) == collections.Counter(each): #check to see if all items match
            sendemail('jordon@aftco.com','{} got a BINGO'.format(key))
            print('!**BINGO**! {}'.format(key))
            bingofile.write('!**BINGO**! {}'.format(key))#write
            bingofile.close()
            os.startfile(savelocation)#Open file for presenting a bingo winner

###PRINT OUT BOARDS FOR EACH PERSON###
    for v in range(25):
        if v == 0:#print Header
            print('B ', 'I ', 'N ', 'G ', 'O')
        if v < 5:# 0 - 4 Row1
            print(boardprint[v], end='  ')
        if v == 5:#add spacing
            print('')
        if v > 4 and v < 10:# 5 - 9
            print(boardprint[v], end='  ')
        if v == 10:#add spacing
            print('')
        if v > 9 and v < 15: #10 - 14
            print(boardprint[v], end='  ')
        if v == 15:#add spacing
            print('')
        if v > 14 and v < 20: #15 - 19
            print(boardprint[v], end='  ')
        if v == 20:#add spacing
            print('')
        if v > 19: #20 - 24
            print(boardprint[v], end='  ')
        if v == 24:#add spacing
            print('')
    print('-------------')#formating
    print()#formating