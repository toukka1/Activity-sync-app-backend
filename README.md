# **Activity Sync Backend**

A FastAPI backend for the Activity Sync App, handling OAuth token exchange.
Hosted at: https://activity-sync-app-backend.fly.dev

---

## **Installation**

1. Clone the repository:
   ```bash
   git clone git@github.com:toukka1/Activity-sync-app-backend.git
   cd activity-sync-backend
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:  
Create a `.env` file in the root directory and add the following:
- STRAVA_CLIENT_ID=your-client-id
- STRAVA_CLIENT_SECRET=your-client-secret


5. Run the server:
```bash
uvicorn main:app --reload
```

The server will be available at `http://127.0.0.1:8000`.

---

## **API Endpoints**

| Method | Endpoint                     | Description                   |
|--------|------------------------------|-------------------------------|
| `POST` | `/exchange-token`       | Handle auth token exchange.   |
| `POST` | `/refresh-token`  | Handle access token refresh.  |

For detailed API documentation, visit `http://127.0.0.1:8000/docs`.

---

## **License**

This project is licensed under the [MIT License](./LICENSE).

---
