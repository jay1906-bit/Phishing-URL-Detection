"""
feature_extraction.py

This module is responsible for extracting phishing-related features
from a single URL. It acts as a bridge between low-level utility
functions (utils.py) and higher-level components like model training
and deployment.

Given a URL, this module produces a fixed-length numerical feature
vector that can be directly used by machine learning models.
"""

from . import utils
import numpy as np
class FeatureExtractor:
    def __init__(self,url):
        self.url = url
    def feature_vector(self):
        feature = np.array([

            utils.get_url_length(self.url),
            utils.has_ip_address(self.url),
            utils.count_hyphens(self.url),
            utils.dot_count(self.url),
            utils.count_at_symbols(self.url),
            utils.has_https(self.url),
            utils.count_subdomains(self.url),
            utils.flag_words_counts(self.url),
            utils.count_encoded_chars(self.url),
            utils.get_query_length(self.url)

        ])

        return feature


