from datetime import date

class Lead:
    """Classe que representa um Lead (potencial cliente)."""
    def __init__(self, name, company, email):
        self.name = name
        self.company = company
        self.email = email
        self.stage = "novo"
        self.created = date.today().isoformat()

    def to_dict(self):
        """Converte o objeto Lead em dicionário para salvar no JSON."""
        return {
            "name": self.name,
            "company": self.company,
            "email": self.email,
            "stage": self.stage,
            "created": self.created,
        }

    @staticmethod
    def from_dict(data):
        """Cria um objeto Lead a partir de um dicionário salvo."""
        lead = Lead(data["name"], data["company"], data["email"])
        lead.stage = data.get("stage", "novo")
        lead.created = data.get("created", date.today().isoformat())
        return lead
