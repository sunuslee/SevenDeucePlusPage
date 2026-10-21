# SevenDeucePlus / 德益记

Bilingual product and support website, served by Caddy on our production server.

- Chinese: https://72plus.pro/
- English: https://72plus.pro/en/

## Edit and preview

Edit bilingual copy in `scripts/build_pages.py`, then run `python3 scripts/build_pages.py`.
Shared responsive styles are in `assets/site.css`. Commit the generated `index.html` and `en/index.html` with source changes.

Run `python3 -m http.server 8873 --bind 127.0.0.1`, then open http://127.0.0.1:8873/.

The current site is plain HTML/CSS, with no JavaScript or external font dependencies. `.nojekyll` lets GitHub Pages serve it directly from the repository root. Historical Jekyll template files remain for reference and are not used by the homepage. Original template licensing is retained in LICENSE.

## Assets

The Chinese and English pages use matching language screenshots, exported with the original device aspect ratio from the current client using sample data. Update the screenshots and pricing copy when app behavior changes. The QR code points to the existing App Store listing (app ID 6460033253).

## Search discovery

Run `python3 scripts/check_site.py` after generating pages. It checks the six sitemap URLs, internal links, canonical/hreflang relationships, JSON-LD syntax, and homepage screenshot locales. `scripts/seo_content.py` holds SEO metadata and bilingual practical guides. Chinese screenshots are in `assets/zh/`; English screenshots remain in `assets/`.

The website has two homepages and four guide pages targeting session tracking and home-game settlement. Google ownership verification is preserved in the generated head. Do not remove that tag while the property is in use. The sitemap is published at `https://72plus.pro/sitemap.xml`.

Production robots.txt is served at https://72plus.pro/robots.txt and declares the XML sitemap. Submit https://72plus.pro/sitemap.xml in the matching Search Console property. The GitHub Pages copy uses production canonical URLs.

App JSON-LD contains no invented reviews or aggregate ratings. It describes the app and its free download, and does not claim eligibility for Google app rich results. Search indexing, rich results and ranking are not guaranteed. Use Search Console performance reports to evaluate actual queries, impressions and clicks over time.

## Production deployment

- SSH host: `aliyun-ecs` (the existing DNS target for `72plus.pro`).
- Public files: `/srv/sevendeuceplus-site/current`, a symlink to a versioned directory under `releases/`.
- Site config: `/etc/caddy-sites/72plus.pro.caddy` (source: `deploy/72plus.pro.caddy`).
- Existing Caddy service: `baby-voice-diary-ai-caddy.service`; its main configuration imports this site separately. Do not replace the main config or existing API blocks.
- Caddy issues/renews HTTPS certificates; `www` redirects permanently to the apex while preserving the path.

After generation and validation, upload only `index.html`, `en/`, `guides/`, `assets/`, `img/appIcon.png`, `sitemap.xml`, `sitemap.txt`, and `robots.txt` into a new release. On macOS, use `COPYFILE_DISABLE=1 tar` to exclude resource forks. Keep files world-readable and atomically switch `current` to the release. The repository, deployment scripts, and server configuration must not be uploaded into the public root.

First deployment: `20261021-domain`. Main Caddy config backup: `/etc/baby-voice-diary-ai-api.caddy.before-72plus-20261021`. To undo first-time routing, restore that backup and reload the existing Caddy service. For later content rollbacks, switch `current` to the retained prior release. Always validate Caddy config before reload.
