#CLASSES
from dataclasses import dataclass



@dataclass
class Usuario:
    nome_usuario: str = ''
    sobrenome_usuario: str = ''
    email_usuario: str = ''
    bairro_usuario: str = ''
    nascimento_usuario: str = ''
    id_usuario: str = '' #PK

@dataclass
class Cartao:
    creditos_disponiveis: str = ''
    tipo_cartao: str = ''
    data_emissao: str = ''
    id_usuario: str = ''
    id_cartao: str = '' #PK
  
@dataclass
class Onibus:
    numero_linha: str = ''
    modelo_onibus: str = ''
    id_motorista: str = ''
    numero_placa: str = '' #PK

@dataclass
class Motorista:
    numero_cnh: str = ''
    nome_motorista: str = ''
    sobrenome_motorista: str = ''
    nascimento_motorista: str = ''
    id_motorista: str = '' #PK
