from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine
import cache

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/books", response_model=list[schemas.BookOut])
def read_books(db: Session = Depends(get_db)):
    return crud.get_books(db)

@app.post("/books", response_model=schemas.BookOut)
def add_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book)

@app.get("/books/{book_id}/reviews", response_model=list[schemas.ReviewOut])
def read_reviews(book_id: int, db: Session = Depends(get_db)):
    reviews = cache.get_cached_reviews(book_id)
    if reviews is None:
        reviews = crud.get_reviews(db, book_id)
        cache.set_cached_reviews(book_id, reviews)
    return reviews

@app.post("/books/{book_id}/reviews", response_model=schemas.ReviewOut)
def add_review(book_id: int, review: schemas.ReviewCreate, db: Session = Depends(get_db)):
    return crud.create_review(db, book_id, review)
