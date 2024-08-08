import json

data = {
    "items":[
            {"id":1,"name":"test","price":100},
            {"id":2,"name":"test2","price":200},
    ]
}

def lambda_handler(event, context):

    http_method = event['httpMethod']
    if http_method == 'GET':
        return {
            'statusCode': 200,
            'body': json.dumps(data)
        }
    elif http_method == 'POST':
        body = json.loads(event["body"])
        data["items"].append(body)
        response = {
            'statusCode': 200,
            'body': json.dumps(data)
        }
        return response
    elif http_method == 'PUT':
        body = json.loads(event["body"])
        for item in data["items"]:
             if item["id"] == body["id"]:
                 item.update(body)
                 break                 
        response = {
            'statusCode': 200,
            'body': json.dumps(data)
        }
        return response
    elif http_method == 'DELETE':
        body = json.loads(event["body"])
        for item in data["items"]:
             if item["id"] == body["id"]:
                 data["items"].remove(item)
                 break                 
        response = {
            'statusCode': 200,
            'body': json.dumps(data)
        }
        return response
    else:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Unsupported method'})
        }