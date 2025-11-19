---
layout: post
title: Automatically Link Text using VB.Net
date: 2011-06-01T10:29:38-05:00
excerpt: Automatically add HTML to link any words with http:// or https:// within text using this VB.net script
permalink: 2011/06/automatically-link-text-using-vb-net/
tags:
  - HTML
  - VB.net
---
At work, we use VB.net and one problem that I encountered involved a forum where they wanted to automatically link any words with http:// or https:// within the posts. Aside from security concerns, you can do this using the following script.

However, it is important to note, that it will only link URLS that are one word. You could modify the regular expression so that if a person put quotes around the URL, they could link the entire thing, but I am going to leave that to someone else.

{% highlight .net %}
' Function: LinkText()
'   Takes a msg and automatically adds HTML to link all words starting
'    http:// or https:// in the text
' Parameters
'   Msg: Is the Message we want to link the links in
' Returns:
'   NewMsg: The linked the links in the text
Function LinkText(ByVal Msg As String)
	' Remove all hrefs (so we can replace them)
	Msg = Msg.Replace("</a>", "")
	Msg = System.Text.RegularExpressions.Regex.Replace(Msg, "<a[^>]*>?","")

	Dim MatchObj as MatchCollection = Regex.Matches(Msg, "(htt(p|ps)://.+?)($|\s+)")

	Dim NewMsg As String = Msg
	For Each m As Match In MatchObj
		NewMsg = System.Text.RegularExpressions.Regex.Replace(NewMsg,
					m.Groups(0).Value, "<a&nbsp;
					href=""" & m.Groups(1).Value & """>"
					& m.Groups(1).Value & "</a>"
					& m.Groups(3).Value
				)
	Next

	Return NewMsg
End Function
{% endhighlight %}