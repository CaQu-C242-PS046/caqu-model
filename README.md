# CaQu (Career Quest)

## Installation:

- Install dependencies:
```
pip install -r requirements.txt
```

- If you encounter any error, try installing the following packages:
```
pip install tensorflow fastapi uvicorn python-multipart
```

- Run the FastAPI web server:
```
uvicorn app:app --reload
```

## Notes:

- The application is configured to run on port 8080 by default.
- Ensure that `requirements.txt` includes all necessary dependencies for the app to function correctly.
- For cloud deployment, such as Google Cloud Run, make sure to use the exposed port 8080 in your service configuration.

