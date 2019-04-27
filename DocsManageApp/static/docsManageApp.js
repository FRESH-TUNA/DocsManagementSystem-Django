$(document).ready(function() {
        var showForm = function() {
            var thisButton = $(this);
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

        var saveForm = function() {
            var thisButton = $(this);
            $.ajax({
                url: thisButton.attr('data-url'),
                data: thisButton.serialize(),	
                type: 'post',
                dataType: 'json',
                beforeSend: function() {
                    $('#modalForMemoak').modal('hide');
                },
                success: function(data) {
                    $('#modalForMemoak .modal-content').html(data.html_form);
                }
            });
        }

        $('.showCreateForm').click(showForm);
        $("#modalForMemoak").on("submit",".createForm",saveForm);

        $('#documentTable').on("click", '.showDeleteForm', showForm);
        $("#modalForMemoak").on("submit",".deleteForm",saveForm);

        $('#documentTable').on("click",'.showUpdateForm', showForm);
        $("#modalForMemoak").on("submit",".updateForm",saveForm);
});