def split_into_chunks(lst, chunk_size):
    
    if chunk_size <= 0:
        raise ValueError("Chunk size must be greater than 0.")

    chunks = []
    for i in range(0, len(lst), chunk_size):
        chunks.append(lst[i:i+chunk_size])
    return chunks    