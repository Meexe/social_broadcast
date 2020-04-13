import csv
import os


PATH = 'app/settings/settings.csv'


settings = dict()
with open(PATH, newline='') as f:
    file = csv.reader(f, delimiter=';')
    for row in file:
        settings[row[0]] = row[1]
