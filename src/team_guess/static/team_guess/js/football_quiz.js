$(function() {
    var clubs = [
        "AC Milan",
        "Inter Milan",
        "Real Madrid",
        "Arsenal",
        "Chelsea",
        "Juventus"
    ];
    $("#clubs").autocomplete({
        source: clubs
    });

    $("#clubs").on('keydown', function(event) {
        if (event.which === 13) {
            if ($("#clubs").val() === "Inter Milan") {
                $("#result").show();
                $("#info").hide();
                $("#wrong_result").hide();
            } else {
                $("#result").hide();
                $("#info").hide();
                $("#wrong_result").show();
            }
        }
    });
});
