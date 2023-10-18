# This file is part of Content Resolver
# Copyright 2023 Red Hat, Inc.
# SPDX-License-Identifier: MIT


class ContentResolverConfigBase:
    def __init__(self, id, path, type, version):
        self.id = id
        self.path = path
        self.type = type
        self.version = version


def _null_load_config(document, allowed_arches):
    return ContentResolverConfigBase(
        id=document["doc_id"],
        path=document["doc_path"],
        type=document["document"],
        version=document["version"],
    )
