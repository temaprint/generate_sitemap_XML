import requests
from bs4 import BeautifulSoup

DOMAIN = 'http://blog.icons8.com/'

# Set of all unique URLs
all_urls = set()

# Extensions to exclude from the sitemap
EXCLUDED_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.gif', '.mp4', '.mp3', '.avi', '.flv']

def is_excluded(url):
    """Check if a URL should be excluded based on its extension."""
    return any(url.endswith(ext) for ext in EXCLUDED_EXTENSIONS)

def find_urls(url):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to access {url}")
            return

        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all links in page
        for a_tag in soup.find_all('a', href=True):
            href = a_tag.attrs['href']

            # Convert relative links to absolute links
            if href.startswith("/"):
                href = DOMAIN + href

            # Check if the URL belongs to our domain, is not visited, and is not excluded
            if DOMAIN in href and href not in all_urls and not is_excluded(href):
                all_urls.add(href)
                print(f"Found URL: {href}")
                find_urls(href)

    except Exception as e:
        print(f"Error fetching URL {url}. Error: {str(e)}")
        return

# Start the crawl
find_urls(DOMAIN)

# Save the URLs to a txt file
with open('blog.icons8.txt', 'w') as file:
    for url in sorted(all_urls):
        file.write(url + '\n')

print("Done!")
