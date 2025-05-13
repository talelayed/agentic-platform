from opensearchpy import OpenSearch, RequestsHttpConnection
from config import OPENSEARCH_HOST

# Master user
username="talel"
password="Talel1234*"

client = OpenSearch(
    hosts=[{'host': OPENSEARCH_HOST.replace("https://", ""), 'port': 443}],
    http_auth=(username,password),
    use_ssl=True,
    verify_certs=True,
    connection_class=RequestsHttpConnection
)

print("**********",vars(client.indices))