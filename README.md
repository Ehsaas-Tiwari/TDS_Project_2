# LLM Analysis Quiz – Automated Solver

This project implements an automated agent that solves data-related quiz tasks using LLMs, Playwright scraping, and dynamic code execution. It exposes a FastAPI /solve endpoint that the evaluator will call during the exam.

## 🚀 Features

/solve endpoint with secret validation

Background agent that visits quiz URLs, extracts tasks, solves them, and submits answers

Playwright-based JS-rendered scraping

File downloading, data analysis, and chart generation

Recursive quiz solving until no further URL is provided

Docker-ready and uv-based environment

## 📌 API Usage
POST /solve

**Request body:**

{
  "email": "your-email",
  "secret": "your-secret",
  "url": "https://tds-llm-analysis.s-anand.net/demo"
}


**Server responds immediately with:**

{"status":"ok"}


The agent continues solving the quiz in the background.

## 📂 Project Structure
project/
├── agent.py
├── main.py
├── tools/
│   ├── web_scraper.py
│   ├── code_generate_and_run.py
│   ├── download_file.py
│   └── send_request.py
├── pyproject.toml
├── Dockerfile
└── README.md

## 🔒 Environment Variables

Create .env:

EMAIL=your-email
SECRET=your-secret
OPENAI_API_KEY=your-key

## 📝 License

MIT License.
