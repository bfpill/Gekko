Currently in POC stage. 

# Project Name

This project uses Notion API, the Notion Manager API and Gekko, a Python based application. Below you will find all the necessary steps to get the project up and running on your local machine.

## Getting Started

To get a local copy up and running, follow these simple steps:

1. **Fork the repository**

Click on the "Fork" button in the upper right corner of this repository's page to create a copy of this project in your own GitHub account.

2. **Clone the repository**

After you have forked the repository, you can make a clone on your local machine by using the following command:

```bash
git clone https://github.com/<Your GitHub Username>/Gekko.git
```

3. **Add Your Notion ENV Variables**

Create a new file in the root directory of the project named `.env`. Here, you'll add your Notion environment variables. It should look something like this:

```bash
NOTION_API_KEY=your-notion-api-key
```

Please replace `your-notion-api-key` with your actual Notion API key.

## Starting the Servers

### Notion Manager API

The Notion Manager API is used to interact with Notion. To start the Notion Manager API, use the following commands:

```bash
cd frontend
yarn run dev
```

This will start the server at `http://localhost:3000`.

### Gekko

Gekko is a Python-based application. To start Gekko, use the following commands:

```bash
cd gekko
python -m app
```

This will start the server at `http://127.0.0.1:8000`.

## Starting the Project

To start the project, make a POST request to the following endpoint:

```bash
http://127.0.0.1:8000/gekko/start
```

This will start whisper in real time, add text to the queue, run your conversation past the AI, and then add to notion.

Make sure your Notion database is set up like this:

<img width="1021" alt="Screenshot 2023-06-05 at 10 10 23 AM" src="https://github.com/bfpill/Gekko/assets/85584607/ee0e64fd-650c-4f38-b2d4-ca5984d0326b">

---

Thank you for using this project. If you encounter any issues or have any questions, feel free to open an issue. Happy coding!


