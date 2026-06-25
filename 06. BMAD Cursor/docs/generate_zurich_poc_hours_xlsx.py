from pathlib import Path
from xml.sax.saxutils import escape
import zipfile


OUTPUT = Path(r"c:\01. Foursys\06. BMAD Cursor\docs\zurich-poc-horas-arquiteto-sre.xlsx")


DETAIL_ROWS = [
    ["Arquiteto", "Levantamento tecnico e alinhamento inicial", 4, 6, 5],
    ["Arquiteto", "Desenho da arquitetura da PoC sem AKS", 6, 8, 7],
    ["Arquiteto", "Definicao do modelo de integracao com Azure DevOps e SonarQube", 4, 6, 5],
    ["Arquiteto", "Definicao do papel do Runner e desenho do fluxo manual/automatizado", 4, 6, 5],
    ["Arquiteto", "Premissas de escalabilidade, seguranca e capacity inicial", 3, 5, 4],
    ["Arquiteto", "Apoio tecnico, revisoes e ajustes de arquitetura durante a configuracao", 3, 5, 4],
    ["SRE / DevOps", "Provisionamento base das VMs e rede da PoC", 8, 12, 10],
    ["SRE / DevOps", "Instalacao e configuracao do Selenium Grid Hub", 6, 10, 8],
    ["SRE / DevOps", "Configuracao do VM Scale Set dos Browser Nodes", 8, 12, 10],
    ["SRE / DevOps", "Configuracao do Self-hosted Agent / Runner", 8, 12, 10],
    ["SRE / DevOps", "Integracao com a esteira Azure DevOps existente", 6, 10, 8],
    ["SRE / DevOps", "Integracao com evidencias, logs e publicacao de artefatos", 4, 6, 5],
    ["SRE / DevOps", "Monitoracao basica, alertas e validacao operacional", 3, 5, 4],
    ["SRE / DevOps", "Testes tecnicos, troubleshooting e estabilizacao inicial", 6, 10, 8],
]


def column_letter(idx: int) -> str:
    result = ""
    while idx > 0:
        idx, rem = divmod(idx - 1, 26)
        result = chr(65 + rem) + result
    return result


def cell_ref(row_idx: int, col_idx: int) -> str:
    return f"{column_letter(col_idx)}{row_idx}"


def inline_cell(row_idx: int, col_idx: int, value: str) -> str:
    ref = cell_ref(row_idx, col_idx)
    return f'<c r="{ref}" t="inlineStr"><is><t>{escape(str(value))}</t></is></c>'


def number_cell(row_idx: int, col_idx: int, value) -> str:
    ref = cell_ref(row_idx, col_idx)
    return f'<c r="{ref}"><v>{value}</v></c>'


def formula_cell(row_idx: int, col_idx: int, formula: str) -> str:
    ref = cell_ref(row_idx, col_idx)
    return f'<c r="{ref}"><f>{escape(formula)}</f></c>'


def build_sheet(rows):
    xml_rows = []
    for row_idx, row in enumerate(rows, start=1):
        cells = []
        for col_idx, value in enumerate(row, start=1):
            if isinstance(value, str) and value.startswith("="):
                cells.append(formula_cell(row_idx, col_idx, value[1:]))
            elif isinstance(value, (int, float)):
                cells.append(number_cell(row_idx, col_idx, value))
            else:
                cells.append(inline_cell(row_idx, col_idx, value))
        xml_rows.append(f"<row r=\"{row_idx}\">{''.join(cells)}</row>")
    sheet_data = "".join(xml_rows)
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
        f"<sheetData>{sheet_data}</sheetData>"
        "</worksheet>"
    )


summary_rows = [
    ["Perfil", "Horas Min", "Horas Max", "Referencia"],
    ["Arquiteto", "=SUMIFS(Detalhamento!C:C,Detalhamento!A:A,A2)", "=SUMIFS(Detalhamento!D:D,Detalhamento!A:A,A2)", "=SUMIFS(Detalhamento!E:E,Detalhamento!A:A,A2)"],
    ["SRE / DevOps", "=SUMIFS(Detalhamento!C:C,Detalhamento!A:A,A3)", "=SUMIFS(Detalhamento!D:D,Detalhamento!A:A,A3)", "=SUMIFS(Detalhamento!E:E,Detalhamento!A:A,A3)"],
    ["Total", "=SUM(B2:B3)", "=SUM(C2:C3)", "=SUM(D2:D3)"],
]

detail_rows = [["Perfil", "Atividade", "Horas Min", "Horas Max", "Referencia"]]
detail_rows.extend(DETAIL_ROWS)

premises_rows = [
    ["Premissa", "Valor"],
    ["Escopo", "PoC simples do Selenium Grid sem AKS"],
    ["Integracoes", "Azure DevOps e SonarQube ja existentes no cliente"],
    ["Execucao", "Manual e automatizada pela esteira"],
    ["Infra", "1 VM para Hub, VM Scale Set para Browser Nodes e camada de Runner"],
    ["Observacao", "Estimativa com gordura por ser a primeira configuracao deste tipo para a equipe"],
]


content_types = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>
  <Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
  <Override PartName="/xl/worksheets/sheet2.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
  <Override PartName="/xl/worksheets/sheet3.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
  <Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>
  <Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
  <Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
</Types>
"""

rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
  <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>
"""

workbook = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"
 xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
  <sheets>
    <sheet name="Resumo" sheetId="1" r:id="rId1"/>
    <sheet name="Detalhamento" sheetId="2" r:id="rId2"/>
    <sheet name="Premissas" sheetId="3" r:id="rId3"/>
  </sheets>
</workbook>
"""

workbook_rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet2.xml"/>
  <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet3.xml"/>
  <Relationship Id="rId4" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
</Relationships>
"""

styles = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
  <fonts count="1"><font><sz val="11"/><name val="Calibri"/></font></fonts>
  <fills count="2"><fill><patternFill patternType="none"/></fill><fill><patternFill patternType="gray125"/></fill></fills>
  <borders count="1"><border><left/><right/><top/><bottom/><diagonal/></border></borders>
  <cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs>
  <cellXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0"/></cellXfs>
  <cellStyles count="1"><cellStyle name="Normal" xfId="0" builtinId="0"/></cellStyles>
</styleSheet>
"""

core = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties"
 xmlns:dc="http://purl.org/dc/elements/1.1/"
 xmlns:dcterms="http://purl.org/dc/terms/"
 xmlns:dcmitype="http://purl.org/dc/dcmitype/"
 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dc:creator>Cursor GPT-5.4</dc:creator>
  <cp:lastModifiedBy>Cursor GPT-5.4</cp:lastModifiedBy>
  <dc:title>Zurich PoC - Horas Arquiteto e SRE</dc:title>
</cp:coreProperties>
"""

app = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties"
 xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">
  <Application>Microsoft Excel</Application>
</Properties>
"""


OUTPUT.parent.mkdir(parents=True, exist_ok=True)

with zipfile.ZipFile(OUTPUT, "w", compression=zipfile.ZIP_DEFLATED) as zf:
    zf.writestr("[Content_Types].xml", content_types)
    zf.writestr("_rels/.rels", rels)
    zf.writestr("xl/workbook.xml", workbook)
    zf.writestr("xl/_rels/workbook.xml.rels", workbook_rels)
    zf.writestr("xl/styles.xml", styles)
    zf.writestr("xl/worksheets/sheet1.xml", build_sheet(summary_rows))
    zf.writestr("xl/worksheets/sheet2.xml", build_sheet(detail_rows))
    zf.writestr("xl/worksheets/sheet3.xml", build_sheet(premises_rows))
    zf.writestr("docProps/core.xml", core)
    zf.writestr("docProps/app.xml", app)

print(f"Arquivo gerado: {OUTPUT}")
