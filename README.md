# 🧠 AI Search Chat Loop (Python)

This simple Python script creates an interactive command-line chatbot that lets users enter queries continuously and receive responses from a generative AI model. The program runs in a loop, sending each user input to the model and printing the output until the user types exit, at which point it closes gracefully with a farewell message.

✅ Features

Continuous input prompt

Sends queries to model.generate_content()

Displays AI-generated responses

Case-insensitive exit command

Lightweight and beginner-friendly

🛠 Requirements

Python 3.x

A configured generative AI model instance (model)

Valid API key (if required by model provider)

🚀 How It Works

Script waits for user input

Checks if user typed exit

Sends text to the model

Prints AI response

Repeats until terminated

💡 Customization Ideas

Add logging or chat history

Wrap into a GUI or Streamlit app

Add voice input / text-to-speech

Integrate error handling

📄 License

Feel free to modify and use in your projects.
