from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
import csv
from datetime import datetime

app = FastAPI()

@app.post("/submit-form")
async def submit_form(
    name: str = Form(...), email: str = Form(...), message: str = Form(...)
):
    # Save data to a CSV file
    with open("form_data.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([datetime.now(), name, email, message])
    return {"status": "success", "message": "Form submitted successfully!"}

# Serve the HTML file if needed
@app.get("/", response_class=HTMLResponse)
async def serve_form():
    with open("your_html_file.html", "r") as file:
        html_content = file.read()
    return html_content
