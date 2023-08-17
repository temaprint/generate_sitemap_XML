# Sitemap XML Elements Explanation

In sitemaps, two optional elements can provide search engines with additional insights into your site's content: `<changefreq>` and `<priority>`.

## 1. `<changefreq>`

This element informs search engines about the expected frequency of updates for a specific URL's content.

### Possible Values:

- **`always`**: The page is continually changing (very rare use case).
- **`hourly`**
- **`daily`**
- **`weekly`**
- **`monthly`**
- **`yearly`**
- **`never`**: Indicates the content of the page will never change, e.g., archived content.

> **Note**: It's essential to provide accurate values. Misleading search engines with incorrect frequencies can be counterproductive.

## 2. `<priority>`

The `<priority>` element denotes the relative importance of a URL in comparison to other URLs on your site.

### Range:

- The value can vary from `0.0` to `1.0`.
- **`1.0`** is the highest priority.
  
> **Note**: It's worth mentioning that setting a high priority for a page doesn't imply it will rank better on search engines. Instead, it hints at the importance of the page in relation to other pages on your site. Most websites either omit this value or set all pages to `0.5`, the default if not specified.

---

When setting up sitemaps, always ensure the content is accurate. Any misleading information can potentially result in suboptimal crawl behavior or even penalties from search engines. The most crucial element in the sitemap is the `<loc>` tag, which specifies the actual URL of the content.
Running the Crawler
From the root directory of the Scrapy project:
---
To start the crawl and save the URLs to urls.json:

## Installation

1. Install Scrapy:
>pip install scrapy
2. Navigate to the project directory:
>cd NAME
3. Running the Crawler
From the root directory of the Scrapy project:
To start the crawl and save the URLs to `urls.json`:
>scrapy crawl NAME -o urls.json
4. filter start (if need)
> python filter_urls.py
 
This script will filter out specific media links (e.g., `.jpg`, `.png`, etc.) and save the resulting URLs to `filtered_urls.txt`.

## Additional Information

- The Scrapy spider is located in `NAME_crawler/spiders/NAME_spider.py`.
- The URL filtering script is `filter_urls.py`.
- Filtered URLs will be saved to `filtered_urls.txt`.
- If needed, you can modify the media extensions to be excluded in the `filter_urls.py` script.