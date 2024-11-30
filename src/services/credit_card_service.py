from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from utils.Config import Config

def analize_credit_card(file):
    credential = AzureKeyCredential(Config.KEY)

    document_Client = DocumentIntelligenceClient(Config.ENDPOINT, credential)

    card_info = document_Client.begin_analyse_document(
        "prebuilt-creditCard", AnalyzeDocumentRequest(url_source=card_url))
    result = card_info.result()

    for document in result.documents:
        fields = document.get('fields', {})

        return {
            "card-name": fields.get('CardHolderName', {}).get('content'),
            "card-number": fields.get('CardHolderName', {}).get('content'),
            "expiry-date": fields.get('CardHolderName', {}).get('content'),
            "bank-name": fields.get('CardHolderName', {}).get('content'),
        }
