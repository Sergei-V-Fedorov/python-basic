class MyDict(dict):

    def get(self, key, fill=0):
        if key in self.keys():
            return self[key]
        else:
            return fill


my_dict = MyDict()
my_dict[1] = 10

value = my_dict.get(1)
print(f"{1}: {value}")

value = my_dict.get(5)
print(f"{5}: {value}")
