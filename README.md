# Graic prints

[https://prints.graic.net](https://prints.graic.net)

Graic prints converts [a Mastodon feed](https://mastodon.social/@graicprints) to a static Svelte site with a [RSS feed](https://prints.graic.net/feed).

Mastodon provides an [RSS feed for every account](https://mastodon.social/@graicprints.rss). [`generate.py`](scripts/generate.py) converts it to a [json file](src/routes/data.json), which is read by Svelte. This is updated periodically by a [GitHub Action](.github/workflows/update.yml). The resulting RSS feed is genereated by [`rss.py`](scripts/rss.py).

The site uses [Siema](https://pawelgrzybek.github.io/siema) for the image carousel.