

class BiMap(object):

    def __init__(self):
        self.dict = {}
        self.reverse_dict = {}

    def put(self, key, value):
        if key in self.dict:
            old_val = self.dict.pop(key)
            self.reverse_dict.pop(old_val)
        if value in self.reverse_dict:
            old_key = self.reverse_dict.pop(value)
            self.dict.pop(old_key)
        self.dict[key] = value
        self.reverse_dict[value] = key

    def get(self, key):
        return self.dict.get(key)

    def get_value(self, value):
        return self.reverse_dict.get(value)


if __name__ == '__main__':
    b = BiMap()
    b.put(1, 'a')
    b.put(2, 'b')
    print b.get(1)
    print b.get(2)
    print b.get_value('a')
    print b.get_value('b')

    b.put(1, 'b')
    print b.get_value('a')
    print b.get_value('b') # none
    print b.reverse_dict
