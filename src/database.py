import os
import datetime 
import time
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
url_table = dynamodb.Table(os.environ.get('URL_TABLE'))
url_table_partition_key = os.environ.get('URL_TABLE_KEY')

def create_url_record(code: str, long_url: str):
    tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
    expiryDateTime = int(time.mktime(tomorrow.timetuple())) 
    url_table.put_item(
        Item={
            url_table_partition_key : code,
            'long_url': long_url,
            'ttl': expiryDateTime
        }
    )


def get_url_record(code: str):
    try:
        response = url_table.get_item(Key={url_table_partition_key: code})
    except ClientError as e:
        raise Exception(e.response['Error']['Message'])
    else:
        return response.get('Item')