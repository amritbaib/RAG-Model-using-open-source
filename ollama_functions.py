from ollama import embed, chat

# ---------- EMBEDDINGS ----------
response = embed(
    model="nutrition",
    input=[
        "here is an example sentence",
        "here is second one"
    ]
)

# Number of embeddings
print(len(response["embeddings"]))

# Dimension of first embedding vector
print(len(response["embeddings"][0]))


# ---------- CHAT ----------
response = chat(
    model="nutrition",
    messages=[
        {
            "role": "user",
            "content": "why did the chicken cross the road?"
        }
    ]
)

print(response.message.content)