import csv, sys
filename = 'names.csv'


class file_op(object):
    def read_cal_data(self, name):
        with open(filename, newline='') as f:
            reader = csv.reader(f)
            try:
                for row in reader:
                    if row[0] == name:
                        print(row)
                        return name

            except csv.Error as e:
                sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))

    def write_new_file(self, row_data):
        with open('names.csv', 'w') as csvfile:
            fieldnames = ['field', 'value', 'comment']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
     
