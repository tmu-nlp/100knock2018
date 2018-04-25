#!/usr/bin/env bash

# -l by line; -b by size in byte/kb/mb
# default prefix is x in working dir
split -l $1 "hightemp.txt" prefix_
