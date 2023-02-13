import datetime
import argparse
import logging
import requests



def download_data(url):

    response = requests.get(url)

    return response.text


def processData(contents):
    lines = contents.split('\n')
    person_data = {}
    header = True
    for line in lines:
        if header:
            header = False
            continue
        if len(line) == 0:
            continue

        data = line.split(",")
        id = int(data[0])
        name = data[1]
        try:
            bday = datetime.datetime.strptime(data[2], "%d/%m/%Y")
            person_data[id] = (name, bday)
        except:
            continue

    return person_data


def displayPerson(id, personData):
    for i in personData:
        if id == i:
            print(personData[i])


def main(url):
    url_data = download_data(url)
    print(f"Running main with URL = {url}...")
    person_data = processData(url_data)

    while True:
        id =  int(input("Enter an ID to search: "))
        if id<0:
            break
        displayPerson(id, person_data)
        break

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)