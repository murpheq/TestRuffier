from PyQt5.QtGui import QFont

win_x, win_y = 135, 100
win_width, win_height = 1650, 900


txt_hello = 'Добро пожаловать в программу по определению состояния здоровья!'
txt_next = 'Начать!'
txt_instruction = ('Данное приложение позволит вам с помощью теста Руфье провести первичную диагностику вашего здоровья.\n'
                   'Проба Руфье представляет собой нагрузочный комплекс, предназначенный для оценки работоспособности сердца \nпри физической нагрузке.\n'
                   'У испытуемого, находящегося в положении лёжа на спине в течение 5 мин, определяют частоту пульса за 15 секунд;\n'
                   'затем в течение 45 секунд испытуемый выполняет 30 приседаний.\n'
                   'После окончания нагрузки испытуемый ложится, и у него вновь подсчитывается число пульсаций за первые 15 секунд,\n'
                   'а потом — за последние 15 секунд первой минуты периода восстановления.\n\n'
                   '* Важно! Если в процессе проведения испытания вы почувствуете себя плохо (появится головокружение, шум в\n'
                   'ушах, сильная одышка и др.), то тест необходимо прервать и обратиться к врачу.' )
txt_title = 'Здоровье'
txt_name = 'Введите имя:'
txt_hintname = "имя"
txt_hintage = "0"
txt_test1 = '1) Лягте на спину и замерьте пульс за 15 секунд. Нажмите кнопку "Начать первый тест", чтобы запустить таймер.\nРезультат запишите в соответствующее поле.'
txt_test2 = '2) Выполните 30 приседаний за 45 секунд. Для этого нажмите кнопку "Начать делать приседания",\nчтобы запустить счётчик приседаний.'
txt_test3 = '3) Лягте на спину и замерьте пульс сначала за первые 15 секунд минуты, затем за последние 15 секунд.\nНажмите кнопку "Начать финальный тест", чтобы запустить таймер.\nКрасным обозначены секунды, в течение которых необходимо \nпроводить измерения, чёрным - секунды без замера пульсаций. Результаты запишите в соответствующие поля.'
txt_sendresults = 'Отправить результаты'
txt_hinttest1 = '0'
txt_hinttest2 = '0'
txt_hinttest3 = '0'
txt_starttest1 = 'Начать первый тест'
txt_starttest2 = 'Начать делать приседания'
txt_starttest3 = 'Начать финальный тест'
txt_timer = ''
txt_age = 'Полных лет:'
txt_finalwin = 'Результаты'
txt_index = 'Индекс Руфье: '
txt_workheart = 'Работоспособность сердца: '
txt_res1 = "низкая. Срочно обратитесь к врачу!"
txt_res2 = "удовлетворительная. Обратитесь к врачу!"
txt_res3 = "средняя. Возможно, стоит дополнительно \nобследоваться у врача."
txt_res4 = "выше среднего"
txt_res5 = "высокая"

fontTitle = QFont('Artegra Sans Extended Bold Italic', 20)
fontBtn = QFont('Artegra Sans Extended SemiBold Italic', 20)
fontText = QFont('Montserrat Medium', 11)
fontTimer = QFont('Helvetica Neue-Black Extended', 24)
fontError = QFont('Artegra Sans Extended Bold', 12)
fontFinal = QFont('Artegra Sans Extended SemiBold', 18)

btn_begin1_StyleSheet = '''
    #btn_begin1 {
    color: #fff;
    font-size: 22px;
    background-color: #DD9A11;
    border: none;
    border-radius: 6px;
    }

    #btn_begin1:hover {background-color: #DDAB43;}

    #btn_begin1:pressed {
    background-color: #8A8E95;
    }

    '''

btn_begin2_StyleSheet = '''
    #btn_begin2 {
    color: #fff;
    font-size: 22px;
    background-color: #DD9A11;
    border: none;
    border-radius: 6px;
    }

    #btn_begin2:hover {background-color: #DDAB43;}

    #btn_begin2:pressed {
    background-color: #8A8E95;
    }

    '''

btn_begin3_StyleSheet = '''
    #btn_begin3 {
    color: #fff;
    font-size: 22px;
    background-color: #DD9A11;
    border: none;
    border-radius: 6px;
    }

    #btn_begin3:hover {background-color: #DDAB43;}

    #btn_begin3:pressed {
    background-color: #8A8E95;
    }

    '''

btn_total_StyleSheet = '''
    #btn_total {
    color: #fff;
    font-size: 26px;
    background-color: #DD9A11;
    border: none;
    border-radius: 5px;
    }

    #btn_total:hover {background-color: #DDAB43;}

    #btn_total:pressed {
    background-color: #8A8E95;
    }

    '''

next_btn_StyleSheet = '''
    #next_btn {
    color: #fff;
    font-size: 32px;
    background-color: #DD9A11;
    border: none;
    border-radius: 6px;
    }

    #next_btn:hover {background-color: #DDAB43;}

    #next_btn:pressed {
    background-color: #8A8E95;
    }

    '''
