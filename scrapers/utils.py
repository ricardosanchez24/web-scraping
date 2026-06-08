import re
from typing import Optional


def limpiar_precio(texto: Optional[str]) -> str:
    if not texto:
        return 'N/A'
    return re.sub(r'[^\d.,]', '', texto).strip()


def extraer_año(texto: Optional[str]) -> Optional[str]:
    if not texto:
        return None
    match = re.search(r'\b(19|20)\d{2}\b', texto)
    return match.group() if match else None


def limpiar_texto(texto: Optional[str]) -> str:
    if not texto:
        return 'N/A'
    return ' '.join(texto.split())
