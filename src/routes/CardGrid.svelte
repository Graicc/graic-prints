<script>
  import Card from './Card.svelte';

  export let items;
</script>

<style>
  /* Add your grid styling here */
  .grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 20px;
  }
</style>

<div class="grid">
  {#each items as item (item.link)}
    <Card {item} />
  {/each}
</div>
