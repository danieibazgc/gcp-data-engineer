"""Ejecuta una consulta publica de BigQuery usando el CLI `bq`.

Uso:
	python bigquery/public_dataset_demo.py --project-id <PROJECT_ID> --location <LOCATION>

Requisitos:
	- Google Cloud CLI instalado
	- `bq` disponible en PATH
	- Sesion iniciada: gcloud auth login
	- Proyecto configurado o enviado por argumento
"""

from __future__ import annotations

import argparse
import shutil
import subprocess


QUERY = """
SELECT
	id,
	name,
	category,
	retail_price,
	brand
FROM
	`bigquery-public-data.thelook_ecommerce.products`
ORDER BY
	retail_price DESC
LIMIT 10;
""".strip()


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(
		description="Ejecuta la consulta de productos de thelook_ecommerce en BigQuery"
	)
	parser.add_argument("--project-id", required=True, help="ID del proyecto de GCP")
	parser.add_argument("--location", default="US", help="Ubicacion de ejecucion para BigQuery")
	return parser.parse_args()


def run_query(project_id: str, location: str) -> int:
	bq_executable = shutil.which("bq.cmd") or shutil.which("bq.exe") or shutil.which("bq")
	if bq_executable is None:
		print("No se encontro el comando 'bq'. Verifica que Google Cloud CLI este instalado y en PATH.")
		return 1

	command = [
		bq_executable,
		"query",
		"--use_legacy_sql=false",
		f"--project_id={project_id}",
		f"--location={location}",
		"--format=prettyjson",
	]

	print("Ejecutando consulta en BigQuery...")
	result = subprocess.run(command, input=QUERY, capture_output=True, text=True)

	if result.returncode != 0:
		print("Fallo la ejecucion de la consulta:")
		if result.stdout.strip():
			print("Salida estandar:")
			print(result.stdout.strip())
		if result.stderr.strip():
			print("Salida de error:")
			print(result.stderr.strip())
		if not result.stdout.strip() and not result.stderr.strip():
			print("Error desconocido")
		return result.returncode

	print("Consulta ejecutada correctamente. Resultado:")
	print(result.stdout.strip())
	return 0


def main() -> None:
	args = parse_args()
	exit_code = run_query(project_id=args.project_id, location=args.location)
	raise SystemExit(exit_code)


if __name__ == "__main__":
	main()
