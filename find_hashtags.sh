#!/bin/sh
# uses: https://rldane.space/gathering-hashtags-from-the-fediverse.html
grep -f fedihashtags.txt -riw sources/
