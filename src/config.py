from dotenv import load_dotenv
import os

load_dotenv()

OPENSEARCH_HOST = os.getenv("OPENSEARCH_HOST")
OPENSEARCH_INDEX = os.getenv("OPENSEARCH_INDEX")
AWS_REGION = os.getenv("AWS_REGION")