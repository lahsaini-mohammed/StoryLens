import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
LLAVA_MODEL = "llava-v1.5-7b-4096-preview"
LLAMA_MODEL = "llama-3.1-70b-versatile"
# LLAMA_MODEL = "llama3-8b-8192"
INPUT_IMAGE_DIR = "data/input_images"
OUTPUT_STORY_DIR = "data/output_stories"

GENRES = {
    "Thriller": "A suspenseful, exciting story that keeps readers on the edge of their seats.",
    "Comedy": "A humorous story designed to entertain and make readers laugh.",
    "Fantasy": "A story set in a magical or otherworldly realm, often featuring mythical creatures and supernatural elements.",
    "Science Fiction": "A story based on imagined future scientific or technological advances and major social or environmental changes.",
    "Action & Adventure": "An exciting story with high stakes, physical challenges, and often a race against time.",
    "Romance": "A story focused on the development of a romantic relationship between characters.",
    "Mystery": "A story that follows the solving of a crime or puzzle, often with clues and suspects.",
    "Horror": "A story designed to frighten, scare, or disgust the reader with elements of the macabre or supernatural.",
    "Historical Fiction": "A story set in a particular period of history, blending real and imagined events.",
    "Drama": "A serious story focusing on realistic characters dealing with emotional themes.",
}

STORY_LENGTHS = {
    "Short Story": "A brief narrative, typically under 750 words.",
    "Novella": "A medium-length work of fiction, typically between 1,750 and 4,000 words.",
    "Full Novel": "A long work of fiction, typically over 4,000 words.",
    "Script": "A written work for film, television, or theater, with dialogue and stage directions.",
}