from machine import Pin, PWM
from states import State
from config import Config
from time_utils import TimeUtils

"""
Controle de atuadores do sistema.

Gerencia LEDs e buzzer com base no estado atual do sistema, indicando
visualmente e sonoramente o nível de desgaste.
"""


class OutputController:
    def __init__(self):
        self._leds = {
            "green": Pin(Config.PIN_LED_GREEN, Pin.OUT),
            "yellow": Pin(Config.PIN_LED_YELLOW, Pin.OUT),
            "orange": Pin(Config.PIN_LED_ORANGE, Pin.OUT),
            "red": Pin(Config.PIN_LED_RED, Pin.OUT),
        }
        self._buzzer = PWM(Pin(Config.PIN_BUZZER), freq=1000, duty=0)

    def update(self, health):
        current = health.get_state()
        # Leds
        for led in self._leds.values():
            led.value(0)

        if current == State.NORMAL:
            self._leds["green"].value(1)

        elif current == State.ATTENTION:
            self._leds["yellow"].value(1)

        elif current == State.ALERT:
            self._leds["orange"].value(1)

        elif current == State.CRITICAL:
            self._leds["red"].value(1)

        # Buzzer
        if current == State.CRITICAL:
            self._buzzer.duty(512)
        else:
            self._buzzer.duty(0)
