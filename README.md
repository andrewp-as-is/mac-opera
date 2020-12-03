<!--
https://readme42.com
-->



[![](https://img.shields.io/badge/OS-macOS-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/v/mac-opera.svg?maxAge=3600)](https://pypi.org/project/mac-opera/)
[![](https://img.shields.io/npm/v/mac-opera.svg?maxAge=3600)](https://www.npmjs.com/package/mac-opera)[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/mac-opera/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/mac-opera/actions)

### Installation
```bash
$ [sudo] pip install mac-opera
```

```bash
$ [sudo] npm i -g mac-opera
```

#### Config
```bash
$ export OPERA_TIMEOUT=10 # 5 by default
```

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

`Opera.app` process
```bash
$ opera pid
42
$ opera isready 5 # timeout 5 seconds
1
$ opera kill
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>
