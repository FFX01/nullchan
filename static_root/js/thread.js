$(document).ready(function() {
    $('button.comment-reply-btn').click(function(){
        $('button.comment-reply-btn').next().css('display', 'block');
    });
});