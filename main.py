import asyncio
from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig, Runner

import streamlit as st
from dotenv import load_dotenv
import os
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")


if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")
# Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# Translation agent
Translator = Agent(
    name="Translator Agent",
    instructions="You translate any given text into the user-specified language. Just provide the translated text only, no explanation."
)


async def translate_text(prompt: str):
    return await Runner.run(
        Translator,
        input=prompt,
        run_config=config
    )
# Streamlit UI
st.title("🌐 AI Text Translator")
st.write("Translate your text into any language using Gemini LLM!")

languages = [
    "Urdu", "French", "Spanish", "German", "Chinese", "Arabic",
    "Hindi", "Italian", "Portuguese", "Russian", "Japanese"
]

# Inputs
input_text = st.text_area("Enter text to translate:")
target_language = st.selectbox("Choose target language:", languages)

if st.button("Translate"):
    if not input_text or not target_language:
        st.warning("Please enter text and select a language.")
    else:
        with st.spinner("🔄 Translating..."):
            user_prompt = f"Translate the following text into {target_language}:\n\n{input_text}"
            response = asyncio.run(translate_text(user_prompt))
            st.subheader("🔁 Translated Text:")
            st.success(response.final_output)
