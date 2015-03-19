# Coins API Docs

This is an orphan branch that serves as a project page for Coins API.
[Github Pages](https://help.github.com/categories/github-pages-basics/)
is based from [Jekyll](http://jekyllrb.com), which dictates the
[directory structure](http://jekyllrb.com/docs/structure/) of this branch.
Aside from that, we use [Flatdoc](http://ricostacruz.com/flatdoc) to
generate pages from [Markdown](https://help.github.com/articles/github-flavored-markdown/)

## Creating a New Page

To create a new page, create a new file `pagename.html` with the following
contents:

```html
---
layout: default
---

<script>
  Flatdoc.run({
    fetcher: Flatdoc.github('coinsph/api', 'pagename.md?ref=gh-pages')
  });
</script>
```

The purpose of this file is to tell Flatdoc which markdown file to load. In the
example given above, we want it to load `pagename.md` from this branch, which
means the next step is to actually create `pagename.md` and fill it up with
contents.

Before you comment about why it needs two steps to create a page, please see
"Possible Improvements" at the bottom of this `README`.

## Page Layout

All page headers appear as sidebar items. Child headers are displayed below its
parent with an indent. Everything is written in Markdown, just like this
`README`.

## Versioning

Feel free to create directories for version-specific API docs. For instance:

```
.gitignore
index.html
index.md
v1/
  buy-api.html
  buy-api.md
  ...
v2/
  buy-api.html
  buy-api.md
  ...
```

## Links

Let's say should `index.md` link to both API versions `v1` and `v2`, Markdown
can do it for you by using relative (as in relative to the directory) links:

```markdown
# v1 API
## [Buy Order](v1/buy-api.html)
...

# v2 API
## [Buy Order](v2/buy-api.html)
```

The contents of `v1` and `v2` html files should look like this:

```
---
layout: default
---

<script>
  Flatdoc.run({
    fetcher: Flatdoc.github('coinsph/api', 'v1/buy-api.md?ref=gh-pages')
  });
</script>
```

Why should we include the containing directory? Because what makes this possible
is Github's [Content API](https://developer.github.com/v3/repos/contents/#get-contents),
which is what Flatdoc is using.

## Possible Improvements

Use [Yeoman](http://yeoman.io/) to create a Flatdoc generator for API docs.
Ideally, we should just forget about the html and create pages with something like:

```zsh
$ yo flatdoc:page pagename
$ yo flatdoc:page 'dir/pagename'
```

which creates the necessary html boilerplate along with the desired Markdown file.