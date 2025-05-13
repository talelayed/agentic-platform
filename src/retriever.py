from src.bedrock_integration import cloudsearch_client
from opensearchpy import OpenSearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
import boto3
import os


region = "eu-west-1"
service= "es"

credentials = boto3.Session.get_credentials()
auth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

# OpenSearch host
host = "https://search-test-3pp67dneihfsthjkogkg2se3re.aos.eu-west-1.on.aws/_dashboards"

# OpenSearch client
client = OpenSearch(
    hosts=[{"host":host, "port": 443}],
    http_auth=auth,
    use_ssl=True,
    verify_certs=True,
    connection_class=RequestsHttpConnection
)

def search_opensearch(query: str, index_name="documents", size=3):
    response = client.search(index=index_name,
    size=size,
    body{
        "query": {
            "match": {
                "content": query
            }
        }
    })
    hits = response['hits']['hits']
    return [hit['_source'] for hit in hits]

def build_prompt_with_context(docs, question):
    context = "\n".join([str(doc) for doc in docs])
    return f"""
You are an assistant. Here is internal knowledge:
{context}

Answer the following question:
{question}
"""
