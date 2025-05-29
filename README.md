# 🌐 AI Text Translator

A powerful text translation application built with Python, Streamlit, and Google's Gemini AI model. This application allows users to translate text into multiple languages using advanced AI technology.

## ✨ Features

- Translate text into 11 different languages
- User-friendly Streamlit interface
- Powered by Google's Gemini AI model
- Real-time translation
- Clean and modern UI

## 🚀 Supported Languages

- Urdu
- French
- Spanish
- German
- Chinese
- Arabic
- Hindi
- Italian
- Portuguese
- Russian
- Japanese

## 🛠️ Prerequisites

Before running this application, make sure you have:

- Python 3.7 or higher installed
- A Google Gemini API key
- pip (Python package manager)

## 📦 Installation

1. Clone this repository:
```bash
git clone <your-repository-url>
cd <repository-name>
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory and add your Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

## 🏃‍♂️ Running the Application

1. Start the Streamlit application:
```bash
streamlit run main.py
```

2. Open your web browser and navigate to the URL shown in the terminal (typically http://localhost:8501)

## 💻 Usage

1. Enter the text you want to translate in the text area
2. Select your target language from the dropdown menu
3. Click the "Translate" button
4. View your translated text in the results section

## 🔧 Technical Details

- Built with Python and Streamlit
- Uses Google's Gemini AI model for translations
- Implements async/await for efficient API calls
- Environment variables for secure API key management

## 📝 Dependencies

- streamlit
- python-dotenv
- agents (custom package)
- asyncio

## 🔐 Security Note

Never commit your `.env` file or expose your API key. Always keep your API keys secure and private.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.


## 🙏 Acknowledgments

- Google Gemini AI for providing the translation capabilities
- Streamlit for the web interface framework 