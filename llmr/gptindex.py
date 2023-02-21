import os
import dotenv

import utils
from gpt_index import GPTSimpleVectorIndex, GPTListIndex, Document

dotenv.load_dotenv("llmr/.env")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

need_index =True

if need_index:
    # text = utils.extract_text_from_pdf(filepath='/Users/syyun/Dropbox (MIT)/17.424/week3/Krasner 2007.pdf')
    text = utils.extract_text_from_pdf(filepath='/Users/syyun/Dropbox (MIT)/17.424/week3/Carnegie2014.pdf')
    # text = utils.extract_text_from_pdf(filepath='/Users/syyun/Dropbox (MIT)/17.261/week2/Miller & Stokes - 1963 - Constituency Influence in Congress.pdf')
    # text = utils.extract_text_from_pdf(filepath='/Users/syyun/Dropbox (MIT)/17.261/week2/Brandice Canes-Wrone, David W. Brady, and John F. Cogan. 2002.pdf')
    # text = utils.extract_text_from_pdf(filepath='/Users/syyun/Dropbox (MIT)/17.424/week3/Milner_Kubota 2005.pdf')

    chunks = utils.spliter(text, maxlen=4097)
    documents = [Document(t) for t in chunks]
    documents = [Document(text)]

    # index = GPTSimpleVectorIndex(documents)
    index = GPTListIndex(documents)
    index.save_to_disk('index.json')
    # index = GPTSimpleVectorIndex.load_from_disk('index.json')
else:
    index = GPTListIndex.load_from_disk('index.json')
    pass

### PLEASE CHECK https://gpt-index.readthedocs.io/en/latest/guides/index_guide.html for detailed use of this parameter
# response = index.query("Summarize the paper including author's main idea. Consider the structure of argument.", response_mode="tree_summarize") # good for summary
# response = index.query("Summarize the paper including author's main idea and fit the answer into the token length limit of the generating output.", response_mode="tree_summarize") # good for summary
response = index.query("What is the political hold-up problem according to author?", response_mode="default") # good for detailed answer
print(response)


if __name__ == "__main__":
    pass
