#!/bin/bash
# divert defualt GET HTTP request to /dev/null; print only `http_code` variable
curl -so /dev/null -w "%{http_code}" "$1"
