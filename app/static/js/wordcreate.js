

$(function () {

    $(document).ready(function () {
        var input_count_tr = 1;
        var input_count_eng = 1;
        $('.add_form_tr').on('click', function (e) {
            e.preventDefault();
            input = ' <input style="margin-top:10px; margin-bottom:10px;", class="trk_input form-control float-left col-lg-11" type="text">\n';
            $('.new_tr_input').append(input);
            input_count_tr++;
        });
        $('.add_form_eng').on('click', function (e) {
            e.preventDefault();
            input = ' <input style="margin-top:10px; margin-bottom:10px;", class="eng_input form-control float-left col-lg-11" type="text">\n';
            $('.new_eng_input').append(input);
            input_count_eng++;
        });

        $('.send_button').on('click', function (e) {
            e.preventDefault();
            var tr_arr = $('.trk_input').map((i, e) => e.value).get();
            var eng_arr = $('.eng_input').map((i, e) => e.value).get();
            if (tr_arr.includes('')) {
                for (i = 0; i < tr_arr.length; i++)
                    if (tr_arr[i] == '')
                        tr_arr.splice(i, input_count_tr);
            }
            if (eng_arr.includes('')) {
                for (i = 0; i < eng_arr.length; i++)
                    if (eng_arr[i] == '')
                        eng_arr.splice(i, input_count_eng);
            }

            var unit = $('.unit').val();
            if (eng_arr == "" || tr_arr == '' || unit == '') {
                alert('Tüm boşlukları doldurmalısnız !!! ');
            } else {
                var create = 1;
                $.ajax({
                    url: '/word_create',
                    data: {
                        'tr_value': tr_arr.toString(),
                        'eng_value': eng_arr.toString(),
                        'unit': unit,
                        'create': create,
                    },
                    success: function (data) {
                        var txt = eng_arr + ' Başarı ile eklendi';
                        $('.success_status').html(txt);
                        $('.eng_word').val('');
                        $('.trk_input').val('');
                    }
                });
            }
        });

    });

});