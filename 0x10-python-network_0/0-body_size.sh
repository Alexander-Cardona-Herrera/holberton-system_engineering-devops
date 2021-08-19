#!/bin/bash
# displaythe size of the body from the response of the request url 
curl -sI "$1" | grep -i content-length | awk '{print $2}'
