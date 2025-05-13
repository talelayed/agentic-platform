import sys
import os

# Add the src/ directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from vector_store import create_vector_index

create_vector_index()