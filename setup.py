import setuptools

setuptools.setup(
    name='mac-opera',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/.DS_Store','scripts/.opera-close.applescript','scripts/.opera-fullscreen-detect.applescript','scripts/.opera-fullscreen-enter.applescript','scripts/.opera-fullscreen-exit.applescript','scripts/.opera-isready.applescript','scripts/.opera-open.applescript','scripts/.opera-refresh.applescript','scripts/.opera-url.applescript','scripts/.opera-urls.applescript','scripts/opera','scripts/opera-close','scripts/opera-frontmost','scripts/opera-fullscreen-detect','scripts/opera-fullscreen-enter','scripts/opera-fullscreen-exit','scripts/opera-isready','scripts/opera-kill','scripts/opera-open','scripts/opera-pid','scripts/opera-refresh','scripts/opera-url','scripts/opera-urls']
)
