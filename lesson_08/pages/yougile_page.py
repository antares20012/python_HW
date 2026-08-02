import requests
from typing import Dict


class YougileApi:

    def __init__(self, url: str, credentials: Dict[str, str]) -> None:
        self.url = url
        self.login = credentials["login"]
        self.password = credentials["password"]
        self.company_id = None
        self.token = credentials["key"]
        self.last_project_id = None
        self.last_status_code = None

    def get_yougile_my_company_id(self):  # ПОЛУЧЕНИЕ ID КОМПАНИИ
        payload = {
            'login': self.login,
            'password': self.password,
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(self.url + '/auth/companies', json=payload, headers=headers)
        self.last_status_code = response.status_code
        response.raise_for_status()
        companies = response.json()
        self.company_id = companies["content"][-1]["id"]
        return self.company_id

    def create_yougile_my_key(self):  # ПОЛУЧЕНИЕ ключей КОМПАНИИ
        company_id = self.get_yougile_my_company_id()
        payload = {
            'login': self.login,
            'password': self.password,
            'companyId': company_id
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(self.url + '/auth/keys', json=payload, headers=headers)
        self.last_status_code = response.status_code
        response.raise_for_status()
        self.token = response.json().get("key")
        return self.token

    def get_yougile_my_key(self): # ПОЛУЧЕНИЕ последнего созданного ключа  КОМПАНИИ
        payload = {
            'login': self.login,
            'password': self.password,
            'companyId': self.company_id or self.get_yougile_my_company_id()
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(self.url + '/auth/keys', json=payload, headers=headers)
        self.last_status_code = response.status_code
        response.raise_for_status()
        return self.token

    @property
    def headers(self):
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

    def create_project(self, title):  # СОЗДАНИЕ проекта
        payload = {
            "title": title
        }
        response = requests.post(self.url + '/projects', json=payload, headers=self.headers)
        self.last_status_code = response.status_code
        response.raise_for_status()
        project_id = response.json()
        self.last_project_id = project_id.get("id")
        return project_id

    def get_last_project_id(self):
        return self.last_project_id

    def get_last_project_title(self):
        if not self.last_project_id:
            return None
        url = f"{self.url}/projects/{self.last_project_id}"
        response = requests.get(url, headers=self.headers)
        self.last_status_code = response.status_code
        response.raise_for_status()
        return response.json().get("title")

    def update_project(self, new_title):
        if not self.last_project_id:
            return None
        url = f"{self.url}/projects/{self.last_project_id}"
        payload = {"title": new_title}
        response = requests.put(url, json=payload, headers=self.headers)
        self.last_status_code = response.status_code
        response.raise_for_status()
        return response.json()

    def delete_project(self):
        if not self.last_project_id:
            return None
        url = f"{self.url}/projects/{self.last_project_id}"
        payload = {"deleted": True}
        response = requests.put(url, json=payload, headers=self.headers)
        self.last_status_code = response.status_code
        response.raise_for_status()
        return response.json()
