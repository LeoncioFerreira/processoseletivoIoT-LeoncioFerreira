"""
Módulo de leitura do botão com debounce.

Detecta eventos de pressionamento evitando leituras falsas causadas por
ruído elétrico. Retorna eventos discretos (cliques) para uso na lógica
do sistema.
"""

from machine import Pin
from config import Config
from time_utils import TimeUtils


class Button:
    def __init__(self):
        self._pin = Pin(Config.PIN_BUTTON, Pin.IN, Pin.PULL_DOWN)
        self._last_time = 0
        self._previous_state = 0  # solto = 0

    def read_event(self, now):
        current = self._pin.value()
        event = False

        # pressionado = 1
        if current == 1 and self._previous_state == 0:
            if TimeUtils.elapsed(now, self._last_time) > Config.DEBOUNCE_MS:
                event = True
                self._last_time = now

        self._previous_state = current
        return event
