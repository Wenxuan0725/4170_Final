$(document).ready(function() {
    $('.correct-choice').on('click', function(event) {
        $('.correct-choice').addClass('show-correct-choice');
        $('.wrong-choice').removeClass('wrong-choice').off('click');
        $('.correct-choice').removeClass('correct-choice').off('click');
        $('.next-question-button').show();
    });

    $('.wrong-choice').on('click', function(event) {
        $(this).addClass('show-wrong-choice');
        $('.correct-choice').addClass('show-correct-choice');
        $('.wrong-choice').removeClass('wrong-choice').off('click');
        $('.correct-choice').removeClass('correct-choice').off('click');
        $('.question-explanation').show();
        $('.next-question-button').show();
    });

    $('.correct-picture-choice').on('click', function(event) {
        $('.correct-picture-choice').addClass('show-correct-choice');
        $('.wrong-picture-choice').removeClass('wrong-picture-choice').off('click');
        $('.correct-picture-choice').removeClass('correct-picture-choice').off('click');
        $('.next-question-button').show();
    });

    $('.wrong-picture-choice').on('click', function(event) {
        $(this).addClass('show-wrong-choice');
        $('.correct-picture-choice').addClass('show-correct-choice');
        $('.wrong-picture-choice').removeClass('wrong-picture-choice').off('click');
        $('.correct-picture-choice').removeClass('correct-picture-choice').off('click');
        $('.question-explanation').show();
        $('.next-question-button').show();
    });
});