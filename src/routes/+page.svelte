<!-- src/routes/index.svelte -->
<script>
  import CardGrid from './CardGrid.svelte';
  import { base } from '$app/paths'
  import items from './data.json'
</script>

<main>
  <h1><marquee> Welcome to Graic's Prints :) </marquee></h1>
  <CardGrid {items} />
</main>

<style>
    h1 {
        color: yellow;
    }
</style>