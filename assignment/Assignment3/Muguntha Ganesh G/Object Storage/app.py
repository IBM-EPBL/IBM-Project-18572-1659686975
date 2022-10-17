from flask import Flask, render_template#
import ibm_boto3#ibm cloud docs
from ibm_botocore.client import Config, ClientError

# Constants for IBM COS values
COS_ENDPOINT = "https://s3.jp-tok.cloud-object-storage.appdomain.cloud" # Current list avaiable at https://control.cloud-object-storage.cloud.ibm.com/v2/endpoints
COS_API_KEY_ID = "K_hQjPtnabMlWG5WQjR6FozZn6KY6yC3YsQw5P_Uway2" # eg "W00YixxxxxxxxxxMB-odB-2ySfTrFBIQQWanc--P3byk"
COS_INSTANCE_CRN = "crn:v1:bluemix:public:iam-identity::a/70a51d17728e4a559f7518b1ef232006::serviceid:ServiceId-109f9da0-b2c8-4e1f-b352-f199bd96bced" # eg "crn:v1:bluemix:public:cloud-object-storage:global:a/3bf0d9003xxxxxxxxxx1c3e97696b71c:d6f04d83-6c4f-4a62-a165-696756d63903::"

# Create resource
cos = ibm_boto3.resource("s3",
    ibm_api_key_id=COS_API_KEY_ID,
    ibm_service_instance_id=COS_INSTANCE_CRN,
    config=Config(signature_version="oauth"),
    endpoint_url=COS_ENDPOINT
)#ibm cloud docs till

def get_bucket_contents(bucket_name):
    print("Retrieving bucket contents from: {0}".format(bucket_name))
    try:#
        files = cos.Bucket(bucket_name).objects.all()
        contents=[]
        for file in files:
            print("Item: {0} ({1} bytes).".format(file.key, file.size))
            contents.append(file.key)
        return contents#
    except ClientError as be:
        print("CLIENT ERROR: {0}\n".format(be))
    except Exception as e:
        print("Unable to retrieve bucket contents: {0}".format(e))
#
app=Flask(__name__)

@app.route('/')
def index():
    files=get_bucket_contents('nutrition-assistant-application-logavanan')
    return render_template('index.html',files=files)

app.run(debug=True)#