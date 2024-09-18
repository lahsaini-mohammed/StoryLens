import streamlit as st
from PIL import Image
import os
from app.core.pipeline import StoryGenerationPipeline
from app.config import GENRES, STORY_LENGTHS, INPUT_IMAGE_DIR, OUTPUT_STORY_DIR
# from TTS.api import TTS  # Coqui TTS
# import io

def main():
    st.title(":red[StoryLens], your Image to Story Generator")

    # Initialize StoryGenerationPipeline
    pipeline = StoryGenerationPipeline()

     # Initialize Coqui TTS model
    # tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)
    # Initialize Coqui TTS model with GPU support (CUDA)
    # tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=True)


    # Image upload
    uploaded_files = st.file_uploader("Choose images", accept_multiple_files=True, type=['png', 'jpg', 'jpeg'])
    
    if uploaded_files:
        image_paths = []
        os.makedirs(INPUT_IMAGE_DIR, exist_ok=True)
        for uploaded_file in uploaded_files:
            image = Image.open(uploaded_file)
            image_path = os.path.join(INPUT_IMAGE_DIR, uploaded_file.name)
            image.save(image_path)
            image_paths.append(image_path)
            st.image(image, caption=uploaded_file.name, use_column_width=True)
        
        # Story generation parameters
        story_params = {}

        # Genre selection
        genre = st.selectbox("Choose a genre (optional)", [""] + list(GENRES.keys()))
        if genre:
            story_params['genre'] = genre
            st.write(GENRES[genre])

        # Story length selection
        story_length = st.selectbox("Choose story length (optional)", [""] + list(STORY_LENGTHS.keys()))
        if story_length:
            story_params['story_length'] = story_length
            st.write(STORY_LENGTHS[story_length])

        # Character customization
        character_examples = [
            "John, a brave firefighter with a fear of heights",
            "Sarah, a brilliant scientist struggling with imposter syndrome",
            "Max, a mischievous cat with the ability to understand human speech"
        ]
        characters = st.text_area("Customize characters (optional)", 
                                  placeholder="e.g. " + " | ".join(character_examples))
        if characters:
            story_params['characters'] = characters

         # Plot points
        plot_point_examples = [
            "A mysterious package arrives at midnight",
            "The main character discovers they have a long-lost sibling",
            "An unexpected solar eclipse plunges the city into darkness"
        ]
        plot_points = st.text_area("Add specific plot points (optional)", 
                                   placeholder="e.g. " + " | ".join(plot_point_examples))
        if plot_points:
            story_params['plot_points'] = plot_points

        # Pacing
        pacing = st.select_slider("Control pacing (optional)", 
                                  options=["", "Slow build-up", "Moderate", "Fast-paced"])
        if pacing:
            story_params['pacing'] = pacing

        # Level of detail
        detail_level = st.select_slider("Level of detail (optional)", 
                                        options=["", "Minimalist", "Balanced", "Rich and vivid"])
        if detail_level:
            story_params['detail_level'] = detail_level

        if st.button("Generate Story"):
            with st.spinner("Generating your story..."):
                # print(image_paths)
                story_output = pipeline.generate_story_from_images(image_paths, **story_params)
                
                st.success("Story generated successfully!")
                st.subheader(story_output['title'])
                st.text_area("Generated Story", story_output['story'], height=300)

                # Save the story
                os.makedirs(OUTPUT_STORY_DIR, exist_ok=True)
                filename = f"{story_output['title'].lower().replace(' ', '_')}.txt"
                with open(os.path.join(OUTPUT_STORY_DIR, filename), 'w') as f:
                    f.write(f"Title: {story_output['title']}\n\n")
                    f.write(story_output['story'])

                # Generate audio for the story
                # with st.spinner('Generating audio...'):
                #     audio_bytes = io.BytesIO()  # Create an in-memory bytes buffer
                #     tts.tts_to_file(text=story_output['story'], file_path=audio_bytes)
                #     audio_bytes.seek(0)  # Move the cursor back to the start of the stream

                #     # Display the audio player
                #     st.markdown("### Listen to the story:")
                #     st.audio(audio_bytes, format='audio/wav')
                
                st.download_button(
                    label="Download Story",
                    data=f"Title: {story_output['title']}\n\n{story_output['story']}",
                    file_name=filename,
                    mime="text/plain"
                )

if __name__ == "__main__":
    main()