from Scraper import Goodreads_Scraper
from pickle import TRUE

if __name__ == "__main__":
    book_scraper = Goodreads_Scraper()
    page = 0
    book_data = []
    while TRUE:
        page += 1
        url = f"https://www.goodreads.com/review/list/89246357-jason-burns?page={page}&per_page=20&ref=nav_mybooks&utf8=%E2%9C%93"
        print(url)
        response = book_scraper.check_site(url)
        if not response.ok:
            print(f"Error reading page {page}. Stopping")
            break
        print(f"Reading page {page}")
        html_data = book_scraper.get_html_data()
        book_titles, book_authors = book_scraper.parse(html_data)
        if not book_titles:
            print(f"Reached the last page (page {page -1}). Stopping")
            break
        for title, author in zip(book_titles, book_authors):
            book_data.append((title, author))
        # print(list(zip(book_titles, book_authors)))
    print(book_data)
    print(len(book_data))
    # Gathered Titles and Authors into a list of tuples.
    # Add rest of data, then push to database