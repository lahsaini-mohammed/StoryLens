from app.core.pipeline import StoryGenerationPipeline
from app.ui.cli import CLI

def main():
    pipeline = StoryGenerationPipeline()
    cli = CLI(pipeline)
    cli.run()

if __name__ == "__main__":
    main()