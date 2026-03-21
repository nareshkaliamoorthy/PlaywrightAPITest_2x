from jsonschema import validate
import json

def validate_schema(response, schema_path):
    with open(schema_path) as json_file:
        schema = json.load(json_file)
    
    validate(response.json(),schema)
