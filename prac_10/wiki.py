import wikipedia

def wiki_search():
    max_attempts = 100  # Limit number of queries to avoid infinite loops
    for _ in range(max_attempts):
        title = input("Enter page title (blank to quit): ").strip()
        if title == "":
            print("Thank you.")
            break

        try:
            page = wikipedia.page(title, auto_suggest=False)
        except wikipedia.DisambiguationError as e:
            print("We need a more specific title. Try one of the following:")
            print(e.options)
        except wikipedia.PageError:
            print(f'Page id "{title}" does not match any pages. Try another id!')
        else:
            print(page.title)
            print(page.summary[:500])  # Print first 500 characters of summary
            print(page.url)

if __name__ == "__main__":
    wiki_search()
