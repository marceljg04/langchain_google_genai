 Requisitos

- Python 3.10 o superior
- Streamlit
- LangChain (Google Generative AI)
- python-dotenv

---

 🛠️ Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/marceljg04/langchain_google_genai.git
cd langchain_google_genai
```

2. Crea un entorno virtual e instálalo:

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

3. Crea un archivo .env en la raíz del proyecto con tu API key de Google:

```bash
GOOGLE_API_KEY=TU_GOOGLE_API_KEY
```

---

 🚀 Uso

1. Ejecuta la aplicación con Streamlit:

```bash
streamlit run app.py
```