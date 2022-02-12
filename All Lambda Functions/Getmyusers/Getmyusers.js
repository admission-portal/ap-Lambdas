const AWS = require("aws-sdk");

const dynamo = new AWS.DynamoDB.DocumentClient();

exports.handler = async (event, context) => {
  let body;
  let statusCode = 404;
  const headers = {
    "Content-Type": "application/json",
  };
  
body = await dynamo
            .get({
              TableName: "APStudents",
              Key: {
                "email": event['params']['querystring']['email'],
              }
            })
            .promise()
            if(!(Object.entries(body).length === 0))
            { 
              statusCode=200
              body={
                name:body.Item.name+" "+body.Item.lastname,
                nationality:body.Item.nationality,
                dob:body.Item.dob,
                timestamp:body.Item.timestamp,
                phone:body.Item.phone,
                gender:body.Item.gender,
                email:body.Item.email
                
              }}
              else
              body={message:"something went wrong !"};

 return JSON.stringify({
   statusCode,
   headers,
   body,
    
  });
};

// exports.handler = async (event) => {
//     // TODO implement
//     const response = {
//         statusCode: 200,
//         body: JSON.stringify('Hello from Lambda!'),
//     };
//     return response;
// };
