# Mini Nivii - Natural Language Data Query Interface

A modern web application that allows users to query their data using natural language and get instant visualizations. Built with FastAPI, Next.js, and powered by OpenAI's GPT models.

![Mini Nivii Demo](https://img.shields.io/badge/Status-MVP-green)
![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Next.js](https://img.shields.io/badge/Next.js-15.4+-black)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue)

## 🚀 Features

- **Natural Language Queries**: Ask questions about your data in plain English
- **Smart SQL Generation**: AI-powered SQL query generation using OpenAI GPT
- **Interactive Visualizations**: Multiple chart types (bar, line, pie, table)
- **Auto Chart Selection**: Intelligent chart type detection based on data
- **Real-time Results**: Instant query execution and visualization
- **Error Handling**: Smart validation for invalid questions
- **Responsive Design**: Modern UI built with Tailwind CSS
- **Containerized**: Full Docker support for easy deployment

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │    Backend      │    │   Database      │
│   (Next.js)     │◄──►│   (FastAPI)     │◄──►│  (PostgreSQL)   │
│   Port: 3000    │    │   Port: 8000    │    │   Port: 5432    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                              │
                              ▼
                       ┌─────────────────┐
                       │   OpenAI API    │
                       │   (GPT-3.5)     │
                       └─────────────────┘
```

## 🛠️ Tech Stack

### Backend

- **FastAPI** - Modern Python web framework
- **SQLAlchemy** - SQL toolkit and ORM
- **PostgreSQL** - Relational database
- **OpenAI API** - GPT-3.5 for SQL generation
- **Pandas** - Data manipulation
- **Uvicorn** - ASGI server

### Frontend

- **Next.js 15** - React framework
- **TypeScript** - Type safety
- **Tailwind CSS** - Utility-first CSS
- **Recharts** - Data visualization library
- **React Hooks** - State management

### Infrastructure

- **Docker & Docker Compose** - Containerization
- **PostgreSQL** - Database
- **Environment Variables** - Configuration management

## 📋 Prerequisites

- **Docker** and **Docker Compose** installed
- **OpenAI API Key** (get one from [OpenAI Platform](https://platform.openai.com/))
- **Git** for cloning the repository

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/nicvazquezdev/mini-nivii.git
cd mini-nivii
```

### 2. Environment Setup

Copy the environment template and add your OpenAI API key:

```bash
cp .env.template .env
```

Edit `.env` and add your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key_here
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_HOST=db
POSTGRES_PORT=5432
POSTGRES_DB=mini_nivii
```

### 3. Start the Application

```bash
docker-compose up --build
```

### 4. Access the Application

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

## 💾 Data Loading

💡 The data is automatically loaded from `backend/data.csv` on backend startup.  
💡 The backend dynamically infers the schema from the database and passes it to the LLM. This means you can replace the CSV file with any other structure and the system will adapt.

## 🎯 Usage Examples

Try these natural language queries:

- "What are the top 5 selling products?"
- "Show me sales by date"
- "Which customer bought the most?"
- "What's the total revenue for October 2024?"
- "Show me products with quantity greater than 100"
- "What are the sales trends over time?"

## 🔧 Development

### Project Structure

```
mini-nivii/
├── backend/
│   ├── app/
│   │   ├── main.py          # FastAPI application
│   │   ├── db.py            # Database configuration
│   │   ├── llm.py           # OpenAI integration
│   │   └── utils.py         # Utility functions
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── load_data.py         # Data loading script
│   └── data.csv             # Sample data
├── frontend/
│   ├── app/
│   │   ├── components/      # React components
│   │   ├── page.tsx         # Main page
│   │   └── layout.tsx       # App layout
│   ├── Dockerfile
│   ├── package.json
│   └── tailwind.config.js
├── docker-compose.yml
├── .env.template
└── README.md
```

## 📊 API Documentation

Once the backend is running, visit http://localhost:8000/docs for interactive API documentation.

### Main Endpoints

- `POST /ask` - Submit a natural language question

## 🐛 Troubleshooting

### Common Issues

1. **OpenAI API Key Error**

   - Ensure your API key is correctly set in `.env`
   - Check if you have sufficient OpenAI credits

2. **Database Connection Error**

   - Ensure PostgreSQL container is running
   - Check database credentials in `.env`

3. **Invalid Question Error**
   - Try more specific questions about your data
   - Ensure your question relates to data analysis
