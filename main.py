from random import randint
from os import getcwd
import time
import itertools

class Sorter:
    def __init__(self, input, properties):
        self.input = input
        self.inputProperties = properties
        self.expectedArray = []
        self.sortedArray = []

    def copy_input(self, index):
        return [self.input[index][i] for i in range(len(self.input[index]))]

    def verify_if_sorted(self):
        if len(self.expectedArray) != len(self.sortedArray):
            return "numarul de elemente nu este acelasi"
        else:
            for i in range(len(self.expectedArray)):
                if self.expectedArray[i] != self.sortedArray[i]:
                    return "sortarea nu este corecta"
            return "sortarea este corecta"

    def expected_sort(self, index):
        self.expectedArray = self.copy_input(index)

        #print(self.expectedArray)
        tstart = time.perf_counter_ns()
        self.expectedArray = sorted(self.expectedArray)
        tend = time.perf_counter_ns()
        print(self.expectedArray)
        print("Native sort done in", float((tend - tstart) / 1000000), "miliseconds")

    def bubble_sort(self, index):
        self.sortedArray = self.copy_input(index)

        tstart = time.perf_counter_ns()
        for i in range(len(self.sortedArray)):
            for j in range(i, len(self.sortedArray)):
                if self.sortedArray[i] < self.sortedArray[j]:
                    self.sortedArray[i], self.sortedArray[j] = self.sortedArray[j], self.sortedArray[i]
        tend = time.perf_counter_ns()

        print("Bubble sort done in:", float((tend - tstart) / 1000000), "miliseconds")

    def count_sort(self, index):
        self.sortedArray = self.copy_input(index)
        maximNum = self.inputProperties[index][1]
        length = self.inputProperties[index][0]

        frequency = [0 for i in range(maximNum + 1)]
        #sortedArrayCopy = [0 for i in range(length)]

        tstart = time.perf_counter_ns()

        # for elem in self.sortedArray:
        #     frequency[elem] += 1
        #
        # for i in range(1, maximNum + 1):
        #     frequency[i] += frequency[i - 1]
        #
        # frequency[0] = 0
        #
        # for i in range(1, maximNum + 1):
        #     frequency[i] = frequency[i - 1]
        #
        # for i in range(length):
        #     value = self.sortedArray[i]
        #     sortedArrayCopy[frequency[value]] = value
        #     frequency[value] += 1

        #self.sortedArray = sortedArrayCopy

        counter = 0
        for i in range(maximNum + 1):
            while frequency[i]:
                self.sortedArray[counter] = i
                counter += 1
                frequency[i] -= 1

        tend = time.perf_counter_ns()

        print("Count sort done in:", float((tend - tstart) / 1000000), "miliseconds")

    def get_digit_number(self, n):
        cnt = 0
        while n:
            n //= 10
            cnt += 1
        return cnt

    def radix_sort(self, index):
        self.sortedArray = self.copy_input(index)
        maximNum = self.inputProperties[index][1]
        maxLen = self.get_digit_number(maximNum)

        #create buckets
        bucket = [[] for i in range(maxLen)]



    def merge_sort(self, index):
        self.sortedArray = self.copy_input(index)
        arrayLen = self.inputProperties[index][0]

        tstart = time.perf_counter_ns()
        #print(self.sortedArray)
        self.merge_sort_reccursion(self.sortedArray)
        tend = time.perf_counter_ns()
        #print(self.sortedArray)
        print("Merge sort done in:", float((tend - tstart) / 1000000), "miliseconds")

    def merge_sort_reccursion(self, array):

        length = len(array)

        if length > 1:
            mid = length // 2

            left = array[:mid]
            right = array[mid:]

            self.merge_sort_reccursion(left)
            self.merge_sort_reccursion(right)

            self.interclass(left, right, array)

    def interclass(self, arr1, arr2, temp):
        lenTemp = len(temp)

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

                #self.create_input(pair[0], pair[1])

                #rndValue = randint(0, 100) % 3

                self.create_input(pair[0], pair[1])
                # if rndValue == 0:
                #     self.create_input(pair[0], pair[1])
                # elif rndValue == 1:
                #     self.create_ordered_input(pair[0], pair[1])
                # else:
                #     self.create_same_value_input(pair[0], pair[1])

    def create_input(self, numOfELem, maxElem):
        result = []
        for i in range(numOfELem):
            result.append(randint(0, maxElem))
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

sorterObject = Sorter(inputObj, propObj)
sorterObject.expected_sort(0)
sorterObject.count_sort(0)
print(sorterObject.verify_if_sorted())
sorterObject.merge_sort(0)
print(sorterObject.verify_if_sorted())
#sorterObject.bubble_sort(0)
#print(sorterObject.verify_if_sorted())
print(sorterObject.get_digit_number(1))