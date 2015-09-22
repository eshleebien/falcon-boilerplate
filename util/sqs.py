from boto3.session import Session


class SQS:
    def __init__(self, config):
        self.session = Session(aws_access_key_id=config['ACCESS_KEY'],
                               aws_secret_access_key=config['SECRET_ACCESS_KEY'],
                               region_name=config['REGION'])

        self.sqs = self.session.resource('sqs')
        self.queue = self.sqs.get_queue_by_name(QueueName=config['PRIORITY_QUEUE'])

    def set_queue(self, s_name):
        self.queue = self.sqs.get_queue_by_name(QueueName=s_name)

        return True

    def send_message(self, s_body, d_attributes):
        response = self.queue.send_message(MessageBody=s_body,
                                           MessageAttributes=d_attributes)

        return response

    def receive_message(self, l_attr_names, l_message_attr_names,
                        i_max_number_of_messages,
                        i_visibility_timeout,
                        i_waittimeseconds):

        message = self.queue.receive_messages(
                l_attr_names,
                l_message_attr_names,
                i_max_number_of_messages,
                i_visibility_timeout,
                i_waittimeseconds)

        return message
