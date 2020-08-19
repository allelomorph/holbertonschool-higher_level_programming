#!/bin/bash
# send GET HTTP request with header variable `X-HolbertonSchool-User-Id` of 98
curl -sH 'X-HolbertonSchool-User-Id:98' "$1"
