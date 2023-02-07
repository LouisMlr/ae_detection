import streamlit as st
import requests


def request_openai_detection_simple(user_input: str) -> str:
    """This function requests the /detection API to detect the adverse
    effect entities from an input text.

    Args:
        user_input (str): patient input

    Returns:
        str: adverse effects detected
    """
    model_ouput = requests.post(
        url=f"http://fastapi:8000/detection?text_message={user_input}"
        )
    # extract entities from output
    return model_ouput.json()['entities']


def request_openai_detection_finetuned(user_input: str) -> str:
    """This function requests the /detection_finetuned API to detect the adverse
    effect entities from an input text. This model has been fine tuned on 100 examples.

    Args:
        user_input (str): patient input

    Returns:
        str: adverse effects detected
    """
    model_ouput = requests.post(
        url=f"http://fastapi:8000/detection_finetuned?text_message={user_input}"
        )
    # extract entities from output
    return ' - '.join(model_ouput.json()['entities'].split('\n-'))


# Application Title
st.title("Détection des Effets Secondaires")

# Text Input
user_input = st.text_area("Avez-vous des symptômes particuliers ?", max_chars=350)

# [Button] Submit
if st.button("Submit", type="primary"):
    # Request models
    model_detection_ouput_simple = request_openai_detection_simple(user_input)
    model_detection_ouput_finetuned = request_openai_detection_finetuned(user_input)

    # Display model outputs
    st.write("Détection des effets secondaires : ")
    st.success(f"Model 1: {model_detection_ouput_simple}")
    st.success(f"Model 2: {model_detection_ouput_finetuned}")

# [Button] Clear
if st.button("Clear"):
    user_input = ""
    st.write()
