'''Write a function that takes an amount of money in cents and
returns the fewest number of coins possible for the number of cents.
Here's an example, given the input 387. Now that you have a few tools at your disposal,
the output should be a dictionary, as shown below:'''

def change(cents):
    cents = cents / 100.0
    bills = {
        "hundred": 100,
        "fifty": 50,
        "twenty": 20,
        "ten": 10,
        "five": 5,
        "dollar": 1.0,
        "half-dollar": 0.5,
        "quarter": 0.25,
        "dime": 0.1,
        "nickle": 0.05,
        "penny": 0.01
    }
    change = {}
    for bill in bills:
        while cents >= bills[bill]:
            if bill not in change:
                change[bill] = 1
            else:
                change[bill] += 1
            cents -= bills[bill]
    return change

#####SORTING ALGORITHMS#############3
def push_front(arr,val):
    arr[0] = arr.append(arr[0])
    arr[0] = val
    return arr

def bubble_sort(arr):
    switch = True
    while switch:
        switch = False
        for num in range(len(arr)-1):
            if arr[num] > arr[num+1]:
                arr[num],arr[num+1] = arr[num+1],arr[num]
                switch = True
    return arr

def selection_sort(arr):
    for index,item in enumerate(arr):
        smallest_val = item
        smallest_index = index
        for next_i in range(index,len(arr)):
            if arr[next_i] < smallest_val:
             smallest_index = next_i
        arr[index],arr[smallest_index] = arr[smallest_index], arr[index]
    return arr

def insertion_sort(arr):
    start = 0
    end = len(arr) -1
    for num in range(start,end):
        beginning_of_arr = arr[start:num+1]
        beginning_length = len(beginning_of_arr)
        next_val = arr[num+1]
        rest_of_array = arr[num+2:]
        for index, val in enumerate(beginning_of_arr):
            if next_val < val:
                beginning_of_arr.insert(index,next_val)
                break
        if len(beginning_of_arr) == beginning_length:
            beginning_of_arr.append(next_val)
        arr = beginning_of_arr + rest_of_array
    return arr
class SLNode(object):

    def __init__(self,value,next=None):
        self.value = value
        self.next = next

class SList(object):
    def __init__(self,head=None,next=None):
        self.head = head
        self.tail = next

    def PrintAllVals(self):
        node = self.head
        print(node.value)
        while node.next != None:
            node = node.next
            print(node.value)

    def AddBack(self,val):
        self.tail.next = val

    def AddFront(self,back):
        back.next = self.head
        self.head = back

    def insertBefore(self, nextVal, val):
        if (val == self.head):
            nextVal.next = self.head
            self.head = nextVal
        else:
            node = self.head
            while (node.next != val):
                node = node.next
            nextVal.next = node.next
            node.next = nextVal
        return self

    def insertAfter(self,preval,val):
        if val.next == None:
            val.next = preval
            self.tail = preval
        else:
            node = self.head
            while (node != val):
                node = node.next
            next_node = node.next
            node.next = preval
            preval.next = next_node
        return self

    def RemoveNode(self,val):
        if val == self.head:
            self.head = val.next
        else:
            node = self.head
            while (node.next != val):
                node = node.next
            if val == self.tail:
                self.tail = node
            else:
                node.next = node.next.next
        return self

class DLNode(object):
    def __init__(self,prev=None,next=None,value=None):
        self.prev = prev
        self.next = next
        self.value = value

class DList(object):
    def __init__(self,head=None, tail=None):
        self.head = head
        self.tail = tail

    def add(self,node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        return self

    def insert(self,node_to_insert,insertion_point):
        def find_insertion(node,insertion_point):
            return node if node == insertion_point else find_insertion(node.next)
        insertion_node = find_insertion(insertion_point)
        node_to_insert.next = insertion_node
        node_to_insert.prev = insertion_node.prev
        insertion_node.prev.next = node_to_insert
        insertion_node.prev = node_to_insert
        return self


test = DLNode()
test.value = "test"
tester = DLNode()
tester.value = "tester"
