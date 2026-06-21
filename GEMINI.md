# Reglas del Proyecto (Databricks Cert)

Este archivo contiene las directrices de desarrollo y despliegue del proyecto para guiar a los agentes de IA en este workspace.

> [!NOTE]
> Este archivo (GEMINI.md) se mantiene por compatibilidad. La configuración recomendada y actualizada se encuentra en [AGENTS.md](file:///C:/Users/ivan/Documents/Antigravity/databricks_cert/AGENTS.md).

## 1. Restricciones de Presupuesto y Nivel (Azure)
- Usar siempre el nivel **Standard** para el workspace.
- Usar exclusivamente clusters de **Single Node** (Nodo único).
- En el archivo `databricks.yml`, configurar el cluster siempre con `num_workers: 0` y `"spark.master": "local[*]"` para evitar costos de nodos de trabajo adicionales.

## 2. Restricción Geográfica (Región)
- Desplegar únicamente recursos en la región **`swedencentral`** debido a limitaciones de la suscripción de Azure para Estudiantes (otras regiones producirán `RequestDisallowedByAzure`).

## 3. Control de Costos (Acción Obligatoria)
- Ejecutar siempre el comando `databricks bundle destroy` después de finalizar las pruebas/ejecución para eliminar los recursos del cluster desplegados y no consumir créditos de manera innecesaria.

## 4. Entorno Local (Windows CLI Paths)
- Si los comandos `az` (Azure CLI) o `gh` (GitHub CLI) no se resuelven en la terminal, utilizar sus rutas absolutas predeterminadas en Windows:
  - Azure CLI: `"C:\Program Files\Microsoft SDKs\Azure\CLI2\wbin\az.cmd"`
  - GitHub CLI: `"C:\Program Files\GitHub CLI\gh.exe"`
