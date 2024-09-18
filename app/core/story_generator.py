from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from pydantic import BaseModel, Field
from langchain_core.utils.function_calling import convert_to_openai_tool
from app.config import GROQ_API_KEY, LLAMA_MODEL

class StoryOutput(BaseModel):
    title: str = Field(description="The title of the generated story")
    story: str = Field(description="The full text of the generated story")

def create_story_chain(input_variables):
    llm = ChatGroq(api_key=GROQ_API_KEY, model_name=LLAMA_MODEL)

    base_template = "Write a story based on the following descriptions:\n\n{combined_description}\n\n"
    optional_elements = {
        "genre": "Genre: {genre}\n",
        "story_length": "Story length: {story_length}\n",
        "characters": "Characters: {characters}\n",
        "plot_points": "Plot points: {plot_points}\n",
        "pacing": "Pacing: {pacing}\n",
        "detail_level": "Level of detail: {detail_level}\n"
    }

    template = base_template + "".join(optional_elements[var] for var in input_variables if var in optional_elements)
    template += "\nMake sure the story is engaging and incorporates all the specified elements.\n"
    template += "Also, provide an appropriate title for the story.\n"
    # if you don't want to use function calling and structured output and use a more traditional prompt-based approachuncomment the following
    # template += "Title: [Your story title here]\n"
    # template += "Story: [Your full story here]\n"

    prompt = ChatPromptTemplate.from_template(template)
    story_tool = convert_to_openai_tool(StoryOutput)
    llm_with_tool = llm.with_structured_output(story_tool)
    return prompt, llm_with_tool