# Mock Redis
cache_store = {}

def get_cached_reviews(book_id):
    return cache_store.get(book_id)

def set_cached_reviews(book_id, data):
    cache_store[book_id] = data
