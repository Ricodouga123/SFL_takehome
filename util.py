import csv, re

import pprint

def getUniqueGender(csv_path = "DATA.csv") -> list:

    """
    
    Takes in path of a csv file, find the column corresponding to gender information, then 
    return unique genders in all rows.

    """

    with open(csv_path, "r", newline = "") as csvfile:

        reader = csv.reader(csvfile, delimiter = ",")

        data = [i for i in reader]

        for index_column, element in enumerate(data[0]):

            if re.compile('gender', re.IGNORECASE).match(element):

                gender_column_index = index_column

                break
    
        result = set()

        for row in data[0:]:

            result.add(row[gender_column_index])

        return result


def getDictFromCsv(csv_path = "Data.csv") -> list:

    """
    
    Returns a list of dictionaries dependent on the files header(first row) and remaining rows.

    """

    with open(csv_path, "r", newline = "") as csvfile:

        reader = csv.reader(csvfile, delimiter = ",")

        data = [i for i in reader]

        header = data[0]

        result = []

        for i in data[1:]:

            temp_dict = {}

            for col_name in header:

                temp_dict[col_name] = i[header.index(col_name)]

            result.append(temp_dict)

        return result
