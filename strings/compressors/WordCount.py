class CountCompressor:
    # generate initial count
    def __init__(self, text=""):
        print(" -- init --")
        self.segments = [i for i in getwords(text)]
        self.mapping = {}
        self.reverseMapping = {}

        count_pair = []
        count = {}

        # create count store for each word
        for i in self.segments:
            print(i)
            print("key exists", i in count)
            print("is alphanum", i.isalpha() or i.isnumeric())

            if i in count:
                print("before: ", i, count[i])
                count[i] = count[i] + 1
                print("after: ", i, count[i])
                continue
            
            if i.isalpha() or i.isnumeric() and i not in count:
                count[i] = 1
                print("new: ", i, count[i])
                continue

        count_pair.append([(count[i], i) for i in count.keys()])
        count_pair.sort()

        self.mapping = {count_pair[i][1]: i for i in range(len(count_pair))}
        self.reverseMapping = {i: count_pair[i][1] for i in range(len(count_pair))}

    def update(self, text=""):
        print(" -- update --")
        self.segments += [i for i in getwords(text)]
        self.mapping = {}
        self.reverseMapping = {}

        count_pair = []
        count = {}

        # create count store for each word
        for i in self.segments:
            print(i)
            print("key exists", i in count)
            print("is alphanum", i.isalpha() or i.isnumeric())

            if i in count:
                print("before: ", i, count[i])
                count[i] = count[i] + 1
                print("after: ", i, count[i])
                continue
            
            if i.isalpha() or i.isnumeric() and i not in count:
                count[i] = 1
                print("new: ", i, count[i])
                continue

        count_pair.append([(count[i], i) for i in count.keys()])
        count_pair.sort()

        self.reverseMapping = {count_pair[i][1]: i for i in range(len(count_pair))}
        self.mapping = {i: count_pair[i][1] for i in range(len(count_pair))}

    def gettext(self) -> str:
        return ''.join(self.reverseMapping[i] for i in self.segments)

    def getmapping(self) -> dict:
        return self.mapping

    def getreversemapping(self) -> dict:
        return self.reverseMapping


# separates words numbers and special characters.
def getwords(text=""):
    word = ""
    for i in text:
        if i.isalnum():
            word += i
        else:
            yield word
            yield i
            word = ""
    yield word

if __name__ == '__main__':
    a = CountCompressor("a a a a b b b b c c s s d d d")
    a.update("zz z zz z zz zz zzz zz z z")
    print(a.getmapping())
    print(a.getreversemapping())
    print(a.gettext())
