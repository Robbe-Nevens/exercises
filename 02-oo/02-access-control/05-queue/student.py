class Queue:
    def __init__(self):
        self.__que = []

    def add(self,item):
        self.__que.append(item)

    def next(self):
        return self.__que.pop(0)
    
    def is_empty(self):
        return len(self.__que) <= 0