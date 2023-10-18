# This file is part of Content Resolver
# Copyright 2023 Red Hat, Inc.
# SPDX-License-Identifier: MIT


import logging
import os
import yaml

from .errors import ConfigError
from .base import _null_load_config

doctype_dispatcher = {
    # Special doctype containing an empty data section for tests
    "base": _null_load_config,
}

logger = logging.getLogger(__name__)


def _validate_document_header(document):
    if "document" not in document:
        raise ConfigError(f"{document['doc_path']} does not specify the document type.")

    if document["document"] not in doctype_dispatcher:
        raise ConfigError(
            f"{document['doc_path']} has unknown document type: {document['document']}"
        )

    if "version" not in document:
        raise ConfigError(
            f"{document['doc_path']} does not specify the document version."
        )

    if "data" not in document:
        raise ConfigError(f"{document['doc_path']} does not contain a 'data' section.")


def _read_config_file(path):
    try:
        with open(path, "r") as file:
            document = yaml.safe_load(file)
    except yaml.YAMLError as err:
        raise ConfigError(f"{path} is unparseable") from err

    document["doc_path"] = path
    document["doc_id"] = os.path.basename(path).rsplit(".yaml", maxsplit=1)[0]

    # Call the validation function. No need to check its return value; it
    # will raise a ConfigError if it fails. We will pass that back directly.
    _validate_document_header(document)

    return document


def load_config(path, allowed_arches):
    """
    Read the config file from disk, validate its contents and return the
    parsed document as an appropriate subclass of ContentResolverConfig.
    """
    try:
        document = _read_config_file(path)
    except ConfigError as err:
        logger.debug(f"Failed to parse the document header for {path}")
        raise

    return doctype_dispatcher[document["document"]](
        document, allowed_arches=allowed_arches
    )
