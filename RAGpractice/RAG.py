import chromadb
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

DATA_PATH = "RAGpractice/Data"
CHROMA_PATH =r"chroma_db"
Chroma_client =chromadb.PersistentClient(path=CHROMA_PATH)


collection = Chroma_client.get_or_create_collection(name="Finance Ideology")

loader= PyPDFDirectoryLoader(DATA_PATH)

Raw_doc=loader.load()

text_splitter =RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    length_function=len,
    is_separator_regex=False
)

chunks = text_splitter.split_documents(Raw_doc)

documents=[]
metadata=[]
ids=[]
i=0
for chunk in chunks:
    documents.append(chunk.page_content)
    ids.append("ID"+ str(i))
    metadata.append(chunk.metadata)
    i+=1

#print(documents)
#print(metadata)

#adding to chromadb

collection.upsert(
    documents=documents,
    metadatas=metadata,
    ids=ids
)