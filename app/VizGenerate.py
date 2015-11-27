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
        self.color_string = self.__encodeTextToColor()
        self.__encodeTextToRadius()

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

        return "rgba({0},{1},{2},{3})".format( color_codes['r'],color_codes['g'],color_codes['b'],color_codes['t'])

    def __encodeTextToRadius(self):
        self.radius = randrange(20,50)


class Circle(TextEncode):

    def __init__(self,text):
        TextEncode.__init__(self,text)

        self.x = self.__generateCoord()
        self.y = self.__generateCoord()

        self.circle = self.__generateCircle()

    def __generateCoord(self):
        return randrange(10,90)

    def __generateCircle(self):
        return '<circle cx="{0}" cy="{1}" r="{2}" stroke="{3}" stroke-width="1" fill="{4}" />'.format(self.x,self.y,self.radius,self.color_string,self.color_string)

class SVG:

    def __init__(self,text):
        self.text = text
        self.SVG = self.__fillSVG()

    def __fillSVG(self):
        svg = '<svg width="100%" height="100%">'

        for i in range(15):
            elem = self.__createElement()
            svg += elem

        svg += '</svg>'

        return svg

    def __createElement(self):
        circ = Circle(self.text)
        return circ.circle
