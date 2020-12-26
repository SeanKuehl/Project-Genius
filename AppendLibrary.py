#Sean Liam Kuehl
#Genius/FrontEnd/LoadLibrary.py
#2/4/2020
#Add the user's question and it's answer to the 'Library' file in the 'BackEnd' directory


import os






def Append(question, answer):

    #lines go question, then answer
    file = open("C:/Users/kuehl family/PycharmProjects/Genius/BackEnd/Library", 'a')
    file.write(question)
    file.write(answer)
    file.close()



#I will need the directory syntax