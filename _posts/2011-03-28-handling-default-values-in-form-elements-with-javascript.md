---
layout: post
title: Handling Default Values in Form Elements (with Javascript)
date: 2011-03-28T06:24:47-05:00
excerpt: You can add some fancy Javascript functionality to your forms by handling how form elements behave when a user focuses and blurs focus on different elements.
permalink: 2011/03/handling-default-values-in-form-elements-with-javascript/
tags:
  - HTML
  - Javascript
---
You can add some fancy Javascript functionality to your forms by handling how form elements behave when a user focuses and blurs focus on different elements. When they focus on the element, this script will help you check if they have already entered content into this element or if you should clear it. When they end their focus on the element, another function will fire and check if the element has a blank element and refill it with the default value. This comes in handy when you that element is required in the form.

{% highlight html %}
<label for="FirstName">Sample Input 1:</label><input class="text" name="FirstName" onblur="CheckText(this, 'First Name');" onfocus="ClearText(this, 'First Name');" type="text" value="First Name" />

<label for="LastName">Sample Input 2:</label><input class="text" name="LastName" onblur="CheckText(this, 'Last Name');" onfocus="ClearText(this, 'Last Name');" type="text" value="Last Name" />

<script type="text/javascript">
// Change the color of the input permanently (if they answered the input)
function CheckText(Elem, DefaultValue){
  if (Elem.value == DefaultValue || Elem.value.toString() == ""){
    Elem.value = DefaultValue;
  }
}

// Check the elem's value to see if a user has input text already
// If they have, do nothing
// If not, clear the text area
function ClearText(Elem, DefaultValue){
  if (Elem.value == DefaultValue){
    Elem.value = "";
  }
}
</script>
{% endhighlight %}