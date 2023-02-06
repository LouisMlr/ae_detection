import uvicorn
from fastapi import FastAPI
import openai
from classes import Settings, EntitiesOut

settings = Settings()

app = FastAPI()

openai.api_key = settings.OPENAI_API_KEY


@app.get("/")
def home():
    return {"message": "Hello World"}


@app.post("/detection", response_model=EntitiesOut)
def detection(text_message: str):

    response = openai.Completion.create(
        model="text-davinci-003",
        #model="text-curie-001",
        prompt=entity_detection(text_message),
        temperature=0.2,
    )
        
    return {
        "input_text": text_message, 
        "entities": response.choices[0].text,
        #"api": openai.api_key
           }


@app.post("/detection_v2", response_model=EntitiesOut)
def classification(text_message: str):

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=entity_detection_v2(text_message),
        temperature=0.2,
    )
        
    return {
        "input_text": text_message, 
        "entities": response.choices[0].text,
           }


@app.post("/test")
def test(text_message: str):
        
    return {
            "input_text": text_message, 
            "entities":  "mal de ventre",
           }


def entity_detection(patient_input):
    return """Detect the adverse effect entities in the text.

Text: J'ai un peu mal à la tête depuis hier 
Effet secondaire: mal à la tête
Text: Je me sens fiévreux et j'ai quelques courbatures
Effet secondaire: fiévreux - courbatures
Text: J'ai des nausés et des chutes de cheveux
Effet secondaire: nausés - chutes de cheveux
Text: {}
Effet(s) secondaire(s): """.format(
        patient_input.capitalize()
    )


def entity_detection_v2(patient_input):
    return """Détecte les effets secondaires liés aux traitements contre le cancer

Text: J'ai mal à la gorge quand je mange et j'ai de plus en plus d'aphtes
Effet: Mucite
Text: J'ai remarqué des tâches sur mes mains depuis 3 jours. J'ai cependant retrouvé l'appétit
Effet: Hyperpigmentation
Text: J'ai remarqué que mes pieds étaient rouges et aussi des cloques sous mon pied droit
Effet: Syndrôme Main-Pied
Text: J'ai pris mes médicament sans problème depuis 2 semaines
Effet: Aucun
Text: Je me sens fiévreux et j'ai quelques courbatures
Effet: Fièvre - Douleurs musculaires
Text: J'ai du mal à me tenir debout depuis hier et j'ai le visage rouge avec de l'acné
Effet: Fatigue - Éruptions cutanées
Text: J'ai perdu quelques méches de cheveux dans la douche ainsi que des cils
Effet: Chute des cheveux
Text: J'ai vomis toute la nuit
Effet: Troubles digestifs
Text: J'ai le coeur qui s'accélère depuis vendredi soir
Effet: Troubles cardiaques
Text: J'ai un décalage de 7 jours dans mon cycle menstruel
Effet: Troubles du cycle menstruel
Text: Je n'ai pas beaucoup de force comparé à la semaine dernière. Mon ongle du pouce gauche noirci
Effet(s) secondaire(s): Fatigue - Troubles au niveau des ongles
Text: {}
Effet(s) secondaire(s): """.format(
        patient_input.capitalize()
    )


if __name__ == '__main__':
    uvicorn.run(app)

