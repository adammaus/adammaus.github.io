---
layout: page
---
{%- assign date_format = site.minima.date_format | default: "%b %-d, %Y" -%}

I'm a software developer at the University of Wisconsin - Madison and moonlight as a Wisconsin Master Naturalist, Volunteer, and Researcher.

<hr />

<ul class="homepage-feed">
	{% for post in site.posts %}
	{% if post.hidden == null or post.hidden == false %}
	<li>
		<h3>
			<a class="post-link" href="{{ post.url | relative_url }}">
				{{ post.title | escape }}
			</a>
		</h3>
		<span class="post-meta">{{ post.date | date: date_format }}</span>

		<p>{{ post.excerpt }}</p>
	</li>
	{% endif %}
	{% endfor %}
</ul>