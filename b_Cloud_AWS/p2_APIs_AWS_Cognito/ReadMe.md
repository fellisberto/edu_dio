# DIO Live Coding Activity - 17/11/2021

## Serviços AWS Utilizados
- **Amazon Cognito**
- **Amazon DynamoDB**
- **Amazon API Gateway**
- **AWS Lambda**

## Etapas de Desenvolvimento

### 1. Criando uma API REST no Amazon API Gateway
1. Navegue para o **Dashboard do API Gateway** -> **Create API** -> **REST API** -> **Build**.
2. Selecione **Protocol** - REST -> **Create New API**.
3. Nomeie a API como [dio_live_api] -> Selecione **Endpoint Type** como Regional -> **Create API**.
4. Vá para **Resources** -> **Actions** -> **Create Resource**.
5. Nomeie o **Resource** como [Items] -> **Create Resource**.

### 2. Configurando o Amazon DynamoDB
1. No **Dashboard do DynamoDB** -> **Tables** -> **Create Table**.
2. Nomeie a tabela como [Items] -> Defina **Partition Key** como [id] -> **Create Table**.

### 3. Configurando o AWS Lambda
1. No **Dashboard do Lambda** -> **Create Function**.
2. Nomeie a função como [put_item_function] -> **Create Function**.
3. Insira o código da função `put_item_function.js` disponível na pasta `/src` -> **Deploy**.
4. Acesse **Configuration** -> **Execution Role** -> Abra a **Role** no console do IAM.
5. No IAM -> **Roles** -> Selecione a role criada -> **Permissions** -> **Add Inline Policy**.
6. Escolha **Service** - DynamoDB -> **Manual Actions** -> **Add Actions** -> **putItem**.
7. Adicione o **arn** da tabela criada no DynamoDB -> **Add** -> **Review Policy**.
8. Nomeie a política como [lambda_dynamodb_putItem_policy] -> **Create Policy**.

### 4. Integrando o API Gateway com Lambda
1. No **Dashboard do API Gateway** -> Selecione a API criada -> **Resources** -> Selecione o recurso criado -> **Action** -> **Create Method** - `POST`.
2. Defina **Integration Type** como `Lambda Function` -> **Use Lambda Proxy Integration**.
3. Selecione a função Lambda criada -> **Save**.
4. Vá para **Actions** -> **Deploy API** -> Defina **Deployment Stage** como **New Stage [dev]** -> **Deploy**.

### 5. Testando com POSTMAN
1. Adicione uma requisição -> Defina **Method** como `POST` -> Copie o **Endpoint Gerado** no API Gateway.
2. Navegue para **Body** -> **Raw** -> **JSON** e adicione o seguinte body:
```json
{
  "id
