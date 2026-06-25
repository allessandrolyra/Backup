from pathlib import Path
from xml.sax.saxutils import escape
import zipfile

OUTPUT = Path(r"c:\01. Foursys\06. BMAD Cursor\docs\zurich-v3-poc-qa-k6\zurich-poc-k6-integracao-detalhada.docx")

CONTENT_TYPES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
  <Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
</Types>"""

RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>"""

WORD_RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
</Relationships>"""

STYLES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:style w:type="paragraph" w:styleId="Title">
    <w:name w:val="Title"/>
    <w:pPr><w:jc w:val="left"/></w:pPr>
    <w:rPr><w:b/><w:sz w:val="52"/><w:color w:val="1F4E79"/></w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="Heading1">
    <w:name w:val="heading 1"/>
    <w:pPr><w:spacing w:before="360" w:after="120"/></w:pPr>
    <w:rPr><w:b/><w:sz w:val="36"/><w:color w:val="1F4E79"/></w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="Heading2">
    <w:name w:val="heading 2"/>
    <w:pPr><w:spacing w:before="240" w:after="80"/></w:pPr>
    <w:rPr><w:b/><w:sz w:val="28"/><w:color w:val="2E75B6"/></w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="Heading3">
    <w:name w:val="heading 3"/>
    <w:pPr><w:spacing w:before="200" w:after="60"/></w:pPr>
    <w:rPr><w:b/><w:sz w:val="24"/><w:color w:val="548235"/></w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="Normal">
    <w:name w:val="Normal"/>
    <w:pPr><w:spacing w:after="120" w:line="276" w:lineRule="auto"/></w:pPr>
    <w:rPr><w:sz w:val="22"/></w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="Code">
    <w:name w:val="Code"/>
    <w:pPr><w:spacing w:after="60"/><w:shd w:val="clear" w:color="auto" w:fill="F2F2F2"/></w:pPr>
    <w:rPr><w:rFonts w:ascii="Consolas" w:hAnsi="Consolas"/><w:sz w:val="18"/></w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="ListBullet">
    <w:name w:val="List Bullet"/>
    <w:pPr><w:numPr><w:ilvl w:val="0"/></w:numPr><w:spacing w:after="60"/><w:ind w:left="720" w:hanging="360"/></w:pPr>
    <w:rPr><w:sz w:val="22"/></w:rPr>
  </w:style>
  <w:style w:type="table" w:styleId="TableGrid">
    <w:name w:val="Table Grid"/>
    <w:tblPr>
      <w:tblBorders>
        <w:top w:val="single" w:sz="4" w:space="0" w:color="999999"/>
        <w:left w:val="single" w:sz="4" w:space="0" w:color="999999"/>
        <w:bottom w:val="single" w:sz="4" w:space="0" w:color="999999"/>
        <w:right w:val="single" w:sz="4" w:space="0" w:color="999999"/>
        <w:insideH w:val="single" w:sz="4" w:space="0" w:color="999999"/>
        <w:insideV w:val="single" w:sz="4" w:space="0" w:color="999999"/>
      </w:tblBorders>
    </w:tblPr>
  </w:style>
</w:styles>"""

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"


def p_title(text):
    return f'<w:p><w:pPr><w:pStyle w:val="Title"/></w:pPr><w:r><w:t>{escape(text)}</w:t></w:r></w:p>'


def p_h1(text):
    return f'<w:p><w:pPr><w:pStyle w:val="Heading1"/></w:pPr><w:r><w:t>{escape(text)}</w:t></w:r></w:p>'


def p_h2(text):
    return f'<w:p><w:pPr><w:pStyle w:val="Heading2"/></w:pPr><w:r><w:t>{escape(text)}</w:t></w:r></w:p>'


def p_h3(text):
    return f'<w:p><w:pPr><w:pStyle w:val="Heading3"/></w:pPr><w:r><w:t>{escape(text)}</w:t></w:r></w:p>'


def p_normal(text):
    return f'<w:p><w:pPr><w:pStyle w:val="Normal"/></w:pPr><w:r><w:t xml:space="preserve">{escape(text)}</w:t></w:r></w:p>'


def p_bold(text):
    return f'<w:p><w:pPr><w:pStyle w:val="Normal"/></w:pPr><w:r><w:rPr><w:b/></w:rPr><w:t xml:space="preserve">{escape(text)}</w:t></w:r></w:p>'


def p_bullet(text):
    return f'<w:p><w:pPr><w:pStyle w:val="ListBullet"/></w:pPr><w:r><w:t xml:space="preserve">• {escape(text)}</w:t></w:r></w:p>'


def p_code(text):
    return f'<w:p><w:pPr><w:pStyle w:val="Code"/></w:pPr><w:r><w:t xml:space="preserve">{escape(text)}</w:t></w:r></w:p>'


def p_empty():
    return '<w:p/>'


def table_row(cells, header=False):
    row = "<w:tr>"
    for c in cells:
        shading = ""
        rpr = ""
        if header:
            shading = '<w:shd w:val="clear" w:color="auto" w:fill="1F4E79"/>'
            rpr = '<w:rPr><w:b/><w:color w:val="FFFFFF"/><w:sz w:val="20"/></w:rPr>'
        else:
            rpr = '<w:rPr><w:sz w:val="20"/></w:rPr>'
        row += f'<w:tc><w:tcPr><w:tcW w:w="0" w:type="auto"/>{shading}</w:tcPr>'
        row += f'<w:p><w:r>{rpr}<w:t xml:space="preserve">{escape(str(c))}</w:t></w:r></w:p></w:tc>'
    row += "</w:tr>"
    return row


def table(headers, rows):
    xml = '<w:tbl><w:tblPr><w:tblStyle w:val="TableGrid"/><w:tblW w:w="5000" w:type="pct"/></w:tblPr>'
    xml += table_row(headers, header=True)
    for r in rows:
        xml += table_row(r)
    xml += "</w:tbl>"
    return xml


parts = []

# ===== CAPA =====
parts.append(p_title("Zurich - PoC K6 Performance"))
parts.append(p_normal("Integracao Detalhada: Azure DevOps + SonarQube + Aplicacao"))
parts.append(p_empty())
parts.append(p_normal("Documento preparado pela Foursys para apresentacao ao cliente Zurich."))
parts.append(p_normal("Versao: v3 | Data: Marco 2026"))
parts.append(p_empty())

# ===== 1. VISAO GERAL =====
parts.append(p_h1("1. Visao Geral da Integracao"))
parts.append(p_normal(
    "O K6 se integra a tres pontos do ecossistema Zurich: "
    "Azure DevOps (orquestracao), SonarQube (quality gate de codigo) e a Aplicacao Piloto (alvo dos testes). "
    "Cada ponto de integracao tem um papel especifico e complementar."
))
parts.append(p_normal(
    "O objetivo nao e substituir nenhuma ferramenta existente. "
    "O K6 adiciona uma trilha de performance ao que ja existe, sem alterar a esteira corporativa."
))

# ===== 2. INTEGRACAO COM AZURE DEVOPS =====
parts.append(p_h1("2. Integracao K6 com Azure DevOps"))
parts.append(p_h2("2.1 Como explicar para o cliente"))
parts.append(p_normal(
    "O K6 vira um stage dentro da pipeline que voces ja usam. "
    "Nao e uma ferramenta solta. Ele roda como parte do fluxo que voces ja conhecem no Azure DevOps."
))

parts.append(p_h2("2.2 Como funciona na pratica"))
parts.append(p_normal(
    "O pipeline do Azure DevOps ganha um novo stage chamado 'Performance Test'. "
    "Esse stage so executa depois que o Build e o Quality Gate do SonarQube passarem com sucesso."
))
parts.append(p_normal("Exemplo de pipeline YAML com o stage de K6:"))
parts.append(p_empty())

yaml_lines = [
    "stages:",
    "  - stage: Build",
    "    jobs:",
    "      - job: BuildApp",
    "        steps:",
    "          - script: dotnet build",
    "",
    "  - stage: QualityGate",
    "    dependsOn: Build",
    "    jobs:",
    "      - job: SonarAnalysis",
    "        steps:",
    "          - script: sonar-scanner analyze",
    "",
    "  - stage: PerformanceTest",
    "    dependsOn: QualityGate",
    "    condition: succeeded()",
    "    jobs:",
    "      - job: RunK6",
    "        pool: 'SelfHostedPool-QA'",
    "        steps:",
    "          - task: AzureKeyVault@2",
    "            inputs:",
    "              azureSubscription: 'zurich-sub'",
    "              KeyVaultName: 'kv-qa-zurich'",
    "              SecretsFilter: 'api-token,api-url'",
    "",
    "          - script: |",
    "              k6 run scripts/load-test.js \\",
    "                --env API_URL=$(api-url) \\",
    "                --env API_TOKEN=$(api-token) \\",
    "                --out json=results/output.json",
    "            displayName: 'Executar K6'",
    "",
    "          - task: PublishBuildArtifacts@1",
    "            inputs:",
    "              PathtoPublish: 'results/'",
    "              ArtifactName: 'k6-results'",
]
for line in yaml_lines:
    parts.append(p_code(line))

parts.append(p_empty())
parts.append(p_h2("2.3 Pontos-chave"))
parts.append(p_bullet("O K6 so roda depois que o build e o quality gate passam"))
parts.append(p_bullet("O disparo pode ser automatico (a cada push ou merge) ou manual (Run Pipeline no portal)"))
parts.append(p_bullet("Os segredos vem do Key Vault, nunca ficam no codigo"))
parts.append(p_bullet("Os resultados sao publicados como artefato da pipeline, acessiveis no portal do Azure DevOps"))
parts.append(p_bullet("Se os thresholds falharem, o stage fica vermelho e o pipeline para"))

parts.append(p_h2("2.4 Modos de execucao"))
parts.append(table(
    ["Modo", "Como dispara", "Quando usar"],
    [
        ["Automatico", "Pipeline roda a cada push/merge na branch configurada", "Regressao continua, quality gate automatico"],
        ["Manual", "Run Pipeline no portal do Azure DevOps ou CLI", "Testes sob demanda, validacao antes de release"],
        ["Agendado", "Cron trigger na pipeline (ex: toda noite)", "Testes de carga periodicos, baseline de performance"],
    ]
))

# ===== 3. INTEGRACAO COM SONARQUBE =====
parts.append(p_h1("3. Integracao K6 com SonarQube"))
parts.append(p_h2("3.1 Como explicar para o cliente"))
parts.append(p_normal(
    "O SonarQube continua fazendo o que ja faz: analise de codigo e quality gate de qualidade. "
    "O K6 adiciona um segundo quality gate, focado em performance. Os dois sao complementares."
))

parts.append(p_h2("3.2 Dois quality gates sequenciais"))
parts.append(p_normal("O SonarQube e o K6 nao conversam diretamente entre si. "
    "Eles operam como dois gates sequenciais dentro da mesma pipeline:"))
parts.append(p_empty())
parts.append(p_bold("Build  -->  SonarQube (quality gate de codigo)  -->  K6 (quality gate de performance)"))
parts.append(p_empty())
parts.append(p_bullet("Se o SonarQube reprovar (ex: bugs criticos, cobertura baixa), o K6 nem roda"))
parts.append(p_bullet("Se o SonarQube aprovar mas o K6 reprovar (ex: p95 acima de 800ms), o pipeline falha no stage de performance"))
parts.append(p_bullet("Se ambos aprovarem, o pipeline segue para o proximo passo (deploy, evidencias, etc.)"))

parts.append(p_h2("3.3 Como configurar thresholds no K6"))
parts.append(p_normal("O quality gate de performance se define dentro do script K6:"))
parts.append(p_empty())

k6_threshold_lines = [
    "export const options = {",
    "  thresholds: {",
    "    http_req_duration: ['p(95)<800'],   // 95% das requests < 800ms",
    "    http_req_failed: ['rate<0.02'],     // menos de 2% de erro",
    "    http_reqs: ['rate>50'],             // pelo menos 50 req/s",
    "  },",
    "  stages: [",
    "    { duration: '1m', target: 20 },     // ramp-up",
    "    { duration: '3m', target: 50 },     // carga sustentada",
    "    { duration: '1m', target: 0 },      // ramp-down",
    "  ],",
    "};",
]
for line in k6_threshold_lines:
    parts.append(p_code(line))

parts.append(p_empty())
parts.append(p_normal(
    "Se qualquer threshold for violado, o K6 retorna exit code diferente de zero "
    "e o Azure DevOps marca o stage como failed."
))

parts.append(p_h2("3.4 Comparacao SonarQube vs K6"))
parts.append(table(
    ["Aspecto", "SonarQube", "K6"],
    [
        ["O que analisa", "Codigo-fonte (bugs, vulnerabilidades, cobertura)", "Comportamento real da aplicacao sob carga"],
        ["Quando roda", "Depois do build", "Depois do SonarQube"],
        ["Tipo de gate", "Qualidade de codigo", "Performance e estabilidade"],
        ["Metricas", "Bugs, code smells, cobertura, duplicacao", "Tempo de resposta, throughput, taxa de erro, p95/p99"],
        ["Resultado", "Aprovado/Reprovado no portal SonarQube", "Aprovado/Reprovado no pipeline (thresholds)"],
    ]
))

# ===== 4. INTEGRACAO COM A APLICACAO =====
parts.append(p_h1("4. Integracao K6 com a Aplicacao Zurich"))
parts.append(p_h2("4.1 Como explicar para o cliente"))
parts.append(p_normal(
    "O K6 simula usuarios reais acessando as APIs e endpoints da aplicacao de voces. "
    "Ele nao instala nada na aplicacao. Ele apenas gera trafego controlado de fora para dentro, "
    "exatamente como um usuario faria, mas em escala."
))

parts.append(p_h2("4.2 Fluxo de rede"))
parts.append(p_normal("O K6 Executor (a VM) se conecta a aplicacao-alvo pela rede privada (VNet/Subnet/NSG):"))
parts.append(p_empty())
parts.append(p_bold("VM K6 Executor  -->  VNet/Subnet  -->  NSG (regras de acesso)  -->  Aplicacao Zurich (APIs)"))
parts.append(p_empty())

parts.append(p_h2("4.3 Exemplo de script K6"))
parts.append(p_normal("O script faz chamadas HTTP reais contra a aplicacao piloto:"))
parts.append(p_empty())

k6_script_lines = [
    "import http from 'k6/http';",
    "import { check, sleep } from 'k6';",
    "",
    "const BASE_URL = __ENV.API_URL;",
    "const TOKEN = __ENV.API_TOKEN;",
    "",
    "export default function () {",
    "  const headers = {",
    "    Authorization: `Bearer ${TOKEN}`,",
    "    'Content-Type': 'application/json',",
    "  };",
    "",
    "  const res = http.get(`${BASE_URL}/api/v1/policies`, { headers });",
    "",
    "  check(res, {",
    "    'status 200': (r) => r.status === 200,",
    "    'tempo < 500ms': (r) => r.timings.duration < 500,",
    "  });",
    "",
    "  sleep(1);",
    "}",
]
for line in k6_script_lines:
    parts.append(p_code(line))

parts.append(p_empty())
parts.append(p_h2("4.4 Pontos-chave"))
parts.append(p_bullet("Nada e instalado na aplicacao: o K6 e um gerador de trafego externo"))
parts.append(p_bullet("A conexao e privada: passa pela VNet, sem necessidade de expor APIs publicamente"))
parts.append(p_bullet("A autenticacao e real: usa os mesmos tokens/credenciais que um usuario usaria"))
parts.append(p_bullet("O trafego e controlado: o script define quantos usuarios virtuais, por quanto tempo, com ramp-up gradual"))
parts.append(p_bullet("Os resultados medem a aplicacao real: tempo de resposta, taxa de erro, throughput, p95, p99"))

# ===== 5. VISAO CONSOLIDADA =====
parts.append(p_h1("5. Visao Consolidada do Fluxo"))
parts.append(p_normal("Fluxo completo da integracao, do disparo ate os resultados:"))
parts.append(p_empty())

flow_lines = [
    "1. Time QA cria/atualiza scripts K6 no repositorio",
    "2. Pipeline e disparada (automatica ou manual) no Azure DevOps",
    "3. Stage Build compila a aplicacao",
    "4. Stage SonarQube executa analise de codigo e quality gate",
    "5. Se SonarQube aprova, Stage PerformanceTest inicia",
    "6. Self-hosted Agent (Runner) recebe o job",
    "7. Runner busca segredos no Key Vault",
    "8. Runner aciona o K6 na VM Executor",
    "9. K6 gera carga contra a Aplicacao Piloto Zurich (via VNet privada)",
    "10. K6 valida thresholds (p95, erro, throughput)",
    "11. Resultados sao publicados no Storage e como artefato da pipeline",
    "12. Azure Monitor e Log Analytics capturam telemetria",
    "13. Dashboards e alertas dao visibilidade operacional",
    "14. Se thresholds falharem, pipeline para e alerta o time",
]
for line in flow_lines:
    parts.append(p_normal(line))

# ===== 6. VMs DA INFRA =====
parts.append(p_h1("6. VMs Necessarias na Infraestrutura"))
parts.append(p_normal(
    "Considerando que o Runner e reaproveitado da PoC do Selenium Grid, "
    "a trilha de K6 adiciona apenas 1 VM dedicada ao total:"
))
parts.append(table(
    ["VM", "Funcao", "Compartilhada?"],
    [
        ["VM 1", "Self-hosted Agent / Runner (funcional + performance)", "Sim, atende ambas as trilhas"],
        ["VM 2", "Selenium Grid Hub", "Dedicada para funcional"],
        ["VM 3 (VMSS)", "Browser Nodes (Scale Set)", "Dedicada para funcional"],
        ["VM 4", "K6 Executor - carga e estresse", "Dedicada para performance"],
    ]
))
parts.append(p_empty())
parts.append(p_normal("Total: 4 VMs para a plataforma completa (Selenium Grid + K6)."))

# ===== 7. FAQ =====
parts.append(p_h1("7. Perguntas Frequentes do Cliente"))
parts.append(table(
    ["Pergunta", "Resposta"],
    [
        ["Preciso instalar algo na minha aplicacao?",
         "Nao. O K6 gera trafego de fora. A aplicacao nao precisa de nenhuma mudanca."],
        ["Isso vai derrubar meu ambiente?",
         "Na PoC, a carga e pequena e controlada. O script define limites e ramp-up gradual."],
        ["O SonarQube ja nao cobre isso?",
         "O SonarQube analisa qualidade de codigo. O K6 testa comportamento real sob carga. Sao complementares."],
        ["Posso rodar sem pipeline, manualmente?",
         "Sim. O K6 pode ser executado por SSH na VM ou por Run Pipeline manual no portal."],
        ["Os resultados ficam onde?",
         "Na pipeline como artefato, no Storage Account e opcionalmente em dashboards do Azure Monitor."],
        ["Depois da PoC, meu time consegue rodar sozinho?",
         "Sim. Entregamos o ambiente, os scripts-modelo e a documentacao para autonomia."],
        ["Posso comecar mais simples?",
         "Sim. Na PoC comecamos com 1 VM, poucos cenarios e APIs piloto. A escala vem depois."],
        ["Como isso escala depois?",
         "Adicionando mais VMs de executor, mais cenarios e transformando thresholds em quality gate obrigatorio."],
        ["Precisa de AKS?",
         "Nao. A solucao roda em VMs simples, sem dependencia de Kubernetes."],
        ["Qual a diferenca entre K6 e Selenium?",
         "Selenium valida comportamento funcional (UI, jornadas). K6 valida performance (carga, resposta, estabilidade)."],
    ]
))

# ===== 8. PROXIMOS PASSOS =====
parts.append(p_h1("8. Proximos Passos"))
parts.append(p_normal("Para iniciar a PoC de K6, os seguintes itens precisam ser confirmados:"))
parts.append(p_bullet("Confirmar a aplicacao piloto e o ambiente-alvo"))
parts.append(p_bullet("Confirmar acessos de rede, autenticacao e segredos"))
parts.append(p_bullet("Definir quais APIs/endpoints entram no piloto"))
parts.append(p_bullet("Alinhar thresholds minimos esperados para tempo de resposta e erro"))
parts.append(p_bullet("Definir onde a Zurich quer visualizar resultados: pipeline, storage, dashboards ou todos"))
parts.append(p_bullet("Agendar sessao de discovery com ponto focal tecnico da Zurich"))

body_xml = "\n".join(parts)

DOCUMENT = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:body>
    {body_xml}
    <w:sectPr>
      <w:pgSz w:w="12240" w:h="15840"/>
      <w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440" w:header="720" w:footer="720"/>
    </w:sectPr>
  </w:body>
</w:document>"""

OUTPUT.parent.mkdir(parents=True, exist_ok=True)

with zipfile.ZipFile(OUTPUT, "w", zipfile.ZIP_DEFLATED) as z:
    z.writestr("[Content_Types].xml", CONTENT_TYPES)
    z.writestr("_rels/.rels", RELS)
    z.writestr("word/_rels/document.xml.rels", WORD_RELS)
    z.writestr("word/document.xml", DOCUMENT)
    z.writestr("word/styles.xml", STYLES)

print(f"Documento gerado: {OUTPUT}")
print(f"Tamanho: {OUTPUT.stat().st_size:,} bytes")
