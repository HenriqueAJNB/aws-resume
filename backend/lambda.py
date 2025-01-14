import boto3
from botocore.exceptions import ClientError


def lambda_handler(event, context):
    table_name = "PageHits"
    # Replace 'YourPrimaryKey' with your table's primary key attribute name
    primary_key = "PageID"
    # Replace 'YourPrimaryKeyValue' with the primary key value of the record to update
    primary_key_value = "hits"
    # Replace 'visitor_count' with the name of the attribute to increment
    count_attribute = "visitor_count"

    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(table_name)

    try:
        # Update the visitor count
        response = table.update_item(
            Key={primary_key: primary_key_value},
            UpdateExpression=f"SET {count_attribute} = if_not_exists({count_attribute}, :start) + :inc",
            ExpressionAttributeValues={
                ":start": 0,  # Default value if attribute does not exist
                ":inc": 1,  # Increment by 1
            },
            ReturnValues="UPDATED_NEW",
        )

        # Return the new count
        return {
            "statusCode": 200,
            "body": {
                "message": "Visitor count updated successfully",
                "new_count": response["Attributes"][count_attribute],
            },
        }

    except ClientError as e:
        return {
            "statusCode": 500,
            "body": f"Error updating visitor count: {e.response['Error']['Message']}",
        }
