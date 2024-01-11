cat * # everithing
cat *.py #python extencions
cat config.* #config files

find . -type f | xargs cat # find hidden files and the execs

cat $(find test.py)


find . -type f -readable ! -executable


