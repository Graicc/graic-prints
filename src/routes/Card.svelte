<!-- Card.svelte -->
<script>
	import '@fortawesome/fontawesome-free/css/all.min.css';

	/**
	 * @type {{ link: string; media_link: string; media_alt: string; description: string; pubdate: string; }}
	 */
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

		return formattedDate.replace(/,/g, '') + ' UTC';
	}
</script>

<div class="card">
	<a href={item.media_link}>
		{#if item.media_link.endsWith('.mp4')}
			<video autoplay muted src={item.media_link} />
		{:else}
			<img src={item.media_link.replace('original', 'small')} alt={item.media_alt} />
		{/if}
	</a>

	<!-- This is wildly unsafe, but I trust the rss feed is not giving me any XSS attacks -->
	<p class="desc">{@html item.description}</p>
	<div class="bottom">
		<span class="date">{formatDate(item.pubdate)}</span>
		<a href={item.link} aria-label="View on Mastodon">
			<i class="fa-brands fa-mastodon fa-xl"></i>
		</a>
	</div>
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

		display: flex;
		flex-direction: column;
	}

	.card img,
	.card video {
		width: 100%;
		height: auto;
		border-radius: 10px 10px 0px 0px;
	}

	.card .desc {
		color: black;
		margin: 10px;
	}

	.bottom {
		/* bottom of parent flexbox */
		margin-top: auto;

		display: flex;
		justify-content: space-between;
		align-items: flex-end;
	}

	.card .date {
		margin: 10px;
		color: black;
		font-size: 0.8em;
	}

	.bottom a {
		color: inherit;
		margin: 10px;
		font-size: 0.8em;
	}
</style>
