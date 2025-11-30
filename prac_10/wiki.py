import wikipedia

phrase = input("Enter page title: ")
while phrase != "":
    try:
        page = wikipedia.page(phrase, auto_suggest=False)
        print(f"{page.title}")
        print(page.summary.split('\n')[0])
        print(f"{page.url}")
    except wikipedia.exceptions.DisambiguationError as e:
        print("We need a more specific title. Try one of the following, or a new search:")
        print(e.options)
    except wikipedia.exceptions.PageError:
        print(f"page id \"{phrase}\" does not match any pages. Try another id!")
    phrase = input("Enter page title: ")
print("Thank you.")
