# DataViz AI - Natural Language Data Query Interface

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Next.js](https://img.shields.io/badge/Next.js-15.4+-black.svg)](https://nextjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green.svg)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue.svg)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](CONTRIBUTING.md)
[![Open Issues](https://img.shields.io/github/issues/nicvazquezdev/dataviz-ai)](https://github.com/nicvazquezdev/dataviz-ai/issues)
[![Stars](https://img.shields.io/github/stars/nicvazquezdev/dataviz-ai)](https://github.com/nicvazquezdev/dataviz-ai/stargazers)

A modern, open-source web application that allows users to query their data using natural language and get instant visualizations. Built with FastAPI, Next.js, and powered by OpenAI's GPT models.

<br />
<img width="1892" height="546" alt="Screenshot 2025-08-29 at 5 08 06 PM" src="https://github.com/user-attachments/assets/3df800b0-81cc-4bd4-97f2-1be44887a913" />
<br />
<br />
<img width="1892" height="941" alt="Screenshot 2025-08-29 at 5 10 00 PM" src="https://github.com/user-attachments/assets/f6e398e3-5955-48bd-9e85-97fdd4bc6276" />
<br />

## 🌟 Features

- **Natural Language Queries**: Ask questions about your data
- **Smart SQL Generation**: AI-powered SQL query generation using OpenAI GPT
- **Interactive Visualizations**: Multiple chart types (bar, line, pie, table)
- **Auto Chart Selection**: Intelligent chart type detection based on data
- **Real-time Results**: Instant query execution and visualization
- **Error Handling**: Smart validation for invalid questions
- **Responsive Design**: Modern UI built with Tailwind CSS
- **Containerized**: Full Docker support for easy deployment
- **Demo Mode**: Works without API key - shows realistic sample data
- **Graceful Degradation**: Automatic fallback to demo mode when API key is missing or invalid

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
git clone https://github.com/nicvazquezdev/dataviz-ai.git
cd dataviz-ai
```

### 2. Environment Setup (Optional)

**The app works out of the box without any configuration!**

For full functionality with real data queries using OpenAI's GPT models, you can optionally copy the environment template and add your OpenAI API key:

```bash
cp env.template .env
```

Edit `.env` and add your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key_here
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_HOST=db
POSTGRES_PORT=5432
POSTGRES_DB=dataviz_ai
```

**Note**: If no `.env` file is present or no OpenAI API key is configured, the app will automatically switch to demo mode and provide realistic sample data for testing and demonstration purposes.

💡 **Note**: If you don't configure an API key, the application will automatically run in **Demo Mode** and show realistic sample data based on your questions.

### 3. Start the Application

```bash
docker-compose up --build
```

### 4. Access the Application

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

## 🎭 Demo Mode

The application includes a **Demo Mode** that works without requiring an OpenAI API key:

- **Automatic Activation**: When no API key is configured or if the key is invalid
- **Smart Data Generation**: Creates realistic sample data based on your question type
- **Full Visualizations**: Generates charts and graphs just like with real data
- **Question-Aware**: Different question types produce different visualization types:
  - Product questions → Bar charts of top products
  - Date/time questions → Line charts with trends
  - Waiter questions → Performance comparisons
  - Revenue questions → Category breakdowns
  - Quantity questions → Product quantity analysis
- **Visual Indicator**: Yellow warning banner shows when demo mode is active
- **Seamless Experience**: No interruption to the user workflow

This makes the application perfect for:

- **Demoing** to stakeholders
- **Testing** the interface without API costs
- **Development** without API dependencies
- **Learning** how the system works

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
dataviz-ai/
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

## 🤝 Contributing

We love contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details on how to submit pull requests, report issues, and contribute to the project.

### Quick Contribution Steps

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [OpenAI](https://openai.com/) for providing the GPT API
- [FastAPI](https://fastapi.tiangolo.com/) for the excellent web framework
- [Next.js](https://nextjs.org/) for the React framework
- [Recharts](https://recharts.org/) for the charting library
- [Tailwind CSS](https://tailwindcss.com/) for the styling framework

## 📞 Support

- 🐛 **Issues**: [GitHub Issues](https://github.com/nicvazquezdev/dataviz-ai/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/nicvazquezdev/dataviz-ai/discussions)

## ⭐ Star History

If you find this project helpful, please consider giving it a star on GitHub!

[![Star History Chart](https://api.star-history.com/svg?repos=nicvazquezdev/dataviz-ai&type=Date)](https://star-history.com/#nicvazquezdev/dataviz-ai&Date)

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

## 📈 Roadmap

- [ ] Support for more database types (MySQL, SQLite)
- [ ] Advanced chart types (scatter plots, heatmaps)
- [ ] Data export functionality
- [ ] User authentication and data isolation
- [ ] Custom data source connectors
- [ ] Mobile app version
- [ ] Multi-language support
- [ ] Advanced analytics features

## 🔄 Changelog

See [CHANGELOG.md](CHANGELOG.md) for a detailed history of changes and releases.
