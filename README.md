Got it! Here’s a fresh, original README for your **AI Resume Critiquer** project, inspired by the structure and style of the CourseCraft README but written uniquely:

---

# AI Resume Critiquer 📄✨

**AI Resume Critiquer** is a web application that helps you improve your resume using AI-driven insights. Upload your resume and optionally specify the job role you’re targeting. The app analyzes your resume’s content, structure, and skills presentation, and provides actionable suggestions to make it more effective.

---

## Features 🌟

* Upload resumes in **PDF** or **TXT** formats.
* Specify a job role for **customized feedback**.
* AI evaluates:

  * Content clarity and impact
  * Skills and achievements presentation
  * Experience descriptions
  * Suggestions for improvement tailored to the target role
* Displays feedback in a **clean, readable format** in the browser.
* Uses environment variables to securely manage your API key with **python-dotenv**.

---

## Prerequisites ⚙️

Before running the application, make sure you have the following installed:

* Python 3.13 or later
* Streamlit
* Groq Python SDK
* PyPDF2
* python-dotenv

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/vismayasambatur1997-code/Resume-Critique.git
cd "Resume Critique"
```

### 2. Create and Activate Virtual Environment

```bash
python3 -m venv .venv
```

Activate it:

* macOS/Linux:

```bash
source .venv/bin/activate
```

* Windows:

```bash
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually: `streamlit`, `groq`, `PyPDF2`, `python-dotenv`.

### 4. Configure API Key

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_groq_api_key_here
```

Add `.env` to `.gitignore` to prevent committing your API key:

```
.env
```

---

## Running the App

Launch the Streamlit web app:

```bash
streamlit run "Resume critique/main.py"
```

1. Upload your resume (PDF or TXT).
2. Enter the job role (optional).
3. Click **Analyze Resume** to receive AI-powered feedback.

---

## How It Works 🤖

1. **Resume Upload:** Users upload a PDF or TXT resume.
2. **AI Analysis:** The app sends the content to **Groq AI**, which evaluates the resume and generates structured feedback.
3. **Feedback Display:** The analysis is displayed in the Streamlit app for easy reading and application.

---

## Contribution Guidelines 🤝

Contributions are welcome! You can:

* Fork the repository
* Create a new branch for your changes
* Submit a pull request

Any improvements, bug fixes, or new features are appreciated.

---

## License

This project is open-source under the **MIT License**.

---


