import json as js


class CountCompressor:
    # generate initial count
    def __init__(self, text=""):
        print(" -- init --")
        self.text = text
        self.mapping = {}
        self.reverseMapping = {}

        count_pair = []
        count = {}

        # create count store for each word
        for i in getwords(self.text):
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

            self.mapping[i] = i
            self.reverseMapping[i] = i

        count_pair += [(count[i], i) for i in count.keys()]
        count_pair.sort()

        print(count_pair)

        self.mapping.update({count_pair[i][1]: i for i in range(len(count_pair))})
        self.reverseMapping.update({i: count_pair[i][1] for i in range(len(count_pair))})

    def update(self, text=""):
        print(" -- update --")
        self.text += text
        self.mapping = {}
        self.reverseMapping = {}

        count_pair = []
        count = {}

        # create count store for each word
        for i in getwords(self.text):
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

            self.mapping[i] = i
            self.reverseMapping[i] = i

        count_pair += [(count[i], i) for i in count.keys()]
        count_pair.sort(reverse=True)

        print("count: ", count_pair)

        self.mapping.update({count_pair[i][1]: i for i in range(len(count_pair))})
        self.reverseMapping.update({i: count_pair[i][1] for i in range(len(count_pair))})

    def compress(self) -> str:
        return ''.join(str(self.mapping[i]) for i in getwords(self.text))

    def gettext(self):
        return self.text

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
    a = CountCompressor("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum convallis arcu rhoncus purus porttitor, id vestibulum lacus ullamcorper. Curabitur vel tempus magna, et volutpat turpis. Phasellus aliquam commodo libero sit amet volutpat. Nulla libero mauris, commodo ut mi id, porttitor vestibulum sapien. Suspendisse eu tortor ut urna tincidunt laoreet non ut magna. Proin id scelerisque tortor, id luctus nibh. Sed laoreet massa leo. Duis eu erat porta, consequat metus in, condimentum erat. Nulla fringilla nibh eget velit vulputate, eget congue dui vulputate. Curabitur sagittis velit in vehicula lobortis. Sed eget ultrices eros, et mollis neque. Cras ac facilisis nulla. In ultrices scelerisque diam quis finibus. Ut at urna mattis, vestibulum purus ac, viverra dui. Sed viverra magna lorem.

Nunc consequat magna aliquet elit malesuada, eget rhoncus magna laoreet. Nulla finibus luctus vulputate. Aenean ultricies in dolor vitae malesuada. Mauris iaculis massa ligula, ac finibus nisi dignissim vel. Integer euismod orci sit amet augue vulputate, vitae consequat lacus pellentesque. Mauris pellentesque congue orci, non efficitur nulla posuere in. Ut sapien velit, finibus ac tristique nec, vulputate a augue. Phasellus at vestibulum lectus. Donec cursus ac sapien quis placerat. Sed vel laoreet ante. Vivamus et ante ac lacus venenatis sagittis. Vivamus bibendum viverra ipsum ac ullamcorper.

Mauris ornare congue interdum. Etiam tempor vitae urna quis dapibus. Sed lacinia ultricies eros, in vehicula ex efficitur vitae. Fusce iaculis neque quis pharetra imperdiet. Maecenas faucibus leo nec aliquam tristique. Quisque euismod, est in laoreet pharetra, velit nisi malesuada turpis, et auctor lacus odio eu ipsum. Fusce eu dolor ac nulla fermentum interdum et at augue.

Integer sollicitudin eget nisi quis accumsan. Nulla at pharetra nulla. Duis consequat viverra sem, ac ultrices metus venenatis nec. Etiam ipsum nulla, pulvinar eget mi in, ultricies fringilla dui. Vestibulum in aliquet ligula. Integer sit amet sem sit amet ex porttitor condimentum. Suspendisse at nisi vulputate nulla blandit fermentum. Donec eu pretium arcu. Phasellus semper pretium erat.

Fusce sed convallis lorem. Suspendisse dictum est et justo maximus venenatis in sit amet ligula. Integer bibendum pellentesque nibh id interdum. Curabitur rutrum sapien ac condimentum tempus. Nunc tempor mattis odio vitae condimentum. Cras dapibus quam metus, at rhoncus orci vestibulum vitae. Pellentesque volutpat sem ut aliquet dictum. Donec eget dui sem. Nunc accumsan sodales magna sit amet pulvinar. Praesent odio velit, aliquet in metus non, commodo faucibus tellus. Nullam scelerisque consectetur urna, non ornare nunc. Integer imperdiet, nibh eu vehicula posuere, quam nisi vestibulum lorem, varius fringilla lectus eros sit amet lectus.""")

    print("text: ", a.gettext())
    print("mapping: ", a.getmapping())
    print("reverse mapping: ", a.getreversemapping())
    print(a.compress())

    open("compressed.txt", "w").write(a.compress())
    js.dump(a.mapping, open("mapping.json", "w"))
    js.dump(a.reverseMapping, open("reverseMapping.json", "w"))
