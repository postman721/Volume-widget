#!/bin/sh
#This script is used to get the initial volume level.
amixer get Master | grep "%" | cut -d ' ' -f 7 | uniq | tr -cd [:digit:]
