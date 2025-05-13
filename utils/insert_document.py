import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from bedrock import get_titan_embedding
from opensearchpy import OpenSearch
from config import OPENSEARCH_HOST, OPENSEARCH_INDEX
from opensearchpy import RequestsHttpConnection

# Master user
username="talel"
password="Talel1234*"

# Master user authentication
client = OpenSearch(
    hosts=[{'host': OPENSEARCH_HOST.replace("https://", ""), 'port': 443}],
    http_auth=(username, password),
    use_ssl=True,
    verify_certs=True,
    connection_class=RequestsHttpConnection
)

# Example text to index
text = "Refunds are typically processed within 7 business days."

# Get Titan embedding
embedding = get_titan_embedding(text)

# Compose document
doc = {
    "text": text,
    "embedding": embedding
}

# Index the document
response = client.index(index=OPENSEARCH_INDEX, body=doc)
print("Document inserted:", response["_id"])
