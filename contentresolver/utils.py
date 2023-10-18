# This file is part of Content Resolver
# Copyright 2023 Red Hat, Inc.
# SPDX-License-Identifier: MIT

from datetime import datetime


def format_datetime_console_string(dtime):
    return dtime.strftime("%m/%d/%Y, %H:%M:%S")


def format_datetime_template_string(dtime):
    return dtime.strftime("%-d %B %Y %H:%M UTC")
