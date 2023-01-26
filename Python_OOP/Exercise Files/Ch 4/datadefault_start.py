# Python Object Oriented Programming by Joe Marini course example
# implementing default values in data classes

from dataclasses import dataclass, field
import random


def page_func():
    return random.randrange(10, 1000)


@dataclass
class Book:
    # you can define default values when attributes are declared
    title: str = "No title"
    author: str = "No author"
    pages: int = field(default_factory = page_func)
    price: float = field(default = 0.0)


b1 = Book("War and Peace", "Leo Tolstoy")
b2 = Book("The Catcher in the Rye", "JD Salinger", 234)
print(b1)
