from django.shortcuts import render
from rest_framework import viewsets, generics
import requests
from .models import Empresa

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
 
        res = requests.request('GET', f'{self.baseApiEndpoint}/api/v2/empresa/', headers=self.header).json()[:20]
        
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

    # def saveCompanies():

        


def testview(request):

    a = Services('a@a.com','a')


    
     # a.getCompanyDetail()

    return render(request, 'bla.html', {'comp':a.equipments})

def homeview(request):

    return render(request, 'loading.html')

