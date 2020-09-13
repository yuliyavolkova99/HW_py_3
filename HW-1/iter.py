#реализация через итератор
class CompressedList(list):
    def __iter__(self):
        return ComressedListIterator(self)

class ComressedListIterator:
    def __init__(self, arr):
        self.arr = arr
        self.counter = 0
        self.index = 0
  
    def __next__(self):
        # если все пары перебрали, raise StopIteration()
        if self.index >= self.arr.__len__():
            raise StopIteration
        # если не все повторяющиеся элементы 
        # текущей пары self.index выдали - увеличиваем counter
        # выдаем еще один элемент
        if self.counter < self.arr[self.index][1]:
            self.counter = self.counter + 1
            return self.arr[self.index][0]
        # если все элементы текущей пары выдали, переходим к 
        # следующей паре
        else:
            self.counter = 0
            self.index = self.index + 1
original = [1, 1, 1, 1, 2, 2, 1, 1, 1, 3, 3, 3, 3]
compressed = CompressedList([(1, 4), (2, 2), (1, 3), (3, 4)])

decompressed = [x for x in compressed if x is not None]

print(original)
print(decompressed)
print(original == decompressed)

#реализация через функцию-генератор 
class ComressedList:
    def __init__(self, arr):
        self.arr = arr
        self.counter = 0
        self.index = 0
  
    def __iter__(self):
        while self.arr.__len__() >= self.index:
            for i in range(self.arr[self.index][1]):
                yield self.arr[self.index][0]
            self.index = self.index + 1

original = [1, 1, 1, 1, 2, 2, 1, 1, 1, 3, 3, 3, 3]
compressed = CompressedList([(1, 4), (2, 2), (1, 3), (3, 4)])

decompressed = [x for x in compressed if x is not None]

print(original)
print(decompressed)
print(original == decompressed)
