from random import shuffle
from typing import List
import os
import pyttsx3
import requests

list_questions =    [
                    {"question0": "¿Cuál de los siguientes acuerdos es un compromiso global para limitar el calentamiento?", "answers": ["Pacto de Ginebra", "Convenio de Toronto", "Tratado de Múnich"], "right": "Acuerdo de París"},
                    {"question1": "¿Qué ecosistema es más vulnerable al aumento de temperatura del océano?", "answers": ["Tundra ártica","Bosques templados", "Estepas"], "right": "Arrecifes de coral"},
                    {"question2": "¿Qué consecuencia genera el deshielo de los polos?", "answers": ["Disminución de la radiación solar", "Estabilización del clima", "Reducción de la evaporación del agua"], "right": "Aumento del nivel del mar"},
                    {"question3": "¿Qué acción ayuda a mitigar el cambio climático?", "answers": ["Deforestación para ampliar zonas agrícolas" ,"Expansión del uso de combustibles fósiles", "Incremento del transporte individual motorizado"], "right": "Reforestación y restauración de ecosistemas"},
                    {"question4": "¿Cuál de las siguientes es una energía renovable que ayuda a reducir emisiones?", "answers": ["Gas natural", "Carbón", "Petróleo"], "right": "Energía eólica"},
                    {"question5": "¿Cuál de los siguientes es un efecto asociado al calentamiento global?", "answers": ["Disminución de la temperatura media global", "Reducción del nivel del mar", "Mayor estabilidad climática"], "right": "Aumento en la frecuencia de fenómenos meteorológicos extremos"}
                    ]

meme_list = os.listdir('memes')

fact_list = ["El CO₂ permanece en la atmósfera por siglos",
             "El oceano absorbe la mayoria de CO₂",
             "El hielo del Ártico se está derritiendo a una velocidad que no se veía en al menos 1.000 años",
             "Las olas de calor marinas también existen",
             "Las plantas producen menos nutrientes esenciales bajo niveles altos de CO₂",
             "El nivel del mar está subiendo más rápido que en cualquier momento de los últimos 3.000 años",
             "El cambio climático está alterando sonidos naturales"]


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

