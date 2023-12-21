import streamlit as st
import openai
import urllib.parse
import webbrowser
import streamlit.components.v1 as components
import os

#from transformers import pipeline

#openai.api_key = os.getenv("OPENAI_API_KEY")
#openai.api_key = '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'
openai.api_key = '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'
# Define the available joke types
joke_types = {
    "Pun": "pun",
    "One-liner": "one_liner",
    "Haiku": "haiku",
    "Short story": "short_story",
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
    "Food": "food",
    "Sports": "sports",
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
    joke_setting = st.selectbox("Select joke rating:", list(joke_settings.keys()))

    # Generate joke button
    if st.button("Generate Joke"):
        # Construct the prompt based on user's selection
        prompt = f"Generate a {joke_types[joke_type]} joke that is about {joke_subjects[joke_subject]} and is for {joke_settings[joke_setting]}."
        # Call GPT-3 or other LLM to generate the joke response
        joke_response = generate_joke(prompt)

        # Display the joke response
        st.write(joke_response)

         # Save the joke to the session state
        if 'joke_history' not in st.session_state:
            st.session_state['joke_history'] = []
        st.session_state['joke_history'].append(joke_response)
        
        # Add rating feature
        rating = st.radio("Rate the joke:", ('Thumbs Up', 'Thumbs Down'))
        if rating == 'Thumbs Up':
            st.write('You liked the joke!')
        else:
            st.write('You did not like the joke.')

         # Twitter share button
        if st.button("Share on Twitter"):
            tweet_text = urllib.parse.quote(f"Check out this joke: {joke_response}")
            twitter_url = f"https://twitter.com/intent/tweet?text={tweet_text}"
            st.markdown(f'<a href="{twitter_url}" target="_blank">Click here to tweet!</a>', unsafe_allow_html=True)
            webbrowser.open_new_tab(f"https://twitter.com/intent/tweet?text={tweet_text}")

    # Display the joke history
    if 'joke_history' in st.session_state:
        st.subheader("Joke History")
        for joke in reversed(st.session_state['joke_history']):
            st.write(joke + "\n\n")

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
