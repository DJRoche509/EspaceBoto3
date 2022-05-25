import logging
import boto3
from botocore.exceptions import ClientError

#set up logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('ecpy_describe')


#Begin process for getting basic information about a instance
#create ec2 resource
ec2 = boto3.client('ec2')
#creating starts instance function
def describe_ec2instance(instance_id):
    try:
        response = ec2.describe_instances(InstanceIds=[instance_id])
        logger.info("Describing instance %s.", instance_id)
    except ClientError:
        logger.exception("couldn't describe instace %s.", instance_id)
        raise
    else:
        return response
#replace the parameter with your own instance id
response = describe_ec2instance('i-0e8b15d8e4ac82a03')
print(response)
#end process for getting basic information about a Ec2 instance


#Remove the ''' to unlock the codes below
'''
#Begin process to start a Ec2 instance ---------------------------------------------------
#create ec2 resource
ec2 = boto3.resource('ec2')
#creating starts instance function
def start_instance(instance_id):
    try:
        response = ec2.Instance(instance_id).start()
        logger.info("Started instance %s.", instance_id)
    except ClientError:
        logger.exception("couldn't start instance %s.", instance_id)
        raise
    else:
        return response
response = start_instance('i-0e8b15d8e4ac82a03')
#End process to start a Ec2 instance ------------------------------------------------
'''


#Begin process to check the status of a Ec2 instance ---------------------------------
'''
#create ec2 client
ec2 = boto3.client('ec2')
#creating starts instance function
def describe_ec2instance_state(instance_id):
    try:
        response1 = ec2.describe_instances(InstanceIds=[instance_id])
        logger.info("Describing instance status $s.", instance_id)
    except ClientError:
        logger.exception("couldn't describe instance status %s.", instance_id)
        raise
    else:
        return response1
response = describe_ec2instance_state('i-0e8b15d8e4ac82a03')
print(response)

#End process to check the status of a Ec2 instance ----------------------------------
'''


#Begin process to stop a Ec2 instance -----------------------------------------------------

#create ec2 resource
'''ec2 = boto3.resource('ec2')

#creating starts instance function
def stop_instance(instance_id):
    try:
        response = ec2.Instance(instance_id).stop()
        logger.info("Stopped instance %s.", instance_id)
    except ClientError:
        logger.exception("couldn't stop instance %s.", instance_id)
        raise
    else:
        return response

response = stop_instance('i-0e8b15d8e4ac82a03')
print(response) '''
#End process to stop a Ec2 instance -------------------------------------------------------