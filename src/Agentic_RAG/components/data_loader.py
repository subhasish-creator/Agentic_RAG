from llama_index import SimpleDirectoryReader

def load_documents(input_dir: str):
    return SimpleDirectoryReader(input_dir).load_data()