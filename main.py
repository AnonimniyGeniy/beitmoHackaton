import csv
import pandas as pd
import request_handler
import models
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    # Use a breakpoint in the code line below to debug your script.
    people = models.get_people()
    events = []
    for line in open('data/events.txt', 'r', encoding='utf-8'):
        events.append(line.strip())

    recommendations = request_handler.generate_recommendations(str(people[0]), events)
    for i in recommendations:
        print(i)
    for i, recommendation in enumerate(recommendations):
        print(f"Recommendation {i + 1}: {recommendation}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
