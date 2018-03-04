import alexa_mood_news
import json

true = True
false = False


def lambda_handler(event, context):
    print(event)
    if (event['session']['application']['applicationId'] !=
            "amzn1.ask.skill.fd82cf53-4bc6-4ea3-8ebd-c3ffcdf43151"):
        raise ValueError("Invalid Application ID")
    if event["session"]["new"]:
        on_session_started({"requestId": event["request"]["requestId"]}, event["session"])
    if event["request"]["type"] == "LaunchRequest":
        return on_launch(event["request"], event["session"])
    elif event["request"]["type"] == "IntentRequest":
        return on_intent(event["request"], event["session"])
    elif event["request"]["type"] == "SessionEndedRequest":
        return on_session_ended(event["request"], event["session"])


def on_session_started(session_started_request, session):
    print("Starting new session.")


def on_launch(launch_request, session):
    return "Hello, how are you feeling today?"


def on_intent(intent_request, session):
    intent = intent_request["intent"]
    intent_name = intent["name"]
    print(intent_name)
    if intent_name == "AngerIntent":
        return build_response({}, alexa_mood_news.share_anger())
    elif intent_name == "NoneIntent":
        return alexa_mood_news.none_intent()
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    print("Ending session.")


def handle_session_end_request():
    card_title = "Mood News Exit"
    speech_output = "Thank you for using Mood News!"
    should_end_session = True
    return build_response({}, build_speechlet_response(card_title, speech_output, None, should_end_session))


def get_welcome_response():
    session_attributes = {}
    card_title = "Mood News"
    speech_output = "Welcome to Mood News. " \
                    "How are you feeling?"
    reprompt_text = "Please name a feeling you are expereiencing... " \
                    "My developers gave me the ability to understand " \
                    "Anger, Fear, Joy, Sadness, and a few other special feelings"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        "outputSpeech": {
            "type": "PlainText",
            "text": output
        },
        "card": {
            "type": "Simple",
            "title": title,
            "content": output
        },
        "reprompt": {
            "outputSpeech": {
                "type": "PlainText",
                "text": reprompt_text
            }
        },
        "shouldEndSession": should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        "version": "1.0",
        "sessionAttributes": session_attributes,
        "response": speechlet_response
    }


# if __name__ == '__main__':
#     d = {
#   "session": {
#     "new": true,
#     "sessionId": "SessionId.2c36482b-6fc2-4d69-9fe0-2de6ac337ced",
#     "application": {
#       "applicationId": "amzn1.ask.skill.fd82cf53-4bc6-4ea3-8ebd-c3ffcdf43151"
#     },
#     "attributes": {},
#     "user": {
#       "userId": "amzn1.ask.account.AH3EFUGZE7U3C2DTHKOEJQUJCLUA4VTTZQ2AEJ3B6BHBXFY7RZ3ND5AR553YRJG65Y5SU73NEOUGW26VQ4X63BZIPI3T74EOACESA7FKIIAL5OEDAMW5FAHRI56TVZJD4PJ4BRMBNU4GNS4JDZZPNVAF466MZ4ZKZGVYU456PRPEA7RZRA7DP22MO4JVBRNHKZKXNXSZH5ET7NA"
#     }
#   },
#   "request": {
#     "type": "IntentRequest",
#     "requestId": "EdwRequestId.47fd5d71-c636-4bc2-b91c-3214d3042c0b",
#     "intent": {
#       "name": "AMAZON.StopIntent",
#       "slots": {}
#     },
#     "locale": "en-US",
#     "timestamp": "2018-03-04T00:29:26Z"
#   },
#   "context": {
#     "AudioPlayer": {
#       "playerActivity": "IDLE"
#     },
#     "System": {
#       "application": {
#         "applicationId": "amzn1.ask.skill.fd82cf53-4bc6-4ea3-8ebd-c3ffcdf43151"
#       },
#       "user": {
#         "userId": "amzn1.ask.account.AH3EFUGZE7U3C2DTHKOEJQUJCLUA4VTTZQ2AEJ3B6BHBXFY7RZ3ND5AR553YRJG65Y5SU73NEOUGW26VQ4X63BZIPI3T74EOACESA7FKIIAL5OEDAMW5FAHRI56TVZJD4PJ4BRMBNU4GNS4JDZZPNVAF466MZ4ZKZGVYU456PRPEA7RZRA7DP22MO4JVBRNHKZKXNXSZH5ET7NA"
#       },
#       "device": {
#         "supportedInterfaces": {}
#       }
#     }
#   },
#   "version": "1.0"
# }
#     print(lambda_handler(d, None))