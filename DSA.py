# --- Array ---
'''a = [1, 1, 1, 1, 1]
i = 0

for b in range(len(a)):
    i += a[b]

print(i)

a[2] = 100

print(a)'''

# --- Strings ---

'''a = input("Enter a string : ")
b = ""

for i in range(len(a)):
    b += a[len(a) - i - 1]

print(b)

c = 0
a = a.lower()

for i in range(len(a)):
    if a[i] in 'aeiou':
        c += 1

print(c)'''

# --- Linear Search ---

'''def Linear_search(arr, target):
    count = 0
    for i in range(len(arr)):
        if arr[i] == target:
            print(f"{target} found at index {i}!")
            count = 1
    
    if count == 0:
        print(f"{target} not found!")

arr = []
for i in range(5):
    arr.append(int(input("Enter a number : ")))

target = int(input("Target number : "))

Linear_search(arr, target)'''

# --- Bubble Sort ---

'''arr = []

for i in range(5):
    arr.append(int(input("Enter number : ")))

def Bubble_Sort(arr):
    for i in range(len(arr)):
        print(i)
        for j in range(len(arr) - i - 1):
            print(j)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            print(arr)

    return arr

print(Bubble_Sort(arr))'''

# --- Linked Lists ---

'''class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linking:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def in_index(self, data, index):
        new_node = Node(data)

        if index == 0 or self.head is None:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        c = 0

        while current.next is not None and c < index - 1:
            current = current.next
            c += 1

        new_node.next = current.next
        current.next = new_node

    def del_index(self, index):
        if index == 0:
            if self.head is None:
                return
            self.head = self.head.next
            return

        c = 0
        current = self.head

        while current.next is not None and c < index - 1:
            current = current.next
            c += 1

        if current.next is None:
            print("Index out of range")
        else:
            current.next = current.next.next

    def search(self, data):
        index = 0
        current = self.head

        while current != None:
            if current.data == data:
                print(f"Target found at index {index}")
                return
            current = current.next
            index += 1

        print("Target not found")
        return

    def reverse(self):
        current = self.head
        prev = None

        while current != None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    def has_cycle(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
            
        return False

    def traversing(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next

l1 = Linking()
for i in range(25):
    l1.append(i)

l1.del_index(15)
l1.in_index(15, 55)
l1.search(25)
l1.reverse()

if not l1.has_cycle():
    l1.traversing()
'''