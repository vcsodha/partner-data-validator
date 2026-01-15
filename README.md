# 📌 Partner Data Validator

A lightweight FastAPI service that validates uploaded partner datasets using schema-based validation and returns structured, row-level errors without rejecting the entire file.

---

## ✨ Features

- Upload partner data as a CSV file
- Validate each row against a defined schema
- Return a clear summary of valid vs invalid rows
- Provide structured error reporting with:
  - Row number
  - Field name
  - Validation message
- Allows partial success (valid rows are accepted even if some rows fail)

---

## 🛠 Tech Stack

- **FastAPI** – API framework
- **Pydantic** – Schema validation
- **Pandas** – CSV parsing
- **Uvicorn** – ASGI server
- **Python 3.9+**

---

## 📂 Project Structure

```

partner_data_validator/
├── app/
│   ├── main.py        # FastAPI app and endpoint
│   ├── models.py     # Data schema definitions
│   └── validator.py  # Row-level validation logic
├── requirements.txt
└── README.md

````

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/vcsodha/partner-data-validator.git
cd partner-data-validator
````

---

### 2. Create and Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run the Application

```bash
uvicorn app.main:app --reload
```

The server will start at:

```
http://127.0.0.1:8000
```

---

## ⚙️ Using the API

### Swagger UI

Open the interactive API documentation:

```
http://127.0.0.1:8000/docs
```

---

### ☁️ Endpoint

**POST** `/validate`

* Accepts a CSV file
* Returns validation summary and structured errors

---

### Example CSV (`partners.csv`)

```csv
partner_id,name,email,country,status
p_001,Acme Corp,contact@acme.com,US,active
p_002,Globex Inc,info@globex.com,IN,active
p_003,Invalid Email,bad-email,US,active
p_004,Missing Status,missing@status.com,UK,
p_005,,noname@company.com,US,inactive
```


---

## Design Decisions

* **Schema-based validation** ensures early detection of bad data
* **Row-level error reporting** improves usability for large datasets
* **Partial validation** avoids rejecting entire uploads due to small issues
* Kept intentionally simple for clarity and correctness

---

## 🔮 Possible Extensions

* JSON upload support
* Database persistence
* Schema versioning
* AI-powered correction suggestions
* Dockerization

---

## Author 👩‍💻

Vidisha Sodha 
