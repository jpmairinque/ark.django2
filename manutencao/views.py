from django.shortcuts import render
from rest_framework import viewsets, generics
import requests
from .models import Company, Equipment
from .serializer import CompanySerializer, EquipmentSerializer, CompanyEquipmentsSerializer

# Create your views here.

class Services:

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.authData = {           
            "email": self.email,
            "password": self.password    
            }
        print('Gerando token de autenticação')
        self.token = self.getAuthToken()
        self.header = {
            'Authorization': f'JWT {self.token}',
            }
        print('Gerando empresas')
        self.companies = self.getAllCompanies()
        print('Gerando detalhes das empresas')
        self.companyDetail = self.getCompanyDetail()
        print('Gerando equipamentos')
        self.equipments = self.getEquipments()
        print('Gerando chamados de equipamentos')
        self.postChamado()


    baseApiEndpoint = 'https://desenvolvimento.arkmeds.com'

    def getAuthToken(self):

        token = requests.request('POST', f'{self.baseApiEndpoint}/rest-auth/token-auth/', data=self.authData).json()['token']

        if token:
            return token
        else: 
            return None


    def getAllCompanies(self):
 
        res = requests.request('GET', f'{self.baseApiEndpoint}/api/v2/empresa/', headers=self.header).json()[:40]
        
        if res:
            return res        
        else:
            return None

    def getCompanyDetail(self):

        companyDetail = []

        for company in self.companies:
            res = requests.request('GET', f"{self.baseApiEndpoint}/api/v2/company/{company['id']}", headers=self.header).json()
            companyDetail.append(res)


        def checkType(company):
            if company['tipo'] == 5:
                return False
            else:
                return True

        filtredRes = list(filter(checkType, companyDetail))

        print(filtredRes)
   
        return filtredRes

    def getEquipments(self):

        equipments = []

        for company in self.companyDetail:
            res = requests.request('GET', f"{self.baseApiEndpoint}/api/v2/equipamentos_paginados/?empresa_id={company['id']}", headers=self.header).json()
            if res['results']:
                for equipment in res['results']:
                    equipments.append(equipment)
               
              
        return equipments

    def postChamado(self):

        for equipment in self.equipments:

            data = {
                "equipamento": equipment['id'],
                "solicitante": equipment['proprietario']['id'], 
                "tipo_servico": 3, 
                "problema": 5,
                "observacoes": "texto gerado aleatoriamente com até 100 palavras", 
                "data_criacao": "1595446943974", 
                "id_tipo_ordem_servico": 1
            }
            res = requests.request('POST',
                                   f"{self.baseApiEndpoint}/api/v1/chamado/novo/",
                                   headers=self.header,
                                   data=data).json()

    def saveCompanies(self):

        inDatabaseCompanies = Company.objects.all().values_list('id', flat=True)

        for company in self.companyDetail:
            if company['id'] not in inDatabaseCompanies:
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

                )

    def saveEquipments(self):

         inDatabaseEquipments = Equipment.objects.all().values_list('id', flat=True)

         for equipment in self.equipments:
            if equipment['id'] not in inDatabaseEquipments:
                Equipment.objects.create(
                    id=equipment['id'],
                    fabricante=equipment['fabricante'],
                    modelo=equipment['modelo'],
                    patrimonio=equipment['patrimonio'],
                    numero_serie=equipment['numero_serie'],
                    proprietario=equipment['proprietario']['id']
                )

                
def testview(request):

    a = Services('a@a.com','a')

    print("saving to db")
    a.saveCompanies()
    print("saving equip to db")
    a.saveEquipments()

    
     # a.getCompanyDetail()

    return render(request, 'bla.html', {'comp':a.equipments})

def homeview(request):

    return render(request, 'loading.html')


#######################################################################################

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

class CompanyEquipmentsViewSet(generics.ListAPIView):

    def get_queryset(self):
        queryset = Equipment.objects.filter(proprietario=self.kwargs['pk'])
        return queryset
    
    serializer_class = CompanyEquipmentsSerializer

