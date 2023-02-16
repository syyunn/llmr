import os
import dotenv

import utils
from gpt_index import GPTSimpleVectorIndex, GPTListIndex, Document

dotenv.load_dotenv("llmr/.env")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


text = utils.extract_text_from_pdf(filepath='llmr/pdfs/Matthews1959.pdf')
# chunks = utils.spliter(text, maxlen=4097)
# documents = [Document(t) for t in chunks]
documents = [Document(text)]

# index = GPTSimpleVectorIndex(documents)
index = GPTListIndex(documents)

# index.save_to_disk('index.json')
# index = GPTSimpleVectorIndex.load_from_disk('index.json')

### PLEASE CHECK https://gpt-index.readthedocs.io/en/latest/guides/index_guide.html for detailed use of this parameter
# response = index.query("Summarize the paper including main point of the author.", response_mode="tree_summarize") # good for summary
response = index.query("What kind of folkways are mentioned in the paper as an example?", response_mode="default") # good for detailed answer
print(response)



if __name__ == "__main__":
    pass
