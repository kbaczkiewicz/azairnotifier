from typing import Union

from azairnotifier.application.command import CreateFlightSearchCommand, UpdateFlightSearchCommand
from azairnotifier.application.value import Parameters


class ParametersFactory:
    @staticmethod
    def from_command(command: Union[CreateFlightSearchCommand, UpdateFlightSearchCommand]) -> Parameters:
        parameters_dict = {
            'airport_from': command.main_source_airport + ' +(' + ', '.join(command.optional_source_airports) + ')',
            'airport_to': command.main_dest_airport + ' +(' + ', '.join(command.optional_dest_airports) + ')',
            'date_from': command.date_from,
            'date_to': command.date_to,
            'adult_passengers': command.adults,
            'child_passengers': command.children,
            'infant_passengers': command.infants,
            'min_days': command.min_days,
            'max_days': command.max_days,
            'max_changes': command.max_changes,
            'max_price': command.max_price
        }

        return Parameters.from_dict(**parameters_dict)