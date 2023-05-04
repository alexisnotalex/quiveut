from guizero import App, Text, PushButton, Box
import csv
import random

# Initialisation de l'interface utilisateur
# Initialisation des variables
score = 0
question_actuelle = 0

# Chargement des questions et des réponses depuis le fichier CSV
questions = []
with open('questions.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        questions.append({'question': row[0], 'reponses': row[1:], 'correcte': row[1]})



# Fonction pour charger la prochaine question
def charger_question():
    global question_actuelle
    question_actuelle += 1
    if question_actuelle >= len(questions):
        question_label.value = 'Vous avez gagné {} € !'.format(score)
        suivant_button.disable()
        return
    question = questions[question_actuelle]
    question_label.value = question['question']
    reponses = question['reponses']
    random.shuffle(reponses)
    for i, reponse in enumerate(reponses):
        button = PushButton(reponses_box, text=reponse, command=lambda r=reponse: verifier_reponse(r, question['correcte']), grid=[0, i])
    suivant_button.disable()

# Fonction pour vérifier si la réponse est correcte et mettre à jour le score
def verifier_reponse(reponse, correcte):
    global score
    if reponse == correcte:
        score += 1000
        score_label.value = 'Score: {} €'.format(score)
        suivant_button.enable()
    else:
        question_label.value = 'Désolé, la réponse correcte était "{}".'.format(correcte)
        suivant_button.enable()

# Configuration de la première question
charger_question()

# Affichage de l'interface utilisateur
app = App(title='Qui veut gagner des millions', width=600, height=400)
score_label = Text(app, text='Score: 0 €', size=20, font='Helvetica', color='green')
question_label = Text(app, text='Question', size=20, font='Helvetica', color='black', align='top')
reponses_box = Box(app, layout='grid')
suivant_button = PushButton(app, text='Suivant', command=charger_question, enabled=False)

app.display()
