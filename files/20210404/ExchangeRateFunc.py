import logging
import json

import azure.functions as func
from forex_python.converter import CurrencyRates


def main(req: func.HttpRequest) -> func.HttpResponse:
    
    logging.info('Demo ExchangeRate API Call - Get Available ExchangeRate.')
    currencyClient = CurrencyRates()

    supportRates = list(currencyClient.get_rates('USD').keys())
    supportRates.append('USD')
    
    respTxt = {}
    respTxt['supportedRates'] = supportRates
    return func.HttpResponse(body=json.dumps(respTxt))