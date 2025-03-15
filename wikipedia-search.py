import webbrowser
import sys

def search_wikipedia(query):
    base_url = "https://en.wikipedia.org/wiki/"
    search_url = base_url + query.replace(" ", "_")
    webbrowser.open(search_url)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        search_query = " ".join(sys.argv[1:])
    else:
        search_query = input("Enter your Wikipedia search query: ")
    search_wikipedia(search_query)
