/def stack_check(stack):
    if len(stack) > 10:
        return True
    else:
        return False

// 


// merge 2 array using binary search
/ def merge(arr1, arr2):
    i = 0
    j = 0
    k = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1
        k += 1
    while i < len(arr1):
        arr[k] = arr1[i]
        i += 1
        k += 1
    while j < len(arr2):
        arr[k] = arr2[j]
        j += 1
        k += 1
    return arr  

arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr = merge(arr1, arr2)
print(arr)


// sort array using binary search
def binary_search(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, l, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, r, x)
    else:
        return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 10
result = binary_search(arr, 0, len(arr) - 1, x)


// find the index of the element in the array
def find_index(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
x = 10
result = find_index(arr, x)
print (result)

/ find the smalled element in array
def find_smallest(arr):
    smallest = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
    return smallest
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = find_smallest(arr)
print(result)

import datetime

def parse_expenses(expenses_string):
    """Parse the list of expenses and return the list of triples (date, value, currency).
    Ignore lines starting with #.
    Parse the date using datetime.
    Example expenses_string:
        2016-01-02 -34.01 USD
        2016-01-03 2.59 DKK
        2016-01-03 -2.72 EUR
    """
    expenses = []
    for line in expenses_string.splitlines():
        if line.startswith('#'):
            continue
        date, value, currency = line.split()
        expenses.append((datetime.datetime.strptime(date, '%Y-%m-%d'), float(value), currency))
    return expenses



// upload XLSX file to database on sqlite
import sqlite3 as sql
import xlrd


// merge 2 array using binary search
/ def merge(arr1, arr2):
    i = 0
    j = 0
    k = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1
        k += 1
    while i < len(arr1):
        arr[k] = arr1[i]
        i += 1
        k += 1
    while j < len(arr2):
        arr[k] = arr2[j]
        j += 1
        k += 1
    return arr

// swap 2 element in array
def swap(arr, i, j):   # i, j is index
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

