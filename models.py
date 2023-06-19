import pandas as pd
import data_handler as dh


class Svinota:
    isu = None
    name = None
    education = None
    job = None
    powers = None
    publications = []
    projects = []
    events = []

    def __init__(self, name, education, job, powers, isu, publications, projects, events):
        self.isu = isu
        self.name = name
        self.education = education
        self.job = job
        self.powers = powers
        self.publications = publications
        self.projects = projects
        self.events = events
    def __str__(self):
        return f"{self.education} {self.job} {self.powers}{self.publications} {self.projects} {self.events}"

def get_people():
    people_data = dh.get_people_data()
    events_data = dh.get_events_data()
    articles_data = dh.get_articles_data()
    projects_data = dh.get_projects_data()
    people = []

    for row in people_data.iterrows():
        isu = row[1]["ИСУ"]
        name = row[1]["ФИО"]
        education = row[1]["ОБУЧЕНИЕ"]
        job = row[1]["ДОЛЖНОСТИ"]
        powers = row[1]["ПОЛНОМОЧИЯ"]
        events = []
        articles = []
        projects = []
        for event in events_data.iterrows():
            if event[1]["ИСУ"] == isu:
                events.append(list(event[1]))
        for article in articles_data.iterrows():
            if article[1]["ИСУ"] == isu:
                articles.append(list(article[1]))
        for project in projects_data.iterrows():
            if project[1]["ИСУ"] == isu:
                projects.append(list(project[1]))
        people.append(Svinota(name, education, job, powers, isu, articles, projects, events))
    return people


def main():
    pass


if __name__ == '__main__':
    main()
