from django.shortcuts import render
from rest_framework import viewsets, generics
import requests


# Create your views here.

class Services:

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.authData = {           
            "email": self.email,
            "password": self.password    
            }
        self.token = self.getAuthToken()
        self.header = {
            'Authorization': f'JWT {self.token}',
            }
        self.companies = self.getAllCompanies()
        self.companyDetail = self.getCompanyDetail()
        self.equipments = self.getEquipments()


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
                equipments.append(res)


        print(equipments)        
        return equipments


def testview(request):

    a = Services('a@a.com','a')
    
    # a.getCompanyDetail()

    return render(request, 'bla.html', {'comp':a.companies})

def homeview(request):

    return render(request, 'loading.html')

