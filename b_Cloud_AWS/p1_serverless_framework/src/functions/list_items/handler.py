import json
import boto3
from boto3.dynamodb.conditions import key, Attr

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('items')

def list_items(event, context):
    try:
        # Consulta todos os itens na tabela DynamoDB com Suporte à paginação
        response = table.scan()
        items = response['Items']

        #verifica se há mais itens a serem escaneados
        while 'lastEvaluatedkey' in response:
            response = table.scan(ExclusiveStartKey=response['LastEvaLuatedKey'])
            items.exted(response['items'])

        return{
            'statusCode': 200,
            'body': json.dumps(items)
        }
    except Exception as e:
        return{
            'statusCode': 200,
            'body': json.dumps({'error': str(e)})
        }