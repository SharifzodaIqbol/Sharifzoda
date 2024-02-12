class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

    def __len__(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def remove_first(self):
        if not self.head:
            raise ValueError("Лист пустой")
        self.head = self.head.next

    def remove_last(self):
        if not self.head:
            raise ValueError("Лист пустой")
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def remove_at(self, index):
        if index < 0 or index >= len(self):
            raise ValueError("Индекс выходит за пределы диапазона")
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        for _ in range(index - 1):
            current = current.next
        current.next = current.next.next

    def remove_first_value(self, value):
        current = self.head
        previous = None
        while current:
            if current.data == value:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return
            previous = current
            current = current.next
        raise ValueError("Число не найдено!")

    def remove_last_value(self, value):
        current = self.head
        previous = None
        last_match = None
        while current:
            if current.data == value:
                last_match = current
            previous = current
            current = current.next
        if last_match:
            if last_match == self.head:
                self.head = last_match.next
            else:
                previous.next = last_match.next
        else:
            raise ValueError("Число не найдено!")

my_list = LinkedList()

my_list.append(5)
my_list.append(10)
my_list.append(15)

print(len(my_list))  # Выведет: 3

my_list.remove_first()

my_list.remove_last()

my_list.remove_at(0)

try:
    my_list.remove_first_value(10)
except ValueError as e:
    print(e) #Число не найдено!