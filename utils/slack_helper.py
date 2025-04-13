
import requests
import json
class SlackHelper:

    def send_slack_notification(self, message):
        slack_webhook_url = 'https://hooks.slack.com/services/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'  # Replace with your Slack webhook URL

        slack_payload = {
            'text': message  # This will be the message sent to your Slack channel
        }

        headers = {
            'Content-Type': 'application/json',
        }

        try:
            response = requests.post(slack_webhook_url, data=json.dumps(slack_payload), headers=headers)
            if response.status_code == 200:
                print("Error notification sent to Slack successfully!")
            else:
                print(f"Failed to send notification to Slack. Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error sending to Slack: {e}")