import json
from ibm_watson import VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('vdmUDa33QWw8VUut4IxuBQjGZHoGR3VS8Di56SFXNbi2')
visual_recognition = VisualRecognitionV3(
    version='2018-03-19',
    authenticator=authenticator
)

visual_recognition.set_service_url('https://api.us-south.visual-recognition.watson.cloud.ibm.com/instances/4b74b35a-5da0-42fd-ace7-80684dd59378')

def trainClassifier():
    with open('./with_mask.zip', 'rb') as masked, open(
            './without_mask.zip', 'rb') as unnmasked :
        model = visual_recognition.create_classifier(
            'masked',
            positive_examples={ 'masked':masked},
            negative_examples=unnmasked).get_result()
    print(json.dumps(model, indent=2))

def retrieveClassifier():
    classifier = visual_recognition.get_classifier(
    classifier_id='masked_277425930').get_result()
    print(json.dumps(classifier, indent=2))

def classifyImage():
    with open('./15.jpg', 'rb') as images_file:
        classes = visual_recognition.classify(
            images_file=images_file,
            threshold='0.6',
            owners=["me"]).get_result()
        print(json.dumps(classes, indent=2))

# trainClassifier()
retrieveClassifier()
classifyImage()