#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import unicodedata
import re

# <entry><id>tag:blogger.com,1999:blog-6541117673219117663.post-8571794499126069391</id><published>2021-05-04T17:29:00.002+02:00</published><updated>2021-05-04T17:29:27.616+02:00</updated><category scheme="http://schemas.google.com/g/2005#kind" term="http://schemas.google.com/blogger/2008/kind#post"></category><category scheme="http://www.blogger.com/atom/ns#" term="commandes"></category><category scheme="http://www.blogger.com/atom/ns#" term="bash"></category><title type="text">bash, copier les fichiers d'une sortie standard vers un répertoire en utilisant xargs et cp</title><content type="html">&lt;script src="https://pastebin.com/embed_js/UwhpNTCY"&gt;&lt;/script&gt;</content><link href="https://mezalor-sc.blogspot.com/feeds/8571794499126069391/comments/default" rel="replies" title="Publier les commentaires" type="application/atom+xml"/><link href="https://draft.blogger.com/comment.g?blogID=6541117673219117663&amp;postID=8571794499126069391" rel="replies" title="0 commentaires" type="text/html"/><link href="https://draft.blogger.com/feeds/6541117673219117663/posts/default/8571794499126069391" rel="edit" type="application/atom+xml"/><link href="https://draft.blogger.com/feeds/6541117673219117663/posts/default/8571794499126069391" rel="self" type="application/atom+xml"/><link href="https://mezalor-sc.blogspot.com/2021/05/bash-copier-les-fichiers-dune-sortie.html" rel="alternate" title="bash, copier les fichiers d'une sortie standard vers un répertoire en utilisant xargs et cp" type="text/html"/><author><name>jfgiraud</name><uri>https://draft.blogger.com/profile/15160298712111915290</uri><email>noreply@blogger.com</email><gd:image height="32" rel="http://schemas.google.com/g/2005#thumbnail" src="//1.bp.blogspot.com/-QzawLfL9qzA/YUQXoyBHZrI/AAAAAAAAEsg/7b2rDBYNEmMPDuviizR9hbOw-hCyRtSygCK4BGAYYCw/s32/IMG_1627.jpg" width="24"></gd:image></author><thr:total>0</thr:total></entry>
# ----------
# <entry><id>tag:blogger.com,1999:blog-6541117673219117663.post-5775529831394495834</id><published>2021-04-29T18:44:00.000+02:00</published><updated>2021-04-29T18:44:00.008+02:00</updated><app:control xmlns:app="http://purl.org/atom/app#"><app:draft>yes</app:draft></app:control><category scheme="http://schemas.google.com/g/2005#kind" term="http://schemas.google.com/blogger/2008/kind#post"></category><title type="text">bash, enregistrer ses commandes et les rejouer</title><content type="html">https://www.tecmint.com/record-and-replay-linux-terminal-session-commands-using-script/  https://medium.com/@pczarkowski/how-to-make-an-animated-gif-of-your-terminal-commands-62b08dfb6089  https://github.com/icholy/ttygif</content><link href="https://draft.blogger.com/feeds/6541117673219117663/posts/default/5775529831394495834" rel="edit" type="application/atom+xml"/><link href="https://draft.blogger.com/feeds/6541117673219117663/posts/default/5775529831394495834" rel="self" type="application/atom+xml"/><author><name>jfgiraud</name><uri>https://draft.blogger.com/profile/15160298712111915290</uri><email>noreply@blogger.com</email><gd:image height="32" rel="http://schemas.google.com/g/2005#thumbnail" src="//1.bp.blogspot.com/-QzawLfL9qzA/YUQXoyBHZrI/AAAAAAAAEsg/7b2rDBYNEmMPDuviizR9hbOw-hCyRtSygCK4BGAYYCw/s32/IMG_1627.jpg" width="24"></gd:image></author><thr:total>0</thr:total></entry>


import bs4

with open('blog-09-20-2021.xml', 'rt') as fd:
    content = fd.read()


from bs4 import BeautifulSoup

soup = BeautifulSoup(content, "lxml")

def getv(l):
    return l[0] if len(l)>=1 else ''


def deaccent(some_unicode_string):
    if not some_unicode_string:
        return ''
    return ''.join(c for c in unicodedata.normalize('NFD', some_unicode_string)
               if unicodedata.category(c) != 'Mn')

_punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.:]+')

def slugify(text, delim='-'):
    """Generates an slightly worse ASCII-only slug."""
    if not text:
        return text
    result = []
    for word in _punct_re.split(deaccent(text).lower()):
        word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore')
        if word:
            result.append(word.decode('ascii'))
    return delim.join(result)


def to_ymdhms(s):
    return s[:4]+s[5:7]+s[8:10]+s[11:13]+s[14:16]+s[17:19]

def to_date(s):
    return s

def to_ymd(s):
    return s[:4]+'-'+s[5:7]+'-'+s[8:10]

def to_ymd_hms_t(s):
    return s[:4]+'-'+s[5:7]+'-'+s[8:10]+' '+s[11:13]+':'+s[14:16]+':'+s[17:19]

i=0
for s in soup.find_all('entry'):
    try:
        draft='yes' in str(s.find('app:draft'))
        category=str(s.category)
        if 'atom/ns#' in category or 'kind#post"' in category:
            dt = getv(s.published.contents)
            title = getv(s.title.contents)
            if draft:
                if not title:
                    i=i+1
                    title='numero_' + i
                path = '_drafts/' + slugify(title) + '.md'
            else:
                path = '_posts/' + to_ymd(dt) + '-' + slugify(title) + '.md'
            print('file: ', path)
            print('draft: ', draft)
            print('title:', title)
            print('date:', to_ymd_hms_t(dt))
            content = getv(s.content.contents)
            print('content:', content)
            print('-----')
            with open(path, 'wt') as fo:
                print("---", file=fo)
                print("layout: post", file=fo)
                print("title: \"%s\"" % title.replace('"', ''), file=fo)
                print("date: \"%s\"" % to_ymd_hms_t(dt), file=fo)
                #print("date: %s" % dt, file=fo)
                print("---", file=fo)
                print(content, file=fo)
    except Exception as e:
        print(e, file=sys.stderr)
        print(s, file=sys.stderr)