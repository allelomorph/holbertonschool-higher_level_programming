#!/bin/bash
# navigates 1 redirect, and supplies values for `user_id` and header `Origin`
curl -sd 'user_id=98' -X PUT -H 'Origin: HolbertonSchool' -L 0.0.0.0:5000/catch_me
