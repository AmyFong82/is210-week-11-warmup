#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A class that returns time."""

import time


class Snapshot(object):
    """Object that gives snapshots of time."""

    def __init__(self):
        """Constructor for Snapshot class.

        Attributes:
            created (float): returns the current Unix Timestamp.
        """
        self.created = time.time()
