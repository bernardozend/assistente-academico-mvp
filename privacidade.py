import re


# =========================================================
# MENSAGENS PADRÃO
# =========================================================

MENSAGEM_BLOQUEIO = """
🛡️ **Proteção de privacidade ativada**

Sua mensagem parece conter informação pessoal, sensível
ou uma credencial que não é necessária para esta consulta.

Por segurança, não envie senhas, CPF, dados bancários,
informações médicas ou outros dados pessoais.

Posso tentar orientar você sem utilizar esses dados.
""".strip()


MENSAGEM_DADOS_TERCEIROS = """
🛡️ **Proteção de dados**

Este assistente não fornece, consulta ou expõe dados
pessoais de estudantes, professores ou terceiros.

Para situações que exijam acesso a informações pessoais,
utilize o canal institucional responsável.
""".strip()


# =========================================================
# PADRÕES DE DADOS
# =========================================================

PADROES = {

    "CPF": re.compile(
        r"\b\d{3}\.?\d{3}\.?\d{3}-?\d{2}\b"
    ),

    "E-mail": re.compile(
        r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    ),

    "Telefone": re.compile(
        r"\b(?:\+?55\s?)?"
        r"(?:\(?\d{2}\)?\s?)?"
        r"(?:9\d{4}|\d{4})[-\s]?\d{4}\b"
    ),

    "Cartão": re.compile(
        r"\b(?:\d[ -]*?){13,19}\b"
    ),

    "Senha": re.compile(
        r"(?i)\b(?:senha|password|pass)\s*"
        r"(?:é|:|=)?\s*\S+"
    ),
}


# =========================================================
# TERMOS SENSÍVEIS
# =========================================================

TERMOS_SENSIVEIS = [
    "meu diagnóstico",
    "meu diagnostico",
    "meu laudo",
    "minha doença",
    "minha doenca",
    "meu prontuário",
    "meu prontuario",
    "minha medicação",
    "minha medicacao",
    "meus dados bancários",
    "meus dados bancarios",
    "minha conta bancária",
    "minha conta bancaria",
]


# =========================================================
# CONSULTAS SOBRE DADOS DE TERCEIROS
# =========================================================

TERMOS_TERCEIROS = [
    "cpf do aluno",
    "cpf do professor",
    "cpf da professora",
    "telefone do aluno",
    "telefone do professor",
    "telefone da professora",
    "email do aluno",
    "e-mail do aluno",
    "endereço do aluno",
    "endereco do aluno",
    "nota do aluno",
    "histórico do aluno",
    "historico do aluno",
    "senha do aluno",
    "senha do professor",
]


# =========================================================
# FUNÇÃO PRINCIPAL
# =========================================================

def analisar_privacidade(texto):
    """
    Analisa a mensagem antes de enviá-la ao RAG.

    Retorno:
    {
        "permitido": True/False,
        "motivos": [],
        "mensagem": None ou mensagem de bloqueio
    }
    """

    texto_lower = texto.lower()

    motivos = []

    # Dados detectados por expressão regular
    for nome, padrao in PADROES.items():

        if padrao.search(texto):

            motivos.append(nome)

    # Informações potencialmente sensíveis
    for termo in TERMOS_SENSIVEIS:

        if termo in texto_lower:

            motivos.append("Informação sensível")
            break

    # Tentativa de consultar dados de terceiros
    for termo in TERMOS_TERCEIROS:

        if termo in texto_lower:

            return {
                "permitido": False,
                "motivos": ["Dados pessoais de terceiros"],
                "mensagem": MENSAGEM_DADOS_TERCEIROS
            }

    # Caso algum dado pessoal tenha sido detectado
    if motivos:

        return {
            "permitido": False,
            "motivos": list(set(motivos)),
            "mensagem": MENSAGEM_BLOQUEIO
        }

    # Pergunta permitida
    return {
        "permitido": True,
        "motivos": [],
        "mensagem": None
    }


# =========================================================
# TESTE LOCAL
# =========================================================

if __name__ == "__main__":

    testes = [
        "Quando acontece a AV2?",
        "Meu CPF é 123.456.789-00, consegue verificar?",
        "Minha senha é teste123",
        "Qual o telefone do aluno João?",
        "Quantos livros posso pegar na biblioteca?"
    ]

    for pergunta in testes:

        resultado = analisar_privacidade(pergunta)

        print("\n--------------------------------")
        print("PERGUNTA:", pergunta)
        print("PERMITIDO:", resultado["permitido"])
        print("MOTIVOS:", resultado["motivos"])