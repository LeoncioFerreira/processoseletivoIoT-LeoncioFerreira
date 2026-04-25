"""
Arquivo de configuração global do sistema.

Centraliza constantes utilizadas no sistema, incluindo:
- Mapeamento de pinos (hardware)
- Limiares de estados (FSM)
- Parâmetros de tempo
- Regras de cálculo do desgaste

Facilita manutenção e ajustes sem alterar a lógica principal.
"""


class Config:
    # Hardware e pinos
    PIN_POTENTIOMETER = 34
    PIN_BUTTON = 14
    PIN_BUZZER = 23

    # Leds
    PIN_LED_GREEN = 32
    PIN_LED_YELLOW = 33
    PIN_LED_ORANGE = 25
    PIN_LED_RED = 26

    # Estados
    THRESHOLD_ATTENTION = 30
    THRESHOLD_ALERT = 55
    THRESHOLD_CRITICAL = 75

    # Tempo
    LOOP_INTERVAL_MS = 300
    DEBOUNCE_MS = 200

    # Regras de desgaste
    STRESS_HIGH_THRESHOLD = 65
    STRESS_LOW_THRESHOLD = 30

    # Parâmetros que controlam a dinâmica do desgaste
    WEAR_INCREASE_FACTOR = 0.2
    WEAR_DECREASE_VALUE = 0.5
    WEAR_OFFSET = 60
    HYSTERESIS = 5
