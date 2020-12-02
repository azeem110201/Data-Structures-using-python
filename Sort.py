import time


def swap(a, b):
    temp = a
    a = b
    b = temp


def selectionSort(array):
    length = len(array)
    if length == 0:
        return None
    elif length == 1:
        return array
    else:
        for i in range(length):
            for j in range(i, length):
                if array[i] > array[j]:
                    temp = array[i]
                    array[i] = array[j]
                    array[j] = temp

    return array


def bubbleSort(array):
    if len(array) == 0:
        return None

    elif len(array) == 1:
        return array

    else:

        flag = True
        i = 0
        while flag:
            flag = False
            for j in range(len(array) - i - 1):
                if array[j] > array[j+1]:
                    array[j+1], array[j] = array[j], array[j+1]
                    flag = True
            i += 1

    return array


def insertionSort(array):
    if len(array) == 0:
        return None

    elif len(array) == 1:
        return array

    else:
        for i in range(1, len(array)):
            j = i - 1
            x = array[i]
            while j >= -1 and array[j] > x:
                array[j+1] = array[j]
                j -= 1

            array[j+1] = x

    return array
            





start = time.time()
array = [5687, 64225, 62581, 645234, 5452545, 5658461254, 2565245, 25, 45, 5, 6, 9559545, 6,
         855121, 5421512, 412, 54212, 41, 5, 15, 1215, 4212, 5112545, 1215, 41255651426, 41552, 55]
print('selection sort')
print(selectionSort(array))
end = time.time()

print('Total time taken', (end-start))

print('*'*100)

array = [5687, 64225, 62581, 645234, 5452545, 5658461254, 2565245, 25, 45, 5, 6, 9559545, 6,
         855121, 5421512, 412, 54212, 41, 5, 15, 1215, 4212, 5112545, 1215, 41255651426, 41552, 55]
start = time.time()
print('bubble sort')
print(bubbleSort(array))
end = time.time()

print('Total time taken', (end-start))

print('*'*100)

array = [5687, 64225, 62581, 645234, 5452545, 5658461254, 2565245, 25, 45, 5, 6, 9559545, 6,
         855121, 5421512, 412, 54212, 41, 5, 15, 1215, 4212, 5112545, 1215, 41255651426, 41552, 55]
start = time.time()
print('insertion sort')
print(insertionSort(array))
end = time.time()

print('Total time taken', (end-start))

print('*'*100)
