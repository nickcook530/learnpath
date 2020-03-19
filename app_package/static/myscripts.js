$('.step-options').on('click', ".edit-step", function() {
    const card = $(this).closest(".step-card");
    document.querySelector('#newStep #stepid').value = card.data("stepid");
    document.getElementById("newStepLabel").innerHTML = "Edit Step";
    document.querySelector('#newStep #name').value = card.find(".card-title")[0].innerHTML;
    document.querySelector('#newStep #description').value = card.find(".card-text")[0].innerHTML;
    document.querySelector('#newStep #link').value = card.find(".step-link")[0].href;
    $('#newStep').modal('show');
});

$('#new-step-btn').on('click', function() {
    document.querySelector('#newStep #stepid').value = "";
    document.getElementById("newStepLabel").innerHTML = "New Step";
    document.querySelector('#newStep #name').value = "";
    document.querySelector('#newStep #description').value = "";
    document.querySelector('#newStep #link').value = "";
    $('#newStep').modal('show');
});