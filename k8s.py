from kubernetes import client, config
from kubernetes.client.rest import ApiException
import urllib3

urllib3.disable_warnings()


class Connection():

    def __init__(self, server, token):
        self.server = server
        self.token = token

    def openConnection(self):
        self.configuration = client.Configuration()
        self.configuration.host = self.server
        self.configuration.verify_ssl=False
        self.configuration.api_key={"authorization":"Bearer "+ self.token}
        self.client = client.Configuration.set_default(self.configuration)

    def k8Api(self):
        self.v1 = client.CoreV1Api()

    def getPods(self):
        self.pods = self.v1.list_pod_for_all_namespaces(watch=False)

