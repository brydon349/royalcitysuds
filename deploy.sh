#!/bin/bash

# Exit script if any command fails
set -e

# Build the site
pelican content -o output -s publishconf.py

npx wrangler pages deploy output --project-name=royalcitysuds --commit-dirty=true --branch=main
