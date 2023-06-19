import pandas as pd


def get_people_data():
    data = pd.read_csv('data/data_people.csv')
    return data


def get_events_data():
    data = pd.read_csv('data/data_events.csv')
    return data


def get_articles_data():
    data = pd.read_csv('data/data_articles.csv')
    return data


def get_projects_data():
    data = pd.read_csv('data/data_projects.csv')
    return data


def main():
    people_data = get_people_data()


if __name__ == '__main__':
    main()
