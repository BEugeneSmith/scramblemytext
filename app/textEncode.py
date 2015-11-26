from random import randrange

text = 'Brian'

numDict = {
    "ajs":1, "bkt":2, "clu":3,
    "dmw":4, "enx":5, "foy":6,
    "gpz":7, "hq":8,  "ir":9
}

def encodeText(n):
    lowercase_n = n.lower()

    encodedText = ''

    for l in lowercase_n:
        for grp in numDict.keys():
            if l in grp:
                encodedText += str(numDict[grp])
                break
            else:
                next

    return encodedText

def encodeTextToColor(n):
    color_params = ['r','g','b']
    color_codes= {}

    for i in range(3):
        color_num = 1
        for j in range(3):
            random_index = randrange(len(n))
            color_num *= int(n[random_index])
        while color_num > 255:
            color_num /= 2
        color_codes[color_params[i]] = int(color_num)

    return color_codes
