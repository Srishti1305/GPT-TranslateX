# 🌐 GPT TranslateX

**GPT TranslateX** is a modern, pastel-themed, AI-powered translator web app that translates text into 25+ languages using the RapidAPI Text Translator API. It features a clean UI, dark/light mode toggle, translation history, and more.

---

## 🚀 Features

- 🎨 **Pastel-Themed Modern UI** with smooth animations and hover effects
- 🗣️ **Speech-to-Text Input**
- 🔊 **Text-to-Speech Output**
- 🌙 **Dark/Light Mode Toggle** with localStorage support  
- 🌍 **Auto Language Detection** from input  
- 🌐 **Translate into 25+ Languages**
- 🤏 **Touch-Friendly UI Improvements**
- 🔄 **Animated Spinner** while translating  
- 📋 **Copy to Clipboard** with toast notification (no intrusive alerts)  
- 🔍 **Searchable Language Dropdown** (via TomSelect)  
- 🕓 **Recent Translation History** (stored in browser session)  
- 🗑️ **Clear History Button**  
- ✅ **Fully Responsive Design**  
- 🔐 **.env Secured API Key**

---

## 📁 Project Structure

GPT-TranslateX/
├── app.py # Flask web app logic
├── translator.py # Translation API logic
├── .env # Stores API keys securely
├── requirements.txt # Python dependencies
├── static/
│ ├── style.css # UI styling
│ ├── logo.png # App branding logo
│ └── script.js # (Optional) extra JavaScript functions
├── templates/
│ └── index.html # Main HTML template
└── README.md # Project documentation

## 🌐 API Used

**Text Translator API by RapidAPI**  
- **Endpoint:** `https://text-translator2.p.rapidapi.com/translate`  
- **Supports:** Auto language detection and translation to multiple languages
## 📸Screenshots
<img width="1888" height="907" alt="image" src="https://github.com/user-attachments/assets/670abc39-0b07-4df8-bf62-1e9f3f511cb9" />


---

📱 Future Enhancements
💾 Persistent History Saved Across Sessions
🌍 Language Detection Confidence Display

📝 License
This project is licensed under the MIT License — feel free to use and modify it for your needs.

🤝 Credits
Built with ❤️ using Flask, HTML, CSS, and RapidAPI
