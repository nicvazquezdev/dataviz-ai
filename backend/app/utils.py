def is_valid_question(question: str) -> bool:
    """Check if the question is a valid data query"""
    question = question.strip().lower()
    
    # Check if question is too short or just gibberish
    if len(question) < 3:
        return False
    
    # Check if question contains mostly non-alphabetic characters
    alpha_chars = sum(1 for c in question if c.isalpha())
    total_chars = len(question.replace(' ', ''))
    if total_chars > 0 and alpha_chars / total_chars < 0.3:
        return False
    
    # Check if question contains common query words
    query_indicators = [
        'what', 'how', 'when', 'where', 'who', 'which', 'show', 'get', 'find',
        'list', 'count', 'sum', 'total', 'average', 'max', 'min', 'top', 'bottom',
        'sales', 'product', 'customer', 'order', 'date', 'price', 'quantity'
    ]
    
    has_query_indicator = any(indicator in question for indicator in query_indicators)
    
    return has_query_indicator
