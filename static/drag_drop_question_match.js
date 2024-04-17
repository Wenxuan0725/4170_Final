$(document).ready(function() {
    var correctMappings = {
        'step2_match': 'box2_match',
        'step5_match': 'box5_match',
        'step3_match': 'box3_match',
    };

    var answersChecked = false;
    var q8_score = 10

    // Allow drop
    $('.quiz_droppable_match').on('dragover', function(event) {
        event.preventDefault();
    });

    // Drag
    $('.quiz_draggable_match').on('dragstart', function(event) {
        event.originalEvent.dataTransfer.setData("text", event.target.id);
    });

    // Drop
    $('.quiz_droppable_match').on('drop', function(event) {
        event.preventDefault();
        if (answersChecked) {
            // Don't allow dropping if answers have already been checked
            return;
        }
        var data = event.originalEvent.dataTransfer.getData("text");
        var $dropTarget = $(event.target).closest('.quiz_droppable_match');

        if (!$dropTarget.has('.quiz_draggable_match').length) {
            $('#' + data).detach().appendTo($dropTarget);

            // Check if all items have been placed
            if ($('.quiz_droppable_match').find('.quiz_draggable_match').length === Object.keys(correctMappings).length) {
                checkAnswers();

                var questionSection = $(this).closest('.quiz-question-section-order');
                var currentQuestionId = questionSection.data('question-id');
                submitAnswer(currentQuestionId, q8_score);
            }
        }
    });

    function checkAnswers() {
        var wrongAnswer = false;
        $('.quiz_droppable_match').each(function() {
            var $this = $(this);
            var childId = $this.find('.quiz_draggable_match').attr('id');
            console.log(childId,correctMappings[childId], $this.attr('id'))
            $this.find('.quiz_draggable_match').css('border', '0');
            if (correctMappings[childId] !== $this.attr('id')) {
                wrongAnswer = true;
                $this.addClass('incorrect_match');
                q8_score = 0
            } else {
                $this.addClass('correct_match');
            }
        });
        if (wrongAnswer) {
            // Show the explanation if there's a wrong answer
            $('.question-explanation').show();
        } 
            $('.next-question-button').show();
        // Prevent further drops after checking
        answersChecked = true;
    }


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

