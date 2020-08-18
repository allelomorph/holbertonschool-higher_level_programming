#!/bin/bash
# displays body size of HTTP response in bytes
curl -sI "$1" | grep 'Content-Length' | sed 's/^Content-Length: //'
