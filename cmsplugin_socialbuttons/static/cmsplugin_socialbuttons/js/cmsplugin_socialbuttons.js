var socialbuttons = socialbuttons || {};

socialbuttons.showTitle = function() {
  $('#socialbuttons_hover_title').html($(this).attr('title'));
}

socialbuttons.clearTitle = function() {
    $('#socialbuttons_hover_title').html('');
}

$('#socialbuttons_list .socialbutton').hover(
  socialbuttons.showTitle, socialbuttons.clearTitle);
$('#socialbuttons_list .socialbutton').bind('focusin touchstart', socialbuttons.showTitle);
$('#socialbuttons_list .socialbutton').bind('focusout touchend', socialbuttons.clearTitle);
