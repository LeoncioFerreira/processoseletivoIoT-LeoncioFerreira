from machine import Pin, ADC
from config import Config

"""
Módulo de leitura do potenciômetro.

Realiza leitura analógica do sensor e aplica suavização (média móvel)
para reduzir ruídos, retornando um valor de estresse normalizado (0–100).
"""


class Potentiometer:
    def __init__(self):
        self._adc = ADC(Pin(Config.PIN_POTENTIOMETER))
        self._adc.atten(ADC.ATTN_11DB)
        self._readings = []

    def _read_raw(self):
        return self._adc.read()

    def read_smoothed(self):
        raw = self._read_raw()
        value = (raw / 4095.0) * 100

        self._readings.append(value)

        if len(self._readings) > 5:
            self._readings.pop(0)

        return sum(self._readings) / len(self._readings) if self._readings else 0
