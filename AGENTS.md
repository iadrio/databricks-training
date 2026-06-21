# Reglas del Proyecto (Databricks Cert)

Este archivo contiene las directrices de desarrollo y despliegue del proyecto para guiar a los agentes de IA en este workspace.

## 1. Restricciones de Presupuesto y Nivel (Azure)
- Usar siempre el nivel **Standard** para el workspace.
- Usar exclusivamente clusters de **Single Node** (Nodo único).
- En el archivo `databricks.yml`, configurar el cluster siempre con `num_workers: 0` y `"spark.master": "local[*]"` para evitar costos de nodos de trabajo adicionales.
- **Caducidad del Entorno (14-15 días)**: Dado que las cuentas de evaluación de Databricks expiran en 14 o 15 días, toda la configuración de infraestructura (scripts de Azure CLI, plantillas y archivos del bundle como `databricks.yml`) debe mantenerse completamente versionada, modular y documentada para permitir la destrucción y recreación completa del entorno desde cero en pocos minutos en caso de expirar.


## 2. Restricción Geográfica (Región)
- Desplegar únicamente recursos en la región **`swedencentral`** debido a limitaciones de la suscripción de Azure para Estudiantes (otras regiones producirán `RequestDisallowedByAzure`).

## 3. Control de Costos (Acción Obligatoria)
- Ejecutar siempre el comando `databricks bundle destroy` después de finalizar las pruebas/ejecución para eliminar los recursos del cluster desplegados y no consumir créditos de manera innecesaria.

## 4. Entorno Local (Windows CLI Paths)
- Si los comandos `az` (Azure CLI) o `gh` (GitHub CLI) no se resuelven en la terminal, utilizar sus rutas absolutas predeterminadas en Windows:
  - Azure CLI: `"C:\Program Files\Microsoft SDKs\Azure\CLI2\wbin\az.cmd"`
  - GitHub CLI: `"C:\Program Files\GitHub CLI\gh.exe"`

## 5. Reglas de Seguridad y Prevención de Fugas
- **Archivos Sensibles**: No subir ni comitear jamás archivos con variables de entorno o credenciales (ej. `.env`, `.env.*`, `secrets.json`, `.pem`, `.key`).
- **Secretos en Código**: No codificar nunca en duro (*hardcode*) tokens de API (ej. `ghp_`, `gho_`, `AIzaSy`), contraseñas o claves secretas en notebooks ni archivos del proyecto.
- **Validación con Git Hooks**: El repositorio cuenta con un hook de `pre-commit` en `.githooks/pre-commit` que intercepta automáticamente cualquier intento de commit si detecta archivos sensibles o patrones de secretos en el código modificado. Asegúrate de tenerlo habilitado localmente con el comando: `git config core.hooksPath .githooks`.

## 6. Reglas de Ejecución de CLI (Azure CLI & Databricks CLI)
- **Verificación de Autenticación**: Antes de ejecutar comandos de despliegue, comprobar la sesión con `az account show` y `databricks auth describe` / `databricks profiles list`.
- **Idempotencia**: Validar configuraciones con `databricks bundle validate` antes de desplegar. Comprobar si un recurso ya existe antes de crearlo con comandos de consulta (ej. `az group exists`).
- **Modo No Interactivo**: Utilizar siempre flags no interactivos (como `--yes`, `-y`) para evitar bloqueos en la terminal.
- **Formato estructurado (JSON)**: Solicitar salidas en formato JSON (`-o json` para Azure CLI y `--output json` para Databricks CLI) para permitir un parseo fiable de recursos.
- **Límites de Costos y Región**: Inyectar explícitamente los parámetros `--location swedencentral` y los perfiles de cluster Single Node (`num_workers: 0`) en los comandos correspondientes.
- **Guardrails Destructivos**: Solicitar confirmación interactiva expresa del usuario antes de proponer cualquier comando de eliminación de recursos (ej. `az group delete`, etc.).


