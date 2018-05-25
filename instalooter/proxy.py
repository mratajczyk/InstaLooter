import os

import logging
import verboselogs

logger = verboselogs.VerboseLogger(__name__)
logger.addHandler(logging.StreamHandler())


LOOTER_PROXY_KEY = 'LOOTER_PROXY'


def get_proxy():
    proxies = {}
    proxy_check = os.getenv(LOOTER_PROXY_KEY)
    if proxy_check:
        proxies = {
            'http': proxy_check,
            'https': proxy_check
        }
        logger.info('using proxy - {}'.format(proxy_check))
    return proxies
