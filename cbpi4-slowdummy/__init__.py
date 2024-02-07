# -*- coding: utf-8 -*-
import asyncio
import random
import logging
from cbpi.api import *
from cbpi.api.base import CBPiBase
from cbpi.api.dataclasses import Kettle, Props, Fermenter

@parameters([])
class SlowDummy(CBPiSensor):

    def __init__(self, cbpi, id, props):
        super(SlowDummy, self).__init__(cbpi, id, props)
        self.value = 0  # Initial Value
        self.phase = 1  # Initial phase -1 = decrease, 0 = stable, 1 = increase
        self.phase_cycles = 0
        self.phase_cycle_max = random.randint(20, 60)  # Initial maximum cycles for a phase

    async def run(self):
        while self.running:
            if self.phase > 0:  # Increase
                self.value += random.randint(0, 10) / 10

            # For stable phase, no need to adjust self.value

            if self.phase < 0:  # Decrease
                self.value -= random.randint(0, 10) / 10

            self.phase_cycles += 1

            # Transition to new phase if cycle limit is reached
            if self.phase_cycles > self.phase_cycle_max:
                self.phase_cycles = 0
                self.phase_cycle_max = random.randint(20, 60)  # Randomize the max cycles for next phase
                self.phase -= 1
                if self.phase < -1:
                    self.phase = 1

            self.log_data(self.value)
            self.push_update(self.value)
            await asyncio.sleep(1)

    def get_state(self):
        return dict(value=self.value)

def setup(cbpi):
    cbpi.plugin.register("SlowDummy", SlowDummy)