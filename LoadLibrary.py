#Sean Liam Kuehl
#Genius/FrontEnd/LoadLibrary.py
#2/4/2020
#Load and format the data in the 'library' text file in the 'BackEnd' directory

import os




path = os.getcwd()
path = path[:-9]
path = path + "/BackEnd/Library"

empty = False
questionList = []
answerList = []
counter = 0
file = open("C:/Users/kuehl family/PycharmProjects/Genius/BackEnd/Library", 'r')
i = 0
lineList = file.readlines()
temp = []
numOfEntries = 0



if lineList == []:
    empty = True
else:

    #need to get rid of new line characters, outside of that it seems to work
    for item in lineList:
        item = item.strip() #gets rid of new line characters
        if item == '' or item == "" or item == ' ' or item == " ":
            pass
        #this gets rid of empty elements
        else:
            temp.append(item)

    lineList = temp

    while (len(lineList) - 1) > counter-1:
        if i == 1:
            answerList.append(lineList[counter])
            i = 0
        elif i == 0:
            questionList.append(lineList[counter])
            i = 1

        counter += 1
numOfEntries = len(questionList)




#cutoff



def ReloadLibrary():

    path = os.getcwd()
    path = path[:-9]
    path = path + "/BackEnd/Library"

    empty = False
    questionList = []
    answerList = []
    counter = 0
    file = open("C:/Users/kuehl family/PycharmProjects/Genius/BackEnd/Library", 'r')
    i = 0
    lineList = file.readlines()
    temp = []
    numOfEntries = 0

    # this function is so if you ask the same question twice in one session you will get the answer
    if lineList == []:
        empty = True
    else:

        # need to get rid of new line characters, outside of that it seems to work
        for item in lineList:
            item = item.strip()  # gets rid of new line characters
            if item == '' or item == "" or item == ' ' or item == " ":
                pass
            # this gets rid of empty elements
            else:
                temp.append(item)

        lineList = temp

        while (len(lineList) - 1) > counter - 1:
            if i == 1:
                answerList.append(lineList[counter])
                i = 0
            elif i == 0:
                questionList.append(lineList[counter])
                i = 1

            counter += 1
    numOfEntries = len(questionList)

    file.close()

    return questionList, answerList


def returnNumOfEntries():
    return numOfEntries


def returnLists():
    return answerList, questionList

def CheckLists(question):

    questionList, answerList = ReloadLibrary()

    counter = 0
    answer = 0
    question = question.strip()
    question = question.lower()

    for item in questionList:
        item = item.lower()

        #the problem is that there is a new line in the one in the questionList
        if item == question:

            answer = answerList[counter]
            return answer


        counter += 1
    return 0
#I will need the directory syntax

file.close()