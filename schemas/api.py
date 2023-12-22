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
            'voices',
            'conversions'
        ]
    }
}