import config

from slack import WebClient
from slack.errors import SlackApiError

client = WebClient(token=config.SLACK_API_KEY)
try:
    response = client.users_list()
    print(response)
    response = client.chat_postMessage(
        channel='#общий',
        link_names=1,
        text="@someone please refresh document <https://phypartners.atlassian.net/wiki/spaces/MONITOR/pages/3592650900/Escalation+Schemes|Escalation Schemes>!")
except SlackApiError as e:
    # You will get a SlackApiError if "ok" is False
    assert e.response["ok"] is False
    assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
    print(f"Got an error: {e.response['error']}")