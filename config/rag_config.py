"""
RAG Configuration
"""

# -----------------------------------
# Text Chunking
# -----------------------------------

CHUNK_SIZE = 800

CHUNK_OVERLAP = 150

# -----------------------------------
# Embedding Model
# -----------------------------------

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# -----------------------------------
# Vector Database
# -----------------------------------

VECTOR_DB = "FAISS"

VECTOR_DB_PATH = "knowledge_base/vector_db"

# -----------------------------------
# Retriever
# -----------------------------------

TOP_K = 4

SEARCH_TYPE = "similarity"

# similarity
# mmr

# -----------------------------------
# Supported Documents
# -----------------------------------

SUPPORTED_DOCUMENTS = [

    ".pdf",

    ".txt"
    

]
"""
=========================================================
RAG (Retrieval-Augmented Generation) Configuration
=========================================================

This file contains all configuration related to:

• Document Chunking
• Embedding Model
• Vector Database
• Retriever
• Similarity Search

=========================================================
"""

# =========================================================
# Document Processing
# =========================================================

# Maximum characters in each chunk
CHUNK_SIZE = 1000

# Number of overlapping characters
CHUNK_OVERLAP = 200

# =========================================================
# Hugging Face Embedding Model
# =========================================================

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# =========================================================
# Vector Database
# =========================================================

VECTOR_STORE = "FAISS"

VECTOR_DB_PATH = "knowledge_base/vector_db"

# =========================================================
# Retriever Configuration
# =========================================================

SEARCH_TYPE = "similarity"

TOP_K = 4

# =========================================================
# Supported File Types
# =========================================================

SUPPORTED_DOCUMENTS = [

    ".pdf",

    ".txt",

    ".docx"

]

# =========================================================
# Text Splitter
# =========================================================

SEPARATORS = [

    "\n\n",

    "\n",

    ".",

    "!",

    "?",

    ",",

    " ",

    ""

]

# =========================================================
# Similarity Search Threshold
# =========================================================

SIMILARITY_SCORE_THRESHOLD = 0.70

# =========================================================
# Enable Caching
# =========================================================

ENABLE_CACHE = True

# =========================================================
# Maximum Retrieved Documents
# =========================================================

MAX_RETRIEVED_DOCUMENTS = 4

# =========================================================
# Retrieval Strategy
# Options:
# similarity
# mmr
# similarity_score_threshold
# =========================================================

RETRIEVAL_STRATEGY = "similarity"

# =========================================================
# Collection Name
# =========================================================

COLLECTION_NAME = "company_knowledge_base"

# =========================================================
# Rebuild Index Automatically
# =========================================================

AUTO_REBUILD_INDEX = False




