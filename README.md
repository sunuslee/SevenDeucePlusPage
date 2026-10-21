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
