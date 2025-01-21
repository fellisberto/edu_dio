import json
import boto3
from src.models import ItemModel 
from src.utils import helper_function #função auxiliar definida em utils (exemplo)!

# inicializa o recurso DynamoDB usando Boto3
dynamodb = boto3.recurse('dynamodb')
table = dynamodb.Table('Items')

def add_item(event, conext):
    # Convertendo o corpo da solicitação JSON para um dicionario python
    body = json.loads(event['body'])

    #cria um item a ser adicionado na tabela usando o modelo ItemModel
    item = {
        'ItemId': body['item_id'], 
        'Description': body['description']
    }

    # Adiciona o item na tabela!
    table.put_item(Item=item)
    
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Item adicionado com sucesso!'})
    }