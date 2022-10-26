document.getElementById("price-total").addEventListener('keyup', autoCompleteNew);

function autoCompleteNew(e) {

    $("#price-total").keyup(autoCompleteNew); 
    var value = $(this).val(); $(this).val = value.toLowerCase().replace(" ", ""); $("#short-name").val(value);

}
