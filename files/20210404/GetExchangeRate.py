import logging
import json

import azure.functions as func
from forex_python.converter import CurrencyRates


def main(req: func.HttpRequest) -> func.HttpResponse:
    
    currentRate = req.params.get('current')
    targetRate = req.params.get('target')

    if not currentRate or not targetRate:        
        return func.HttpResponse(" Empty Value from Exchange Rate Demo !", status_code=200)

    logging.info('Get Exchange Rate with %s and %s', currentRate, targetRate)

    currencyClient = CurrencyRates()

    respTxt = {}
    respTxt['targetRate'] = currencyClient.get_rate(currentRate, targetRate)
    logging.info('Target Exchange Rate is %s', str(respTxt['targetRate']))

    return func.HttpResponse(body=json.dumps(respTxt))