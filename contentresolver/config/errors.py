# This file is part of Content Resolver
# Copyright 2023 Red Hat, Inc.
# SPDX-License-Identifier: MIT

from .. import ContentResolverError


class ConfigError(ContentResolverError):
    # Error in user-provided configs that will be ignored when not in strict
    # mode.
    pass


class ConfigCriticalError(ContentResolverError):
    # Error in user-provided configs that we cannot ignore
    pass
