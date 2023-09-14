import jwt
import json

from django.http import HttpResponse

from diplomado.settings import PDF_GENERATOR_API_KEY, PDF_GENERATOR_API_SECRET, PDF_GENERATOR_WORKSPACE_ID
from datetime import timedelta, datetime
import http.client

class InvalidAPIRequest(Exception):
    pass

class PDFGeneratorAPI:

    secret = PDF_GENERATOR_API_SECRET
    key = PDF_GENERATOR_API_KEY
    workspace_id = PDF_GENERATOR_WORKSPACE_ID
    token = None
    def create_template(self, name, mode):

        conn = http.client.HTTPSConnection("us1.pdfgeneratorapi.com")

        token = self.create_token()

        payload = {
            "name": name,
            "tags": mode,
            "isDraft": True,
            "layout": {
                "format": "A4",
                "width": 21,
                "height": 29.7,
                "unit": "cm",
                "orientation": "portrait",
                "rotation": 0,
                "margins": {
                    "top": 0.5,
                    "right": 0.5,
                    "bottom": 0.5,
                    "left": 0.5
                },
                "repeatLayout": {
                    "format": "A4",
                    "width": 21,
                    "height": 29.7
                },
                "emptyLabels": 0
            },
        }

        headers = {
            'content-type': "application/json",
            'Authorization': "Bearer {}".format(token)
        }

        conn.request("POST", "/api/v4/templates", json.dumps(payload), headers)
        response = conn.getresponse()

        if response.status == 201:
            data = response.read()
            data = json.loads(data.decode("utf-8"))
            data_response = data.get("response")
            return data_response.get("id")
        else:
            raise InvalidAPIRequest

    def create_token(self):
        end_time = datetime.now() + timedelta(days=1)
        token = jwt.encode(
            {
                "iss": PDF_GENERATOR_API_KEY,
                "sub": PDF_GENERATOR_WORKSPACE_ID,
                "exp": datetime.timestamp(end_time)
            },
            PDF_GENERATOR_API_SECRET,
            algorithm='HS256'
        )

        self.token = token
        return token

    def create_ulr_view(self):
        import http.client

        conn = http.client.HTTPSConnection("us1.pdfgeneratorapi.com")
        self.create_token()

        headers = {
            'content-type': "application/json",
            'Authorization': "Bearer {}".format(self.token)
        }
        payload = {
            "data": {
                'email': "alumno@alumno.com",
                'name': "Ramon",
                'first_surname': "Garcia",
                'second_surname': "Garcia",
                'matricula': "201116415",
                'address': "Av. Independencia 123",
                'postal_code': "72000",
                'phone': "123456789",
                'birthdate': "1992-01-01",
                'social_service_name': "Programa especial de servicios",
                'social_service_folio': "SS2012842",
                'social_service_description': "Grande descripción del programa de servicio social",
                'social_service_program_adviser': "Luisa Contreras Cano",
                'professional_practices_name': "Programa de especial para profesionales",
                'professional_practices_folio': "PP9092432",
                'faculty_name': "Facultad de Ingeniería en Todologia",
                "service_social_adviser": "Juan Perez Perez",
                "professional_practices_adviser": "Ricardo Rodriguez Torres",
                'professional_practices_description': "Gran descripción del programa de practicas profesionales",
                'professional_practices_program_adviser': "Antonio Guillermo Rojas Rojas"
            }
        }
        payload = json.dumps(payload)
        conn.request("POST", f"/api/v4/templates/{self.api_identifier}/editor", payload, headers)
        response = conn.getresponse()
        if response.status == 200:
            data = response.read()
            data = json.loads(data.decode("utf-8"))
            return data.get("response")
        else:
            raise InvalidAPIRequest

    def generate_document(self, data):

        conn = http.client.HTTPSConnection("us1.pdfgeneratorapi.com")
        payload = {
            "template":
                {
                    "id": self.api_identifier,
                    "data": data
                },

            "format": "pdf",
            "output": "file",
        }
        payload = json.dumps(payload)
        self.create_token()
        headers = {
            'content-type': "application/json",
            'Authorization': "Bearer {}".format(self.token)
        }

        conn.request("POST", "/api/v4/documents/generate", payload, headers)
        res = conn.getresponse()
        print(type(res))
        print(res)
        if res.status == 201:
            response = HttpResponse(res, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="download-pdf"'
            return response
        else:
            raise InvalidAPIRequest

