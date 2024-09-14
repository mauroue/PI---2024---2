from django import forms
from .models import Tecnico

class TecnicoForm(forms.ModelForm):
    class Meta:
        model = Tecnico
        fields = [
            'nome', 'rg', 'cpf', 'crea', 'licenca_anac_gmp', 'licenca_anac_cel', 'licenca_anac_avi',
            'licenca_faa', 'passaporte_validade', 'visto_validade', 'escolaridade', 'cursos_tecnicos',
            'cursos_aeronaves', 'historico_trabalho', 'data_entrada', 'data_saida', 'cargo', 'empresa',
            'projeto', 'regioes'
        ]
