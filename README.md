# SevenDeucePlus / 德益记

Bilingual product and support website, served by Caddy on our production server.

- Chinese: https://72plus.pro/
- English: https://72plus.pro/en/

## Edit and preview

Edit bilingual copy in `scripts/build_pages.py`, then run `python3 scripts/build_pages.py`.
Shared responsive styles are in `assets/site.css`. The build generates the full production site in `build/production/` (gitignored), and six migration pages at the repository root for GitHub Pages. Commit the migration pages with source changes.

Run `python3 -m http.server 8873 --bind 127.0.0.1 --directory build/production`, then open http://127.0.0.1:8873/.

The production site is plain HTML/CSS, with no JavaScript or external font dependencies. `.nojekyll` lets GitHub Pages serve the legacy migration pages directly from the repository root. Historical Jekyll template files remain for reference and are not used by the homepage. Original template licensing is retained in LICENSE.

## Assets

The Chinese and English pages use matching language screenshots, exported with the original device aspect ratio from the current client using sample data. Update the screenshots and pricing copy when app behavior changes. The QR code points to the existing App Store listing (app ID 6460033253).

## Search discovery

Run `python3 scripts/check_site.py` after generating pages. It checks the ten sitemap URLs, internal links, canonical/hreflang relationships, JSON-LD syntax, and homepage screenshot locales. `scripts/seo_content.py` holds SEO metadata and bilingual practical guides. Chinese screenshots are in `assets/zh/`; English screenshots remain in `assets/`.

The website has two homepages and eight guide pages covering session tracking, home-game settlement, PRO PLAY and Insights. Google ownership verification is preserved in the generated head. Do not remove that tag while the property is in use. The sitemap is published at `https://72plus.pro/sitemap.xml`.

Production robots.txt is served at https://72plus.pro/robots.txt and declares the XML sitemap. Submit https://72plus.pro/sitemap.xml in the matching Search Console property. Each GitHub Pages page uses a zero-second meta refresh and canonical pointing to its corresponding production URL. Google treats immediate meta refresh as a permanent redirect signal; this is not an HTTP 301. Keep the old site crawlable and keep its ownership verification tag.

App JSON-LD contains no invented reviews or aggregate ratings. It describes the app and its free download, and does not claim eligibility for Google app rich results. Search indexing, rich results and ranking are not guaranteed. Use Search Console performance reports to evaluate actual queries, impressions and clicks over time.

## Production deployment

- SSH host: `dmit` (`154.26.179.8`). The apex and `www` DNS A records must point here.
- Public files: `/srv/sevendeuceplus-site/current`, a symlink to a versioned directory under `releases/`.
- Site config: `/etc/caddy/sites-enabled/72plus.pro.caddy` (source: `deploy/72plus.pro.caddy`).
- Existing Caddy service: `caddy.service`; `/etc/caddy/Caddyfile` imports `sites-enabled/*.caddy`. Do not replace the main config or existing API blocks.
- Caddy issues/renews HTTPS certificates; `www` redirects permanently to the apex while preserving the path.

After generation and validation, upload only files **from `build/production/`**, never from the repository root: `index.html`, `en/`, `guides/`, `assets/`, `img/appIcon.png`, `sitemap.xml`, `sitemap.txt`, and `robots.txt` into a new release. On macOS, use `COPYFILE_DISABLE=1 tar --no-xattrs` to exclude resource forks. Keep files world-readable and atomically switch `current` to the release. The repository, deployment scripts, and server configuration must not be uploaded into the public root.

DMIT release: `20261021-dmit`. For content rollback, switch `current` to a retained prior release. To remove website routing, remove only `72plus.pro.caddy` from the imported directory, validate `/etc/caddy/Caddyfile`, and reload Caddy. Never overwrite the API site files.

### Cutover verified — 2026-10-21

Both apex and www resolve to DMIT via Google's public DNS. DMIT has valid HTTPS certificates; all six pages return 200, and www redirects to the apex. Search Console ownership is verified for https://72plus.pro/; sitemap.xml reports **Success**, with **6 discovered pages** (discovery does not mean all pages are indexed).

The temporary Aliyun website import was removed and its Caddy service reloaded successfully. Its site config is retained as `/etc/caddy-sites/72plus.pro.caddy.disabled-20261021`, and files are archived at `/srv/sevendeuceplus-site.retired-20261021`. Existing API routes were preserved.


### Legacy URL migration — 2026-10-22

`scripts/build_redirects.py` maps the old Chinese and English homepages and all four guides to the same paths on `https://72plus.pro/`. Both directory and `index.html` URLs are covered by these static files; GitHub Pages handles directory slash normalization. Each page has a zero-delay meta refresh, matching canonical, and a clickable fallback link. No JavaScript, noindex, or robots blocking is used. The production builder writes to a separate directory to prevent self-redirects on DMIT. Run `python3 scripts/check_site.py` to validate both outputs before publishing. The live DMIT content does not need redeployment for this migration.

### Search content expansion — 2026-10-22

Added bilingual PRO PLAY and Insights guides, localized real screenshots on every guide, practical FAQ examples and related-guide links. Production sitemap now contains 10 URLs. Legacy redirects still cover only the original six URLs. No analytics tracker has been installed; Search Console reports search visibility, not app installs.
