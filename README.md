<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
-->

[![](https://img.shields.io/badge/OS-macOS-blue.svg?longCache=True)]()
[![](https://img.shields.io/badge/language-AppleScript-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/v/mac-opera.svg?maxAge=3600)](https://pypi.org/project/mac-opera/)
[![](https://img.shields.io/npm/v/mac-opera.svg?maxAge=3600)](https://www.npmjs.com/package/mac-opera)
[![Travis](https://api.travis-ci.org/looking-for-a-job/mac-opera.svg?branch=master)](https://travis-ci.org/looking-for-a-job/mac-opera/)

#### Installation
```bash
$ [sudo] npm i -g mac-opera
```
```bash
$ [sudo] pip install mac-opera
```

#### Scripts usage
command|`usage`
-|-
`opera` |`usage: opera command [args]`
[`opera-close`](# "close tab by url") |`usage: opera-close url ...`
[`opera-frontmost`](# "print 1 if 'Opera.app' is frontmost, else 0") |`usage: opera-frontmost`
[`opera-fullscreen-detect`](# "print 1 if 'Opera.app' is in fullscreen mode, else 0") |`usage: opera-fullscreen-detect`
[`opera-fullscreen-enter`](# "enter fullscreen mode") |`usage: opera-fullscreen-enter`
[`opera-fullscreen-exit`](# "exit fullscreen mode") |`usage: opera-fullscreen-exit`
[`opera-kill`](# "list tabs with playing audio") |`usage: opera-kill`
[`opera-open`](# "open url(s)") |`usage: opera-open url ...`
[`opera-pid`](# "print 'Opera.app' pid") |`usage: opera-pid`
[`opera-refresh`](# "refresh url(s)") |`usage: opera-refresh url ...`
[`opera-url`](# "print active url") |`usage: opera-url`
[`opera-urls`](# "print urls") |`usage: opera-urls`

#### Examples
url(s)
```bash
$ opera urls
https://github.com/
https://google.com/
$ opera url
https://github.com/
```

open/refresh
```bash
$ opera open "https://github.com/" "https://google.com/"
$ opera refresh "https://github.com/"
```

fullscreen
```bash
$ opera fullscreen-enter
$ opera fullscreen-detect
1
$ opera fullscreen-exit
```

frontmost (`1` or `0`)
```bash
$ opera frontmost
0
```

<p align="center">
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>