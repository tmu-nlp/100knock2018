#!/usr/bin/env bash

echo using sed with ctrl+v+tab # or execute $'\t'
cat hightemp.txt | sed 's/	/ /g' # s/'\t'/' '/
echo using tr
cat hightemp.txt | tr '\t' ' '
echo using expand with -t 2
cat hightemp.txt | expand -t 2
