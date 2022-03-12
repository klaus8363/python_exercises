class LinkedList():
    def __init__(self, value):
        self.head = self
        self.value = value
        self.next = None

    def __str__(self):
        return self.head.value

    def traverse(self):
        current = self.head
        while current.next:
            print(current, '-> ', end='')
            current = current.next
        print(current)

    def reverse(self):
        current = self.head
        previous = None
        next_ = current.next

        while next_:

            tmp_next = current.next
            current.next = previous
            previous = current

            if tmp_next is None:
                return current
            next_ = tmp_next
            current = next_
            





        return next_ 

a = LinkedList('A')
b = LinkedList('B')
c = LinkedList('C')
d = LinkedList('D')
e = LinkedList('E')
a.next = b
b.next = c
c.next = d
d.next = e


a.traverse()
new_head = a.reverse()
print("NEW", new_head)
new_head.traverse()


l0 = LinkedList('-1')
head = l0
for i in range(10):
    ll = LinkedList(str(i))
    l0.next = ll
    l0 = ll

head.traverse()
head.reverse().traverse()
# print(head.reverse())