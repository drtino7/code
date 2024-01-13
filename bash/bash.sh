cat * # everithing
cat *.py #python extencions
cat config.* #config files

find . -type f | xargs cat # find hidden files and the execs

cat $(find test.py)


find . -type f -readable ! -executable

find test.txt | xargs cat | head -n 1 #show first line
find test.txt | xargs cat | head -n 2 #show two first lines

cat test.txt | tail -n 1 #show last line
cat test.txt | tail -n 2 #show two last lines

cat test.txt | sed 's/test1/juan' #we turn test1 to juan
cat test.txt | sed 's/teat1/juan/g' #same but in all matches

cat test.txt | grep -n 'test1' #-n show the line
cat test.txt | grep '^test$'
grep 'test1'test.txt

find / -user juan -group managers 2>dev/null #dev/null balck hole

code | disown

cat test.txt | wc -l #count lines
cat test.txt | wc -v #count caracters

cat test.txt | sort | uniq -u
