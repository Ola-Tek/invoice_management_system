$(document).ready(function() {
    alert ("we are all set")

    $('#more-line').click(function(){
        $('#div_id_line_five, #div_id_line_five_quantity, #div_id_line_five_unit_price, #div_id_line_five_total_price').slideToggle(200)
        $('#div_id_line_six, #div_id_line_six_quantity, #div_id_line_six_unit_price, #div_id_line_six_total_price').slideToggle(200)
        $('#div_id_line_seven, #div_id_line_seven_quantity, #div_id_line_seven_unit_price, #div_id_line_seven_total_price').slideToggle(200)
        $('#div_id_line_eight, #div_id_line_eight_quantity, #div_id_line_eight_unit_price, #div_id_line_eight_total_price').slideToggle(200)
        $('#div_id_line_nine, #div_id_line_nine_quantity, #div_id_line_nine_unit_price, #div_id_line_nine_total_price').slideToggle(200)
    });

});