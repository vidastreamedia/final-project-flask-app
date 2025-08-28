# Final Project: Flask Healthcare Application

This project is a full-stack web application designed to function as a survey tool for collecting user data on income and spending habits. Developed as a final project, it demonstrates key skills in web development, database management, data analysis, and cloud deployment. The application features a user-friendly web form built with Flask, stores data securely in a MongoDB Atlas database, and includes a data processing pipeline that exports the information to a CSV file. Finally, the collected data is analyzed and visualized in a Jupyter Notebook to derive insights, such as identifying spending patterns across different demographics.

## Features
- A simple, user-friendly web form to collect user data.
- Data storage using a cloud-based NoSQL database (MongoDB Atlas).
- A data processing script to export collected data into a CSV format.
- Data analysis and visualization using Python libraries in a Jupyter Notebook.
- The application is deployed on the Render cloud platform.

## Tech Stack
- **Backend:** Flask, Gunicorn (Python)
- **Database:** MongoDB (via PyMongo)
- **Data Processing:** Pandas
- **Data Visualization:** Matplotlib, Seaborn
- **Deployment:** Render

## Project Demo

A quick look at the application's interface and the data visualizations it produces.

**Survey Web Form:**
**

**Data Analysis Chart:**
**

---
## Setup and Local Installation

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```
    git clone <your-repo-link>
    cd Final_Project_Healthcare_App
    ```

2.  **Create and activate a virtual environment:**
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required packages:**
    ```
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables:**
    - Create a file named `.env` in the root of your project folder.
    - Add your MongoDB Atlas connection string to this file like so:
      ```
      MONGO_URI="mongodb+srv://<username>:<password>@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority"
      ```
    - The Python scripts are configured to read this file for local development.

5.  **Run the Flask application:**
    ```
    flask run
    ```
    Open your browser and go to `http://127.0.0.1:5000/`.

---
## Deployment on Render

This application is deployed on Render. The deployment is automated via GitHub.

1.  **Push to GitHub:** Ensure your final code, including a `.gitignore` file and `requirements.txt`, is pushed to a GitHub repository.

2.  **Sign up for Render:** Create a free account at [Render.com](https://render.com) using your GitHub profile.

3.  **Create a New Web Service:**
    - On the Render dashboard, click **New +** -> **Web Service**.
    - Connect the GitHub repository for this project.
    - Render will auto-detect a Python environment. Configure the following settings:
      - **Name:** A unique name for your app (e.g., `healthcare-survey-app`).
      - **Region:** Choose a region close to you (e.g., Frankfurt).
      - **Build Command:** `pip install -r requirements.txt`
      - **Start Command:** `gunicorn app:app`
      - **Plan:** Select the **Free** plan.

4.  **Add Environment Variable:**
    - Go to the **Environment** tab for your new service.
    - Click **Add Environment Variable**.
    - **Key:** `MONGO_URI`
    - **Value:** Paste your full MongoDB Atlas connection string.
    - This keeps your database password secure and separate from your code.

5.  **Deploy:** Click **Create Web Service**. Render will automatically build and deploy your application. Once it's live, you can access it at the URL provided on your dashboard.

The live URL is: https://segun-healthcare-app.onrender.com

---
## File Structure

The project is organized with the following file structure:

`Final_Project_Healthcare_App/`
├── `app.py`                # Main Flask application
├── `data_processor.py`     # Script to process data from MongoDB to CSV
├── `analysis.ipynb`        # Jupyter Notebook for data visualization
├── `templates/`
│   └── `index.html`        # HTML file for the web form
├── `.env`                  # Local environment variables (not in git)
├── `.gitignore`            # Specifies files for Git to ignore
├── `requirements.txt`      # Python package dependencies
└── `README.md`             # This file