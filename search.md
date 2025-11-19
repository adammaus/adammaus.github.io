---
layout: default
title: Search
permalink: search/
---
<script src="https://unpkg.com/lunr@2.3.9/lunr.js"></script>
<script src="/assets/js/search.js"></script>

<div class="search-wrapper">
	<h2>Search</h2>

	<div id="search-container" class="search-container">
		<input type="text" id="search-input" placeholder="Search..." autocomplete="off">
		<h3 id="num-search-results"></h3>
		<div id="search-results" class="search-results"></div>
	</div>
</div>

<script>
const numSearchResultsContainer = document.getElementById("num-search-results");
const searchInput = document.getElementById('search-input');
const searchResults = document.getElementById('search-results');

function displayResults(results) {
	if (results.length == 0) {
		return;
	}

	numSearchResultsContainer.innerHTML = results.length + " result" + (results.length != 1 ? "s" : "");

	var resultItems = '';

	results.forEach(function(result) {
		var item = getItemFromIndex(result.ref);
		resultItems += '<li class="search-item"><a href="' + item.url + '">' + item.title + '</a><p>' + item.excerpt + '</p></li>';
	});

	resultItems = "<ul>" + resultItems + "</ul>";

	searchResults.innerHTML = resultItems;
}

// Lazy load search only when needed
document.addEventListener('DOMContentLoaded', function() {
	if (searchInput) {
		loadSearchData(); // Only load if search exists
	}

	searchInput.addEventListener('input', function() {
		location.hash = "search=" + this.value;
		let results = searchIndex(this.value);
		displayResults(results);
	});

	if (location.hash != "") {
		query = location.hash.replace("#search=", "");
		searchInput.value = query;
	}

	var myInterval = setInterval(() => {
		if (dataLoaded) {
			let results = searchIndex(searchInput.value);
			displayResults(results);

			clearInterval(myInterval);
		}
	}, 1000)
});
</script>