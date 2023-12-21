import streamlit as st
import openai
import os

#from transformers import pipeline

#openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = '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'

# Define the available joke types
joke_types = {
    "Pun": "pun",
    "One-liner": "one_liner",
    "Haiku": "haiku"
}

# Define the available joke settings
joke_settings = {
    "For Kids": "kids",
    "For Adults": "adults",
    "For Old people": "old_people",
}

# Define the available joke settings
joke_subjects = {
    "Science": "science",
    "Politics": "politics",
    "Hollywood": "hollywood",
}

#generator = pipeline('text-generation', model='gpt2')

# Streamlit app
def main():
    st.title("Would you like to hear a joke?")
    
    # Select joke type
    joke_type = st.selectbox("Select joke type:", list(joke_types.keys()))

    # Select joke subject
    joke_subject= st.selectbox("Select joke subject:", list(joke_subjects.keys()))

    # Select joke settings
    joke_setting = st.selectbox("Select joke setting:", list(joke_settings.keys()))

    # Generate joke button
    if st.button("Generate Joke"):
        # Construct the prompt based on user's selection
        prompt = f"Generate a {joke_types[joke_type]} joke that is about {joke_subjects[joke_subject]} and is for {joke_settings[joke_setting]}."
        # Call GPT-3 or other LLM to generate the joke response
        joke_response = generate_joke(prompt)

        # Display the joke response
        st.write(joke_response)

# Function to generate joke using GPT-3 or other LLM
def generate_joke(prompt):
    #results = generator(prompt, max_length=100, num_return_sequences=1, temperature=0.9)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # You can choose your desired model here
        messages=[
            {"role": "system", "content": "You are a irreverent comedian. You are going to tell a joke and make it funny"},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.8,
        #stop=["\n"]
    )
    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    main()
