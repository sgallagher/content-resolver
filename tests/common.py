# This file is part of Content Resolver
# Copyright 2023 Red Hat, Inc.
# SPDX-License-Identifier: MIT


import os
import pathlib


ALLOWED_ARCHES=[
    "aarch64",
    "ppc64le",
    "s390x",
    "x86_64",
]

test_config_base_dir = os.path.join(pathlib.Path(__file__).parent, "test_configs")

def get_test_config_dir(namespace):
    return os.path.join(test_config_base_dir, namespace)