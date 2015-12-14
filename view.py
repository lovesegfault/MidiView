#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

import pygame
import pygame.midi

pygame.midi.init()
input_id = 3
i = pygame.midi.Input(input_id)

while(True):
    if i.poll():
        midi_events = i.read(20)
        print(midi_events[0][0][1])
