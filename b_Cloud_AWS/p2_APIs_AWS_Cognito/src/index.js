var AWS = require('aws-sdk');
const dynamodb = new AWS.DynamoDB.DocumentClient();

exports.handler = async (event) => {
  let responseBody = "";
  let statusCode = 0;

  let { id, price } = JSON.parse(event.body);

  const params = {
    TableName: 'Items',
    Item: {
      id: id,
      price: price
    }
  };

  try {
    await dynamodb.put(params).promise();
    statusCode = 200;
    responseBody = JSON.stringify('Item inserido com sucesso!');
  } catch (err) {
    statusCode = 500;
    responseBody = JSON.stringify(err);
  }

  const response = {
    statusCode: statusCode,
    body: responseBody,
  };
  return response;
};
