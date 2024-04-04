import boto3
import logging
import time

def send_to_cloudwatch_log_group(log_group_name, log_stream_name, log_data):
    try:
        # Initialize Boto3 CloudWatch Logs client
        client = boto3.client('logs')

                                                                                    # Put log event to CloudWatch Logs log stream
        response = client.put_log_events(
        logGroupName=log_group_name,
        logStreamName=log_stream_name,
        logEvents=[
            {
                'timestamp': int(round(time.time() * 1000)),
                'message': log_data
            }
            ]
        )
        logging.info("Data sent to CloudWatch Logs successfully")
    except Exception as e:
        logging.error(f"Failed to send data to CloudWatch Logs: {e}")
if __name__ == "__main__":
            # Set up logging
    logging.basicConfig(level=logging.INFO)

                        # Example usage
    log_group_name = 'Test'
    log_stream_name = 'logs'
    log_data = 'Redux Test log 2 for logs '

    send_to_cloudwatch_log_group(log_group_name, log_stream_name, log_data)
