# Imports and config
# =================================================================

import json
import language_support as lang
import pandas as pd
import plotly.express as px
import requests
import streamlit as st


# Streamlit Config
st.set_page_config(layout='wide')
st.cache(allow_output_mutation=True)

# =================================================================
# Language Selector
# =================================================================

selected_page = st.sidebar.selectbox('Select your language | Selecione seu idioma:', ('English 🇺🇸', 'Português 🇧🇷'))
sel_lang = lang.lang_dict.get(selected_page)

# =================================================================
# API Config
# =================================================================

# url = 'http://0.0.0.0:5000/diabetes/diabetes_predict' #Only for local test
url = 'https://diabetes-predict-ptbr1.herokuapp.com/diabetes/diabetes_predict'
header = {'Content-type': 'application/json'}


# =================================================================
# Funções de apoio
# =================================================================


def scenarios_otimizados(df):
    """Creates a dataframe to simulate the probability if the user improves some factors
    Args:
        df: Dataframe created from user's data

    Returns:
        df: New dataframe with better habits scenarios
        d: Dictionary with better habits sugestions
        scenarios: Number of better habits sugestions
    """

    scenarios = 0
    d = {}

    # Weight control
    if df[2].iloc[0] >= 30:
        scenarios = scenarios + 1
        df = df.append(df.iloc[scenarios - 1])
        df[2].iloc[scenarios] = 24.9
        d[scenarios] = sel_lang.weight_advice

    # Coholesterol control
    if df[1].iloc[0] == 1:
        scenarios = scenarios + 1
        df = df.append(df.iloc[scenarios - 1])
        df[1].iloc[scenarios] = 0
        d[scenarios] = sel_lang.cholesterol_advice

    # Stops smoking
    if df[3].iloc[0] == 1:
        scenarios = scenarios + 1
        df = df.append(df.iloc[scenarios - 1])
        df[3].iloc[scenarios] = 0
        d[scenarios] = sel_lang.smoker_advice

    # Exercises
    if df[5].iloc[0] == 0:
        scenarios = scenarios + 1
        df = df.append(df.iloc[scenarios - 1])
        df[5].iloc[scenarios] = 1
        d[scenarios] = sel_lang.exercises_advice

    # Eat better
    if df[11].iloc[0] == 0:
        scenarios = scenarios + 1
        df = df.append(df.iloc[scenarios - 1])
        df[5].iloc[scenarios] = 1
        d[scenarios] = sel_lang.eat_advice

    return df, d, scenarios


def age_scenario(df):
    """Creates a dataframe to simulate the probability for all next age ranges
    Args:
        df: Dataframe created from user's data

    Returns:
        df_ages: New dataframe with next age ranges scenarios
    """
    df_ages = df.iloc[[0]]
    idade_atual = df[10].iloc[0]
    loop_times = 0

    for cenario in range(int(idade_atual + 1), 14):
        loop_times = loop_times + 1
        df_ages = df_ages.append(df_ages.iloc[[0]])
        df_ages[10].iloc[loop_times] = cenario

    return df_ages


def age_opt_scenarios(df, scenarios):
    """Creates a dataframe to simulate the probability for all next age ranges and better habits
    Args:
        df: Dataframe created from user's data
        scenarios: Number of better habits sugestions

    Returns:
        df_ages_opt: New dataframe with next age ranges scenarios and better habits
    """
    # st.dataframe(df)
    df_ages_opt = df.iloc[[scenarios]]
    idade_atual = df[10].iloc[0]
    loop_times = 0

    for scenario in range(int(idade_atual + 1), 14):
        loop_times = loop_times + 1
        df_ages_opt = df_ages_opt.append(df_ages_opt.iloc[[0]])
        df_ages_opt[10].iloc[loop_times] = scenario

    return df_ages_opt


def call_api(df):
    """Call API with ML that predictis diabetes probability from a dataframe
    Args:
        df: Dataframe created from user's data

    Returns:
        df_pred: New dataframe with diabetes probability
    """
    data_json_pred_df = json.dumps(df.to_dict(orient='records'))

    r = requests.post(url, data=data_json_pred_df, headers=header)
    df_pred = pd.DataFrame(r.json(), columns=r.json()[0].keys())

    return df_pred


# =================================================================
# Page Build
# =================================================================

# Url Links
magnun_url = "https://www.linkedin.com/in/magnun-nascimento-a5bab381/"
github_url = "https://github.com/magnunn/diabetes_pred"
dataset_url = "https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset"

# Header
st.markdown(sel_lang.title)
st.write(sel_lang.autor % magnun_url)
st.markdown('---')

# Introduction
st.markdown(sel_lang.introduction_title)
st.write(sel_lang.introduction_text)

# Goal
st.markdown(sel_lang.goal_title)
st.write(sel_lang.goal_text)

# Calculator
st.markdown(sel_lang.calculate_title)
c1, c2, c3, c4 = st.columns(4)
with c1:
    gender_rad = st.radio(sel_lang.gender_text,
                          sel_lang.gender_options,
                          horizontal=True)

with c2:
    smoker_rad = st.radio(sel_lang.smoker_text,
                          sel_lang.no_yes_options,
                          horizontal=True)

with c3:
    high_bp_rad = st.radio(sel_lang.high_bp_text,
                           sel_lang.no_yes_options,
                           horizontal=True)

with c4:
    high_chol_rad = st.radio(sel_lang.high_chol_text,
                             sel_lang.no_yes_options,
                             horizontal=True)

c5, c6, c7, c8 = st.columns(4)
with c5:
    avc_rad = st.radio(sel_lang.stroke_text,
                       sel_lang.no_yes_options,
                       horizontal=True)

with c6:
    eat_rad = st.radio(sel_lang.eat_text,
                       sel_lang.no_yes_options,
                       horizontal=True)

with c7:
    alchool_rad = st.radio(sel_lang.alchool_text,
                           sel_lang.no_yes_options,
                           horizontal=True)

with c8:
    physic_rad = st.radio(sel_lang.physic_text,
                          sel_lang.no_yes_options,
                          horizontal=True)

c9, c10, c11, c12 = st.columns(4)
with c9:
    walk_rad = st.radio(sel_lang.diff_walk_text,
                        sel_lang.no_yes_options,
                        horizontal=True)

c13, c14, c15 = st.columns(3)
with c13:
    age_sel = st.selectbox(sel_lang.age_text, sel_lang.age_options)


with c14:
    #st.write(sel_lang)
    if sel_lang == lang.EnglishText:
        altura_input = st.number_input('Height (ft)',
                                       min_value=1, max_value=9,
                                       step=1)
    else:
        altura_input = st.number_input('Altura (m)',
                               min_value=0.5, max_value=3.0,
                               step=0.01, format="%.2f")

with c15:
    if sel_lang == lang.EnglishText:
        altura_input2 = st.number_input('Height (inch)',
                                       min_value=0.1, max_value=12.0,
                                       step=0.1, format="%.1f")

c16, c17, c18 = st.columns(3)
with c16:
    if sel_lang == lang.EnglishText:
        peso_input = st.number_input("Weight (pounds)",
                                     min_value=60.0, max_value=450.0,
                                     step=0.1, format="%.1f")
    else:
        peso_input = st.number_input("Peso (Kg)",
                             min_value=30.0, max_value=300.0,
                             step=0.1, format="%.1f")

with c17:
    health_sel = st.selectbox(sel_lang.health_text, sel_lang.health_options)
with c18:
    PhysHlth_sel = st.selectbox(sel_lang.physhlth_text, sel_lang.physhlth_options)

calculate_btn = st.button(sel_lang.calculate_btn_text)
st.write(sel_lang.calculate_text)

if calculate_btn:
    # Calculate BMI
    if sel_lang == lang.EnglishText:
        BMI = 703 * peso_input / (((altura_input * 12) + altura_input2)*((altura_input * 12) + altura_input2))

    else:
        BMI = peso_input / (altura_input * altura_input)

    # Get inputed data
    raw_list = [high_bp_rad, high_chol_rad, BMI, smoker_rad, avc_rad, physic_rad,
                alchool_rad, int(health_sel[0:2]), walk_rad, gender_rad, int(age_sel[0:2]), eat_rad,
                int(PhysHlth_sel[0:2])]

    # Convert yes/no and gender to number according to ML
    for i, n in enumerate(raw_list):
        if (n == "Não") or (n == "No") or (n == "Feminino") or (n == "Female"):
            raw_list[i] = 0
        if (n == "Sim") or (n == "Yes") or (n == "Masculino") or (n == "Male"):
            raw_list[i] = 1

    # Call API with user's data
    df = pd.DataFrame(raw_list).T
    df_pred_user = call_api(df)

    st.markdown(sel_lang.prob_title)
    st.write(sel_lang.prob_text)

    st.write("{0:.2%}".format(df_pred_user.loc[0, 'probabilidade']))

    # Call API for optimized scenarios
    df_otimizados, dict_sugestoes, num_sugestoes = scenarios_otimizados(df)
    if num_sugestoes >= 1:
        df_pred_user_opt = call_api(df_otimizados)

        st.markdown(sel_lang.good_habits_title)
        st.write(sel_lang.good_habits_text)
        df_pred_user_opt = df_pred_user_opt.rename(columns={'probabilidade': sel_lang.new_prob_text})
        df_pred_user_opt[sel_lang.new_prob_text] = df_pred_user_opt[sel_lang.new_prob_text] * 100
        df_pred_user_opt.drop([0], axis=0, inplace=True)
        df_pred_user_opt[sel_lang.suggestions_text] = pd.Series(dict_sugestoes)
        st.dataframe(df_pred_user_opt[[sel_lang.suggestions_text, sel_lang.new_prob_text]])

    # Life long prediction
    if int(age_sel[0:2]) < 13:
        st.markdown(sel_lang.vs_age_title)
        st.write(sel_lang.vs_age_text)
        df_age = age_scenario(df)
        df_pred_age = call_api(df_age)
        # Renaming columns and age range to help chart understanding
        df_pred_age = df_pred_age.rename(columns={'probabilidade': sel_lang.current_habits_text})
        df_pred_age = df_pred_age.rename(columns={'10': 'Age'})
        df_pred_age[sel_lang.current_habits_text] = df_pred_age[sel_lang.current_habits_text] * 100
        df_pred_age = df_pred_age.set_index('Age')
        df_pred_age = df_pred_age.reindex(df_pred_age.index.union(sel_lang.dict_age_ranges.values(), sort=False)).rename_axis(
            'Age').reset_index()
        df_pred_age['Age'] = df_pred_age['Age'].map(sel_lang.dict_age_ranges)
        df_pred_age['Age'] = df_pred_age['Age'].astype("string")

        # If there is at least one better habit suggestion
        if num_sugestoes >= 1:
            df_age_otimizado = age_opt_scenarios(df_otimizados, num_sugestoes)
            df_pred_age_opt = call_api(df_age_otimizado)
            df_pred_age[sel_lang.better_habits_text] = df_pred_age_opt['probabilidade'] * 100
            fig = px.line(df_pred_age, x='Age', y=[sel_lang.current_habits_text, sel_lang.better_habits_text], title=None, markers=True)

        else:
            fig = px.line(df_pred_age, x='Age', y=sel_lang.current_habits_text, title=None, markers=True)

        df_pred_age = df_pred_age.dropna()

        # Chart Config
        fig.update_layout(
            xaxis=dict(
                showline=True,
                showgrid=True,
                linecolor='rgb(204, 204, 204)',
                linewidth=6,
                title=None,
                ticks='outside',
                tickfont=dict(
                    family='Arial',
                    size=12,
                    color='rgb(82, 82, 82)',
                ),
            ),
            yaxis=dict(
                showgrid=True,
                zeroline=False,
                showline=True,
                showticklabels=True,
                ticksuffix="%",
                title=None
            ),
            legend=dict(
                title=None,
                orientation="v",
                y=1,
                yanchor="bottom",
                x=0.5,
                xanchor="center",
            ),
            margin=dict(
                autoexpand=True
            )
        )

        st.plotly_chart(fig, use_container_width=True)

    # Remarks
    st.markdown(sel_lang.final_comments_title)
    st.write(sel_lang.final_comments_text % (github_url, dataset_url))
