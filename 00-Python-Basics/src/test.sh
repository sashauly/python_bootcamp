#!/bin/sh

MAGENTA="\e[35m"
BOLDBLUE="\e[1;34m"
ENDCOLOR="\e[0m"

echo "${BOLDBLUE}Running ex00: blocks.py test${ENDCOLOR}"
cd ./ex00
echo "${MAGENTA}Test file: ${ENDCOLOR}"
cat data_hashes_10lines.txt
echo "${MAGENTA}Result: ${ENDCOLOR}"
cat data_hashes_10lines.txt | python blocks.py 10
cd ../
echo "\n"

echo "${BOLDBLUE}Running ex01: decypher.py tests${ENDCOLOR}"
cd ./ex01
echo -n "${MAGENTA}Have you delivered eggplant pizza at restored keep? ${ENDCOLOR}"
python decypher.py "Have you delivered eggplant pizza at restored keep?"
echo -n "${MAGENTA}The only way everyone reaches Brenda rapidly is delivering groceries explicitly ${ENDCOLOR}"
python decypher.py "The only way everyone reaches Brenda rapidly is delivering groceries explicitly"
echo -n "${MAGENTA}Britain is Great because everyone necessitates ${ENDCOLOR}"
python decypher.py "Britain is Great because everyone necessitates"
cd ../
echo "\n"

echo "${BOLDBLUE}Running ex02: mfinder.py${ENDCOLOR}"
cd ./ex02
echo -n "${MAGENTA}ALL STARS: ${ENDCOLOR}" && cat ./tests/stars.txt | python mfinder.py
cat ./tests/stars.txt
echo "\n"

echo -n "${MAGENTA}Clearly not an m pattern: ${ENDCOLOR}" && cat ./tests/not_m.txt | python mfinder.py
cat ./tests/not_m.txt
echo "\n"

echo -n "${MAGENTA}M pattern: ${ENDCOLOR}" && cat ./tests/m.txt | python mfinder.py
cat ./tests/m.txt
echo "\n"

cd ../
