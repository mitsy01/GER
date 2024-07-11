def write_reviews(reviews: list) -> list:
    review = input("Залиште свій відгук:\n")
    reviews.append(review)
    
    return reviews
    
def find_simbols_repeated_all_reviews(reviews: list) -> None:
    reviews = " ".join(reviews)
        
    repeated_groups = set()
    for i in range(len(reviews)):
        for j in range(i+1, len(reviews)):
            slice = reviews[i:j]
            if reviews.count(slice) >= 2:
                repeated_groups.add(slice)
        
    print(f"Списокк груп символів, котрі повторюються не мешне 2 разів:\n{repeated_groups}")