# 📖 Emoji Story Generator

A fun, interactive web application that uses Google's Gemini AI to generate short, magical stories from a sequence of emojis.

This app is built with Python and Streamlit, allowing users to select emojis and instantly receive a creative story based on their choices.

## ✨ Features

* **Interactive UI**: Click on emojis to add them to your story prompt.
* **AI-Powered Stories**: Leverages the power of Google's `gemini-1.5-pro-latest` to write imaginative stories.
* **Random Suggestions**: Don't know which emojis to pick? Get a new random set with the "Refresh Emojis" button.
* **Simple & Fast**: Built with Streamlit for a clean and responsive user experience.

## 🚀 Getting Started

Follow these instructions to get the project running on your local machine.

### Prerequisites

* Python 3.8 or higher
* A Google AI API Key. You can get one from [Google AI Studio](https://aistudio.google.com/app/apikey).

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/emoji-story-generator.git](https://github.com/your-username/emoji-story-generator.git)
    cd emoji-story-generator
    ```

2.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up your API Key:**
    * Create a file named `.env` in the project's root directory.
    * Add your API key to this file like so:
        ```
        GOOGLE_API_KEY="YOUR_API_KEY_HERE"
        ```

### Running the Application

To start the Streamlit web server, run the following command in your terminal:

```bash
streamlit run app.py
```

Your web browser should automatically open with the application running.

## 💡 Inspiration

This project was inspired by the idea of Story-Pot, a creative tool for generating stories. I saw the concept in a blog post and wanted to build my own version to learn more about AI and Streamlit.

You can check out the original inspiration here: https://app.thestorypot.com/

## 🖼️ Screenshot

![Screenshot of the Emoji Story Generator app](https://i.imgur.com/your-screenshot-url.png)
*Replace this with a URL to a screenshot of your finished app.*
