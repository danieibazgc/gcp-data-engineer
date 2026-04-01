"""Crea un bucket multirregional usando Google Cloud CLI.

Uso:
	python cloud-storage/create_bucket_multiregional.py --project-id <PROJECT_ID> --bucket <BUCKET_NAME> --location US

Requisitos:
	- gcloud CLI instalado
	- gcloud auth login
"""

from __future__ import annotations

import argparse
import shutil
import subprocess


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(description="Crear bucket multirregional con gcloud CLI")
	parser.add_argument("--project-id", required=True, help="ID del proyecto de GCP")
	parser.add_argument("--bucket", required=True, help="Nombre unico del bucket")
	parser.add_argument("--location", default="US", help="Multi-region: US, EU o ASIA")
	parser.add_argument("--storage-class", default="STANDARD", help="Clase de almacenamiento")
	return parser.parse_args()


def resolve_gcloud_executable() -> str:
	"""Resuelve el ejecutable de gcloud de forma portable en Windows/macOS/Linux."""
	for candidate in ("gcloud.cmd", "gcloud.exe", "gcloud"):
		found = shutil.which(candidate)
		if found:
			return found
	raise FileNotFoundError("No se encontro gcloud en PATH. Verifica la instalacion de Google Cloud CLI.")


def main() -> None:
	args = parse_args()
	gcloud_executable = resolve_gcloud_executable()
	cmd = [
		gcloud_executable,
		"storage",
		"buckets",
		"create",
		f"gs://{args.bucket}",
		"--project",
		args.project_id,
		"--location",
		args.location,
		"--default-storage-class",
		args.storage_class,
	]

	result = subprocess.run(cmd, capture_output=True, text=True)
	if result.returncode == 0:
		print("Bucket multirregional creado correctamente.")
		print(result.stdout.strip())
	else:
		print("Error al crear bucket:")
		print(result.stderr.strip())


if __name__ == "__main__":
	main()
