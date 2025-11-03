from stages import Lead
from repo import LeadRepository

class MiniCRMApp:
    def __init__(self):
        self.repo = LeadRepository()

    def add_lead(self):
        name = input("Nome: ").strip()
        company = input("Empresa: ").strip()
        email = input("E-mail: ").strip()
        if not name or "@" not in email:
            print("Nome e e-mail válido são obrigatórios.")
            return
        lead = Lead(name, company, email)
        self.repo.add_lead(lead)
        print("✔ Lead adicionado!")

    def list_leads(self):
        leads = self.repo.list_all()
        if not leads:
            print("Nenhum lead ainda.")
            return
        print("\n# | Nome                 | Empresa            | E-mail")
        print("--+----------------------+-------------------+-----------------------")
        for i, l in enumerate(leads):
            print(f"{i:02d}| {l.name:<20} | {l.company:<17} | {l.email:<21}")

    def search_leads(self):
        q = input("Buscar por: ").strip()
        if not q:
            print("Consulta vazia.")
            return
        results = self.repo.search(q)
        if not results:
            print("Nada encontrado.")
            return
        print("\n# | Nome                 | Empresa            | E-mail")
        print("--+----------------------+-------------------+-----------------------")
        for i, l in enumerate(results):
            print(f"{i:02d}| {l.name:<20} | {l.company:<17} | {l.email:<21}")

    def export_csv(self):
        path = self.repo.export_csv()
        if path:
            print(f"✔ Exportado para: {path}")
        else:
            print("Erro ao exportar. Feche o arquivo e tente novamente.")

    def run(self):
        while True:
            print("\nMini CRM de Leads — Versão OO")
            print("[1] Adicionar lead")
            print("[2] Listar leads")
            print("[3] Buscar lead")
            print("[4] Exportar CSV")
            print("[0] Sair")
            op = input("Escolha: ").strip()
            if op == "1":
                self.add_lead()
            elif op == "2":
                self.list_leads()
            elif op == "3":
                self.search_leads()
            elif op == "4":
                self.export_csv()
            elif op == "0":
                print("Até mais!")
                break
            else:
                print("Opção inválida.")

if __name__ == "__main__":
    MiniCRMApp().run()
