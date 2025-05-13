import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from bedrock import get_titan_embedding

text = "This is a test to check if Titan embedding works correctly."

embedding = get_titan_embedding(text)

print("Embedding works!")
print(embedding)
print(f"Total length: {len(embedding)}")
