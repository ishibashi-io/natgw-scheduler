import os
import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    public_subnet_id = os.environ['PUBLIC_SUBNET_ID']
    eip_allocation_id = os.environ['EIP_ALLOCATION_ID']
    rtb_id = os.environ['RTB_ID']

    response = ec2.create_nat_gateway(
        AllocationId=eip_allocation_id,
        SubnetId=public_subnet_id
    )
    nat_id = response['NatGateway']['NatGatewayId']
    ec2.get_waiter('nat_gateway_available').wait(NatGatewayIds=[nat_id])

    response = ec2.create_route(
        DestinationCidrBlock = '0.0.0.0/0',
        NatGatewayId = nat_id,
        RouteTableId = rtb_id
    )
