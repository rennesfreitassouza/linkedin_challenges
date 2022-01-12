import csv

# https://www.linkedin.com/learning/python-code-challenges/merge-csv-files
def field_names_reader(dataFilesList, my_dict):
    for data_file in dataFilesList:
        with open(data_file, mode="r") as dataFile:
            for fieldname in csv.DictReader(dataFile).fieldnames: my_dict[fieldname] = ''

def merge_csv_files(dataFilesList, outputFilePath, my_dict):
    with open(outputFilePath, mode="w", newline="") as output_csvfile:
        writer = csv.DictWriter(output_csvfile, fieldnames=my_dict.keys())
        writer.writeheader()
        for data_file in dataFilesList:
            with open(data_file, 'r') as dataFile:
                reader = csv.DictReader(dataFile)
                for row in reader:
                    writer.writerow(row)


def main(inputFilesPath=["class1.csv", "class2.csv"] , outputFilePath='all_files.csv'):
    
    my_dict = dict()
    field_names_reader(inputFilesPath, my_dict)
    merge_csv_files(inputFilesPath, outputFilePath, my_dict)
    
main()