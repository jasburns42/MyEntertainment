from Scraper import Goodreads_Scraper


if __name__ == "__main__":
    """
    Run this script to gather books I have read from Goodreads.
    """
    book_scraper = Goodreads_Scraper()
    page = 0
    book_data = []
    scraping_error = False
    while True:
        page += 1
        url = f"https://www.goodreads.com/review/list/89246357-jason-burns?page={page}&per_page=20&ref=nav_mybooks&utf8=%E2%9C%93"
        response = book_scraper.check_site(url)
        if not response.ok and not scraping_error:
            print(f"Error reading page {page}. Try again")
            scraping_error = True
            continue
        if not response.ok and scraping_error:
            print("Two errors in a row. Something is wrong. Stopping")
            break
        scraping_error = False
        print(f"Reading page {page}")
        html_data = book_scraper.get_html_data()
        book_titles, book_authors = book_scraper.parse(html_data)
        if not book_titles:
            print(f"Reached the last page (page {page -1}). Stopping")
            break
        for title, author in zip(book_titles, book_authors):
            book_data.append((title, author))
    print(book_data)
    print(f"I have read {len(book_data)} books!!!")
    # Gathered Titles and Authors into a list of tuples.
    # Add rest of data, then push to database
    