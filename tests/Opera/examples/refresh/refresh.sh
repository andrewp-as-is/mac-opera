#!/usr/bin/env bash
{ set +x; } 2>/dev/null

url="$(opera url)" || exit
( set -x; opera refresh "$url" ) || exit

( set -x; sleep 5 )
urls="$(opera urls)" || exit
IFS=$'\n';set $urls
( set -x; opera refresh "$@" ) || exit
