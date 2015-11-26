class Text:
    def __init__(self,text):
        self.text = text

    def backwards(self):
        return self.text[::-1]

    def palindrome(self):
        rev = self.backwards()[1:]
        return self.text + rev

    def piglatin(self):
        split_text = (self.text).split(' ')

        for i in range(len(split_text)):
            split_text[i] = self.__piglatinize(split_text[i])
        return ' '.join(split_text)

    def __piglatinize(self,text):
        vowels = 'aAeEiIoOuU'

        ending = ''
        pl_text = ''

        for l in text:
            if l in vowels:
                pl_text += text[text.index(l):]
                break
            else:
                ending += l

        return pl_text + ending + 'ay'
