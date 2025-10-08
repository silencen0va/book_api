from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI(title="Библиотека книг")

class Book(BaseModel):
    id: int | None = None
    title: str
    author: str
    year: int

books = []
next_id = 1

@app.get("/books")
def get_books():
    return books

@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Книга не найдена")

@app.post("/books")
def add_book(book: Book):
    global next_id
    book.id = next_id
    next_id += 1
    books.append(book.dict())
    return book

@app.put("/books/{book_id}")
def update_book(book_id: int, new_book: Book):
    for book in books:
        if book["id"] == book_id:
            book["title"] = new_book.title
            book["author"] = new_book.author
            book["year"] = new_book.year
            return book
    raise HTTPException(status_code=404, detail="Книга не найдена")

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"message": "Книга удалена"}
    raise HTTPException(status_code=404, detail="Книга не найдена")
