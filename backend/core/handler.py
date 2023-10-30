from rest_framework import status
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    if response := exception_handler(exc, context):
        if response.status_code == status.HTTP_403_FORBIDDEN:
            method = context['request'].method

            if method == 'POST':
                response.data = {'message': 'Você não tem permissão para Adicionar.'}
            elif method in ['PUT', 'PATCH']:
                response.data = {'message': 'Você não tem permissão para Editar.'}
            elif method == 'DELETE':
                response.data = {'message': 'Você não tem permissão para Deletar.'}

        return response
