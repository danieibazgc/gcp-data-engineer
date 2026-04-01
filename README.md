# Práctica de Data Engineering en Google Cloud

Proyecto práctico orientado a demostrar habilidades base de Data Engineering en Google Cloud Platform (GCP), usando Python y Google Cloud CLI.

## Objetivo

Construir y ejecutar tareas reales de plataforma de datos en GCP:

- Aprovisionamiento de almacenamiento en Cloud Storage (regional y multirregional).
- Ejecución de consultas SQL en BigQuery sobre datasets públicos.
- Automatización reproducible con scripts en Python y uso de CLI.

## Stack técnico

- Google Cloud Platform (GCP)
- Cloud Storage
- BigQuery
- Python 3
- Google Cloud CLI (`gcloud`, `bq`)
- Librería `google-cloud-storage`
- PowerShell (entorno local en Windows)

## Estructura del repositorio

```text
bigquery/
  public_dataset_demo.py
cloud-storage/
  create_bucket.py
  create_bucket_multiregional.py
init.py
```

## Implementaciones realizadas

### 1) Creación de bucket regional con SDK de Python

Script: `cloud-storage/create_bucket.py`

Qué hace:
- Valida formato de nombre de bucket (reglas de GCS).
- Crea bucket con proyecto, nombre, ubicación y storage class parametrizables.
- Maneja errores comunes (nombre inválido, bucket ya existente, errores generales).

Habilidades demostradas:
- Uso de `google-cloud-storage`.
- Manejo de argumentos por línea de comandos con `argparse`.
- Buenas prácticas básicas de validación y manejo de excepciones.

### 2) Creación de bucket multirregional con CLI

Script: `cloud-storage/create_bucket_multiregional.py`

Qué hace:
- Resuelve de forma portable el ejecutable de `gcloud` (`gcloud.cmd`, `gcloud.exe`, `gcloud`).
- Ejecuta creación de bucket con `gcloud storage buckets create`.
- Permite configurar multi-región y storage class.

Habilidades demostradas:
- Integración Python + CLI con `subprocess`.
- Automatización operativa y compatibilidad cross-platform.

### 3) Consulta de dataset público en BigQuery

Script: `bigquery/public_dataset_demo.py`

Qué hace:
- Ejecuta una consulta SQL sobre `bigquery-public-data.thelook_ecommerce.products`.
- Obtiene los 10 productos de mayor precio.
- Envía SQL por stdin al comando `bq query` para mayor robustez en Windows.

Habilidades demostradas:
- SQL en BigQuery y uso de datasets públicos.
- Integración con CLI `bq` y ejecución automatizada.
- Resolución de problemas de compatibilidad en entorno Windows.

## Evidencia de práctica ejecutada

Durante la práctica se ejecutaron comandos de creación y verificación con resultado exitoso (código de salida 0), incluyendo:

- Creación de buckets con nombres dinámicos.
- Validación de propiedades del bucket (`storageClass`, `defaultStorageClass`, ubicación).
- Ejecución de consulta en BigQuery con formato JSON y presentación tabular.

## Cómo ejecutar

### Requisitos

- Tener un proyecto de GCP activo.
- Instalar Google Cloud CLI.
- Tener Python 3 instalado.
- Instalar dependencia:

```bash
pip install google-cloud-storage
```

- Autenticación:

```bash
gcloud auth login
gcloud auth application-default login
```

### Ejemplos

Crear bucket regional:

```bash
python cloud-storage/create_bucket.py --project-id TU_PROJECT_ID --bucket tu-bucket-unico-123 --location us-central1
```

Crear bucket multirregional:

```bash
python cloud-storage/create_bucket_multiregional.py --project-id TU_PROJECT_ID --bucket tu-bucket-unico-456 --location US --storage-class STANDARD
```

Ejecutar consulta de BigQuery:

```bash
python bigquery/public_dataset_demo.py --project-id TU_PROJECT_ID --location US
```

## Perfil profesional (resumen)

Esta práctica demuestra capacidad para:

- Construir automatizaciones básicas de infraestructura de datos en GCP.
- Integrar servicios cloud con Python y CLI de manera reproducible.
- Ejecutar y validar consultas analíticas en BigQuery.
- Resolver problemas prácticos de ejecución en Windows.

## Próximos pasos técnicos

- Versionar resultados de consultas en tablas propias de BigQuery.
- Orquestar estos procesos con Cloud Composer o Workflows.
- Agregar pruebas automatizadas y CI/CD para scripts de infraestructura.
- Incorporar monitoreo y logging estructurado.

---

Si querés, puedo convertir este README en una versión bilingüe (ES/EN) para aplicar a búsquedas internacionales.
