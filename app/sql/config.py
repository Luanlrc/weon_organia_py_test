from pathlib import Path

def load_sql(filename: str) -> str:
    sql_dir = Path(__file__).parent
    file_path = sql_dir / filename
    return file_path.read_text(encoding="utf-8")