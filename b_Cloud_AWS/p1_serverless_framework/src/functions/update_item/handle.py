import json
import boto3


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Items')

def update_item(event, context):
    body = json.loads(event['body'])
    item_id = body['item_id']  # Obtém o ID do item do corpo da solicitação
    description = body['description']  # Obtém a nova descrição do corpo da solicitação
    
    try:
        # Atualiza o item na tabela DynamoDB com a nova descrição
        response = table.update_item(
            Key={'ItemId': item_id},
            UpdateExpression="set Description=:d",
            ExpressionAttributeValues={
                ':d': description
            },
            ReturnValues="UPDATED_NEW"
        )

        return {
            'statusCode': 200,  
            'body': json.dumps(response['Attributes'])  
        }
    except Exception as e:
        return {
            'statusCode': 500,  
            'body': json.dumps({'error': str(e)})  
        }
