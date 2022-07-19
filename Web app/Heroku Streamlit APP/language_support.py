"""
File to support on language selection
"""


class PortugueseText:
    title = '# Predição da Probabilidade p/ Diabetes Tipo 2'
    autor = "Algoritmo e visualizações por [Magnun Nascimento](%s)."

    introduction_title = '## Introdução'
    introduction_text = """Calcula-se que 9,3% da população adulta mundial vive com diabetes, segundo a Federação 
                           Internacional de Diabetes (IDF), sendo o tipo 2 o mais comum com 90% desse número. A doença 
                           pode levar à óbito por eventos cardíacos ou cerebrais, além de outras comorbidades."""

    goal_title = '## Objetivo'
    goal_text = """Tem-se como objetivo conscientizar sobre os fatores críticos para o desenvolvimento da doença 
                   e estimular a adoção de hábitos mais saudáveis."""

    calculate_title = '## Calcule sua probabilidade!'
    no_yes_options = ['Não', 'Sim']
    gender_text = 'Gênero biológico'
    gender_options = ['Feminino', 'Masculino']
    smoker_text = 'Fuma frequentemente?'
    high_bp_text = 'Hipertenso(a)?'
    high_chol_text = 'Possui colesterol alto?'
    stroke_text = 'Já sofreu um AVC?'
    eat_text = 'Come frutas e vegetais frequentemente?'
    alchool_text = 'Ingere bebidas alcoólicas com frequência?'
    physic_text = 'Pratica atividades físicas regularmente?'
    diff_walk_text = 'Possui dificuldades para movimentação?'
    age_text = 'Idade'
    age_options = ('01 - Entre 18 e 24 anos',
                   '02 - Entre 25 e 29 anos',
                   '03 - Entre 30 e 34 anos',
                   '04 - Entre 35 e 39 anos',
                   '05 - Entre 40 e 44 anos',
                   '06 - Entre 45 e 49 anos',
                   '07 - Entre 50 e 54 anos',
                   '08 - Entre 55 e 59 anos',
                   '09 - Entre 60 e 64 anos',
                   '10 - Entre 65 e 69 anos',
                   '11 - Entre 70 e 74 anos',
                   '12 - Entre 75 e 79 anos',
                   '13 - 80 anos ou mais')
    dict_idades = {1.0: 'Entre 18 e 24 anos',
                   2: 'Entre 25 e 29 anos',
                   3: 'Entre 30 e 34 anos',
                   4: 'Entre 35 e 39 anos',
                   5: 'Entre 40 e 44 anos',
                   6: 'Entre 45 e 49 anos',
                   7: 'Entre 50 e 54 anos',
                   8: 'Entre 55 e 59 anos',
                   9: 'Entre 60 e 64 anos',
                   10: 'Entre 65 e 69 anos',
                   11: 'Entre 70 e 74 anos',
                   12: 'Entre 75 e 79 anos',
                   13: '80 anos ou mais'}

    height_text = 'Altura (m) *também é possivel digitar o valor'
    weight_text = 'Peso (Kg) *também é possivel digitar o valor'
    health_text = 'Como você classificaria sua saúde?'
    health_options = ('01 - Excelente',
                      '02 - Muito boa',
                      '03 - Boa',
                      '04 - Mediana',
                      '05 - Ruim')
    physhlth_text = 'Dos últimos 30 dias, quantos passou com problemas de saúde?'
    physhlth_options = ('01 - Nenhum',
                        '02 - De 1 a 5 dias',
                        '03 - De 6 a 10 dias',
                        '04 - De 11 a 15 dias',
                        '05 - De 16 a 20 dias',
                        '06 - Mais de 20 dias')
    calculate_btn_text = 'CALCULAR'
    calculate_text = '*Essa página não armazenará nenhum dado do usuário. \n \n Pode levar cerca de 1 min para executar'
    prob_title = '#### Sua probabilidade'
    prob_text = 'Baseado em suas informações, calcula-se uma probabilidade de:'
    good_habits_title = '#### Bons hábitos podem te ajudar!'
    good_habits_text = """Diversos fatores que favorecem o desenvolvimento da doença estão diretamente relacionados aos 
                          seus hábitos. Abaixo é apresentada a probabilidade de forma acumulada, assim considerar 
                          alteração da condição da linha em questão e das linhas acima."""
    vs_age_title = '#### Diabetes vs Idade'
    vs_age_text = """A probabilidade de desenvolvimento da doença é maior conforme ficamos mais velhos, assim como os 
                     cuidados com a nossa saúde ficam cada vez mais importantes. Veja o gráfico estimando a 
                     probabilidade ao longo dos seus próximos anos."""
    final_comments_title = '## Considerações do estudo'
    final_comments_text = """Esse é um projeto de estudo de ciência de dados, sua metodologia é aberta a todos e pode 
                             ser consultada [neste repositório do github](%s).\n \n Para o estudo foi utilizado 
                             [este dataset](%s), tendo como origem uma pesquisa realizada em 2018 pela The Behavioral 
                             Risk Factor Surveillance System (BRFSS), um sistema nacional estadunidense de pesquisas 
                             estatísticas da saúde no país. \n \n Por falta de dados da fonte, alguns fatores críticos 
                             para a doença não foram considerados, como o fator genético e maiores detalhes sobre a 
                             alimentação. Por esse e outros motivos, este material não deve ser utilizado como 
                             diagnóstico médico."""
    new_prob_text = 'Nova probabilidade (%)'
    suggestions_text = 'Sugestões'
    current_habits_text = 'Hábitos atuais'
    better_habits_text = 'Hábitos melhores'
    dict_age_ranges = {1.0: 'Entre 18 e 24 anos',
                   2: 'Entre 25 e 29 anos',
                   3: 'Entre 30 e 34 anos',
                   4: 'Entre 35 e 39 anos',
                   5: 'Entre 40 e 44 anos',
                   6: 'Entre 45 e 49 anos',
                   7: 'Entre 50 e 54 anos',
                   8: 'Entre 55 e 59 anos',
                   9: 'Entre 60 e 64 anos',
                   10: 'Entre 65 e 69 anos',
                   11: 'Entre 70 e 74 anos',
                   12: 'Entre 75 e 79 anos',
                   13: 'Mais de 80 anos'}
    weight_advice = 'Atinja peso para IMC ideal'
    cholesterol_advice = 'Controle o colesterol'
    smoker_advice = 'Pare de fumar'
    exercises_advice = 'Faça atividades físicas regularmente'
    eat_advice = 'Coma frutas e vegetais'



class EnglishText:
    title = '# Type 2 Diabetes Predictor'
    autor = 'Algorithm and visualization by [Magnun Nascimento](%s).'
    introduction_title = '## Introduction'
    introduction_text = """According to the International Federation of Diabetes (IDF) It is estimated that 9.3% of the 
                           world's adult population has diabetes, type 2 is the most common with 90% of this number. 
                           This disease can lead to death caused by cardiac events or brain issues and it can also require 
                           some drastic life style changes."""
    goal_title = '## Goal'
    goal_text = """This project's goal is to make people aware of the main risk factors for Type 2 Diabetes and encourage 
                   them having better habits."""
    calculate_title = '## Check your probability!'
    no_yes_options = ['No', 'Yes']
    gender_text = 'Assigned sex at birth:'
    gender_options = ['Female', 'Male']
    smoker_text = 'Are you a smoker?'
    high_bp_text = 'Dou you have high blood pressure?'
    high_chol_text = 'Dou you have high cholesterol?'
    stroke_text = 'Have you ever had a stroke?'
    eat_text = 'Do you eat fruits and vegetables often?'
    alchool_text = 'Do you drink alcohol often?'
    physic_text = 'Do you exercise regularly?'
    diff_walk_text = 'Do you have any movement disorder?'
    age_text = 'Age'
    age_options = ('01 - From 18 to 24 years old',
                   '02 - From 25 to 29 years old',
                   '03 - From 30 to 34 years old',
                   '04 - From 35 to 39 years old',
                   '05 - From 40 to 44 years old',
                   '06 - From 45 to 49 years old',
                   '07 - From 50 to 54 years old',
                   '08 - From 55 to 59 years old',
                   '09 - From 60 to 64 years old',
                   '10 - From 65 to 69 years old',
                   '11 - From 70 to 74 years old',
                   '12 - From 75 to 79 years old',
                   '13 - 80 years old or more')
    dict_idades = {1.0: 'From 18 to 24 years old',
                   2: 'From 25 to 29 years old',
                   3: 'From 30 to 34 years old',
                   4: 'From 35 to 39 years old',
                   5: 'From 40 to 44 years old',
                   6: 'From 45 to 49 years old',
                   7: 'From 50 to 54 years old',
                   8: 'From 55 to 59 years old',
                   9: 'From 60 to 64 years old',
                   10: 'From 65 to 69 years old',
                   11: 'From 70 to 74 years old',
                   12: 'From 75 to 79 years old',
                   13: '80 years old or more'}
    height_text = 'Height (m) *também é possivel digitar o valor'
    weight_text = 'Peso (Kg) *também é possivel digitar o valor'
    health_text = 'How would you rate your health?'
    health_options = ('01 - Great',
                      '02 - Very good',
                      '03 - Good',
                      '04 - Ordinary',
                      '05 - Bad')
    physhlth_text = 'From the last 30 days, how many of them were you sick?'
    physhlth_options = ('01 - None',
                        '02 - From 1 to 5 days',
                        '03 - From 6 to 10 days',
                        '04 - From 11 to 15 days',
                        '05 - From 16 to 20 days',
                        '06 - More than 20 days')

    calculate_btn_text = 'CALCULATE'
    calculate_text = "*This page does not store any user's data. \n \n  It can take about a minute to run."
    prob_title = '#### Your probability'
    prob_text = 'Based on these data, the calculated probability is:'
    good_habits_title = '#### Better habits can help you!'
    good_habits_text = """Many risk factors are associated with your lifestyle. You can see in the table below the 
                          cumulative impact of some habit changes."""
    vs_age_title = '#### Diabetes vs age'
    vs_age_text = """The probability increases as we get older, thus caring for our own health becomes more important.
                     Take a look at your life-long projection."""
    final_comments_title = '## Concluding remarks'
    final_comments_text = """This is a data science project, you can check its methodology on this 
                             [github repository](%s).\n \n It's based on [this dataset](%s), with data from 2018 by 
                             The Behavioral Risk Factor Surveillance System (BRFSS), a state-based system of 
                             telephone health surveys that collects information on health risk behaviors and preventive 
                             health practices. \n \n Due to lack of data from the surveillance, some critical factors 
                             may not have been considered, such as more detailed feed habits and genetics factors. 
                             This project should not be used as a medical diagnostic."""
    new_prob_text = 'New probability (%)'
    suggestions_text = 'Suggestions'
    current_habits_text = 'Current habits'
    better_habits_text = 'Better habits'
    dict_age_ranges = {1.0: 'From 18 to 24 years old',
                   2: 'From 25 to 29 years old',
                   3: 'From 30 to 34 years old',
                   4: 'From 35 to 39 years old',
                   5: 'From 40 to 44 years old',
                   6: 'From 45 to 49 years old',
                   7: 'From 50 to 54 years old',
                   8: 'From 55 to 59 years old',
                   9: 'From 60 to 64 years old',
                   10: 'From 65 to 69 years old',
                   11: 'From 70 to 74 years old',
                   12: 'From 75 to 79 years old',
                   13: '80 years old or more'}
    weight_advice = 'Reach weight for ideal BMI'
    cholesterol_advice = 'Lower your cholesterol'
    smoker_advice = 'Stop smoking'
    exercises_advice = 'Exercise regularly'
    eat_advice = 'Eat fruits and vegetables'



# Dict to help associate the language select in streamlit with the correct class
lang_dict = {'English 🇺🇸': EnglishText,
             'Português 🇧🇷': PortugueseText}
