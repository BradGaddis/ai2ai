from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA

def load_pdf(path: str) -> list:
    """
    Loads a PDF file from the given path and returns a list of strings, one for each page.
    """
    loader = PyPDFLoader(file_path=path)
    document = loader.load()
    return document


def chunkify_pdf(
    documents: list, chunk_size: int = 1000, chunk_overlap=30, separator="\n"
) -> list:
    """
    Splits a list of strings into chunks of the given size.
    """
    text_splitter = CharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap, separator=separator
    )
    docs = text_splitter.split_documents(documents=documents)
    return docs


def embbed_pdf(docs: list, save= True) -> list:
    """
    Embeds a list of strings into a list of embeddings.
    """
    embeddings = OpenAIEmbeddings() # I need to look more into this. It seems that I can use localAI to get it from the docker container with Bert or something.
    return embeddings


def vectorize_pdf_embeddings(docs: list, embeddings: list) -> list:
    """
    Vectorizes a list of embeddings into a list of vectors.
    """
    vectorstore = FAISS.from_documents(documents=docs,embedding=embeddings)
    vectorstore.save_local("VectorStore/test")
    return vectorstore


def query_pdf(
    chain_type,
    embeddings,
    llm,
    retriever = None,
    prompt="Please sarcastically explain what the PDF is about and that the user didn't fill the prompt argument out of the method that generated this sarcasm",
):
    """
    Opens vector store and runs a chain to query the PDF in the LLM
    """

    vectorstore = FAISS.load_local(folder_path="VectorStore/test", embeddings=embeddings)

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type=chain_type,
        retriever=retriever if retriever else vectorstore.as_retriever(),
    )

    res = qa.run(prompt)
    print(res)