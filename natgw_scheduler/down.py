import os

import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    rtb_id = os.environ['RTB_ID']

    response = ec2.delete_route(
        DestinationCidrBlock = '0.0.0.0/0',
        RouteTableId = rtb_id
    )

    filters = [{'Name': 'state', 'Values': ['available']}]
    response = ec2.describe_nat_gateways(Filters=filters)
    for rec in response['NatGateways']:
        natgw = rec['NatGatewayId']
        ec2.delete_nat_gateway(NatGatewayId=natgw)

