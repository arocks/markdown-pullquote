# -*- coding: utf-8 -*-
from mdx_pullquote.extension import PullQuoteExtension


def makeExtension(configs=None):

    if isinstance(configs, list):
        configs = dict(configs)
    return PullQuoteExtension(configs=configs)
