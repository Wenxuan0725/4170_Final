$(document).ready(function() {
    var correctMappings = {
        'step1': 'box1',
        'step2': 'box2',
        'step3': 'box3',
        'step4': 'box4',
        'step5': 'box5',
        'step6': 'box6',
    };

    var answersChecked = false;

    // Allow drop
    $('.quiz_droppable').on('dragover', function(event) {
        event.preventDefault();
    });

    // Drag
    $('.quiz_draggable').on('dragstart', function(event) {
        event.originalEvent.dataTransfer.setData("text", event.target.id);
    });

    // Drop
    $('.quiz_droppable').on('drop', function(event) {
        event.preventDefault();
        if (answersChecked) {
            // Don't allow dropping if answers have already been checked
            return;
        }
        var data = event.originalEvent.dataTransfer.getData("text");
        var $dropTarget = $(event.target).closest('.quiz_droppable');

        if (!$dropTarget.has('.quiz_draggable').length) {
            $('#' + data).detach().appendTo($dropTarget);

            // Check if all items have been placed
            if ($('.quiz_droppable').find('.quiz_draggable').length === Object.keys(correctMappings).length) {
                checkAnswers();
            }
        }
    });

    function checkAnswers() {
        var wrongAnswer = false;
        $('.quiz_droppable').each(function() {
            var $this = $(this);
            var childId = $this.find('.quiz_draggable').attr('id');
            if (correctMappings[childId] !== $this.attr('id')) {
                wrongAnswer = true;
                $this.addClass('incorrect');
            } else {
                $this.addClass('correct');
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


});

