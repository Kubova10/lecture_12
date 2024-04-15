import os
import csv

def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)

    data = {}
    with open(file_path, "r", newline="") as csvfile:
        csv_reader = csv.reader(csvfile)
        headers = next(csv_reader)

        for header in headers:
            data[header] = []

        for row in csv_reader:
            for i, value in enumerate(row):
                data[headers[i]].append(float(value))

    return data

def selection_sort(list_of_nums,direction):
    for ind in range(len(list_of_nums)):
        min_index = ind
        max_index = ind

        for j in range(ind + 1, len(list_of_nums)):
            if list_of_nums[j] < list_of_nums[min_index]:
                min_index = j
            else:
                if list_of_nums[j] > list_of_nums[max_index]:
                    max_index = j

        if direction == "asc":
            (list_of_nums[ind], list_of_nums[min_index]) = (list_of_nums[min_index], list_of_nums[ind])
        else:
            (list_of_nums[ind], list_of_nums[max_index]) = (list_of_nums[max_index], list_of_nums[ind])

    return list_of_nums

def bubble_sort(nums):
    for i in range(len(nums)-1):
        for j in range(0,len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    return nums

def  insertion_sort(nums):
    n = len(nums)
    if n <= 1:
        return
    for i in range(1, n):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums

def main():
    file_name = "numbers.csv"
    data = read_data(file_name)
    #print(data)
    key = data['series_1']
    ssort = selection_sort(key,"as")
    #print(ssort)
    bsort = bubble_sort(key)
    #print(bsort)
    isort = insertion_sort(key)
    print(isort)

if __name__ == '__main__':
    main()