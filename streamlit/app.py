import streamlit as st
import requests

def request_openai_detection(user_input: str) -> str:
    """This function requests the /detection API to detect the adverse
    effect entities from an input text.

    Args:
        user_input (str): patient input

    Returns:
        str: adverse effects detected
    """
    model_ouput = requests.post(
        url=f"http://fastapi:80/detection?text_message={user_input}"
        )
    # extract entities from output
    return model_ouput.json()['entities']


def request_openai_classification(user_input: str) -> str:
    model_ouput = requests.post(
        url=f"http://fastapi:80/classification?text_message={user_input}"
        )
    # extract entities from output
    return model_ouput.json()['entities']


# Application Title
st.title("Détection des Effets Secondaires")

# Text Input
user_input = st.text_input("Avez-vous des symptômes particuliers ?")

# [Button] Submit
if st.button("Submit", type="primary"):
    model_detection_ouput = request_openai_detection(user_input)
    # model_classification_ouput = request_openai_classification(user_input)

    st.success("Détection des effets secondaires : " + model_detection_ouput)
    # st.success("Classification des effets secondaires : " + model_classification_ouput)

# [Button] Clear
if st.button("Clear"):
    user_input = ""

