
FROM python:3.11-slim

# Ορίζουμε φάκελο εργασίας μέσα στο container
WORKDIR /app

# Αντιγράφουμε όλα τα αρχεία του project στο container
COPY . /app

# Εγκαθιστούμε Flask
RUN pip install flask

# Ανοίγουμε την πόρτα 5000 για το Flask app
EXPOSE 5000

# Εκτελούμε το Flask app
CMD ["python", "main.py"]

