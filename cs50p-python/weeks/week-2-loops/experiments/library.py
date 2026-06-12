def main():
    library = {
        "godan": "munshi premchand",
        "the god of small things": "arundhati roy",
        "train to pakistan": "khushwant singh"
    }
    while True:
        user = input("What you wanna do : add, list, exit: ").lower().strip()
        if user == "exit":
            break
        elif user == "add":
            add_book(library)
        elif user == "list":
            list_books(library)
        else:
            print("Type what you wanna do: ")
        
def add_book(lib):
    title = input("Book title: ").strip().lower()
    author = input("Book author: ").strip().lower()
    lib[title] = author
    print("Book successfully added to the library: ")
    return lib

def list_books(lib):
    for title in lib:
        author = lib[title]
        print(f"Book title is {title} and author is {author}")
        

if __name__ == "__main__":
    main()


