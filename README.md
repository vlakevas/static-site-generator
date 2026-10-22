# Static Site Generator

A static site generator written in Python. It converts a directory of Markdown files into a complete HTML website, using a single HTML template and a folder of static assets.

**Live demo:** https://vlakevas.github.io/static-site-generator/

## How it works

The generator runs in three stages:

1. **Copy static assets.** Everything in `static/` (CSS, images) is copied into the output directory `docs/`.
2. **Parse Markdown into a tree.** Each Markdown file is split into blocks (headings, paragraphs, code blocks, quotes, ordered and unordered lists). Inline text is then split into text nodes for bold, italic, inline code, links and images. Both levels are converted into a tree of `HTMLNode` objects (`ParentNode` for elements with children, `LeafNode` for elements without).
3. **Render and write pages.** The tree is rendered to HTML recursively, inserted into `template.html` together with the page title (taken from the first `#` heading), and written to the matching path under `docs/`. The `content/` directory is walked recursively, so nested folders become nested pages.

## Supported Markdown

- Headings (`#` to `######`)
- Paragraphs
- Code blocks
- Block quotes
- Ordered and unordered lists
- Inline **bold**, _italic_ and `code`
- Links and images

## Project structure

```
content/      Markdown source pages
static/       CSS and images copied as-is
template.html Page template with {{ Title }} and {{ Content }} placeholders
src/          Generator source code
src/tests/    Unit tests
docs/         Generated site (served by GitHub Pages)
```

## Usage

Requires Python 3.10 or newer. No third-party packages are needed.

Build the site and serve it locally at http://localhost:8888:

```bash
./main.sh
```

Build the site for GitHub Pages, where it lives under the `/static-site-generator/` path:

```bash
./build.sh
```

Run the test suite (53 unit tests):

```bash
./test.sh
```
