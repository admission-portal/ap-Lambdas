const AWS = require("aws-sdk");

const dynamo = new AWS.DynamoDB.DocumentClient();

exports.handler = async (event, context) => {
  let body='';
  let statusCode = 200;
  const headers = {
    "Content-Type": "application/json",
   
  };
try {
  let requestJSON = event;
        await dynamo
          .put({
            TableName: "APStudents",
           
            Item: {
              "email": requestJSON.email,
              "name": requestJSON.name,
              "lastname":requestJSON.lastname,
              "phone": requestJSON.phone,
              "dob" : requestJSON.dob,
              "gender": requestJSON.gender,
              "nationality":requestJSON.nationality,
              "timestamp":requestJSON.timestamp
 
            }
          })
          .promise();
      }
      finally{
        body = "Over";
      }

    return {
    statusCode,
    body,
    headers
  };      
};

