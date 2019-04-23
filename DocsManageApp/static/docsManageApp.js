$(document).ready(
    function() {
        var showForm = function() {
            var thisButton =  $(this);
            $.ajax({
                url: thisButton.attr('data-url'),
                type: 'get',
                dataType: 'json',
                beforeSend: function() {
                    $('#modalForMemoak').modal('show');
                },
                success: function(data) {
                    $('#modalForMemoak .modal-content').html(data.html_form);
                }
            });
        };

        $('.createForm').click(showForm)
        $('.deleteForm').click(showForm)
        $('.updateForm').click(showForm)
    }
);