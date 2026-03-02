class Document:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def display(self):
        print(self.__str__())
    
    def __str__(self):
        return f"Document: '{self.title}' by {self.author} ({self.year})"
    
    def __repr__(self):
        return f"Document('{self.title}', '{self.author}', {self.year})"

class Book(Document):
    def __init__(self, title, author, year, num_pages, isbn):
        super().__init__(title, author, year)
        self.num_pages = num_pages
        self.isbn = isbn
    
    def display(self):
        print(self.__str__())
    
    def __str__(self):
        return f"Book: '{self.title}' - {self.author} ({self.year}) - {self.num_pages}p - ISBN: {self.isbn}"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year}', {self.num_pages}, '{self.isbn}')"
    
    def __eq__(self, other):
        if isinstance(other, Book):
            return self.isbn == other.isbn
        return False

class ScientificArticle(Document):
    def __init__(self, title, author, year, journal, doi):
        super().__init__(title, author, year)
        self.journal = journal
        self.doi = doi
    
    def display(self):
        print(self.__str__())
    
    def __str__(self):
        return f"Article: '{self.title}' - {self.author} ({self.year}) - {self.journal} - DOI: {self.doi}"
    
    def __repr__(self):
        return f"ScientificArticle('{self.title}', '{self.author}', {self.year}', '{self.journal}', '{self.doi}')"

class Library:
    def __init__(self, name="My Library"):
        self.name = name
        self.documents = []
    
    def add(self, document):
        
        if not isinstance(document, Document):
            raise TypeError(f"Only Document objects can be added. Received: {type(document).__name__}")
        
        if isinstance(document, Book):
            for doc in self.documents:
                if isinstance(doc, Book) and doc.isbn == document.isbn:
                    print(f"Error: A book with ISBN {document.isbn} already exists in the library")
                    return False
        
        self.documents.append(document)
        print(f"Added: {document.title}")
        return True
    
    def search(self, title):
        title_lower = title.lower()
        for document in self.documents:
            if document.title.lower() == title_lower:
                return document
        return None
    
    def display_catalog(self):
        print(f"\n--- Catalog of {self.name} ---")
        if not self.documents:
            print("The library is empty")
        else:
            for i, doc in enumerate(self.documents, 1):
                print(f"{i}. {doc}")
    
    def __len__(self):
        return len(self.documents)
    
    def __contains__(self, document):
        if isinstance(document, Book):
            for doc in self.documents:
                if isinstance(doc, Book) and doc.isbn == document.isbn:
                    return True
        else:
            for doc in self.documents:
                if doc == document:  
                    return True
        return False
    
    def __str__(self):
        return f"Library '{self.name}' containing {len(self)} documents"
    
    def __repr__(self):
        return f"Library('{self.name}')"

print("\n" + "="*50)
print("INTEGRATOR PROJECT - Library System")
print("="*50)

lib = Library("Central Library")
print(f"Library created: {lib}")

book1 = Book("Python for Beginners", "John Doe", 2023, 500, "978-2-1234-5678-9")
book2 = Book("Advanced Algorithms", "Jane Smith", 2022, 350, "978-2-8765-4321-0")
article1 = ScientificArticle("Deep Learning Review", "Alan Turing", 2024, "Nature AI", "10.1234/nature.2024.001")
article2 = ScientificArticle("Quantum Computing", "Richard Feynman", 2023, "Science", "10.5678/science.2023.002")

print("\nAdding documents:")
lib.add(book1)
lib.add(book2)
lib.add(article1)
lib.add(article2)

print("\nSearching for 'Python for Beginners':")
result = lib.search("Python for Beginners")
if result:
    print(f"Found: {result}")
else:
    print("Not found")

print(f"\nNumber of documents: {len(lib)}")

print(f"\nTest 'in':")
print(f"book1 in library? {book1 in lib}")
print(f"new book in library? {Book('Test', 'Author', 2024, 100, '999') in lib}")

lib.display_catalog()

print("\nAttempt to add a non-Document object:")
try:
    lib.add("This is a string")
except TypeError as e:
    print(f"Error caught: {e}")

print("\nAttempt to add the same book twice:")
lib.add(book1)  # Should be rejected

book1_copy = Book("Python for Beginners (copy)", "John Doe", 2023, 500, "978-2-1234-5678-9")
lib.add(book1_copy)
