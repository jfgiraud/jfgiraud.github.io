#!/bin/bash
chmod a+w /srv/jekyll/Gemfile.lock
chmod 777 /srv/jekyll
jekyll serve --watch --incremental
