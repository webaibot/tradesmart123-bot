def generate_response(analysis: list) -> str:
    if not analysis:
        return 'I didn’t understand that. Could you clarify?'
    return '\n'.join(f'{idx+1}. {item}' for idx, item in enumerate(analysis))