$(function () {

    var a = JSON.parse('{{ value|tojson|safe }}');
    var question_type = 'karisik_sor';
    var word_number = 0;

    function change_value(a) {
        var key = '';
        const keys = Object.keys(a);
        if (question_type == "karisik_sor") {
            const randIndex = Math.floor(Math.random() * keys.length);
            key = keys[randIndex];
        } else {
            key = keys[word_number];
            word_number++;
            if (word_number >= keys.length)
                word_number = 0;
        }
        const name = a[key];
        return name
    }

    var true_count = 0;
    var false_count = 0;
    var question = '';
    var q_answer = '';

    function change_question(working_type, value) {
        if (working_type == 'eng_tr') {
            question = value.eng_word;
            q_answer = value.turk_word;
        } else {
            question = value.turk_word;
            q_answer = value.eng_word;
        }
        if (question.length > 1) {
            var show_question = question[0];
            for (i = 1; i < question.length; i++) {
                show_question += ', ' + question[i];
            }
            $this.find('#value').html(show_question);
        } else {
            $this.find('#value').html(question);
        }
    }

    $(document).ready(function () {

        var working_type = $('input[name=options]:checked').val();
        var value = change_value(a);
        $this = $(this);
        change_question(working_type, value);
        $('.tebrikler ').hide();

        $('#languageForm input').on('change', function () {
            working_type = $('input[name=options]:checked', '#languageForm').val();
            if (working_type == 'tr_eng') {
                $('.eng-tr-label').removeClass("active");
                $(".tr-eng-label").addClass("active");
                change_question(working_type, value)

            } else {
                $('.tr-eng-label').removeClass("active");
                $(".eng-tr-label").addClass("active");
                change_question(working_type, value);
            }
        });

        $('#questionTypeForm input').on('change', function () {
            question_type = $('input[name=options]:checked', '#questionTypeForm').val();
            if (question_type == 'karisik_sor') {
                $('.sirayla_sor_label').removeClass("active");
                $(".karisik_sor_label").addClass("active");
            } else {
                $('.karisik_sor_label').removeClass("active");
                $(".sirayla_sor_label").addClass("active");
            }
        });


        $('.answer').on('keyup', function (e) {
                e.preventDefault();
                var answer = $this.find('.answer').val();
                if (q_answer.includes(answer.toLowerCase())) {
                    $('.tebrikler').show();
                    true_count++;
                    $('.dogru_bilinen').prepend(question + ' -> ' + q_answer + '</br>');
                    $('.true_count').html(true_count);
                    value = change_value(a);
                    change_question(working_type, value);

                    $('.answer').val('');
                    var delayInMilliseconds = 1000;
                    setTimeout(function () {
                        $('.tebrikler ').hide();
                    }, delayInMilliseconds);
                }
            }
        );

        $('.skip').on('click', function (e) {
            e.preventDefault();

            $('.yanlis_bilinen').prepend(question + ' -> ' + q_answer + '</br>');
            false_count++;
            $('.false_count').html(false_count);
            var value = change_value(a);
            change_question(working_type, value);
            $('.answer').val('');
            var delayInMilliseconds = 1000;
            setTimeout(function () {
                //kelime gösterilecek
            }, delayInMilliseconds);
        });


    });
});