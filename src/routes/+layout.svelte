<script>
  import "../app.css";

  // This can be false if you're using a fallback (i.e. SPA mode)
  export const prerender = true;
</script>

<div>
  <slot />
</div>

<style>
  /* Add your layout styling here */
  div {
    margin: 0 10px;
  }
</style>