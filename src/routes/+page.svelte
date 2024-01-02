<!-- src/routes/index.svelte -->
<script>
	import CardGrid from './CardGrid.svelte';
	import { base } from '$app/paths';
	import items from './data.json';
	import Fa from 'svelte-fa';
	import { faRssSquare } from '@fortawesome/free-solid-svg-icons';
	import { faMastodon } from '@fortawesome/free-brands-svg-icons';
</script>

<main>
	<h1><marquee> Welcome to Graic's Prints :) </marquee></h1>
	<div class="content">
		<p>
			Follow on <a href="/feed"> RSS <Fa icon={faRssSquare} size="lg" /></a> or chat on
			<a href="https://mastodon.social/@graicprints">
				Mastodon <Fa icon={faMastodon} size="lg" />
			</a>
		</p>
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
