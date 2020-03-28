from random import randint, choice
from os import getcwd
import time

MEDIAN_CONSTANT = 5

class Sorter:
    def __init__(self, input, properties):
        self.input = input
        self.inputProperties = properties
        self.expectedArray = []

    def copy_input(self, index):
        return [self.input[index][i] for i in range(len(self.input[index]))]

    def verify_if_sorted(self, array):
        if len(array) != len(self.expectedArray):
            return "numarul de elemente nu este acelasi"
        else:
            for i in range(len(array)):
                if array[i] != self.expectedArray[i]:
                    return "sortarea nu este corecta"
            return "sortarea este corecta"

    def expected_sort(self, array):

        tstart = time.perf_counter_ns()
        array = sorted(array)
        tend = time.perf_counter_ns()

        print("Native sort done in", float((tend - tstart) / 1000000), "miliseconds")
        self.expectedArray = array

        return array

    def bubble_sort(self, array):
        tstart = time.perf_counter_ns()

        for i in range(len(array)):
            for j in range(i, len(array)):
                if array[i] > array[j]:
                    array[i], array[j] = array[j], array[i]

        tend = time.perf_counter_ns()
        return array

        #print("Bubble sort done in:", float((tend - tstart) / 1000000), "miliseconds")

    def count_sort(self, array, index=-1):

        if index == -1:
            maximNum = max(array)
        else:
            maximNum = self.inputProperties[index][1]

        frequency = [0 for i in range(maximNum + 1)]

        tstart = time.perf_counter_ns()

        for elem in array:
            frequency[elem] += 1

        counter = 0
        for i in range(maximNum + 1):
            while frequency[i]:
                array[counter] = i
                counter += 1
                frequency[i] -= 1

        tend = time.perf_counter_ns()
        print("Count sort done in:", float((tend - tstart) / 1000000), "miliseconds")
        return array

    def get_digit_number(self, n, base=10):
        cnt = 0
        if (base & (base-1)) == 0: #base is a power of two
            while n:
                n = n >> base
                cnt += 1
        else:
            while n:
                n //= base
                cnt += 1
        return cnt

    def get_digit(self, value, n, base=10):
        cutter = base ** n
        value = (value % (cutter * base)) // cutter
        return value

    def radix_sort(self, array, index=0, base=10):
        maximNum = self.inputProperties[index][1]
        maxLen = self.get_digit_number(maximNum, base)

        tstart = time.perf_counter_ns()

        # create buckets

        for i in range(maxLen):
            buckets = [[] for j in range(base)]

            for elem in array:
                buckets[self.get_digit(elem, i, base)].append(elem)

            for bucket in buckets:
                if bucket != []:
                    self.count_sort(bucket)

            counter = 0
            for bucket in buckets:
                for j in range(len(bucket)):
                    array[counter] = bucket[j]
                    counter += 1

        tend = time.perf_counter_ns()
        print("Radix sort done in:", float((tend - tstart) / 1000000), "miliseconds")
        return array

    def merge_sort(self, array):

        tstart = time.perf_counter_ns()
        self.merge_sort_recursion(array)
        tend = time.perf_counter_ns()

        print("Merge sort done in:", float((tend - tstart) / 1000000), "miliseconds")
        return array

    def merge_sort_recursion(self, array):

        length = len(array)
        if length > 1:
            mid = length // 2

            left = array[:mid]
            right = array[mid:]

            self.merge_sort_recursion(left)
            self.merge_sort_recursion(right)

            self.interclass(left, right, array)

    def interclass(self, arr1, arr2, temp):

        i = 0
        j = 0
        counter = 0

        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                temp[counter] = arr1[i]
                i += 1
            else:
                temp[counter] = arr2[j]
                j += 1
            counter += 1

        while i < len(arr1):
            temp[counter] = arr1[i]
            i += 1
            counter += 1

        while j < len(arr2):
            temp[counter] = arr2[j]
            j += 1
            counter += 1

    """
    def median(self, array, start, end):

        length = end - start
        #print(array)

        if length <= MEDIAN_CONSTANT:

            obj = self.bubble_sort(array[start:end])
            return obj[len(obj) // 2]
        else:
            bucketsNum = (length // MEDIAN_CONSTANT) + 1
            buckets = [[] for i in range(bucketsNum)]

            for i in range(length):
                buckets[i % bucketsNum].append(array[start + i])

            for bucket in buckets:
                self.bubble_sort(bucket)

            med = []
            for bucket in buckets:
                if bucket != []:
                    med.append(self.median(bucket, 0, len(bucket) - 1))

            return self.median(med, 0, len(med) - 1)
    """

    def pivot_choose(self, array, start, end):

        poz1, poz2, poz3 = randint(start, end), randint(start, end), randint(start, end)
        val1, val2, val3 = array[poz1], array[poz2], array[poz3]

        if (val1 <= val2 <= val3) or (val3 <= val2 <= val1):
            return val2
        elif (val1 <= val3 <= val2) or (val2 <= val3 <= val1):
            return val3
        elif (val2 <= val1 <= val3) or (val3 <= val1 <= val2):
            return val1

    """
    def partition(self, array, start, end):

        pivot = self.pivot_choose(array, start, end)

        low = start
        high = end - 1

        while low < high:
            while low <= high and array[high] > pivot:
                high = high - 1

            while low <= high and array[low] < pivot:
                low = low + 1

            if array[low] == array[high] and low != high:
                low = low + 1

            array[low], array[high] = array[high], array[low]
            print(pivot, array, low, high)

            #print(pivot, array, low, high)
        return high
    """""

    def partition(self, array, start, end):
        p = self.pivot_choose(array, start, end)

        low = start - 1
        high = end + 1

        while 1:
            low += 1
            while array[low] < p:
                low += 1

            high -= 1
            while array[high] > p:
                high -= 1

            if low < high:
                array[low], array[high] = array[high], array[low]
            else:
                return high


    def quick_sort_recursion(self, array, start, end):
        if start < end:
            p = self.partition(array, start, end)
            self.quick_sort_recursion(array, start, p)
            self.quick_sort_recursion(array, p + 1, end)

    def quick_sort(self, array, index=-1):
        if index == -1:
            length = len(array)
        else:
            length = self.inputProperties[index][0] - 1

        tstart = time.perf_counter_ns()
        self.quick_sort_recursion(array, 0, length)
        tend = time.perf_counter_ns()

        print("Quick sort done in:", float((tend - tstart) / 1000000), "miliseconds")
        return array

class Reader:
    def __init__(self):
        self.inputObjects = []
        self.propertiesObject = []
        self.path = getcwd()
        self.testNumber = 0

    def add_input_test(self, name):
        filePath = self.path + "\\" + name
        with open(filePath) as f:

            # citirea numarului de teste
            line = f.readline()
            self.testNumber = int(line.split(" ")[-1])

            #citirea formatului de test
            for i in range(self.testNumber):

                line = f.readline()
                if len(line) == 0:
                    break

                line = line.split(" ")
                pair = (int(line[2]), int(line[-1]))

                #adaugarea propietatilor testului
                self.propertiesObject.append(pair)

                rndValue = randint(0, 100) % 3

                if rndValue == 0:
                    self.create_input(pair[0], pair[1])
                elif rndValue == 1:
                    self.create_ordered_input(pair[0], pair[1])
                else:
                    self.create_same_value_input(pair[0], pair[1])

    def create_input(self, numOfELem, maxElem):
        result = []
        for i in range(numOfELem):
            value = randint(0, maxElem)
            result.append(value)
        self.inputObjects.append(result)

    def create_ordered_input(self, numOfElem, maxElem):
        result = [i if i <= maxElem else maxElem for i in range(numOfElem)]
        self.inputObjects.append(result)

    def create_same_value_input(self, numOfElem, maxElem):
        result = [maxElem for i in range(numOfElem)]
        self.inputObjects.append(result)

    def show_input(self):
        for test in self.inputObjects:
            print(*test)

    def get_input(self):
        return self.inputObjects

    def get_input_properties(self):
        return self.propertiesObject

    def get_test_number(self):
        return self.testNumber

readerObject = Reader()
readerObject.add_input_test("input.txt")
#readerObject.show_input()

inputObj = readerObject.get_input()
propObj = readerObject.get_input_properties()
numberOfTests = readerObject.get_test_number()

sorterObject = Sorter(inputObj, propObj)


for i in range(numberOfTests):
    print("Acesta este testul", i)

    vec = sorterObject.copy_input(i)
    sorterObject.expected_sort(vec)
    print(vec)

    vec = sorterObject.copy_input(i)
    sorterObject.count_sort(vec, i)
    print(sorterObject.verify_if_sorted(vec))

    vec = sorterObject.copy_input(i)
    sorterObject.merge_sort(vec)
    print(sorterObject.verify_if_sorted(vec))

    vec = sorterObject.copy_input(i)
    sorterObject.radix_sort(vec, i, 256)
    print(sorterObject.verify_if_sorted(vec))

    vec = sorterObject.copy_input(i)
    sorterObject.quick_sort(vec, i)
    print(sorterObject.verify_if_sorted(vec))
