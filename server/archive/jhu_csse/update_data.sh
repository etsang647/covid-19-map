#!/bin/bash

# pull and process data from JHU CSSE

python3 pull_data.py

for file in data/*.json
do
  prettier --write "$file"
done
