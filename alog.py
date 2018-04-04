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
