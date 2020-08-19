#!/bin/bash
# send POST HTTP request with values for `email` and `subject` variables
curl -sd 'email=hr@holbertonschool.com&subject=I will always be here for PLD' "$1"
