## **Setup**

### **Prerequisites**

To set up the guestbook, you'll need:

- Python 3.x installed on your system.
- Supabase Account: Sign up at [https://supabase.io](https://supabase.io) if you haven't already.
- Supabase Project: Create a new project in Supabase and note down your project URL and API key.

### **Installation**

#### **Clone the Repository:**

Clone the repository:

```bash
git clone https://github.com/notSoEliel/fasthtml-guestbook-form.git
cd fasthtml-guestbook-form
```

#### **Install Dependencies:**

Install the required Python packages using `pip`:

```bash
pip install supabase-py python-dotenv pytz fasthtml
```

#### **Set Up Supabase:**

Create a new table named `guestbook` in your Supabase project with the following columns:

- `id` (int8, primary key)
- `name` (text)
- `message` (text)
- `timestamp` (text)

Create a `.env` file in the root directory of your project with the following content:

```env
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_api_key
```

Replace `your_supabase_project_url` and `your_supabase_api_key` with your actual Supabase project URL and API key.

#### **Run the Application:**

Start the server by running:

```bash
python main.py
```

Visit [http://localhost:5001](http://localhost:5001) in your browser to see the guestbook in action.

### **Deployment**

You can deploy this guestbook application using your preferred hosting service. Follow the steps in the FastHTML documentation to learn how to deploy your application.

---

## **Configuración**

### **Requisitos Previos**

Para configurar el libro de visitas, necesitarás:

- Python 3.x instalado en tu sistema.
- Cuenta en Supabase: Regístrate en [https://supabase.io](https://supabase.io) si aún no lo has hecho.
- Proyecto en Supabase: Crea un nuevo proyecto en Supabase y anota tu URL del proyecto y la clave de la API.

### **Instalación**

#### **Clonar el Repositorio:**

Primero, clona el repositorio:

```bash
git clone https://github.com/notSoEliel/fasthtml-guestbook-form.git
cd fasthtml-guestbook-form
```

#### **Instalar Dependencias:**

Instala los paquetes de Python necesarios usando `pip`:

```bash
pip install supabase-py python-dotenv pytz fasthtml
```

#### **Configurar Supabase:**

Crea una nueva tabla llamada `guestbook` en tu proyecto de Supabase con las siguientes columnas:

- `id` (int8, clave primaria)
- `name` (texto)
- `message` (texto)
- `timestamp` (texto)

Crea un archivo `.env` en el directorio raíz de tu proyecto con el siguiente contenido:

```env
SUPABASE_URL=tu_url_de_proyecto_supabase
SUPABASE_KEY=tu_clave_de_api_supabase
```

Reemplaza `tu_url_de_proyecto_supabase` y `tu_clave_de_api_supabase` con la URL real de tu proyecto en Supabase y la clave de API.

#### **Ejecutar la Aplicación:**

Inicia el servidor ejecutando:

```bash
python main.py
```

Visita [http://localhost:5001](http://localhost:5001) en tu navegador para ver el libro de visitas en acción.

### **Despliegue**

Puedes desplegar esta aplicación del libro de visitas usando el servicio de hosting que prefieras. Sigue los pasos en la documentación de FastHTML para aprender cómo desplegar tu aplicación.
