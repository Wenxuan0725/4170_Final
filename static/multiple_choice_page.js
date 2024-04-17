$(document).ready(function() {
    $('.correct-choice').on('click', function(event) {
        $('.correct-choice').addClass('show-correct-choice');
        $('.wrong-choice').removeClass('wrong-choice').off('click');
        $('.correct-choice').removeClass('correct-choice').off('click');
        $('.next-question-button').show();

        var questionSection = $(this).closest('.quiz-question-section');
        var currentQuestionId = questionSection.data('question-id');
        submitAnswer(currentQuestionId, 10);
    });

    $('.wrong-choice').on('click', function(event) {
        $(this).addClass('show-wrong-choice');
        $('.correct-choice').addClass('show-correct-choice');
        $('.wrong-choice').removeClass('wrong-choice').off('click');
        $('.correct-choice').removeClass('correct-choice').off('click');
        $('.question-explanation').show();
        $('.next-question-button').show();

        var questionSection = $(this).closest('.quiz-question-section');
        var currentQuestionId = questionSection.data('question-id');
        submitAnswer(currentQuestionId, 0);
    });

    $('.correct-picture-choice').on('click', function(event) {
        $('.correct-picture-choice').addClass('show-correct-choice');
        $('.wrong-picture-choice').removeClass('wrong-picture-choice').off('click');
        $('.correct-picture-choice').removeClass('correct-picture-choice').off('click');
        $('.next-question-button').show();

        var questionSection = $(this).closest('.quiz-question-section');
        var currentQuestionId = questionSection.data('question-id');
        submitAnswer(currentQuestionId, 10);
    });

    $('.wrong-picture-choice').on('click', function(event) {
        $(this).addClass('show-wrong-choice');
        $('.correct-picture-choice').addClass('show-correct-choice');
        $('.wrong-picture-choice').removeClass('wrong-picture-choice').off('click');
        $('.correct-picture-choice').removeClass('correct-picture-choice').off('click');
        $('.question-explanation').show();
        $('.next-question-button').show();

        var questionSection = $(this).closest('.quiz-question-section');
        var currentQuestionId = questionSection.data('question-id');
        submitAnswer(currentQuestionId, 0);
    });

    function submitAnswer(questionId, answer_score) {
        $.ajax({
            url: "/submit_answer/" + questionId,
            method: "POST",
            contentType: "application/json",
            data: JSON.stringify({ answer_score: answer_score }),
            success: function(response) {
                console.log('Score updated to: ' + response.score);
            },
            error: function(xhr, status, error) {
                console.error("Error submitting answer: " + error);
            }
        });
    }
});