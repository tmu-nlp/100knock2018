#! /usr/bin/env bash

# ls | paste - - # intersting -d "circular symbos", -s single_line
# sed = col1.txt | paste - -
# find / -name bin -type d | paste -s -d : - # auto make up PATH
# This command should be rename to rearrange
paste col1.txt col2.txt > col_1_2.txt
