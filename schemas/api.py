API_SCHEMA = {
    'method': {
        'type': str,
        'required': True,
        'constraints': lambda method: method in [
            'GET',
            'POST'
        ]
    },
    'endpoint': {
        'type': str,
        'required': True,
        'constraints': lambda method: method in [
            'generate',
            'chat',
            'stop-stream',
            'model',
            'token-count'
        ]
    }
}