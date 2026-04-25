"""
Implementação da máquina de estados do sistema.

Define as transições entre os estados (NORMAL, ATTENTION, ALERT, CRITICAL)
com base no índice de desgaste. Também controla o comportamento no estado
crítico e o reset via botão.

Utiliza thresholds definidos no Config.
"""

from states import State
from config import Config


class StateMachine:
    def update(self, health, button_event):
        current = health.get_state()
        wear = health.get_wear_index()
        # Retenção do estado crítico até reset manual
        if current == State.CRITICAL:
            if button_event:
                health.reset_after_maintenance()
                return
            else:
                return

        # Estados
        if wear >= Config.THRESHOLD_CRITICAL:
            health.set_state(State.CRITICAL)

        elif wear >= Config.THRESHOLD_ALERT:
            health.set_state(State.ALERT)

        elif wear >= Config.THRESHOLD_ATTENTION:
            health.set_state(State.ATTENTION)

        elif wear < Config.THRESHOLD_ATTENTION - Config.HYSTERESIS:
            health.set_state(State.NORMAL)
