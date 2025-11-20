# Estrategia DevSecOps

## Herramientas clave

- **GitHub Actions**: orquesta la pipeline CI/CD.
- **SonarQube**: analiza calidad del código (bugs, code smells, cobertura).
- **Bandit**: análisis estático de seguridad para Python.
- **pip-audit**: auditoría de vulnerabilidades en dependencias Python.
- **Vercel**: despliegue del frontend (HTML) y la API Python serverless.

## Flujo por fases

1. **Plan**
   - Definimos como quality gate: no se despliega si la pipeline falla.
   - SonarQube recibe reportes de cada push a `main` y PR.

2. **Code**
   - El código se organiza en:
     - `calculator/` (lógica de negocio)
     - `api/` (endpoint para Vercel)
     - `tests/` (pytest)
   - Se aconseja ejecutar `pytest` y `bandit -r calculator` en local antes de hacer push.

3. **Build / Test / Security (CI)**
   - Job `ci-security`:
     - Instala dependencias (`requirements.txt`).
     - Ejecuta tests y genera `coverage.xml`.
     - Lanza `bandit` y `pip-audit`.
     - Ejecuta `sonar-scanner`, que usa `sonar-project.properties` para identificar el proyecto en SonarQube.

4. **Release / Deploy (CD)**
   - Job `deploy-vercel`:
     - Se ejecuta solo si `ci-security` termina en éxito.
     - Construye y despliega usando el CLI de Vercel.

5. **Operate / Monitor**
   - Se revisa SonarQube de manera periódica (tendencias de bugs, code smells, cobertura).
   - Se planifica refactorización en función de la deuda técnica reportada.

## Configuración de SonarQube

- Se usa un proyecto llamado `calc-devsecops-vercel` en SonarQube.
- El archivo `sonar-project.properties` se encuentra en la raíz del repo.
- Variables necesarias en GitHub:
  - `SONAR_HOST_URL` (URL del servidor SonarQube).
  - `SONAR_TOKEN` (token del proyecto o usuario).
