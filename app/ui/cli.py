import os
from app.config import INPUT_IMAGE_DIR, OUTPUT_STORY_DIR, GENRES, STORY_LENGTHS

class CLI:
    def __init__(self, pipeline):
        self.pipeline = pipeline

    def run(self):
        print("Welcome to the StoryLens your Image to Story Generator!")
        story_params = {}

        image_paths = self.get_image_paths()
        
        genre = self.get_optional_input(f"Enter the genre ({', '.join(list(GENRES.keys()))}) for your story (or press Enter to skip): ", list(GENRES.keys()))
        if genre:
            story_params['genre'] = genre

        story_length = self.get_optional_input(f"Enter the story length ({', '.join(list(STORY_LENGTHS.keys()))}, or press Enter to skip): ", list(STORY_LENGTHS.keys()))
        if story_length:
            story_params['story_length'] = story_length

        pacing = self.get_optional_input("Enter pacing (Slow build-up, Moderate, Fast-paced, or press Enter to skip): ", ["Slow build-up", "Moderate", "Fast-paced"])
        if pacing:
            story_params['pacing'] = pacing

        detail_level = self.get_optional_input("Enter detail level (Minimalist, Balanced, Rich and vivid, or press Enter to skip): ", ["Minimalist", "Balanced", "Rich and vivid"])
        if detail_level:
            story_params['detail_level'] = detail_level
        
        characters = input("Enter character details (or press Enter to skip): ")
        if characters:
            story_params['characters'] = characters

        plot_points = input("Enter specific plot points (or press Enter to skip): ")
        if plot_points:
            story_params['plot_points'] = plot_points

        print("Generating story...")
        story_output = self.pipeline.generate_story_from_images(image_paths, **story_params)
        
        self.save_story(story_output)
        print(f"Story '{story_output.title}' generated and saved in {OUTPUT_STORY_DIR}!")
        print("\nHere's your story:\n")
        print(story_output.story)

    def get_image_paths(self):
        image_paths = []
        while True:
            image_name = input("Enter image filename (or 'done' to finish): ")
            if image_name.lower() == 'done':
                break
            image_path = os.path.join(INPUT_IMAGE_DIR, image_name)
            if os.path.exists(image_path):
                image_paths.append(image_path)
            else:
                print(f"Image {image_name} not found. Please try again.")
        return image_paths

    def get_optional_input(self, prompt, options):
        while True:
            value = input(prompt)
            if not value or value in options:
                return value or None
            print(f"Invalid input. Please choose from {', '.join(options)} or press Enter to skip.")

    def save_story(self, story_output):
        os.makedirs(OUTPUT_STORY_DIR, exist_ok=True)
        filename = f"{story_output.title.lower().replace(' ', '_')}.txt"
        with open(os.path.join(OUTPUT_STORY_DIR, filename), 'w') as f:
            f.write(f"Title: {story_output.title}\n\n")
            f.write(story_output.story)