import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.table('items')

def get_item_id(event, context):
    # Obtém  o ID do item dos parâmetros do caminho
    item_id = event['pathParameters']['id']

    try:
        # Consulta o item na tabela DynamoDB usando o ID fornecido
        response = table.get_item(key={'ItemId': item_id})
        item_id = response.get('Item')

        if item:
            return {
                'statusCode': 200, # 
                'body': json.dumps(item) 
            }
        else: 
            return { 
                'statusCode': 404, 
                'body': json.dumps({'error': 'Item not found'})
            }
    except Exception as e: 
        return { 
            'statusCode': 500, 
            'body': json.dumps({'error': str(e)}) 
        }