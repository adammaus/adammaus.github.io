const maxResults = 10;
let searchData = null;
let lunrIndex = null;
let dataLoaded = false;

function getItemFromIndex(ref) {
	return searchData[ref];
}

// Load search data and build index
function loadSearchData() {
    fetch('/search-index.json')
        .then(response => response.json())
        .then(data => {
            searchData = data;
            buildSearchIndex();
        });
	dataLoaded = true
}

function buildSearchIndex() {
    lunrIndex = lunr(function() {
        this.field('title', { boost: 10 });      // Titles are most important
        this.field('excerpt', { boost: 7 });     // Excerpts are highly relevant
        this.field('content', { boost: 3 });     // Content is searchable
        this.field('tags', { boost: 5 });        // Tags help categorization
        this.ref('id');

        searchData.forEach(function(doc, index) {
            doc.id = index;
            this.add(doc);
        }, this);
    });
}

function searchIndex(query) {
	if (query.trim() == '') {
		return null;
	}

	query = query.toLowerCase();
	return lunrIndex.search(query);
}