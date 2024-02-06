import requests
from bs4 import BeautifulSoup

class Scraper:
    """
    This is the parent class to scrape entertainment
    data from websites
    """
    def __init__(self):
        pass
    def __repr__(self):
        return "This is the Scraper class"
    def check_site(self, url):
        self.url = url
        self.html_data = requests.get(self.url)
        return self.html_data
    def get_html_data(self):
        soup = BeautifulSoup(self.html_data.content, "html.parser")
        return soup

class Goodreads_Scraper(Scraper):
    """
    This scraper parses results from Goodreads
    """
    def parse(self, soup):
        results = soup.find(id="booksBody")
        # print(results)
        book_titles = results.find_all("td", class_="field title")
        titles = []
        for book_title in book_titles:
            links = book_title.find_all("a")
            for link in links:
                title = link["title"]
                titles.append(title)
        book_authors = results.find_all("td", class_="field author")
        authors = []
        for book_author in book_authors:
            links = book_author.find_all("a")
            for link in links:
                author = link.contents[0]
                authors.append(author)
        return titles, authors
        
if __name__ == "__main__":
    """Quick test to make sure above classes work correctly"""
    url = "https://www.goodreads.com/review/list/89246357-jason-burns?page=1&per_page=20&ref=nav_mybooks&utf8=%E2%9C%93"
    book_scraper = Goodreads_Scraper()
    response = book_scraper.check_site(url)
    print(response)
    html_data = book_scraper.get_html_data()
    book_titles, book_authors = book_scraper.parse(html_data)
    
    print(list(zip(book_titles, book_authors)))
    
        