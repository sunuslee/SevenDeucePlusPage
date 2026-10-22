"""Publish only migration pages at the old GitHub Pages URLs."""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://72plus.pro/'
PATHS = ('', 'en/', 'guides/session-tracking/', 'guides/home-game-settlement/',
         'en/guides/session-tracking/', 'en/guides/home-game-settlement/')

def build():
    for path in PATHS:
        english = path.startswith('en/')
        target = BASE + path
        title = 'SevenDeucePlus has moved' if english else '德益记官网已迁移'
        text = 'Continue to our official website.' if english else '正在前往德益记新官网。如未自动跳转，请点击下方链接。'
        html = f'''<!doctype html>
<html lang="{'en' if english else 'zh-Hans'}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="refresh" content="0; url={target}">
<link rel="canonical" href="{target}">
<meta name="google-site-verification" content="q2xwd1uOt4LnEns07kvi5OlC2WJ-DHVE-IfghfIUI70">
<title>{escape(title)}</title>
</head>
<body><h1>{escape(title)}</h1><p>{escape(text)}</p><p><a href="{target}">{target}</a></p></body>
</html>
'''
        destination = ROOT / path / 'index.html'
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(html, encoding='utf-8')
    print('Built six GitHub Pages migration redirects.')

if __name__ == '__main__':
    build()
