from sqlalchemy.orm import Session
from models import Book, Review
import schemas

def get_books(db: Session):
    return db.query(Book).all()

def create_book(db: Session, book: schemas.BookCreate):
    db_book = Book(title=book.title)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_reviews(db: Session, book_id: int):
    return db.query(Review).filter(Review.book_id == book_id).all()

def create_review(db: Session, book_id: int, review: schemas.ReviewCreate):
    db_review = Review(**review.dict(), book_id=book_id)
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review
