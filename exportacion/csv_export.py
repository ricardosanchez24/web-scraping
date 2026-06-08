import csv
from typing import Optional


def exportar_a_csv(
    productos: list[dict],
    nombre_archivo: str = 'resultados.csv',
    encoding: str = 'utf-8-sig',
) -> Optional[str]:
    if not productos:
        print("No hay productos para exportar.")
        return None

    try:
        with open(nombre_archivo, 'w', newline='', encoding=encoding) as f:
            writer = csv.DictWriter(f, fieldnames=productos[0].keys())
            writer.writeheader()
            writer.writerows(productos)

        print(f"Datos exportados a {nombre_archivo}")
        return nombre_archivo
    except (OSError, PermissionError) as e:
        print(f"Error al exportar CSV: {e}")
        return None


def exportar_a_json(
    productos: list[dict],
    nombre_archivo: str = 'resultados.json',
) -> Optional[str]:
    import json

    if not productos:
        print("No hay productos para exportar.")
        return None

    try:
        with open(nombre_archivo, 'w', encoding='utf-8') as f:
            json.dump(productos, f, ensure_ascii=False, indent=2)

        print(f"Datos exportados a {nombre_archivo}")
        return nombre_archivo
    except (OSError, PermissionError) as e:
        print(f"Error al exportar JSON: {e}")
        return None
