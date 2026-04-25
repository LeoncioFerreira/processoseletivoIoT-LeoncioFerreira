"""
Definição dos estados possíveis do sistema.

Contém as constantes utilizadas pela máquina de estados para representar
os diferentes níveis de desgaste.
"""


class State:
    NORMAL = "NORMAL"
    ATTENTION = "ATTENTION"
    ALERT = "ALERT"
    CRITICAL = "CRITICAL"
