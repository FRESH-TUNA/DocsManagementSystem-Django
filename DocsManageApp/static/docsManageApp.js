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
                    $('.modal-body').html(data.html_form);
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
                success: function(data) {
                    if(data.form_is_valid){
                        $('#documentTable tbody').html(data.documents);
                        $('#modalForMemoak').modal('hide');
                    } else {
                        $('.modal-body').html(data.html_form);
                    }  
                }
            });
            return false; ////추가하니깐 에러 제거됨
        }

        $('.showCreateForm').click(showForm);
        $("#modalForMemoak").on("submit",".createForm",saveForm);

        $('#documentTable').on("click", '.showDeleteForm', showForm);
        $("#modalForMemoak").on("submit",".deleteForm",saveForm);

        $('#documentTable').on("click",'.showUpdateForm', showForm);
        $("#modalForMemoak").on("submit",".updateForm",saveForm);
});