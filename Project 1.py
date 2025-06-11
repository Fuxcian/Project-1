#Imports
import json
import ssl
from urllib.request import urlopen, Request

def main():
    # Get weather alerts for a specific state
    title = input("Enter the title of the article: ")
    url = "https://www.mediawiki.org/w/api.php" + title

main()

#NOTE: Client wishes to study behavior of wikipedia editors.
    #Must be able to type Wiki article title in command line
    #Must display recent edits to that article: oldest to newest, display all if less than 30
        #time of change, name of editor, new line
    #Exit with error code 0
