#-*- coding:utf-8 -*-
import csv
from os import path


def analyze_corpus(file_path):
    try:
        file = open(file_path, "r", encoding="utf-8")
    except Exception:
        file_path = path.abspath(__name__)
        raise

    # * Read the \"title\" column from the csv file and convert it to lower case\n",
    dict_reader = csv.DictReader(file)
    all_titles = []
    for row in dict_reader:
        print(row['title'].lower())
        all_titles.append(row['title'].split())

    count_array = []



if __name__ == "__main__":
    analyze_corpus("question.csv")