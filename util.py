import csv, re

import pprint

def getUniqueGender(csv_path = "DATA.csv") -> list:

    """
    
    Takes in path of a csv file, find the column corresponding to gender information, then 
    return unique genders in all rows.

    """

    with open(csv_path, "r", newline = "") as csvfile:

        reader = csv.reader(csvfile, delimiter = ",")

        data_list = [i for i in reader]

        for index_column, element in enumerate(data_list[0]):

            if re.compile('gender', re.IGNORECASE).match(element):

                gender_column_index = index_column

                break
    
        result = set()

        for row in data_list[0:]:

            print(row[gender_column_index])

            result.add(row[gender_column_index])

        return result
    
getUniqueGender()