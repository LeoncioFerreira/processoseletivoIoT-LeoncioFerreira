import time

"""
Utilitários para controle de tempo.

Fornece funções baseadas em ticks para cálculo de intervalos, controle
de execução periódica e geração de sinais intermitentes (blink),
sem uso de delays bloqueantes.
"""


class TimeUtils:
    @staticmethod
    def now():
        return time.ticks_ms()

    @staticmethod
    def elapsed(current, previous):
        return time.ticks_diff(current, previous)

    @staticmethod
    def is_interval_passed(current, previous, interval):
        return time.ticks_diff(current, previous) >= interval

    @staticmethod
    def blink(current, interval):
        return (current // interval) % 2 == 0
