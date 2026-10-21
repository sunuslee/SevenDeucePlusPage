# SevenDeucePlus / 德益记

Bilingual product and support website, hosted on GitHub Pages.

- Chinese: https://sunuslee.github.io/SevenDeucePlusPage/
- English: https://sunuslee.github.io/SevenDeucePlusPage/en/

## Edit and preview

Edit bilingual copy in `scripts/build_pages.py`, then run `python3 scripts/build_pages.py`.
Shared responsive styles are in `assets/site.css`. Commit the generated `index.html` and `en/index.html` with source changes.

Run `python3 -m http.server 8873 --bind 127.0.0.1`, then open http://127.0.0.1:8873/.

The current site is plain HTML/CSS, with no JavaScript or external font dependencies. `.nojekyll` lets GitHub Pages serve it directly from the repository root. Historical Jekyll template files remain for reference and are not used by the homepage. Original template licensing is retained in LICENSE.

## Assets

The six WebP screenshots are aspect-preserving exports from the current English client using sample data. Both pages identify the screenshot language. Update the screenshots and pricing copy when app behavior changes. The QR code points to the existing App Store listing (app ID 6460033253).

## Search discovery

Run `python3 scripts/check_site.py` after generating pages. It checks the six sitemap URLs, internal links, canonical/hreflang relationships, JSON-LD syntax, and homepage screenshot locales. `scripts/seo_content.py` holds SEO metadata and bilingual practical guides. Chinese screenshots are in `assets/zh/`; English screenshots remain in `assets/`.

The website has two homepages and four guide pages targeting session tracking and home-game settlement. Google ownership verification is preserved in the generated head. Do not remove that tag while the property is in use. The sitemap is published at `https://sunuslee.github.io/SevenDeucePlusPage/sitemap.xml`.

This is a GitHub Pages project subpath. A robots.txt here would not govern crawling: crawlers consult `https://sunuslee.github.io/robots.txt`, which currently returns 404 (no crawl restrictions). No ineffective project-level robots file is presented as a solution. Submit the sitemap through the verified URL-prefix property instead.

App JSON-LD contains no invented reviews or aggregate ratings. It describes the app and its free download, and does not claim eligibility for Google app rich results. Search indexing, rich results and ranking are not guaranteed. Use Search Console performance reports to evaluate actual queries, impressions and clicks over time.
