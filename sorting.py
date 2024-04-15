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

def selection_sort(list_of_nums):
    for ind in range(len(list_of_nums)):
        min_index = ind

        for j in range(ind + 1, len(list_of_nums)):
            # select the minimum element in every iteration
            if list_of_nums[j] < list_of_nums[min_index]:
                min_index = j
        # swapping the elements to sort the array
        (list_of_nums[ind], list_of_nums[min_index]) = (list_of_nums[min_index], list_of_nums[ind])
    return list_of_nums

def main():
    file_name = "numbers.csv"
    data = read_data(file_name)
    print(data)
    key = data['series_1']
    sort = selection_sort(key)
    print(sort)


if __name__ == '__main__':
    main()