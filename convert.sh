#!/bin/bash

file=${1:-src_posts/2014-02-01-awk-extraire-des-paragraphes.md}

n=$(grep -n '^---' ${file} | cut -d ':' -f 1 | tail -n 1)

head -n $n ${file} > /tmp/header.txt
tail -n +$((n+1)) ${file} > /tmp/content.txt

sed -ri 's#<br[ /]*>#\n\n#g' /tmp/content.txt

cat /tmp/content.txt | pandoc -t markdown | sponge /tmp/content.txt

cat /tmp/content.txt | sed -r -e 's#<a[[:space:]]+href="([^"]+)"[[:space:]]*>([^<]*)</a>#[\2](\1)#' | sponge /tmp/content.txt


mapfile -t lines < <( cat /tmp/content.txt | sed -r -e 's#(<script[[:space:]]+src="([^"]+)">[[:space:]]*</script>)#\2#' )
for url in "${lines[@]}"; do
    k=${url##*/}
    if ! grep -qE '^[[:space:]]*$' <<< "$url"; then
	curl -s https://pastebin.com/raw/${k} -o /tmp/${k}
	cat /tmp/content.txt | sed -r -e "s#(<script[[:space:]]+src=\"https://pastebin.com/([^/]+/)+$k\">[[:space:]]*</script>)#pastebin:$k#" | awk -v f="/tmp/${k}" pat="/pastebin:$k/" 'BEGIN {while (getline < f) txt=txt $0 "\n"} pat {sub("pastebin:$k", txt)}' -
	
    fi
done

