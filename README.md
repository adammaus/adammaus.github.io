# Serving the site
1. Run: $ bundle exec jekyll serve
	a. This will usually serve at: http://127.0.0.1:4000/
	b. Any changes to the files will be automatically updated.

# Resources
* https://devhints.io/jekyll
* https://github.com/jekyll/minima

# Installation
1. Install Ruby and Bundler
2. Install Jekyll
	1. $ bundle init
	2. $ bundle config set --local path 'vendor/bundle'
	3. $ bundle add jekyll
3. Add Jekyll site: $ bundle exec jekyll new --force --skip-bundle .
4. Install dependencies: $ bundle install
5. Run commands under "Serving the site"

# Symbols to replace
* “ => "
* ” => "
* ’ => '
* &#8220; => "
* &#8221; => "
* &lt; => <
* &gt; => >
* &#8217; => '