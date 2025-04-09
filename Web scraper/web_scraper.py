# Task 04:
# Web Scraper Tool

import requests
from bs4 import BeautifulSoup

def fetch_cnn_news():
    url = "https://edition.cnn.com/world"
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        print("\n Top CNN Headlines:\n" + "-" * 40)

        headlines = soup.find_all("span", class_="cd__headline-text")
        if not headlines:
            print(" Could not find CNN headlines. The website structure may have changed.")
        for i, headline in enumerate(headlines[:10], 1):  # Show top 10
            print(f"{i}. {headline.get_text(strip=True)}")
    except Exception as e:
        print(f" Error fetching CNN news: {e}")

def fetch_ndtv_news():
    url = "https://www.ndtv.com/latest"
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        print("\n Top NDTV Headlines:\n" + "-" * 40)

        headlines = soup.find_all("h2", class_="newsHdng")
        if not headlines:
            print(" Could not find NDTV headlines. The website structure may have changed.")
        for i, headline in enumerate(headlines[:10], 1):  # Show top 10
            print(f"{i}. {headline.get_text(strip=True)}")
    except Exception as e:
        print(f" Error fetching NDTV news: {e}")

def fetch_bbc_news():
    """Fetches and displays BBC headlines."""
    url = "https://www.bbc.com/news"
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        print("\n Top BBC Headlines:\n" + "-" * 40)

        headlines = soup.find_all("h3")
        if not headlines:
            print("Could not find BBC headlines. The website structure may have changed.")
        count = 1
        for h in headlines:
            text = h.get_text(strip=True)
            if len(text) > 10:  # Ignore short tags
                print(f"{count}. {text}")
                count += 1
                if count > 10:
                    break
    except Exception as e:
        print(f"Error fetching BBC news: {e}")

def main():
    while True:
        print("\n News Scraper Menu")
        print("1. CNN")
        print("2. NDTV")
        print("3. BBC")
        print("4. Exit")
        choice = input(" Choose a source (1-4): ")

        if choice == "1":
            fetch_cnn_news()
        elif choice == "2":
            fetch_ndtv_news()
        elif choice == "3":
            fetch_bbc_news()
        elif choice == "4":
            print(" Exiting. Stay informed!")
            break
        else:
            print(" Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()
