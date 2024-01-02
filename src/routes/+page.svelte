<!-- src/routes/index.svelte -->
<script>
  import CardGrid from './CardGrid.svelte';
  import { base } from '$app/paths'
  import items from './data.json'
  import '@fortawesome/fontawesome-free/css/all.min.css'
</script>

<main>
  <h1><marquee> Welcome to Graic's Prints :) </marquee></h1>
  <div class="content">
    <p> Follow on <a href="/feed">RSS <i class="fa-solid fa-square-rss fa-xl"></i></a> or chat on <a href="https://mastodon.social/@graicprints">Mastodon <i class="fa-brands fa-mastodon fa-xl"></i></a> </p>
    <CardGrid {items} />
  </div>
</main>

<style>
    h1 {
        color: yellow;
    }

    .content {
      max-width: 1100px;
      margin: 0 auto;
      padding: 0 10px;
    }

    a {
        color: black;
    }
</style>