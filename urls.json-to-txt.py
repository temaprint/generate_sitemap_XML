import json

# Define the list of media extensions to filter out
EXCLUDED_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.gif', '.mp4', '.mp3', '.avi', '.flv']

# Load URLs from the Scrapy output
with open('temaprint_crawler/temaprint_crawler/spiders/urls.json', 'r') as json_file:
    urls = json.load(json_file)

# Filter out media URLs
filtered_urls = [url['url'] for url in urls if not any(url['url'].endswith(ext) for ext in EXCLUDED_EXTENSIONS)]

# Write filtered URLs to a txt file
with open('filtered_urls.txt', 'w') as txt_file:
    for url in filtered_urls:
        txt_file.write(url + '\n')

print(f"Saved {len(filtered_urls)} URLs to filtered_urls.txt.")
