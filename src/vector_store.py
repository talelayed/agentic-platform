# from requests_aws4auth import AWS4Auth
# import boto3
from bedrock import get_titan_embedding
from opensearch_client import client

# Auth setup
# session = boto3.Session()
# credentials = session.get_credentials()
# region = "eu-west-1"
# auth = AWS4Auth(
#     credentials.access_key,
#     credentials.secret_key,
#     region,
#     "es",
#     session_token=credentials.token
# )


def create_vector_index(index):
    if client.indices.exists(index=index):
        print(f"Index '{OPENSEARCH_INDEX}' already exists !")
        return

    index_body = {
    'settings': {
        'index': {
        'number_of_shards': 4
        }
    }
    }


    if client.indices.exists(index=OPENSEARCH_INDEX)
        print("Index already exists!")
        return
    response = client.indices.create(index=OPENSEARCH_INDEX, body=index_body)
    print(f"Index '{OPENSEARCH_INDEX}' created successfully")

