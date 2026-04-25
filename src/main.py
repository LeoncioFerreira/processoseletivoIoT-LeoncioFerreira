"""
Arquivo principal do sistema.

Responsável por inicializar os componentes e executar o loop principal
não-bloqueante. Realiza leitura de sensores, atualização da lógica de desgaste,
transições de estado (FSM) e controle de atuadores.

Utiliza controle de tempo baseado em ticks para garantir execução periódica
sem uso de delays bloqueantes.
"""

from health import Health
from fsm import StateMachine
from config import Config
from states import State
from button import Button
from potentiometer import Potentiometer
from output import OutputController
from time_utils import TimeUtils


def main():
    health = Health()
    fsm = StateMachine()
    button = Button()
    potentiometer = Potentiometer()
    output = OutputController()

    last_loop = TimeUtils.now()
    button_event_pending = False

    print("Teste")  # Saída obrigatória para validação do CI
    while True:
        now = TimeUtils.now()

        button_event_pending |= button.read_event(now)

        if not TimeUtils.is_interval_passed(now, last_loop, Config.LOOP_INTERVAL_MS):
            continue

        last_loop = now

        stress = potentiometer.read_smoothed()

        is_critical = health.get_state() == State.CRITICAL

        if not is_critical:
            health.update(stress)

        fsm.update(health, button_event_pending)
        button_event_pending = False

        print(f"[{health.get_state()}] Desgaste: {health.get_wear_index():.1f}/100 | Tendência: {health.get_trend()}")

        output.update(health)


main()
