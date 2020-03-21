$('.step-options').on('click', ".edit-step", function() {
    var card = $(this).closest(".step-card");
    document.querySelector('#stepModal #stepid').value = card.data("stepid");
    document.getElementById("stepModalLabel").innerHTML = "Edit Step";
    document.querySelector('#stepModal #name').value = card.find(".card-title")[0].innerHTML;
    document.querySelector('#stepModal #description').value = card.find(".card-text")[0].innerHTML;
    document.querySelector('#stepModal #link').value = card.find(".step-link")[0].href;
    $('#stepModal').modal('show'); //Is this redundant?
});

$('#new-step-btn').on('click', function() {
    document.querySelector('#stepModal #stepid').value = "";
    document.getElementById("stepModalLabel").innerHTML = "New Step";
    document.querySelector('#stepModal #name').value = "";
    document.querySelector('#stepModal #description').value = "";
    document.querySelector('#stepModal #link').value = "";
    $('#stepModal').modal('show');
});

$('.step-options').on('click', ".delete-step", function() {
    var result = confirm("Want to delete step?");
    if (result) {
        var url_name = $(this).attr('data-url');
        $.ajax({
        url: url_name,
        type: "DELETE",
        success: function(resp){
            location.reload(true);
            }
        });
    }
});