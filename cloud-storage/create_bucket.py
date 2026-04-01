"""Crea un bucket en Google Cloud Storage.

Uso:
	python cloud-storage/create_bucket.py --project-id <PROJECT_ID> --bucket <BUCKET_NAME> --location <LOCATION>

Requisitos:
	pip install google-cloud-storage
	gcloud auth application-default login
"""

from __future__ import annotations

import argparse
import re
from typing import Final

from google.cloud import storage
from google.cloud.exceptions import Conflict


BUCKET_NAME_PATTERN: Final[re.Pattern[str]] = re.compile(r"^[a-z0-9][a-z0-9._-]{1,61}[a-z0-9]$")


def validate_bucket_name(bucket_name: str) -> str:
	"""Valida reglas comunes de nombres de bucket en GCS."""
	if not BUCKET_NAME_PATTERN.match(bucket_name):
		raise ValueError(
			"Nombre de bucket invalido. Usa 3-63 caracteres en minuscula con '-', '_' o '.'."
		)
	return bucket_name


def create_bucket(project_id: str, bucket_name: str, location: str, storage_class: str = "STANDARD") -> storage.Bucket:
	"""Crea y retorna un bucket de GCS."""
	client = storage.Client(project=project_id)
	bucket = client.bucket(bucket_name)
	bucket.storage_class = storage_class

	return client.create_bucket(bucket, location=location)


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(description="Crea un bucket en Google Cloud Storage")
	parser.add_argument("--project-id", required=True, help="ID del proyecto de GCP")
	parser.add_argument("--bucket", required=True, help="Nombre unico del bucket")
	parser.add_argument("--location", default="US", help="Region o multi-region, por ejemplo US o us-central1")
	parser.add_argument("--storage-class", default="STANDARD", help="Clase de almacenamiento, por ejemplo STANDARD")
	return parser.parse_args()


def main() -> None:
	args = parse_args()

	try:
		bucket_name = validate_bucket_name(args.bucket)
		bucket = create_bucket(
			project_id=args.project_id,
			bucket_name=bucket_name,
			location=args.location,
			storage_class=args.storage_class,
		)
	except ValueError as exc:
		print(f"Error de validacion: {exc}")
		return
	except Conflict:
		print(f"El bucket '{args.bucket}' ya existe. Prueba con otro nombre unico global.")
		return
	except Exception as exc:
		print(f"No se pudo crear el bucket: {exc}")
		return

	print("Bucket creado correctamente")
	print(f"Nombre: {bucket.name}")
	print(f"Ubicacion: {bucket.location}")
	print(f"Clase de almacenamiento: {bucket.storage_class}")


if __name__ == "__main__":
	main()
