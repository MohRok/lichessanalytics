# Lichess Data Science Project Web Application

## Overview
The Lichess Data Science Project Web Application is a comprehensive web-based data visualization tool designed to provide deep insights into chess game data from Lichess.org. This project is built using the Dash framework and Plotly for interactive data visualization.

## Table of Contents
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Running the Web Application Locally](#running-the-web-application-locally)
- [Running the Web Application Online](#running-the-web-application-online)



## Project Structure

The website directory is organized as follows:


- `assets/`: Contains static assets such as images.
- `json files/`: Contains JSON data files used for visualization.
- `lichessanalytics.py`: The main application script.
- `README.md`: This documentation file.
- `requirements.txt`: Lists the Python packages required to run the application.

## Getting Started
To set up and run the web application, follow these steps:

### Prerequisites
- Python 3.x (Download from [Python's official website](https://www.python.org/downloads/))

### Installation
1. Download the project ZIP archive and extract it to a directory of your choice.

2. Open a command prompt or terminal window and navigate to the project directory.

3. Create a virtual environment (recommended):

   - **Windows:**

     ```bash
     python -m venv venv
     ```

   - **Linux/macOS:**

     ```bash
     python3 -m venv venv
     ```

4. Activate the virtual environment:

   - **Windows:**

     ```bash
     .\venv\Scripts\activate
     ```

   - **Linux/macOS:**

     ```bash
     source venv/bin/activate
     ```
5. Install the required Python packages:

     ```bash
     pip install -r requirements.txt
     ```


## Running the Web Application Locally

To run the web application locally, please follow these steps:

1. Open a terminal or command prompt.

2. Navigate to the project directory.

3. Execute the following command to start the application:

```bash
python lichessanalytics.py
```

Once the application is running, manually open your web browser and enter the following 
URL in the address bar: 

[http://localhost:8050].

This will access the locally hosted web application.

 - **Note:** If you prefer to have the application automatically open in your default web browser when you start the application, you can uncomment the following lines of code in lichessanalytics.py:

(# import webbrowser)
(# webbrowser.open_new_tab('http://localhost:8050'))

Uncommenting these lines will automatically open the application in your default web browser when you run the application script.

## Running the Web Application Online

To deploy the web application online, you can use hosting services such as Render, Heroku, AWS, or Azure. Detailed deployment instructions may vary depending on the hosting platform you choose. Refer to the official documentation of your chosen platform for deployment guidance.

### Hosting on Render Example

This guide will walk you through the steps to deploy your web application using Render, a cloud platform for hosting web applications.

### Prerequisites

Before you begin, make sure you have the following:

1. An account on [Render](https://render.com/). If you don't have one, create an account.

2. Your web application code ready for deployment.

### Installation of Render CLI

You need to install the Render Command Line Interface (CLI) to interact with Render services.

### Linux:

```bash
curl -o /usr/local/bin/render https://render.com/download/linux
```
### Windows:

1. Download the Render CLI installer for Windows from the [Render CLI Releases page](https://render.com/docs/cli#getting-started).

2. Run the installer to install the Render CLI on your Windows machine.

### macOS:

1. Download the Render CLI installer for macOS from the [Render CLI Releases page](https://render.com/docs/cli#getting-started).

2. Run the installer to install the Render CLI on your macOS machine.

### Logging In

Once the Render CLI is installed, open a terminal or command prompt and log in to your Render account by running:

```bash
render login
```

1. Follow the on-screen instructions to log in to your Render account.

### Deploying Your Web Application

1. Navigate to the directory where your web application code is located using the `cd` command.

2. Deploy your web application to Render by running:      ```
							  render up
						          ```
### Configuring Deployment Settings

1. Follow the prompts to configure your deployment settings.

### Accessing Your Web Application

1. After the deployment is complete, Render will provide you with a URL where your web application is hosted.

2. You can access your application using this URL.

For more information and detailed documentation, visit the [Render documentation](https://render.com/docs/).


### Hosting Information

This web application is hosted on Render. You can access it at [https://lichessanalytics.onrender.com](https://lichessanalytics.onrender.com).

   

