from pydantic import BaseModel

class ReviewCreate(BaseModel):
    review_text: str

class BookCreate(BaseModel):
    title: str

class BookOut(BookCreate):
    id: int
    class Config:
        orm_mode = True

class ReviewOut(ReviewCreate):
    id: int
    class Config:
        orm_mode = True
