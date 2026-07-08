# from langchain_unstructured import UnstructuredLoader


# def read_file(filePath):

#     loader = UnstructuredLoader(filePath)
#     documents = loader.load()
    
#     return documents


#using langChain Generated messy results so I am using pandas

import pandas as pd
from langchain_core.documents import Document


def read_excel(file_path):
  
    df = pd.read_excel(file_path)

    documents = []

    for _, row in df.iterrows():

        content = ""

        for column, value in row.items():
            content += f"{column}: {value}\n"

        document = Document(
            page_content=content.strip(),
            metadata={
                "source": file_path
            }
        )

        documents.append(document)

    return documents