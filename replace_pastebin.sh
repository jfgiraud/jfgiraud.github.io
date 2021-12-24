#!/bin/bash

file="$1"

~/bin/sandr -S '<script src="https://pastebin.com/embed_js/([0-9a-zA-Z]+)"></script>' -x -r 'printf "\n\`\`\`\n"; curl -s https://pastebin.com/raw/\1 ; printf "\n\`\`\`\n"' $file

cat $file