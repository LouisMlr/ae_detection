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
        #model="text-davinci-003",
        model="text-curie-001",
        prompt=entity_detection(text_message),
        temperature=0.3,
    )
        
    return {
        "input_text": text_message, 
        "entities": response.choices[0].text,
        #"api": openai.api_key
           }


@app.post("/classification", response_model=EntitiesOut)
def classification(text_message: str):

    response = openai.Completion.create(
        #model="text-davinci-003",
        model="text-curie-001",
        prompt=entity_classification(text_message),
        temperature=0.3,
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
Effet(s) secondaire(s): mal à la tête
Text: Je me sens fiévreux et j'ai quelques courbatures
Effet(s) secondaire(s): fiévreux - courbatures
Text: J'ai des nausés et des chutes de cheveux
Effet(s) secondaire(s): nausés - chutes de cheveux
Text: {}
Effet(s) secondaire(s): """.format(
        patient_input.capitalize()
    )


def entity_classification(patient_input):
    return """Détecte les mentions d'effets secondaires dans le texte parmis la liste suivante : aucun, Fièvre, Sensations d’engourdissement ou de fourmillement dans les mains ou les pieds, Douleurs musculaires et articulaires, Troubles cutanés, Chute des cheveux, Nausées et vomissements, Troubles cardiaques, Troubles du cycle menstruel, Fatigue, Autres effets secondaires)

Text: J'ai un peu mal à la tête depuis hier 
Effet(s) secondaire(s): Fièvre
Text: J'ai des foumis dans les doigts de la main
Effet(s) secondaire(s): Sensations d’engourdissement ou de fourmillement
Text: J'ai pris mes médicament sans problème depuis 2 semaines
Effet(s) secondaire(s): aucun
Text: Je me sens fiévreux et j'ai quelques courbatures
Effet(s) secondaire(s): Fièvre - Douleurs musculaires et articulaires
Text: Je me sens faible depuis hier j'ai le visage rouge
Effet(s) secondaire(s): Troubles cutanés
Text: J'ai perdu quelques méches de cheveux au réveil
Effet(s) secondaire(s): Chute des cheveux
Text: J'ai vomis toute la nuit
Effet(s) secondaire(s): Nausées et vomissements
Text: J'ai le coeur qui s'accélère depuis vendredi soir
Effet(s) secondaire(s): Troubles cardiaques
Text: J'ai un décalage dans mon cycle menstruel
Effet(s) secondaire(s): Troubles du cycle menstruel
Text: Je n'ai pas beaucoup de force comparé à la semaine dernière
Effet(s) secondaire(s): Fatigue
Text: {}
Effet(s) secondaire(s): """.format(
        patient_input.capitalize()
    )


if __name__ == '__main__':
    uvicorn.run(app)

