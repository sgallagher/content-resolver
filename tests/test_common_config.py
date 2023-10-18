# This file is part of Content Resolver
# Copyright 2023 Red Hat, Inc.
# SPDX-License-Identifier: MIT

import os
import unittest

import contentresolver.config
import contentresolver.config.errors
import contentresolver.config.base

from . import common

allowed_arches = [
    "aarch64",
    "ppc64le",
    "s390x",
    "x86_64",
]

class TestContentResolverCommonConfig(unittest.TestCase):
    def test_read_config_file_valid(self):
        config_path = os.path.join(common.get_test_config_dir("common"), "header-valid.yaml")

        document = contentresolver.config._read_config_file(config_path)
        self.assertEqual(document["doc_path"], config_path)
        self.assertEqual(document["doc_id"], "header-valid")

    def test_read_config_file_missing_doc(self):
        config_path = os.path.join(common.get_test_config_dir("common"), "missing-doc.yaml")

        with self.assertRaises(contentresolver.config.errors.ConfigError):
            contentresolver.config._read_config_file(config_path)

    def test_read_config_file_missing_version(self):
        config_path = os.path.join(common.get_test_config_dir("common"), "missing-version.yaml")

        with self.assertRaises(contentresolver.config.errors.ConfigError):
            contentresolver.config._read_config_file(config_path)

    def test_read_config_file_missing_version(self):
        config_path = os.path.join(common.get_test_config_dir("common"), "missing-data.yaml")

        with self.assertRaises(contentresolver.config.errors.ConfigError):
            contentresolver.config._read_config_file(config_path)

    def test_load_config_base(self):
        config_path = os.path.join(common.get_test_config_dir("common"), "base.yaml")

        cfgobj = contentresolver.config.load_config(config_path, allowed_arches=allowed_arches)

        self.assertIsInstance(cfgobj, contentresolver.config.base.ContentResolverConfigBase)
        self.assertEqual(cfgobj.path, config_path)
        self.assertEqual(cfgobj.id, "base")
        self.assertEqual(cfgobj.type, "base")
        self.assertEqual(cfgobj.version, 1)
