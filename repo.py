import json, csv
from pathlib import Path
from stages import Lead

class LeadRepository:
    """Gerencia o armazenamento e recuperação de leads."""
    def __init__(self):
        self.data_dir = Path(__file__).resolve().parent / "data"
        self.data_dir.mkdir(exist_ok=True)
        self.db_path = self.data_dir / "leads.json"

    def _load(self):
        if not self.db_path.exists():
            return []
        try:
            data = json.loads(self.db_path.read_text(encoding="utf-8"))
            return [Lead.from_dict(d) for d in data]
        except json.JSONDecodeError:
            return []

    def _save(self, leads):
        leads_data = [l.to_dict() for l in leads]
        self.db_path.write_text(json.dumps(leads_data, ensure_ascii=False, indent=2), encoding="utf-8")

    def add_lead(self, lead):
        leads = self._load()
        leads.append(lead)
        self._save(leads)

    def list_all(self):
        return self._load()

    def search(self, query):
        query = query.lower()
        results = []
        for lead in self._load():
            blob = f"{lead.name} {lead.company} {lead.email}".lower()
            if query in blob:
                results.append(lead)
        return results

    def export_csv(self, path=None):
        path = Path(path) if path else (self.data_dir / "leads.csv")
        leads = self._load()
        try:
            with path.open("w", newline="", encoding="utf-8") as f:
                w = csv.DictWriter(f, fieldnames=["name","company","email","stage","created"])
                w.writeheader()
                for l in leads:
                    w.writerow(l.to_dict())
            return path
        except PermissionError:
            return None
