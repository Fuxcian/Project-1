#Imports
import json
import ssl
from urllib.request import urlopen
import sys

def main():
    title = page_name(input("Enter name of Wikipedia article: "))
    if title == "":
        print("Please provide an article name.")
        return sys.exit(1)
    json_dict = edit_title(title)
    display(json_dict)


def page_name(page_name: str) -> str:
    condensed = page_name.strip()
    condensed = condensed.replace(" ", "_")
    return condensed


def edit_title(condensed: str) -> dict:
    url = f"https://en.wikipedia.org/w/api.php?action=query&prop=revisions&meta=siteinfo&titles={condensed}&rvprop=user|timestamp&continue=&redirects&rvlimit=30&format=json"
    context = ssl._create_unverified_context()
    try:
        response = urlopen(url, context=context)
    except:
        print("Sorry there is a network error.")
        return sys.exit(3)
    return json.loads(response.read())
    
def display(json_dict: dict) -> None:
    try:
        for item in json_dict["query"]["redirects"]:
            print(f"Redirected from {item['from']} to {item['to']}\n")
    except:
        pass
    try:
        for item in json_dict["query"]["pages"].values():
            for revision in item["revisions"]:
                print(f"{revision['timestamp']} {revision['user']}\n")
    except:
        print("No article found.")
        return sys.exit(2)

main()

#NOTE: Client wishes to study behavior of wikipedia editors.
    #Must be able to type Wiki article title in command line
    #Must display recent edits to that article: oldest to newest, display all if less than 30
        #time of change, name of editor, new line
    #Exit with error code 0
