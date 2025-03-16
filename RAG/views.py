from django.shortcuts import render
from django.http import JsonResponse
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.groq import Groq
import os
from django.conf import settings
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return render(request, 'index.html')

# Initialize the RAG settings
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
Settings.llm = Groq(model="llama3-70b-8192", api_key="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")

# Initialize the index (you might want to do this in a more appropriate place)
data_dir = os.path.join(settings.BASE_DIR, 'data')
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

def initialize_index():
    try:
        documents = SimpleDirectoryReader(data_dir).load_data()
        index = VectorStoreIndex.from_documents(documents)
        return index.as_query_engine()
    except Exception as e:
        print(f"Error initializing index: {str(e)}")
        return None

@csrf_exempt
def chat(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('message', '')
            
            # Initialize query engine
            query_engine = initialize_index()
            if query_engine is None:
                return JsonResponse({
                    'error': 'Failed to initialize query engine',
                    'status': 'error'
                }, status=500)
            
            # Get response from the model
            response = query_engine.query(user_message)
            
            return JsonResponse({
                'response': str(response),
                'status': 'success'
            })
        except json.JSONDecodeError:
            return JsonResponse({
                'error': 'Invalid JSON data',
                'status': 'error'
            }, status=400)
        except Exception as e:
            print(f"Error in chat endpoint: {str(e)}")
            return JsonResponse({
                'error': str(e),
                'status': 'error'
            }, status=500)
    
    return JsonResponse({'error': 'Invalid request method'}, status=400)