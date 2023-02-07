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
    effect entities from an input text.

    Args:
        user_input (str): patient input

    Returns:
        str: adverse effects detected
    """
    model_ouput = requests.post(
        url=f"http://fastapi:8000/detection_finetuned?text_message={user_input}"
        )
    # extract entities from output
    return model_ouput.json()['entities']

def request_openai_detection_finetuned_v2(user_input: str) -> str:
    """This function requests the /detection_finetuned_v2 API to detect the adverse
    effect entities from an input text.

    Args:
        user_input (str): patient input

    Returns:
        str: adverse effects detected
    """
    model_ouput = requests.post(
        url=f"http://fastapi:8000/detection_finetuned_v2?text_message={user_input}"
        )
    # extract entities from output
    return model_ouput.json()['entities']

# Application Title
st.title("Détection des Effets Secondaires")

# Text Input
user_input = st.text_area("Avez-vous des symptômes particuliers ?", max_chars=350)

# [Button] Submit
if st.button("Submit", type="primary"):
    model_detection_ouput_v2 = request_openai_detection_simple(user_input)
    model_detection_ouput_finetuned = request_openai_detection_finetuned(user_input)
    model_detection_ouput_finetuned_v2 = request_openai_detection_finetuned_v2(' - '.join(user_input.split('\n')))

    st.write("Détection des effets secondaires : ")
    st.success(model_detection_ouput_v2)
    st.success(model_detection_ouput_finetuned)
    st.success(model_detection_ouput_finetuned_v2)

# [Button] Clear
if st.button("Clear"):
    user_input = ""
    st.write()
    


