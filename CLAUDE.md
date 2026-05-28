# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Royal City Suds is a static website for a mobile car washing business serving Guelph, Ontario. It's built with [Pelican](https://getpelican.com/) (Python static site generator) using the Flex theme, and deployed to Cloudflare Pages via Wrangler.

## Common Commands

```bash
# Development — build and serve with live reload
make devserver

# Build only (dev settings, no feeds, relative URLs off)
make html

# Build with production settings (enables Atom feeds, sets SITEURL)
make publish

# Deploy to Cloudflare Pages (builds with publishconf.py, then deploys)
./deploy.sh

# Clean generated output
make clean
```

The `invoke`/`tasks.py` alternative also works (e.g. `invoke build`, `invoke serve`, `invoke livereload`), but the `make` commands cover the same operations.

## Architecture

### Config split

- `pelicanconf.py` — dev config (feeds disabled, `SITEURL=""`)
- `publishconf.py` — production config (imports pelicanconf, sets `SITEURL="https://royalcitysuds.com"`, enables Atom feeds, `DELETE_OUTPUT_DIRECTORY=True`)

### Content

All site content lives in `content/`. Currently there is only one page:

- `content/pages/index.md` — homepage (overrides the default index via `Save_as: index.html`)
- `content/images/` — static image assets (e.g. `logo.png`)

Blog articles (if added) go directly in `content/` as `.md` files.

### Theme

The `themes/flex/` directory is a copy of the [Flex theme](https://github.com/alexandrevicenzi/Flex). Templates are Jinja2 HTML in `themes/flex/templates/`. Theme configuration variables (sidebar links, social icons, dark mode, analytics integrations) are set in `pelicanconf.py`.

### Output & Deployment

Pelican generates the static site into `output/`. The deploy script builds with production settings and pushes `output/` to Cloudflare Pages project `royalcitysuds` using `npx wrangler pages deploy`.
