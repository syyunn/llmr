from langchain.llms import OpenAI
from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from langchain.docstore.document import Document
import utils

# filepath = './llmr/pdfs/Fenno1962.pdf'
# # filepath = 'Matthews - 1959 - Folkways of the US Senate.pdf'
# # filepath = './week1/Mayhew - 1974 - Congress The Electoral Connection intro, Ch. 1.pdf'
# # filepath = './week1/Shepsle & Weingast (1994).pdf'
# # filepath='./week1/Krehbiel - 1998 - Pivotal Politics Ch. 1-3.pdf'

# text = utils.extract_text_from_pdf(filepath='/Users/syyun/Dropbox (MIT)/17.261/week2/Miller & Stokes - 1963 - Constituency Influence in Congress.pdf')
# text = utils.extract_text_from_pdf(filepath='/Users/syyun/Dropbox (MIT)/17.261/week2/Brandice Canes-Wrone, David W. Brady, and John F. Cogan. 2002.pdf')
# text = utils.extract_text_from_pdf(filepath='/Users/syyun/Dropbox (MIT)/17.424/week3/Carnegie2014.pdf')
text = utils.extract_text_from_pdf(filepath='/Users/syyun/Dropbox (MIT)/17.424/week3/Milner_Kubota 2005.pdf')
# text = utils.extract_text_from_pdf(filepath='/Users/syyun/Dropbox (MIT)/17.424/week3/Krasner2007.pdf')

maxlen = 4097
chunks = utils.spliter(text, maxlen)
print(len(text))

def make_documents(chunks, sources):
    Documents = []
    for chunk, source in zip(chunks, sources):
        Documents.append(Document(page_content=chunk, metadata={"source": source}))
    return Documents

sources = [f'Chunk {i}' for i in range(len(chunks))]
Documents = make_documents(chunks, sources)

import dotenv
import os
dotenv.load_dotenv("llmr/.env")
openai_apikey = os.getenv("OPENAI_API_KEY")

chain = load_qa_with_sources_chain(OpenAI(temperature=0, api_key=openai_apikey))

def print_answer(question, documents, show_locator=False, show_question=False):
    if show_question:
        print(question)
    if show_locator:
        print(
        chain(
            {
                "input_documents": documents,
                "question": question,
            },
            return_only_outputs=True,
        )["output_text"]
        )
        print('\n')
        pass
    else:
        res = chain(
                {
                    "input_documents": documents,
                    "question": question,
                },
                return_only_outputs=True,
            )["output_text"]
        print(res[:-30])
        print('\n')
        pass
    pass

# For full summary
for doc in Documents:
    print_answer("Summarize this section without starting your answer with \'this section\' or \'this paper, etc\'. In addition, Include the main findings of the author as well.", [doc], show_locator=True, show_question=False)
    pass

# # For specific section
# # for doc in Documents[9:]:
# #     print_answer("Why is it hard to maintain the reciprocity when subcommittee badly divided? what does it even mean badly divided?", [doc], show_locator=True, show_question=False)

# For specific section
# print_answer("What is the political hold-up problem according to author?", [Documents[1]], show_locator=True, show_question=False)
pass