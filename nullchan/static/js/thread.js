$(document).ready(function() {
    $('.comment-reply-btn').click(function(){
        $('button.comment-reply-btn').nextAll('form').css('display', 'block');
        $('button.comment-reply-btn').nextAll('button.comment-reply-cancel-btn').css('display', 'block');
    });
    $('.comment-reply-cancel-btn').click(function(){
        $('.comment-reply-cancel-btn').css('display', 'none');
        $('button.comment-reply-cancel-btn').nextAll('form').css('display', 'none');
    });
});