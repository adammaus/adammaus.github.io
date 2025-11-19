---
layout: post
permalink: "2014/12/easy-pop-ups-with-jquery/"
title: "Easy Pop-Ups with JQuery"
date: 2014-12-22T13:31:04-06:00
tags:
  - CSS
  - HTML
  - Javascript
  - jQuery
  - PHP
---
JQuery is a powerful Javascript framework and I recently wanted to use it to make a popup submenu for [MausJewelers.com](http://mausjewelers.com/) on non-touch devices. I also wanted to position the popup dynamically on pageload since I wasn’t sure where the link that would trigger the popup would be positioned since the site is responsive.

You start with a DIV that contains the content to be displayed that you can trigger using the OnMouseOver event on a link or other HTML element. You can hide the popup using the OnMouseOut event event. In this example, the popup is triggered when the user positions their mouse over the Showcase link as shown here:

![Showcase Popup](/assets/imgs/easy-pop-ups-with-jquery-image-1.png){:.centered}

The trickiest part comes when you want to trigger the popup but you want to allow the user to move their mouse over the popup without causing the popup to disappear since their mouse is leaving the link.

To achieve this, you need to set up a timeout mechanism that will allow you hide the popup only when the user is NOT hovering the link or the popup. After that it is a matter of positioning the popup so it is under the link (and the user can move between the link and the popup. Here is a bit of code that I used for Maus Jewelers.

{% highlight javascript %}
<!-- The Nav menu, I am using Bootstrap so this will be hidden on extra small devices -->
<div class="header-bottom header-nav hidden-xs">
    <ul class="nav navbar-nav">
          <li class="<?php checkActive("Location", $section); ?>"><a href="/location">Location</a></li>
          <li class="<?php checkActive("Services", $section); ?>"><a href="/services">Services</a></li>
          <li class="<?php checkActive("About", $section); ?>"><a href="/about">About Us</a></li>
          <li class="<?php checkActive("Showcase", $section); ?>" onmouseover="openPopup();" onmouseout="closePopup(true);" id="link"><a href="/showcase">Our Showcase</a></li>
         <li class="<?php checkActive("Home", $section); ?>"><a href="/">Home</a></li>
   </ul>
</div>

<!-- The popup -->
<div id="popup" style="display:none; z-index:10; position:absolute; top: 135px;" onmouseover="openPopup();" onmouseout="closePopup(true);" class="popup hidden-xs">
     <!-- I manually position the div so it will be far enough down the on the page. In this case, the nav link will not change it's top position. I am also using Bootstrap so this will be hidden on extra small devices. -->
     Hello Popup.
</div>

<script type="text/javascript">
var enablePopup = true; // if set to false, we won't open a popup
var pixelOffsetFromLink = 75; // The number of pixels to move to the left, from the link, this helps to align the popup

// Global variables
var popupOpen = false; // Indicates if the popup is currently open
var popupTimer = null; // Is a timer that triggers the closePopup function

/**
 * Calculate where the popup should be positioned based on where the link is currently at
 *
 * @return null
 */
function calculatePopupPosition() {
     var $popup = $("#popup");
     var $link = $("#link");
     $popup.css("left", ($link.offset().left - pixelOffsetFromLink) + "px");

     return null;
}

/**
 * Close the popup if the popup is open and we don't want to set a timer
 *
 * @param boolean setTimer: Indicates if we should set the timer and then close the popup after the timer's function is triggered
 *
 * @return null
 */
function closePopup(setTimer) {
     // Return if the popup isn't open
     if (!popupOpen) {
          return null;
     }

     // If we have a popup timer already, clear it so we can make a new one
     if (popupTimer != null) {
          window.clearTimeout(popupTimer);
          popupTimer = null;
     }

     // If we have set the timer, we will return early but set a timer to trigger this function and actually close the popup
     if (setTimer) {
          popupTimer = window.setTimeout("closePopup(false);", 250);
          return null;
     }

     // Check if the mouse is over the popup, if it is, keep the popup open

     // If we aren't hovering anymore, close the popup and remove the hover class from the link
     if ($("#link:hover").length == 0 && $("#popup:hover").length == 0) {
          $("#popup").hide();
          popupOpen = false;
          $("#link:nth-child(1)").removeClass("hover");
     }

     return null;
}

/**
 * Open the popup
 *
 * @return null
 */
function openPopup() {
     // If the popup is open or if we don't want to show a popup at all, return
     if (popupOpen || !enablePopup) {
          return null;
     }

     popupOpen = true;
     calculatePopupPosition();
     $("#popup").show();

     // Give the link a hover class
     $("#link:nth-child(1)").addClass("hover");

     return null;
}
</script>
{% endhighlight %}