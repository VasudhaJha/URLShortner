import os
import boto3

table_name = os.environ.get('URL_TABLE')
partition_key = os.environ.get('URL_TABLE_KEY')
dynamodb = boto3.resource('dynamodb')

def create_table():
    
    dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {
                'AttributeName': partition_key,
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': partition_key,
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

if __name__ == "__main__":
    create_table()
    


