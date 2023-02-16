import os
import dotenv

import utils
from gpt_index import GPTSimpleVectorIndex

dotenv.load_dotenv("llmr/.env")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


# text = utils.extract_text_from_pdf(filepath='llmr/pdfs/Matthews1959.pdf')
# chunks = utils.spliter(text, maxlen=4097)

# from gpt_index import Document

# documents = [Document(t) for t in chunks]


# index = GPTSimpleVectorIndex(documents)

# # save to disk
# index.save_to_disk('index.json')
# # load from disk

index = GPTSimpleVectorIndex.load_from_disk('index.json')
print(index.query("Does the apprenticeship could be understood as a type of folkways?"))

if __name__ == "__main__":
    pass
