# This module serves  to prepare encoded data for use in D3

from random import randrange
from json import dumps

class TextEncode:
    numDict = {
        "ajs":1, "bkt":2, "clu":3,
        "dmw":4, "enx":5, "foy":6,
        "gpz":7, "hq":8,  "ir":9
    }

    def __init__(self,text):
        self.text = text
        self.encodedText = self.__encodeText()
        self.x = self.__generateCoord()
        self.y = self.__generateCoord()
        self.color_str = self.__encodeTextToColor()
        self.__encodeTextToRadius()
        self.dataset = dumps([self.x,self.y,self.radius,self.color_str])

    def __encodeText(self):
        lowercase_n = (self.text).lower()

        encodedText = ''

        for l in lowercase_n:
            for grp in self.numDict.keys():
                if l in grp:
                    encodedText += str(self.numDict[grp])
                    break
                else:
                    next

        return encodedText

    def __encodeTextToColor(self):
        color_params = ['r','g','b']
        color_codes= {}

        for i in range(3):
            color_num = 1
            for j in range(3):
                random_index = randrange(len(self.encodedText))
                color_num *= int(self.encodedText[random_index])
            while color_num > 255:
                color_num /= 2
            color_codes[color_params[i]] = int(color_num)

        color_codes['t'] = randrange(20,80)/100

        #maybe this is inaccurate for D3
        return "rgba({0},{1},{2},{3})".format( color_codes['r'],color_codes['g'],color_codes['b'],color_codes['t'])

    def __encodeTextToRadius(self):
        self.radius = randrange(20,50)

    def __generateCoord(self):
        return randrange(10,90)

class CreateDataset:

    def __init__(self,text):
        self.text = text
        self.ds = []
        self.__fillDS()

    def __fillDS(self):

        for i in range(25):
            elem = self.__createEntry()
            self.ds.append(elem)


    def __createEntry(self):
        encoding = TextEncode(self.text)
        return encoding.dataset
