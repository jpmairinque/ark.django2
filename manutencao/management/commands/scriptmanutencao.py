from django.core.management.base import BaseCommand, CommandError
import requests
from manutencao.models import Chamado, Company, Equipment
from datetime import datetime
import math
class Command(BaseCommand):

    help = 'Fetching and saving to DB'

    def __init__(self, *args, **kwargs):

        super(Command, self).__init__(*args, **kwargs)

        self.baseApiEndpoint = 'https://desenvolvimento.arkmeds.com'
        self.authData = {           
            "email": 'a@a.com',
            "password": 'a'
        }
        self.token = self.getAuthToken()
        self.header = {
            'Authorization': f'JWT {self.token}',
        }
        self.inDatabaseEquipments = Equipment.objects.all().values_list('id', flat=True)
        self.inDatabaseCompanies = Company.objects.all().values_list('id', flat=True)
        self.inDatabaseChamados = Chamado.objects.all().values_list('id', flat=True)
        
        

    def getAuthToken(self):

        token = requests.request('POST', f'{self.baseApiEndpoint}/rest-auth/token-auth/', data=self.authData).json()['token']

        if token:
            return token
        else: 
            return None


    def getAllCompanies(self):
        
 
        res = requests.request('GET', f'{self.baseApiEndpoint}/api/v2/empresa/', headers=self.header).json()[500:520]
        
        if res:
            return res        
        else:
            return None

    def getCompanyDetail(self, allCompanies):

        self.stdout.write(self.style.SUCCESS('[Baixando empresas detalhadas]'))

        companyDetail = []
        for index,company in enumerate(allCompanies):
            if company['id'] not in self.inDatabaseCompanies:
                self.stdout.write(self.style.SUCCESS(f'[{index} empresas baixadas]'))                     
                res = requests.request('GET', f"{self.baseApiEndpoint}/api/v2/company/{company['id']}", headers=self.header).json()
                companyDetail.append(res)

        def checkType(company):
            if company['tipo'] == 5:
                return False
            else:
                return True

        filtredRes = list(filter(checkType, companyDetail))

        
   
        return filtredRes

    def getEquipments(self, companyDetail):

        self.stdout.write(self.style.SUCCESS('[Baixando equipamentos]'))
        equipments = []
        

        for index,company in enumerate(companyDetail):
            self.stdout.write(self.style.SUCCESS(f'[{index} equipamentos baixados]'))            
            res = requests.request('GET', f"{self.baseApiEndpoint}/api/v2/equipamentos_paginados/?empresa_id={company['id']}", headers=self.header).json()
            company['count_equipments'] = res['count']
            for equipment in res['results']:                
                equipments.append(equipment)
               
        

        return equipments

    def postChamado(self, allEquipments):
        self.stdout.write(self.style.SUCCESS('[Registrando chamados]'))

        nowStamp = str(math.trunc(datetime.now().timestamp()))

        for equipment in allEquipments:

            data = {
                "equipamento": equipment['id'],
                "solicitante": equipment['proprietario']['id'], 
                "tipo_servico": 3, 
                "problema": 5,
                "observacoes": "texto gerado aleatoriamente com até 100 palavras", 
                "data_criacao": nowStamp, 
                "id_tipo_ordem_servico": 1
            }
            res = requests.request('POST',
                                   f"{self.baseApiEndpoint}/api/v1/chamado/novo/",
                                   headers=self.header,
                                   data=data).json()

    def getChamados(self, allEquipments):

        self.stdout.write(self.style.SUCCESS('[Baixando chamados]'))
        chamados = []
       

        for index,equipment in enumerate(allEquipments):
            self.stdout.write(self.style.SUCCESS(f'[{index} chamados baixados]'))                      
            res = requests.request('GET', f"{self.baseApiEndpoint}/api/v2/chamado/?equipamento_id={equipment['id']}", headers=self.header).json()
            equipment['count_chamados'] = res['count']
            for chamado in res['results']:                   
                    chamado['equipment_id'] = equipment['id']
                    chamado['proprietario_nome'] = equipment['proprietario']['nome']
                    chamado['proprietario_apelido'] = equipment['proprietario']['apelido']
                    chamados.append(chamado)
        
        
        return chamados

    def saveCompanies(self, companyDetail):

        self.stdout.write(self.style.SUCCESS('[Salvando empresas no BD]'))

        for company in companyDetail:            
                Company.objects.create(

                    id=company['id'],
                    tipo=company['tipo'],
                    nome=company['nome'],
                    nome_fantasia=company['nome_fantasia'],
                    superior=company['superior'],
                    cnpj=company['cnpj'],
                    observacoes=company['observacoes'],
                    contato=company['contato'],
                    email=company['email'],
                    telefone1=company['telefone1'],
                    ramal1=company['ramal1'],
                    telefone2=company['telefone2'],
                    ramal2=company['ramal2'],
                    fax=company['fax'],
                    cep=company['cep'],
                    rua=company['rua'],
                    numero=company['numero'],
                    bairro=company['bairro'],
                    cidade=company['cidade'],
                    estado=company['estado'],
                    qtequipments=company['count_equipments']

                )

    def saveEquipments(self, allEquipments):        

        self.stdout.write(self.style.SUCCESS('[Salvando equipamentos no BD]')) 

        for equipment in allEquipments:
            if equipment['id'] not in self.inDatabaseEquipments:
                Equipment.objects.create(
                    id=equipment['id'],
                    fabricante=equipment['fabricante'],
                    modelo=equipment['modelo'],
                    patrimonio=equipment['patrimonio'],
                    numero_serie=equipment['numero_serie'],
                    proprietario=equipment['proprietario']['id'],
                    qtchamados=equipment['count_chamados']
                )
    
    def saveChamados(self, allChamados):

         self.stdout.write(self.style.SUCCESS('[Salvando chamados no BD]')) 

         for chamado in allChamados:
            if chamado['id'] not in self.inDatabaseChamados:
                Chamado.objects.create(
                    id=chamado['id'],
                    numero=chamado['numero'],
                    equipamento_id=chamado['equipment_id'],
                    responsavel_str=chamado['responsavel_str'],
                    proprietario_nome = chamado['proprietario_nome'],
                    proprietario_apelido = chamado['proprietario_apelido']
                )

    def handle(self, *args, **options):

        self.stdout.write(self.style.SUCCESS('[Iniciando script de manutenção]'))

        allCompanies = self.getAllCompanies()
        companyDetail = self.getCompanyDetail(allCompanies)
        allEquipments = self.getEquipments(companyDetail)
        self.postChamado(allEquipments)
        allChamados = self.getChamados(allEquipments)

        self.stdout.write(self.style.SUCCESS('[Iniciando salvamento no BD]'))

        self.saveCompanies(companyDetail)
        self.saveEquipments(allEquipments)
        self.saveChamados(allChamados)

        self.stdout.write(self.style.SUCCESS('[Script finalizado!]'))