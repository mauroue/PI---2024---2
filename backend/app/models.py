from django.db import models

class Tecnico(models.Model):
    nome = models.CharField(max_length=255)
    rg = models.CharField(max_length=20)
    cpf = models.CharField(max_length=14)
    crea = models.CharField(max_length=20, blank=True, null=True)
    
    licenca_anac_gmp = models.BooleanField(default=False)
    licenca_anac_cel = models.BooleanField(default=False)
    licenca_anac_avi = models.BooleanField(default=False)
    licenca_faa = models.BooleanField(default=False)
    
    passaporte_validade = models.DateField(blank=True, null=True)
    visto_validade = models.DateField(blank=True, null=True)
    
    escolaridade = models.CharField(max_length=255, blank=True, null=True)
    cursos_tecnicos = models.TextField(blank=True, null=True)
    cursos_aeronaves = models.TextField(blank=True, null=True)
    
    historico_trabalho = models.TextField(blank=True, null=True)
    
    data_entrada = models.DateField()
    data_saida = models.DateField(blank=True, null=True)
    
    cargo = models.CharField(max_length=100, blank=True, null=True)
    empresa = models.CharField(max_length=255, blank=True, null=True)
    
    projeto = models.CharField(max_length=255, blank=True, null=True)
    
    # Escolha de Regiões de Atuação
    regioes = models.TextField(blank=True, null=True)

    # Status de aprovação
    aprovado = models.BooleanField(default=False)
    pendencias = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome
