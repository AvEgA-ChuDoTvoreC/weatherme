
# 'type': 'string',
# 'enum': ["Street", "Avenue", "Boulevard", "Of", "Broken", "Dreams"]
TOWNS_ADD_SCHEMA = {
    '$schema': 'http://json-schema.org/schema#',
    'type': 'object',
    'properties': {
        'town_list': {
            'type': 'array',
            'items': {
                'type': 'string'
            },
            'minItems': 1,
            'maxItems': 11,
            'uniqueItems': True
        }
    },
    'required': ['town_list']
}

TOWNS_GET_SCHEMA = {
    '$schema': 'http://json-schema.org/schema#',
    'type': 'object',
    'properties': {
        'text': {
            'type': 'string',
            'minLength': 1,
            'maxLength': 1024
        },
        'grade': {
            'anyOf': [
                {
                    'type': 'integer',
                    'minimum': 1,
                    'maximum': 10,
                },
                {
                    'type': 'string',
                    'minLength': 1,
                    'pattern': '^\d+$'
                }
            ]
        },
    },
    'required': ['text', 'grade']
}
