---
layout: post
title: Javascript Email Parser
date: 2011-03-28T06:17:45-05:00
excerpt: 'A form and downloadable script that parses the emails from a list of email addresses and names (or any text actually).'
permalink: 2011/03/javascript-email-parser/
tags:
  - HTML
  - Javascript
---
A form and downloadable script that parses the emails from a list of email addresses and names (or any text actually). This problem came up during work and for a quick solution, I made an html file that parses the input and looks for email addresses. For those interested in regular expressions, the parsing is done with the .match function in javascript using the following pattern: `/[a-zA-Z\d\._\-]+@[a-zA-Z\d\.\-]+\.[a-zA-Z]{2,4}/` This pattern is suitable for this task but not the best, other more complex patterns are available to handle every possible email but this one will do for now.

**Parse Email Addresses**

{% highlight html %}
List of Emails
<textarea id="Emails" cols="50" rows="10"></textarea>

Separator
<input id="Separator" type="text" value=", " />

<a onclick="ParseEmails(); return false;" href="javascript:">Parse</a>

<p id="Results"></p>

<script type="text/javascript">
function ParseEmails() {
  var EmailStr = document.getElementById("Emails").value;

  // Very simple Email Regular Expression
  var EmailPattern = /[a-zA-Z0-9\._\-]+@[a-zA-Z0-9\.\-]+\.[a-zA-Z]{2,4}/g;

  // Match only emails
  var EmailsArr = EmailStr.match(EmailPattern);

  // Write out the new list of email
  var HtmlStr = "";
  for (x in EmailsArr){
    HtmlStr += EmailsArr[x] + document.getElementById("Separator").value;
  }

  if (EmailsArr.length > 0){
    HtmlStr = HtmlStr.substring(0, HtmlStr.length-document.getElementById("Separator").value.length);
    document.getElementById('Results').innerHTML = "Results:" + HtmlStr;
  }
}
</script>
{% endhighlight %}