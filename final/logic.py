from random import shuffle
from typing import List
import os

list_questions =    [
                    {"question0": "¿Cuál de los siguientes acuerdos es un compromiso global para limitar el calentamiento?", "answers": ["Pacto de Ginebra", "Convenio de Toronto", "Tratado de Múnich"], "right": "Acuerdo de París"},
                    {"question1": "¿Qué ecosistema es más vulnerable al aumento de temperatura del océano?", "answers": ["Tundra ártica","Bosques templados", "Estepas"], "right": "Arrecifes de coral"},
                    {"question2": "¿Qué consecuencia genera el deshielo de los polos?", "answers": ["Disminución de la radiación solar", "Estabilización del clima", "Reducción de la evaporación del agua"], "right": "Aumento del nivel del mar"},
                    {"question3": "¿Qué acción ayuda a mitigar el cambio climático?", "answers": ["Deforestación para ampliar zonas agrícolas" ,"Expansión del uso de combustibles fósiles", "Incremento del transporte individual motorizado"], "right": "Reforestación y restauración de ecosistemas"},
                    {"question4": "¿Cuál de las siguientes es una energía renovable que ayuda a reducir emisiones?", "answers": ["Gas natural", "Carbón", "Petróleo"], "right": "Energía eólica"},
                    {"question5": "¿Cuál de los siguientes es un efecto asociado al calentamiento global?", "answers": ["Disminución de la temperatura media global", "Reducción del nivel del mar", "Mayor estabilidad climática"], "right": "Aumento en la frecuencia de fenómenos meteorológicos extremos"}
                    ]

meme_list = os.listdir('memes')

fact_list = ["",
             "",
             "",
             "",
             "",
             "",
             ""]


def get_question(num_Question):
    ind = f"question{num_Question}"

    return list_questions[num_Question][ind]


def get_answers(num_Question) -> List[str]:
    answers = list_questions[num_Question]["answers"]
    answers.append(list_questions[num_Question]["right"])
    shuffle(answers)

    return answers


def get_right_ans(num_Question):
    return list_questions[num_Question]["right"]

