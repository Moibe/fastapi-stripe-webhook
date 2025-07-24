from datetime import datetime
import pytz
import os

def imprimeTime(): 
    """
    Devuelve la fecha y hora actual en la zona horaria de la Ciudad de México (GMT-6).
    """
    # 1. Definir la zona horaria de la Ciudad de México
    # Puedes usar 'America/Mexico_City' para que pytz maneje el horario de verano automáticamente.
    mexico_city_tz = pytz.timezone('America/Mexico_City')

    # 2. Obtener la hora actual en UTC
    utc_now = datetime.now(pytz.utc)

    # 3. Convertir la hora UTC a la zona horaria deseada
    mexico_city_now = utc_now.astimezone(mexico_city_tz)

    # 4. Formatear la fecha y hora
    # El formato que deseas es "YYYY-MM-DD HH:MM:SS"
    formatted_time = mexico_city_now.strftime("%Y-%m-%d %H:%M:%S")

    return formatted_time

def registrar_evento(event_type: str):
    """
    Guarda la fecha y hora actual junto con un tipo de evento
    en un archivo 'registro.txt' en la raíz del proyecto.

    Args:
        event_type (str): Una descripción del tipo de evento a registrar.
    """
    # 1. Obtener la fecha y hora actual en el formato deseado
    fecha = imprimeTime() # Utiliza tu función existente

    # 2. Definir el nombre del archivo de registro
    file_name = "registro.txt"

    # 3. Obtener la ruta completa al archivo en la raíz del proyecto
    # Esto asume que el script que llama a esta función está en la raíz.
    script_dir = os.path.dirname(os.path.abspath(__file__))
    registro_path = os.path.join(script_dir, file_name)

    # 4. Formatear la línea que se guardará en el archivo
    # Puedes elegir el formato que prefieras. Un buen formato sería CSV o algo legible.
    # Por ejemplo: "FECHA_HORA,TIPO_DE_EVENTO\n"
    log_line = f"{fecha},{event_type}\n"

    # 5. Abrir el archivo en modo de añadir ('a') y escribir la línea
    try:
        with open(registro_path, 'a') as f:
            f.write(log_line)
        print(f"[{fecha}] Evento '{event_type}' registrado con éxito en '{registro_path}'")
    except Exception as e:
        print(f"Error al escribir en el archivo de registro '{registro_path}': {e}")
