## DevSecOps y pipeline CI/CD

Este proyecto sigue un enfoque DevSecOps donde la calidad, la seguridad y el despliegue se integran desde el inicio:

- **Fase Plan / Governance**
  - Solo la rama `main` puede desplegar a producción.
  - Todos los cambios entran a `main` mediante Pull Requests.
  - Todo PR debe pasar la pipeline `DevSecOps CI/CD` (tests, análisis de seguridad y análisis de calidad).
  - Existe un umbral mínimo de calidad:
    - Tests unitarios con cobertura reportada.
    - Análisis estático de seguridad (Bandit).
    - Auditoría de dependencias (pip-audit).
    - Análisis de calidad de código y cobertura en SonarQube (quality gate).

- **Fase Code**
  - El código Python sigue una estructura modular (`calculator/core.py`) con tests en `tests/`.
  - Se recomienda usar VS Code con extensiones de Python y, opcionalmente, SonarLint para feedback estático en local.
  - Cada nueva funcionalidad debe venir acompañada de tests unitarios.

- **Fase Build / Test / Security (CI)**
  - GitHub Actions instala dependencias, ejecuta:
    - `pytest` + `coverage` para pruebas.
    - `bandit` para SAST en la carpeta `calculator/`.
    - `pip-audit` para detectar vulnerabilidades en dependencias.
    - `sonar-scanner` para enviar el análisis a SonarQube (bugs, code smells, cobertura).

- **Fase Release / Deploy (CD)**
  - Si la pipeline de CI pasa correctamente, se ejecuta el job de despliegue a Vercel.
  - El despliegue usa el CLI de Vercel y los secretos `VERCEL_TOKEN`, `VERCEL_ORG_ID` y `VERCEL_PROJECT_ID`.

- **Fase Operate / Monitor**
  - El estado de la calidad se monitorea en el dashboard de SonarQube.
  - Los logs de ejecución y fallos de build/deploy se revisan en GitHub Actions y en el panel de Vercel.

  hola
