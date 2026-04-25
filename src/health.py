"""
Módulo responsável pelo cálculo do índice de desgaste (wear_index).

Atualiza o desgaste com base no nível de estresse do sistema e define
a tendência (subindo, caindo ou estável). Também mantém o estado atual
e permite reset após condição crítica.
"""
from states import State
from config import Config


class Health:
    def __init__(self):
        self._wear_index = 0.0
        self._trend = "ESTAVEL"
        self._current_state = State.NORMAL

    def update(self, stress):
        if stress > Config.STRESS_HIGH_THRESHOLD:
            self._wear_index += ((stress - Config.WEAR_OFFSET)
                                 * Config.WEAR_INCREASE_FACTOR)
            self._trend = "SUBINDO"

        elif stress < Config.STRESS_LOW_THRESHOLD:
            self._wear_index -= Config.WEAR_DECREASE_VALUE
            self._trend = "CAINDO"

        else:
            self._trend = "ESTAVEL"

        self._wear_index = max(0.0, min(100.0, self._wear_index))

    # Getters
    def get_wear_index(self):
        return self._wear_index

    def get_trend(self):
        return self._trend

    def get_state(self):
        return self._current_state

    # Setters
    def set_state(self, new_state):
        self._current_state = new_state

    def reset_after_maintenance(self):
        self._wear_index = 0.0
        self._current_state = State.NORMAL
        self._trend = "ESTAVEL"
