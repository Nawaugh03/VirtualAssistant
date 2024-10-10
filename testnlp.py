from transformers import pipeline

# Create a simple Q&A model
qa_pipeline = pipeline("question-answering")

result = qa_pipeline({
    'question': 'What is the capital of France?',
    'context': 'Paris is the capital of France.'
})
print(result['answer'])