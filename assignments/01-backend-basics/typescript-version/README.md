# Assignment 01: Backend Basics (TypeScript Version)

## Overview
This is the TypeScript equivalent of the minimal Python backend. Following the requirement to use **NestJS** when a framework similar to FastAPI is needed, this implementation shrinks the typically heavy NestJS boilerplate into a single, highly readable file (`main.ts`) of roughly 25 lines. 

It features the exact same two endpoints:
- `GET /health`
- `POST /echo`

## Technologies Used
- **TypeScript**: The core programming language, providing static typing over JavaScript.
- **NestJS** (`@nestjs/core`, `@nestjs/common`): A progressive Node.js framework. It was chosen because its architecture—relying heavily on decorators (`@Get()`, `@Post()`) and class-based controllers—is the closest ecosystem match to Python's FastAPI. 
- **ts-node**: A utility that allows us to run TypeScript files directly without needing a separate compilation step to JavaScript.

## Approach
Usually, NestJS requires multiple files (Controllers, Services, Modules). To meet the "smallest possible backend" requirement, I combined the Data Transfer Object (`MessageDto`), the Controller (`AppController`), the Module (`AppModule`), and the bootstrap script into a single `main.ts` file. 

## Running Locally

### 1. Install Dependencies
Ensure you have [Node.js](https://nodejs.org/) installed, then run:
```bash
npm install
```

### 2. Start the Server
Run the application using `ts-node`:
```bash
npm start
```
The server will start at `http://127.0.0.1:8000`.

### 3. Test the Endpoints

**Test the `/health` Endpoint (GET request via Browser)**
Navigate to: [http://127.0.0.1:8000/health](http://127.0.0.1:8000/health)

**Test the `/echo` Endpoint (POST request via Terminal)**
Open another terminal window and run:

**For Mac/Linux (Bash):**
```bash
curl -X POST "http://127.0.0.1:8000/echo" -H "Content-Type: application/json" -d '{"message": "Hello from curl!"}'
```

**For Windows (PowerShell):**
```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/echo" -Method Post -Headers @{"Content-Type"="application/json"} -Body '{"message": "Hello from PowerShell!"}'
```
You should receive a JSON response with your message!
