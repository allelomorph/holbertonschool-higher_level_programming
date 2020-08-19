#!/bin/bash
# sends second arg as JSON POST HTTP request; displays response
curl -sd "$(cat "$2")" -H 'Content-Type: application/json' "$1"
