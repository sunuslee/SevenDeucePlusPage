from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit
import json,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]/'build'/'production';BASE='https://72plus.pro/'
class Page(HTMLParser):
 def __init__(self):super().__init__();self.refs=[];self.ids=set();self.canonical=[];self.alt={};self.h1=0;self.images=[];self.jsons=[];self.injson=False
 def handle_starttag(self,t,attrs):
  a=dict(attrs)
  if t=='h1':self.h1+=1
  if 'id'in a:self.ids.add(a['id'])
  if t=='img':assert a.get('alt') is not None;self.images.append(a['src'])
  if t=='link' and a.get('rel')=='canonical':self.canonical.append(a['href'])
  if t=='link' and a.get('rel')=='alternate':self.alt[a['hreflang']]=a['href']
  if t=='script' and a.get('type')=='application/ld+json':self.injson=True
  for k in ['href','src']:
   if k in a:self.refs.append(a[k])
 def handle_endtag(self,t):
  if t=='script':self.injson=False
 def handle_data(self,d):
  if self.injson:self.jsons.append(json.loads(d))
urls=[e.text for e in ET.parse(ROOT/'sitemap.xml').findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
assert len(urls)==len(set(urls))==10
assert (ROOT/'sitemap.txt').read_text(encoding='utf-8').splitlines()==urls
for url in urls:
 rel=url.removeprefix(BASE);path=ROOT/rel/'index.html';p=Page();p.feed(path.read_text());assert p.h1==1 and p.canonical==[url]
 assert set(p.alt)=={'en','zh-Hans','x-default'}
 for ref in p.refs:
  u=urlsplit(ref)
  if u.scheme or u.netloc:
   if not ref.startswith(BASE):continue
   target=ROOT/ref.removeprefix(BASE).split('#')[0]
  else:target=path.parent/u.path
  assert target.exists(),(path,ref)
  if not u.path and u.fragment:assert u.fragment in p.ids
 if rel in ('','en/'):
  assert p.jsons
  shots=[s for s in p.images if s.endswith('.webp')]
  assert len(shots)==7
  assert all(('/zh/' in s)==(rel=='') for s in shots)
 print(rel or '/', 'PASS: links, canonical, hreflang, structure, screenshot locale')
print('Sitemap: 10 canonical URLs. JSON-LD parsed. No fake ratings included.')

# Migration destinations must match production canonical pages; production must not redirect.
from build_redirects import ROOT as LEGACY_ROOT, PATHS
for path in PATHS:
 legacy=(LEGACY_ROOT/path/'index.html').read_text()
 production=(ROOT/path/'index.html').read_text()
 assert f'http-equiv="refresh" content="0; url={BASE+path}"' in legacy
 assert f'rel="canonical" href="{BASE+path}"' in legacy
 assert f'href="{BASE+path}"' in legacy
 assert 'http-equiv="refresh"' not in production
 assert 'noindex' not in legacy
print('PASS: six immediate legacy redirects, matching canonical targets, no production redirect loops.')
