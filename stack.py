class Stack:
    def __init__(self, blank = []):
        self.items = blank

    def isEmpty(self):
        return self.items == []

    def clear(self):
        self.items = []

    def sort(self):
        list.sort(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


    def __iter__(self):
        return iter(self.items)

