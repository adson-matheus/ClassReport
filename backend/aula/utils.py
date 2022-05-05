from datetime import datetime

def converter_para_datetime(data, horario):
    """
        Recebe um date e time e retorna uma datetime.
    """
    return datetime(year=data.year,
                    month=data.month,
                    day=data.day,
                    hour=horario.hour,
                    minute=horario.minute)
