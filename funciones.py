from datetime import datetime
import json


def load_json_dict(landing_path_configs: str):
    try:
        return json.loads(landing_path_configs)
    except Exception:
        print("Error! El archivo no existe.")


def periodos_relativos(meses, periodo_corriente):
    """Devuelve periodos en formato 'AAAAMM'."""
    return [periodo_corriente for _ in meses]


def transformar_datos(x):
    return x * 2
