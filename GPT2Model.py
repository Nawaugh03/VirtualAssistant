from transformers import GPT2LMHeadModel, GPT2Tokenizer
import speech_recognition as sr

# Load pre-trained GPT-2 model and tokenizer
model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# Fine-tune the model on your conversational dataset (not shown here)

# Chatbot loop
while True:
    user_input = input("User: ")
    
    # Tokenize user input
    input_ids = tokenizer.encode(user_input, return_tensors="pt")
    
    # Generate response from the model
    output = model.generate(input_ids, max_length=50, num_beams=5, no_repeat_ngram_size=2, top_k=50, top_p=0.95, temperature=0.7)
    
    # Decode and print the response
    bot_response = tokenizer.decode(output[0], skip_special_tokens=True)
    print("Chatbot:", bot_response)
