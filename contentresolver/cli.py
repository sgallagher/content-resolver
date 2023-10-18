#!/usr/bin/python3

# This file is part of Content Resolver
# Copyright 2023 Red Hat, Inc.
# SPDX-License-Identifier: MIT

import argparse
import logging

from datetime import datetime

from . import config
from . import utils


logger = logging.getLogger(__name__)


def parse_cli_args():
    settings = {}

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "configs",
        help="Directory with YAML configuration files. Only files ending with '.yaml' are accepted.",
    )
    parser.add_argument("output", help="Directory to contain the output.")
    parser.add_argument(
        "--use-cache",
        dest="use_cache",
        action="store_true",
        help="Use local data instead of pulling Content Resolver. Saves a lot of time! Needs a 'cache_data.json' file at the same location as the script is at.",
    )
    parser.add_argument(
        "--dev-buildroot",
        dest="dev_buildroot",
        action="store_true",
        help="Buildroot grows pretty quickly. Use a fake one for development.",
    )
    parser.add_argument(
        "--dnf-cache-dir",
        dest="dnf_cache_dir_override",
        help="Override the dnf cache_dir.",
    )
    parser.add_argument(
        "--debug",
        dest="debug",
        action="store_true",
        help="Enable debug logging",
    )
    args = parser.parse_args()

    settings["configs"] = args.configs
    settings["output"] = args.output
    settings["use_cache"] = args.use_cache
    settings["dev_buildroot"] = args.dev_buildroot
    settings["dnf_cache_dir_override"] = args.dnf_cache_dir_override

    settings["root_log_deps_cache_path"] = "cache_root_log_deps.json"

    settings["max_subprocesses"] = 10

    settings["allowed_arches"] = ["armv7hl", "aarch64", "ppc64le", "s390x", "x86_64"]

    settings["weird_packages_that_can_not_be_installed"] = ["glibc32"]

    return settings


def main():
    # -------------------------------------------------
    # Stage 1: Data collection and analysis using DNF
    # -------------------------------------------------

    # measuring time of execution
    time_started = datetime.now()

    # Handle the command line arguments
    settings = parse_cli_args()

    logging.basicConfig(
        format="%(asctime)s : %(name)s : %(levelname)s : %(message)s",
        level=settings["log_level"],
    )

    settings["global_refresh_time_started"] = utils.format_datetime_template_string(
        time_started
    )

    # TODO: Enable cached data load here.

    configs = config.get_all_configs(settings["configs"])


if __name__ == "__main__":
    main()
