import os
import json
from pypdf import PdfReader

DOCUMENTS_FOLDER = "documents"

all_chunks = []

chunk_size = 200


for filename in os.listdir(DOCUMENTS_FOLDER):

    filepath = os.path.join(DOCUMENTS_FOLDER, filename)

    print(f"Processing: {filename}")

    text = ""

    # PDF FILES
    if filename.endswith(".pdf"):

        reader = PdfReader(filepath)

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    # TXT FILES
    elif filename.endswith(".txt"):

        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()

    else:
        continue

    words = text.split()

    for i in range(0, len(words), chunk_size):

        chunk = " ".join(words[i:i + chunk_size])

        all_chunks.append(chunk)

with open("documents/chunks.json", "w", encoding="utf-8") as f:

    json.dump(all_chunks, f, indent=2)

print(f"\nSaved {len(all_chunks)} chunks")