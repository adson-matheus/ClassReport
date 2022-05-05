from datetime import date, datetime

def converter_para_datetime(data, horario):
    """
        Recebe um date e time e retorna uma datetime.
    """
    return datetime.combine(date=data, time=horario)

def converter_de_datetime(date_time):
    data = datetime.date(date_time)
    hora = datetime.time(date_time)
    return data, hora
