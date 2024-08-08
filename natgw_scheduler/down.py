import os

import boto3

client = boto3.client('ec2')

def lambda_handler(event, context):
    rtb_id = os.environ['RTB_ID']

    response = client.delete_route(
        DestinationCidrBlock = '0.0.0.0/0',
        RouteTableId = rtb_id
    )

    filters = [{'Name': 'state', 'Values': ['available']}]
    response = client.describe_nat_gateways(Filters=filters)
    for rec in response['NatGateways']:
        natgw = rec['NatGatewayId']
        client.delete_nat_gateway(NatGatewayId=natgw)

