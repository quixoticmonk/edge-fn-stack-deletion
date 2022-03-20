import json
import boto3
from datetime import datetime, timedelta

client = boto3.client('cloudformation')

def lambda_handler(event, context):
    response= client.list_stacks(StackStatusFilter=['DELETE_FAILED'])
    num_stacks, stacks_to_delete = 0, []
    for stack in response["StackSummaries"]:
        if((datetime.now().date() - stack["DeletionTime"].date()).days > 0): # Edge functions -  usually take 24 hours for replicated instances to be available for deletion
            stacks_to_delete.append(stack["StackName"])
            num_stacks +=1
            client.delete_stack(
                StackName=stack["StackName"]
                )
    
    return {
        "stacks_deleted" : stacks_to_delete,
        "number_of_stacks": num_stacks
    }
