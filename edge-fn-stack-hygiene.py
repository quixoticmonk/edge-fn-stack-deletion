import json
import boto3
from datetime import datetime, timedelta

client = boto3.client('cloudformation')

def lambda_handler(event, context):
  response = client.list_stacks(StackStatusFilter=['DELETE_FAILED'])
  num_stacks, stacks_to_delete = 0 , []
  for stack in response["StackSummaries"]:
    
