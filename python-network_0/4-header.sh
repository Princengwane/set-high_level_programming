#!/bin/bash
# Sends a GET request with the X-School-User-Id header set to 98.
curl -s -H "X-School-User-Id: 98" "$1"
