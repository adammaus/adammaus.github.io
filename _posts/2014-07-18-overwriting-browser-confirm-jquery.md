---
layout: post
title: Overwriting the Browser Confirm pop up using jQuery
date: 2014-07-18T14:31:12-05:00
excerpt: 'You can overwrite the default confirm function using the following snippet of code which combines jQuery UI and Bootstrap to create a nice looking confirm box that is easier to read. '
permalink: 2014/07/overwriting-browser-confirm-jquery/
tags:
  - Bootstrap
  - HTML
  - Javascript
  - jQuery
---
The browser's default confirm function is a synchronous blocking function that usually pops up a dialog box causing a web page to stop executing code and wait for user input. In most browsers, the user is allowed to select "OK" or "Cancel" and developers usually have very little control over the confirm box other than the message displayed.

This can lead to some problems when the confirm box blends into the website such as in the case with Chrome 35.0 or when you simply want more control over the button options.

You can overwrite the default confirm function such as in the following snippet of code which combines jQuery UI and Bootstrap to create a nice looking confirm box that is easier to read.

It is important to note that you will still run into a problem if you attempt to write code that blocks until the user presses a button. For that reason, the code will fall back to the old confirm function if you don't give it a function to call when you press the OK or the Cancel button.

{% highlight html %}
<html>
<head>
<link rel="stylesheet" href="http://code.jquery.com/ui/1.11.0/themes/smoothness/jquery-ui.css" />
<script src="http://code.jquery.com/jquery-1.10.2.js"></script>
<script src="http://code.jquery.com/ui/1.11.0/jquery-ui.js"></script>
<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" />
<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
</head>
<body>
<div id="wrap">
<div class="container">
<div class="row">
<div class="col-sm-12">

<h1>Overwrite the Browser's Default Confirm Box</h1>

<div id="status"></div>

<div>
	<a href="#" class="btn btn-default" onclick="confirm('Are you sure that you want to continue?', confirm_function1, cancel_function1); return false;">Click to confirm</a>
</div>

<div>
	<a href="#" class="btn btn-default" onclick="if (confirm('Are you sure that you want to continue?')) { confirm_function1(); } else { cancel_function1() }; return false;">Click to confirm using default confirm box</a>
</div>

<script type="text/javascript">
function confirm_function1() {
	$('#status').html('Pressed OK');
}

function cancel_function1() {
	$('#status').html('Pressed Cancel');
}

/**
 * Replace the jQuery UI buttons styles in the confirm box with Bootstrap styles
 *
 * @param string id: The jQuery object to update
 * @param string buttonClass: The button class to the give the button
 * @return void
 */
function updateConfirmBoxButton(id, buttonClass) {
	var disableJqueryUICss = function() {
		$(id)
			.removeClass("ui-state-hover")
			.removeClass("ui-state-focus")
			.removeClass("ui-state-active");
	};

	$(id)
		.prop("class", buttonClass)
		.mouseover(disableJqueryUICss)
		.mousedown(disableJqueryUICss)
		.focus(disableJqueryUICss)
		.focusout(disableJqueryUICss);
}

// Adjust how the confirm box is rendered
window.default_confirm = window.confirm; // Save the old confirm box function in case we need to fallback to it

/**
 * Create a new confirm box function
 *
 * @param string message: The message to display
 * @param function confirm_function: The function to execute when the user presses the 'confirm' button
 * @param function cancel_function: The function to execute when the user presses the 'cancel' button
 * @return object: If confirm_function or cancel_function are null then return the value returned by the old confirm box function Else return the new confirm box object
 */
window.confirm = function(message, confirm_function, cancel_function){
	// Fall back to the old default confirm box if we don't have both a confirm and cancel function
	if (confirm_function == null || cancel_function == null) {
		return window.default_confirm(message);
	}

	// Create the new confirm box
	var confirmBox = document.createElement("div");
	$(confirmBox)
		.html(message)
		.dialog({
			dialogClass: "confirmBox",
			buttons: {
				"OK": {
					id: "OK",
					text: "OK",
					click: function() {
						confirm_function();
						$(this).remove();
					}
				},
				"Cancel": {
					id: "Cancel",
					text: "Cancel",
					click: function() {
						cancel_function();
						$(this).remove();
					}
				}
			},
			close: function() {
				$(this).remove();
			},
			draggable: false,
			modal: true,
			resizable: false,
			width: 'auto'
		});

	// Adjust the dialog box we just created

	// Update the background so it is higher contrast
	$(".confirmBox.ui-widget-content").css("background", "#fff");

	// Update the background so it is higher contrast and the buttons are centered
	$(".confirmBox .ui-dialog-buttonpane").css("background", "#fff").css("border-width", "0").css("padding", "0");
	$(".confirmBox .ui-dialog-buttonset").css("text-align", "center").css("float", "none");

	// Hide the Titlebar
	$(".confirmBox .ui-dialog-titlebar").hide();

	// Update the confirm box buttons
	updateConfirmBoxButton(".confirmBox .ui-dialog-buttonset #OK", "btn btn-success");
	updateConfirmBoxButton(".confirmBox .ui-dialog-buttonset #Cancel", "btn btn-danger");

	return confirmBox;
};

</script>
</div>
</div>
</div>
</div>
</body>
</html>
{% endhighlight %}