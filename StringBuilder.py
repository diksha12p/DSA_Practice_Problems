from time import time


class StringBuilder:
    def __init__(self, value = u" "):
        self.value=value
        self.list=[]

    def __iadd__(self, other):
        self.list.append(other)
        return self

    def __unicode__(self):
        self.value = u" ".join((self.value, u" ".join(self.list)))
        self.list=[]
        return self.value


str = StringBuilder()
start_time = time()
for i in range(1, 201):
    str.__iadd__(u"more data at {}\n".format(i))
print(str.__unicode__())
print("Execution Time = {}".format(int(time() - start_time)*10^6))