# Private CDN with Flask and GitHub

A simple Flask web application that acts as a private Content Delivery Network (CDN) by uploading files to a GitHub repository via its API.

---

## Features

-   **File Upload**: Provides an API endpoint (`/api/upload`) for uploading files.
-   **Automatic Renaming**: Uploaded files are automatically renamed using the format `timestamp-filesize.extension` to ensure unique filenames.
-   **GitHub Integration**: Directly uploads files to a specified GitHub repository using the GitHub API.
-   **URL Response**: Returns the raw URL of the successfully uploaded file on GitHub.

---

## Requirements

This project requires Python and the following libraries:
-   Flask
-   requests
-   python-dotenv

---

## Setup and Installation

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/Adytm404/github-private-cdn-api
    cd github-private-cdn-api
    ```

2.  **Create and Activate Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Windows, use `venv\Scripts\activate`
    ```

3.  **Install Dependencies**
    Install the dependencies from `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Environment Configuration**
    This application uses environment variables for configuration. Create a `.env` file in the project's root directory. The `.env` file and the `venv` directory are ignored by Git.
    ```
    GITHUB_TOKEN="your_github_personal_access_token"
    REPO_OWNER="your_github_username"
    REPO_NAME="your_github_repository_name"
    ```
    -   `GITHUB_TOKEN`: Your personal GitHub access token with `repo` scope.
    -   `REPO_OWNER`: The username or organization that owns the repository.
    -   `REPO_NAME`: The name of the GitHub repository where files will be stored.

---

## How to Run

1.  **Run the Flask Application**
    ```bash
    python app.py
    ```
    The application will run on `http://0.0.0.0:5000`.

2.  **Use the API to Upload a File**
    Use `curl` or any other API tool to send a `POST` request to the `/api/upload` endpoint.

    Example using `curl`:
    ```bash
    curl -X POST -F "file=@/path/to/your/file.jpg" http://localhost:5000/api/upload
    ```

---

## API Endpoint

### Upload File

-   **Endpoint**: `/api/upload`
-   **Method**: `POST`
-   **Request**: `multipart/form-data`
    -   **Key**: `file`
    -   **Value**: The file to be uploaded.

-   **Success Response (`200 OK` or `201 Created`)**
    ```json
    {
      "success": true,
      "url": "[https://raw.githubusercontent.com/REPO_OWNER/REPO_NAME/main/images/20231027103000-12345.jpg](https://raw.githubusercontent.com/REPO_OWNER/REPO_NAME/main/images/20231027103000-12345.jpg)"
    }
    ```

-   **Error Response (`400 Bad Request`)**
    If no file is included in the request.
    ```json
    {
      "error": "No file provided"
    }
    ```
-   **Error Response (from GitHub)**
    If an error occurs while uploading to GitHub, the response from the GitHub API will be forwarded.
    ```json
    {
        "success": false,
        "error": { ... }
    }
    ```
