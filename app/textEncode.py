from random import randrange

text = 'Brian'
class TextEncode:
    numDict = {
        "ajs":1, "bkt":2, "clu":3,
        "dmw":4, "enx":5, "foy":6,
        "gpz":7, "hq":8,  "ir":9
    }

    def __init__(self,text):
        self.text = text
        self.encodedText = self.__encodeText()
        self.color_codes = self.__encodeTextToColor()

    def __encodeText(self):
        lowercase_n = self.text.lower()

        encodedText = ''

        for l in lowercase_n:
            for grp in numDict.keys():
                if l in grp:
                    encodedText += str(numDict[grp])
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

        color_codes['t'] = randrange(20,80)

        # TODO: Maybe this can encode for the string as it is directly fed into the SVG
        return color_codes

    def __encodeTextToRadius(self):
        # TODO: First, make sure this is okay to use; radius is need for svg circles.

    def __repr__(self):
        #TODO: easy export!!!

class SVG(TextEncode):
    # This object defines all of the information needed to make a SVG
    def __init__(self,text):
        self.colorFill = None
        self.colorOut = None

        # these are determined by by
        self.radius = None
        self.x = None # get this from the page
        self.y = None # this too

class VisObjects:
