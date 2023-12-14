import json
from fastavro import json_writer, parse_schema
from pathlib import Path

from shared import iterdir, prepare_raw_dir, validate_and_get_path


"""
"client": "Michael Wilkerson", 
"purchase_date": "2022-08-09", 
"product": "Vacuum cleaner", 
"price": 346
"""


def transform_sales_data(source_path: Path, dest_path: Path):
    source_path = Path(source_path)
    dest_path = Path(dest_path)

    source_path = validate_and_get_path(source_path)
    prepare_raw_dir(dest_path)

    schema = {
        "doc": "Sales data.",
        "name": "sales",
        "namespace": "lesson2",
        "type": "record",
        "fields": [
            {"name": "client", "type": "string"},
            {"name": "purchase_date", "type": "string"},
            {"name": "product", "type": "string"},
            {"name": "price", "type": "int"},
        ],
    }

    parsed_schema = parse_schema(schema)
    for file in iterdir(source_path):  # type: Path
        filename = file.name.split(".")[0] + ".avro"
        filename_path = dest_path.joinpath(filename)
        with open(file, "rb") as json_file:
            json_data = json.load(json_file)
        with open(filename_path, "w") as out:
            json_writer(out, parsed_schema, json_data)
