# StoryLens: Images to Story Generator

**StoryLens** is an application that generates engaging stories based on uploaded images using advanced AI models such as LLava for image description LLama 3.1 for text generation and Coqui TTS for high-quality text-to-speech. The app allows users to upload multiple images, customize various story elements (like genre, pacing, characters, etc.), and generate a story that can be read, downloaded and listened to directly.

## Features

- **Image Upload**: Upload multiple images (PNG, JPG, JPEG) to generate stories.
- **Story Customization**:
  - Choose the story's genre.
  - Select story length.
  - Customize characters, plot points, pacing, and level of detail.
- **AI-Based Story Generation**: Uses LLava model to generate detailed descriptions of images, Llama 3.1 and LangChain with custom templates to create coherent stories.
- **Text-to-Speech**: Listen to the generated stories using Coqui TTS with CUDA support for GPU acceleration.

## Installation

### Prerequisites

- Python 3.7+
- A capable GPU with CUDA support if you want run models locally (we are using Groq instead) or if you want to use TTS with decent speed (runs slow on cpu )
- Required packages are listed in `requirements.txt` (see below for key packages)

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/lahsaini-mohammed/storylens.git
   cd storylens
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your API key in .env file:


### Running the App

You can run the app in two modes:

1. **Streamlit Web Interface**:
   ```bash
   streamlit run streamlit_main.py
   ```

   This will launch a browser-based interface where you can upload images, customize story generation parameters, and listen to or download the generated story.

2. **Command-Line Interface (CLI)**:
   ```bash
   python main.py
   ```

   This allows you to run the application directly from the command line without using a web interface.

## Usage

### Streamlit (Web Interface)
1. **Upload Images**: Choose images to upload (PNG, JPG, JPEG formats supported).
2. **Customize Story**: Choose a genre, specify characters, plot points, and pacing.
3. **Generate Story**: Click the "Generate Story" button to create your story. 
4. **Listen to Story**: Once generated, you can listen to the story using the in-built text-to-speech functionality.
5. **Download the Story**: Click Download button

### Command-Line Interface
1. Run `python main.py`.
2. Follow the prompts to upload images to the input folder and customize the story.
3. Once the story is generated, the story is shown and or saved to the output dir.


## Customization

You can modify the following aspects of the app:

- **Story Templates**: The story generation is based on a customizable prompt template. You can modify the template in `story_generator.py`.
- **Config**: The model used, the image dir, the output dir, available genres and story lengths can be updated in `app/config.py`.

## Requirements

- `streamlit`
- `Pillow` (for image processing)
- `TTS` (Coqui Text-to-Speech)
- `groq` (GROQ API for cloude inference)
- `langchain`