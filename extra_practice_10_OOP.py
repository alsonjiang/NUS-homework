#question 1
class FreqTable():
    def __init__(self) -> None:
        self.table = {}

    def insert(self, x, c):
        if x in self.table:
            self.table[x] += c
        else:
            self.table[x] = c

    def remove(self, x, c):
        if x in self.table:
            for i in range(c):
                if self.table[x] != 0:
                    self.table[x] -= 1
                else:
                    self.table.remove(x)
    
    def query(self, x):
        print(self.table(x))
    
    def get_size(self):
        print(len(self.table))
    
#question 2
class MeanTable(FreqTable):
    def __init__(self) -> None:
        super().__init__()
        self.total = 0
        self.count = 0
    
    def insert(self, x, c):
        return super().insert(x, c)
