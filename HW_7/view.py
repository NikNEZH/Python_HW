import csv


def logger(data):
    with open('log.csv', 'w', newline= '') as f:
        writer = csv.writer(f)
        writer.writerows((data['Ф.И.О.'],
                         data['номер телефона'],
                         data['адрес']))

