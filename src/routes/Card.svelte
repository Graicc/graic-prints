<!-- Card.svelte -->
<script>
	import Fa from 'svelte-fa';
	import { faMastodon } from '@fortawesome/free-brands-svg-icons';
	import Siema from 'siema';
	import { onMount } from 'svelte';
	import { faChevronLeft, faChevronRight } from '@fortawesome/free-solid-svg-icons';

	/**
	 * @type {{ media: {link: string; alt: string}[]; description: any; pubdate: string; link: any; }}
	 */
	export let item;

	let siema;
	let controller;

	let index = 0;

	onMount(() => {
		if (item.media.length > 1) {
			controller = new Siema({
				selector: siema,
				onChange: () => {
					index = controller.currentSlide;
				}
			});
		}
	});

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
	<div class="images">
		<!-- left and right arrows -->
		{#if index > 0}
			<button class="arrow left" on:click={() => controller.prev()}>
				<Fa icon={faChevronLeft} size="lg" on:click={() => controller.prev()} />
			</button>
		{/if}

		{#if index < item.media.length - 1}
			<button class="arrow right" on:click={() => controller.next()}>
				<Fa icon={faChevronRight} size="lg" on:click={() => controller.next()} />
			</button>
		{/if}

		<div bind:this={siema}>
			{#each item.media as { link, alt }}
				{#if link.endsWith('.mp4')}
					<video autoplay muted src={link} />
				{:else}
					<img src={link.replace('original', 'small')} {alt} />
				{/if}
			{/each}
		</div>
	</div>

	<!-- This is wildly unsafe, but I trust the rss feed is not giving me any XSS attacks -->
	<p class="desc">{@html item.description}</p>
	<div class="bottom">
		<span class="date">{formatDate(item.pubdate)}</span>
		<a href={item.link} aria-label="View on Mastodon">
			<Fa icon={faMastodon} size="lg" />
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

		overflow: hidden;
	}

	.card img,
	.card video {
		width: 100%;
		height: auto;
	}

	.card .desc {
		color: black;
		margin: 10px;
	}

	.images {
		position: relative;
	}
	
	/* reset button css */
	button {
		background: none;
		border: none;
		cursor: pointer;
	}

	.arrow {
		position: absolute;
		top: 50%;
		z-index: 1;
		opacity: 0.8;
		padding: 5px;
	}

	.left {
		left: 0px;
	}

	.right {
		right: 0px;
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
		font-size: 0.9em;
	}
</style>
