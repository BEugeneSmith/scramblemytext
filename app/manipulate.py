class Name:
    def __init__(self,name):
        self.name = name

    def backwards(self):
        return self.name[::-1]

    def palindrome(self):
        rev = self.backwards()[1:]
        return self.name + rev

    def piglatin(self):
        split_name = (self.name).split(' ')

        for i in range(len(split_name)):
            split_name[i] = self.__piglatinize(split_name[i])
        return ' '.join(split_name)

    def __piglatinize(self,name):
        vowels = 'aAeEiIoOuU'

        ending = ''
        pl_name = ''

        for l in name:
            if l in vowels:
                pl_name += name[name.index(l):]
                break
            else:
                ending += l

        return pl_name + ending + 'ay'
