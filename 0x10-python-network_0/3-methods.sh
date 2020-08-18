#!/bin/bash
# displays allowed HTTP requests, no need for `-X OPTIONS`
curl -sI "$1" | grep 'Allow:' | sed 's/^Allow: //'
