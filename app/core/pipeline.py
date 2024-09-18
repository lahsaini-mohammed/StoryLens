from app.core.image_processor import ImageProcessor
from app.core.story_generator import create_story_chain


class StoryGenerationPipeline:
    def __init__(self):
        self.image_processor = ImageProcessor()

    def generate_story_from_images(self, image_paths, **kwargs):
        image_descriptions = []
        for image_path in image_paths:
            description = self.image_processor.process_image(image_path)
            image_descriptions.append(description)

        kwargs['combined_description'] = "\n".join(image_descriptions)

        prompt, llm_with_tool = create_story_chain(list(kwargs.keys()))
        story_output = llm_with_tool.invoke(prompt.format(**kwargs))
        print(story_output)
        return story_output
    
        # try:
        #     story_output = llm.invoke(prompt.format(**kwargs))
        #     content = story_output.content
            
        #     # Parse the content to extract title and story
        #     lines = content.split('\n')
        #     title = next((line.split(':', 1)[1].strip() for line in lines if line.startswith('Title:')), 'Untitled')
        #     story = '\n'.join(line.split(':', 1)[1].strip() if ':' in line else line for line in lines if line.startswith('Story:') or ':' not in line)
            
        #     return {'title': title, 'story': story}
        # except Exception as e:
        #     print(f"An error occurred while generating the story: {str(e)}")
        #     raise