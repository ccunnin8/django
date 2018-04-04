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
