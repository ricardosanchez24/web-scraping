# AGENTS.md - Web Scraper MercadoLibre

## 📋 Contexto del proyecto
- Web scraper en Python para extraer datos de MercadoLibre Venezuela
- Stack: Python 3.x, Selenium, BeautifulSoup, Requests
- Archivos principales: `p.py`, `web_scraping_mercado_libre.py`, `web-scraper.py`, `webScraperSelenium.py`

## 🎯 Convenciones de código
- Código y comentarios en español
- Nombres de variables y funciones en snake_case
- Usar type hints en todas las funciones
- Funciones pequeñas con una sola responsabilidad (SRP)
- Manejar excepciones específicas, no `Exception` genérica
- Preferir `requests` + BeautifulSoup sobre Selenium cuando sea posible

## ⚙️ Entorno y comandos
- Activar entorno virtual: `.venv\Scripts\Activate.ps1` (Windows)
- Instalar dependencias: `pip install -r requirements.txt`
- Ejecutar scraper BS4: `python p.py`
- Ejecutar scraper Selenium: `python web_scraping_mercado_libre.py`

## 🧪 Testing
- Framework: pytest (por configurar)
- Ejecutar tests: `python -m pytest tests/ -v`
- Los tests deben estar en `tests/test_*.py`

## 🚫 Reglas obligatorias
- NO hacer commits, push ni crear PR sin permiso explícito
- NO modificar `requirements.txt` sin consultar
- NO instalar paquetes nuevos sin preguntar
- NO ejecutar scrapers contra producción sin autorización
- NO compartir datos scrapeados fuera del proyecto

## 🔄 Flujo de trabajo
1. **Plan**: Antes de cualquier cambio, proponer un plan detallado
2. **Revisión**: Esperar aprobación del usuario antes de modificar archivos
3. **Ejecución**: Aplicar cambios solo después de recibir el "ok"
4. **Verificación**: Mostrar el diff y ejecutar pruebas después de cada cambio
