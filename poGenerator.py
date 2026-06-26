# Importa o python-docx
from docx import Document

# Pega o molde que será usado para fazer as ordens de pagamento (pegar o molde certo depois)
documento = Document("molde_doc.docx")

# Dicionário para armazenar tudo que precisa ser inserido na OP

itensDic = {
    "solicitante": solicitante,
    "dtSolicitacao": dtSolicitacao,
    "CC1": cc1,
    "CC2": cc2,
    "fornecedor": fornecedor,
    "tipoOp": tipoOp,
    "descricao": descricao,
    "dtPgtos": dataPgtos,
    "valor": valor,
    "formaPAgamento": formaPAgamento,
    "pix": pix,
    "titular": titular,
    "banco": banco,
    "agencia": agencia,
    "contaCorrente": contaCorrente,
    "cnpjCpf": cnpjCpf,
    "status": status    
}

documento.save("docComInsercao.docx")