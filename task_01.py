#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Simple examples of creating instances of a class."""

import produce

TOMATO = produce.Produce()
TOMATO_ARRIVAL = TOMATO.arrival

EGGPLANT = produce.Produce(1311210802)
EGGPLANT_EXPIRES = EGGPLANT.get_expiration()
