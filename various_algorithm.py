import time
import random

aList = [10, 9, 2, 5, 6, 6, 7, 8, 8, 85, 39, 10, 3, 500]
Select_list = []


def main_menu():
    print("Main Menu:")
    print("1. Test an individual sorting algorithm")
    print("2. Test multiple sorting algorithms")
    print("3. Exit")


def generate_random_array(size):
    return [random.randint(0, 1000) for _ in range(size)]


def print_sorted_array(aList, algorithm_name, sorting_function):
    comparisons, runtime, sorted_arr = sorting_function(aList.copy())
    print("Algorithm Name\tArray Size\tNum. of Comparisons\tRun time (in ms.)")
    print("{}\t{}\t{}\t{:.2f}ms".format(algorithm_name, len(aList), comparisons, runtime))


def prompt_for_array_size():
    while True:
        try:
            size = int(input("Enter the size of the array (n > 0): "))
            if size > 0:
                return size
            else:
                print("Please enter a positive integer greater than 0.")
        except ValueError:
            print("Invalid input. Please enter an integer.")


def test_individual_sorting_algorithm():
    print("Choose a sorting algorithm to test:")
    print("1. Selection Sort")
    print("2. Insertion Sort")
    print("3. Merge Sort")
    print("4. Quick Sort")
    print("5. Heap Sort")
    print("6. Counting Sort")
    choice = int(input("Enter your choice: "))
    print("Sorting algorithm name\tArray size\tNum. of Comparisons\tRun time (in ms.)")

    if choice == 1:

        Selection_sort(aList)
        comparisons, runtime, sorted_arr = Selection_sort(aList.copy())
        print("Sorted Array: \t{}\t{}\t{:.2f}ms".format(len(aList), comparisons, runtime))


    elif choice == 2:
        comparisons, runtime, _ = insertion_sort(aList.copy())
        print("Insertion Sort:\t\t{}\t\t{}\t\t\t{:.6f}".format(len(aList), comparisons, runtime))

    elif choice == 3:
        comparisons, runtime, _ = mergeSort(aList.copy())
        print("Merge Sort:\t\t\t{}\t\t{}\t\t\t{:.6f}".format(len(aList), comparisons, runtime))
    elif choice == 4:
        comparisons, runtime, _ = quickSort(aList.copy())
        print("Quick Sort:\t\t\t{}\t\t{}\t\t\t{:.6f}".format(len(aList), comparisons, runtime))
    elif choice == 5:
        heapSort(aList)
        comparisons, runtime, sorted_arr = heapSort(aList.copy())
        print("Sorted Array: \t{}\t{}\t{:.2f}ms".format(len(aList), comparisons, runtime))
    elif choice == 6:
        counting_sort_algorithim2(aList)
        comparisons, runtime, sorted_arr = counting_sort_algorithim2(aList.copy())
        print("Sorted Array: \t{}\t{}\t{:.2f}ms".format(len(aList), comparisons, runtime))

    else:
        print("Invalid choice")


def test_multiple_sorting_algorithms(aList):
    print("Sorting algorithm name\tArray size\tNum. of Comparisons\tRun time (in ms.)")


    comparisons, runtime, _ = Selection_sort(aList.copy())
    print("Selection Sort:\t\t{}\t\t{}\t\t\t{:.6f}".format(len(aList), comparisons, runtime))

    comparisons, runtime, _ = insertion_sort(aList.copy())
    print("Insertion Sort:\t\t{}\t\t{}\t\t\t{:.6f}".format(len(aList), comparisons, runtime))

    comparisons, runtime, _ = mergeSort(aList.copy())
    print("Merge Sort:\t\t\t{}\t\t{}\t\t\t{:.6f}".format(len(aList), comparisons, runtime))

    comparisons, runtime, _ = quickSort(aList.copy())
    print("Quick Sort:\t\t\t{}\t\t{}\t\t\t{:.6f}".format(len(aList), comparisons, runtime))

    comparisons, runtime, _ = heapSort(aList.copy())
    print("Heap Sort:\t\t\t{}\t\t{}\t\t\t{:.6f}".format(len(aList), comparisons, runtime))

    comparisons, runtime, _ = counting_sort_algorithim2(aList.copy())
    print("Counting Sort:\t\t{}\t\t{}\t\t\t{:.6f}".format(len(aList), comparisons, runtime))


def Selection_sort(aList):
    comparisons = 0
    start_time = time.time()
    for i in range(len(aList)):
        least = i
        for k in range(i + 1, len(aList)):
            comparisons += 1
            if aList[k] < aList[least]:
                comparisons += 1
                least = k
        if least != i:
            aList[i], aList[least] = aList[least], aList[i]

    runtime = (time.time() - start_time) * 1000  # Convert to milliseconds


    return comparisons, runtime, aList

def counting_sort_algorithim2(aList):
    start_time= time.time()
    comparison = 0
    new_arr =[0]* len(aList)

    for i in range (len(aList)):
        count = 0

        redata=0

        for x in range (len(aList)):

            comparison += 1

            if aList[i] >= aList[x]:


                if i==x:
                    pass
                else:
                    count = count+1

                    if aList[i] == aList[x]:
                        redata = redata +1
        if redata == 0:
            new_arr[count]=aList[i]
        for y in range(redata + 1):
            comparison += 1
            if new_arr[count] == 0:
                new_arr[count]=aList[i]
                break
            else:
                count = count - 1
    aList =new_arr
    runtime= (time.time()-start_time) *1000
    return comparison,runtime,aList








def heapSort(aList):
    comparisons = [0]  # Initialize comparison count
    start_time = time.time()

    n = len(aList)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(aList, n, i, comparisons)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        aList[i], aList[0] = aList[0], aList[i]  # Swap root with last element
        heapify(aList, i, 0, comparisons)

    end_time = time.time()
    runtime = (end_time - start_time) * 1000  # Convert to milliseconds
    return comparisons[0], runtime, aList  # Return the number of comparisons, runtime, and sorted list


def heapify(aList, n, i, comparisons):
    largest = i  # Initialize largest as root
    left = 2 * i + 1
    right = 2 * i + 2

    # Check if left child exists and is greater than root
    if left < n:
        comparisons[0] += 1  # Increment comparison count
        if aList[left] > aList[largest]:
            largest = left

    # Check if right child exists and is greater than root
    if right < n:
        comparisons[0] += 1  # Increment comparison count
        if aList[right] > aList[largest]:
            largest = right

    # Change root if needed
    if largest != i:
        aList[i], aList[largest] = aList[largest], aList[i]
        heapify(aList, n, largest, comparisons)


def insertion_sort(aList):
    comparisons = 0
    start_time = time.time()

    n = len(aList)
    for i in range(1, n):
        key = aList[i]
        j = i - 1

        while j >= 0 and aList[j] > key:
            comparisons += 1
            aList[j + 1] = aList[j]
            j -= 1
        aList[j + 1] = key

    end_time = time.time()
    runtime = (end_time - start_time) * 1000 # Convert to milliseconds
    return comparisons, runtime, aList


def quickSort(aList):
    comparisons = [0]  # Initialize comparison count
    start_time = time.time()

    quickSortHelper(aList, 0, len(aList) - 1, comparisons)


    runtime = (time.time() - start_time) * 1000  # Convert to milliseconds
    return comparisons[0], runtime, aList  # Return the number of comparisons, runtime, and sorted list


def quickSortHelper(aList, left, right, comparisons):
    if left < right:  # Check termination condition
        pivotIndex = partition(aList, left, right, comparisons)
        quickSortHelper(aList, left, pivotIndex - 1, comparisons)
        quickSortHelper(aList, pivotIndex + 1, right, comparisons)


def partition(aList, left, right, comparisons):
    pivot = aList[right]  # Choose the rightmost element as pivot
    i = left - 1  # Initialize the index of the smaller element

    for j in range(left, right):
        comparisons[0] += 1  # Increment comparison count
        if aList[j] <= pivot:
            i += 1
            aList[i], aList[j] = aList[j], aList[i]  # Swap elements

    aList[i + 1], aList[right] = aList[right], aList[i + 1]  # Swap pivot with correct position
    return i + 1  # Return the index of the pivot element


def mergeSort(aList):
    comparisons = [0]
    start_time = time.time()

    copyBuffer = [None] * (len(aList))
    mergeSortHelper(aList, copyBuffer, 0, len(aList) - 1, comparisons)

    end_time = time.time()
    runtime = (end_time - start_time) * 1000
    return comparisons, runtime, aList


def mergeSortHelper(aList, copyBuffer, low, high, comparisons):
    if low < high:
        middle = (low + high) // 2
        mergeSortHelper(aList, copyBuffer, low, middle, comparisons)
        mergeSortHelper(aList, copyBuffer, middle + 1, high, comparisons)
        merge(aList, copyBuffer, low, middle, high, comparisons)


def merge(aList, copyBuffer, low, middle, high, comparisons):
    i1 = low
    i2 = middle + 1
    temp_comparisons = 0  # Temporary comparison count for this merge step

    for i in range(low, high + 1):
        if i1 > middle:
            copyBuffer[i] = aList[i2]
            i2 += 1
        elif i2 > high:
            copyBuffer[i] = aList[i1]
            i1 += 1
        elif aList[i1] < aList[i2]:
            copyBuffer[i] = aList[i1]
            i1 += 1
            temp_comparisons += 1  # Increment comparison count
        else:
            copyBuffer[i] = aList[i2]
            i2 += 1
            temp_comparisons += 1  # Increment comparison count

    # Update total comparisons
    comparisons[0] += temp_comparisons

    for i in range(low, high + 1):
        aList[i] = copyBuffer[i]



while True:
    main_menu()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        array_size = prompt_for_array_size()
        aList = generate_random_array(array_size)
        print(aList)
        test_individual_sorting_algorithm()
    elif choice == 2:
        array_size = prompt_for_array_size()
        aList = generate_random_array(array_size)
        print(aList)
        test_multiple_sorting_algorithms(aList)
    elif choice == 3:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
