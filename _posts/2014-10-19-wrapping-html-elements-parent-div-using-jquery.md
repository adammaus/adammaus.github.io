---
layout: post
permalink: "2014/10/wrapping-html-elements-parent-div-using-jquery/"
title: "Wrapping HTML Elements with a Parent DIV using jQuery"
date: 2014-10-20T10:13:49-05:00
tags:
  - HTML
  - Javascript
  - jQuery
---
One of our projects required us to add a target element to a parent DIV dynamically. In this example, we are targeting the “child” CSS class and adding any elements that have that CSS class to a DIV with the “parent” CSS class.

{% highlight javascript %}
// Add a selector to a parent DIV with the wrapping class
var targetSelector = ".child";
$(targetSelector).each(function() {
	// Check the parent doesn't already have the wrapperClass on it
	var wrapperClass = "parent";
	if ($(this).parent().hasClass(wrapperClass)) {
		return;
	}

	// Wrap the target element with a parent div with class = wrapperClass
	var parent = document.createElement(“div”);
	$(parent).addClass(wrapperClass);
	var $currNode = $(this).clone();

	// Replace the current node with the parent and append the current node content
	$(this).replaceWith($(parent));
	$(parent).append($currNode);
});
{% endhighlight %}
