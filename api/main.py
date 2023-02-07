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
        prompt=entity_detection_simple(text_message),
        temperature=0.2,
        max_tokens=30
    )
        
    return {
        "input_text": text_message, 
        "entities": response.choices[0].text,
        #"api": openai.api_key
           }


@app.post("/detection_finetuned", response_model=EntitiesOut)
def detection_finetuned(text_message: str):

    response = openai.Completion.create(
        model="davinci:ft-personal-2023-02-07-13-34-24",
        prompt=f"""{text_message} ->""",
        stop=["\n"],
        temperature=0.2,
        max_tokens=30
    )
        
    return {
        "input_text": text_message, 
        "entities": response.choices[0].text,
           }


@app.post("/detection_finetuned_v2", response_model=EntitiesOut)
def detection_finetuned_v2(text_message: str):

    response = openai.Completion.create(
        model="davinci:ft-personal-2023-02-07-16-40-56",
        prompt=f"""{text_message} \n\n###\n\n""",
        stop=[" END"],
        temperature=0.2,
        max_tokens=30
    )
        
    return {
        "input_text": text_message, 
        "entities": response.choices[0].text,
           }

@app.post("/test")
def test(text_message: str):
        
    return {
            "input_text": text_message, 
            "entities":  "Fatigue",
           }


def entity_detection_simple(patient_input):
    """
    Try the entities extraction without fine tuning: few-shot learning approach
    """
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
Text: Je n'ai pas beaucoup de force comparé à la semaine dernière. Mon ongle du pouce gauche noirci
Effet: Fatigue - Troubles au niveau des ongles
Text: J'ai vomis toute la nuit
Effet: Troubles digestifs
Text: J'ai le coeur qui s'accélère depuis vendredi soir
Effet: Troubles cardiaques
Text: J'ai un décalage de 7 jours dans mon cycle menstruel
Effet: Troubles du cycle menstruel
Text: {}
Effet: """.format(
        patient_input.capitalize()
    )


if __name__ == '__main__':
    uvicorn.run(app)


