import xml.etree.ElementTree as ET
import gzip
from datetime import datetime


def generate_sitemap(url_list):
    urlset = ET.Element('urlset', xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")

    for url in url_list:
        url_element = ET.SubElement(urlset, 'url')
        ET.SubElement(url_element, 'loc').text = url

        # Set last modified date to current date
        current_date = datetime.now().strftime('%Y-%m-%d')
        ET.SubElement(url_element, 'lastmod').text = current_date

        # Change frequency is set to daily (can be adjusted if needed)
        ET.SubElement(url_element, 'changefreq').text = 'daily'

        # Priority is set to 1 (can be adjusted if needed)
        ET.SubElement(url_element, 'priority').text = '1'

    return ET.tostring(urlset, encoding='utf-8', method='xml')


def save_gzipped_xml(filename, xml_content):
    with gzip.open(filename, 'wb') as f:
        f.write(xml_content)


def main():
    # Read URLs from txt file
    with open('urls.txt', 'r') as f:
        urls = [line.strip() for line in f.readlines()]

    # Generate sitemap XML
    sitemap_xml = generate_sitemap(urls)

    # Save gzipped XML
    save_gzipped_xml('url.xml.gz', sitemap_xml)

    print('Sitemap generated and saved as url.xml.gz!')


if __name__ == "__main__":
    main()
