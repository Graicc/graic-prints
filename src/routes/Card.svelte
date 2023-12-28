<!-- Card.svelte -->
<script>
  export let item;

  /**
	 * @param {string} dateString
	 */
  function formatDate(dateString) {
    let date = new Date(dateString);
    const options = {
      year: '2-digit',
      month: '2-digit',
      day: '2-digit',
      hour: '2-digit',
      minute: '2-digit',
      second: '2-digit',
      timeZone: 'UTC'
    };

    const formatter = new Intl.DateTimeFormat('en-UK', options);
    const formattedDate = formatter.format(date);

    return formattedDate.replace(/,/g, '') + " UTC";
  }
</script>

<div class="card">
  <a href={item.link}>
    {#if item.media_link.endsWith(".mp4")}
      <video autoplay muted src={item.media_link} alt="Video of the print" />
    {:else}
      <img src={item.media_link} alt={item.media_alt}/>
    {/if}
  </a>
    
  <!-- This is wildly unsafe, but I trust the rss feed is not giving me any XSS attacks -->
  <div class="desc">{@html item.description}</div>
  <p class="date">{formatDate(item.pubdate)}</p>
</div>

<style>
  /* Add your card styling here */
  .card {
    background-color: #00dfdf;
    border: 1px solid #ddd;
    padding: 0px;
    margin: 10px;
    border-radius: 10px;
    height: auto;
  }

  .card img, .card video {
    width: 100%;
    height: auto;
    border-radius: 10px 10px 0px 0px;
  }

  .card .desc {
    color: black;
    margin: 10px;
  }

  .card .date {
    margin: 10px;
    color: black;
    font-size: .8em;
  }
</style>