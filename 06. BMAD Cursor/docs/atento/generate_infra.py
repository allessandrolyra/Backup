"""
Atento ASR Cloud — Diagrama de Infraestrutura Azure
Usa icones oficiais Azure do draw.io (img/lib/azure2/*.svg)
"""

import xml.etree.ElementTree as ET
from xml.dom import minidom
import os

_c = [2]
def nid():
    _c[0] += 1; return str(_c[0])

# ═══════════════════════════════════════════════════════════════════════════════
# AZURE ICON PATHS (img/lib/azure2/...)
# ═══════════════════════════════════════════════════════════════════════════════

AZ = {
    "vpn_gw":       "networking/VPN_Gateways",
    "vnet":         "networking/Virtual_Networks",
    "nsg":          "networking/Network_Security_Groups",
    "private_link": "networking/Private_Link",
    "subnet":       "networking/Subnet",
    "apim":         "integration/API_Management_Services",
    "app_svc":      "app_services/App_Services",
    "aks":          "containers/Kubernetes_Services",
    "redis":        "databases/Azure_Cache_for_Redis",
    "key_vault":    "security/Key_Vaults",
    "speech":       "ai_machine_learning/Cognitive_Services",
    "monitor":      "management_governance/Monitor",
    "app_insights": "devops/Application_Insights",
    "log_analytics":"analytics/Log_Analytics_Workspaces",
    "subscription": "general/Subscriptions",
    "rg":           "general/Resource_Groups",
}

def az_style(key):
    path = AZ[key]
    return (
        f"aspect=fixed;html=1;align=center;fontSize=11;image=img/lib/azure2/{path}.svg;"
        "labelPosition=center;verticalLabelPosition=bottom;verticalAlign=top;"
        "imageAlign=center;spacingTop=0;"
    )

# ═══════════════════════════════════════════════════════════════════════════════
# STYLES
# ═══════════════════════════════════════════════════════════════════════════════

S_ONPREM = (
    "html=1;rounded=1;fillColor=#FFF8E1;strokeColor=#F57F17;strokeWidth=2;"
    "fontSize=14;fontStyle=1;fontColor=#E65100;align=left;verticalAlign=top;"
    "spacing=15;spacingTop=0;container=1;whiteSpace=wrap;"
)

S_AZ_SUB = (
    "html=1;rounded=1;fillColor=#F3F9FF;strokeColor=#0078D4;strokeWidth=2;"
    "fontSize=14;fontStyle=1;fontColor=#0078D4;align=left;verticalAlign=top;"
    "spacing=15;spacingTop=0;container=1;whiteSpace=wrap;"
)

S_RG = (
    "html=1;rounded=1;dashed=1;dashPattern=10 10;fillColor=none;"
    "strokeColor=#767676;strokeWidth=2;fontSize=13;fontStyle=1;fontColor=#767676;"
    "align=left;verticalAlign=top;spacing=15;spacingTop=0;container=1;whiteSpace=wrap;"
)

S_VNET = (
    "html=1;rounded=1;dashed=1;dashPattern=5 5;fillColor=#E6F2FF;"
    "strokeColor=#0078D4;strokeWidth=2;fontSize=13;fontStyle=1;fontColor=#0078D4;"
    "align=left;verticalAlign=top;spacing=12;spacingTop=0;container=1;whiteSpace=wrap;"
)

S_SUBNET = (
    "html=1;rounded=0;fillColor=#F0F7FF;strokeColor=#4A90D9;strokeWidth=1;"
    "fontSize=11;fontStyle=1;fontColor=#0078D4;align=left;verticalAlign=top;"
    "spacing=8;spacingTop=0;container=1;whiteSpace=wrap;"
)

S_PAAS = (
    "html=1;rounded=1;fillColor=#F5F5F5;strokeColor=#BDBDBD;strokeWidth=1;"
    "fontSize=12;fontStyle=1;fontColor=#616161;align=left;verticalAlign=top;"
    "spacing=10;spacingTop=0;container=1;whiteSpace=wrap;dashed=1;dashPattern=5 5;"
)

S_ONPREM_BOX = (
    "html=1;rounded=1;fillColor=#5D4037;strokeColor=#3E2723;strokeWidth=2;"
    "fontSize=12;fontStyle=1;fontColor=#ffffff;align=center;verticalAlign=middle;"
    "whiteSpace=wrap;"
)

S_SERVER = (
    "html=1;aspect=fixed;align=center;fontSize=11;"
    "labelPosition=center;verticalLabelPosition=bottom;verticalAlign=top;"
    "image=img/lib/azure2/general/10021-icon-service-On-Premises-Data-Gateways.svg;"
)

S_ARROW = (
    "html=1;endArrow=blockThin;fontSize=10;fontColor=#333333;"
    "strokeWidth=1.5;endFill=1;strokeColor=#0078D4;endSize=10;"
    "rounded=1;edgeStyle=orthogonalEdgeStyle;"
)

S_ARROW_VPN = (
    "html=1;endArrow=blockThin;startArrow=blockThin;fontSize=12;fontStyle=1;"
    "fontColor=#C62828;strokeWidth=3;endFill=1;startFill=1;strokeColor=#C62828;"
    "dashed=1;dashPattern=8 8;rounded=1;"
)

S_ARROW_PE = (
    "html=1;endArrow=blockThin;fontSize=9;fontColor=#999999;"
    "strokeWidth=1;endFill=1;strokeColor=#999999;endSize=8;"
    "rounded=1;dashed=1;dashPattern=4 4;edgeStyle=orthogonalEdgeStyle;"
)

S_LABEL = (
    "html=1;text;align=center;verticalAlign=middle;resizable=0;points=[];"
    "autosize=1;strokeColor=none;fillColor=none;"
)

S_TITLE = S_LABEL + "fontSize=22;fontStyle=1;fontColor=#333333;"
S_NOTE = (
    "html=1;rounded=1;whiteSpace=wrap;fillColor=#E8F5E9;strokeColor=#2E7D32;"
    "strokeWidth=1;fontColor=#1B5E20;align=center;verticalAlign=middle;fontSize=11;"
)


# ═══════════════════════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════════════════════

def mk():
    m = ET.Element("mxGraphModel",
        dx="1422", dy="762", grid="1", gridSize="10", guides="1",
        tooltips="1", connect="1", arrows="1", fold="1", page="1",
        pageScale="1", pageWidth="2200", pageHeight="1600", math="0", shadow="0")
    ro = ET.SubElement(m, "root")
    ET.SubElement(ro, "mxCell", id="0")
    ET.SubElement(ro, "mxCell", id="1", parent="0")
    return m, ro


def bx(ro, cid, val, sty, x, y, w, h, par="1"):
    c = ET.SubElement(ro, "mxCell", id=cid, value=val, style=sty, vertex="1", parent=par)
    g = ET.SubElement(c, "mxGeometry", x=str(x), y=str(y), width=str(w), height=str(h))
    g.set("as", "geometry")


def ed(ro, eid, src, tgt, val="", sty=S_ARROW, par="1"):
    c = ET.SubElement(ro, "mxCell", id=eid, value=val, style=sty, edge="1", source=src, target=tgt, parent=par)
    g = ET.SubElement(c, "mxGeometry", relative="1"); g.set("as", "geometry")


def icon(ro, cid, label, key, x, y, sz=50, par="1"):
    bx(ro, cid, label, az_style(key), x, y, sz, sz, par)


# ═══════════════════════════════════════════════════════════════════════════════
# INFRASTRUCTURE DIAGRAM
# ═══════════════════════════════════════════════════════════════════════════════

def build_infra():
    _c[0] = 2
    m, r = mk()

    # ── TITLE ──
    bx(r, nid(), "Diagrama de Infraestrutura Azure - Atento ASR Cloud", S_TITLE, 500, 15, 1200, 40)
    bx(r, nid(), "Foursys SaaS | Region: Brazil South | VPN Site-to-Site com Atento",
       S_LABEL + "fontSize=13;fontColor=#666666;", 600, 55, 1000, 25)

    # ══════════════════════════════════════════════════════════════════════════
    # ON-PREMISES — Atento
    # ══════════════════════════════════════════════════════════════════════════

    g_on = nid()
    bx(r, g_on, "ON-PREMISES  |  Atento Data Center  |  Sao Paulo",
       S_ONPREM, 30, 100, 900, 250)

    # Avaya SBC
    avaya_sbc = nid()
    bx(r, avaya_sbc, "Avaya SBC<br/>Session Border Controller",
       S_ONPREM_BOX, 40, 60, 180, 80, par=g_on)

    # URA/IVR
    avaya_ura = nid()
    bx(r, avaya_ura, "URA / IVR<br/>Avaya AAEP/VXML",
       S_ONPREM_BOX, 270, 60, 180, 80, par=g_on)

    # Backend
    backend = nid()
    bx(r, backend, "Backend Atento<br/>CRM + Cadastro",
       S_ONPREM_BOX.replace("fillColor=#5D4037", "fillColor=#78909C").replace("strokeColor=#3E2723", "strokeColor=#546E7A"),
       500, 60, 180, 80, par=g_on)

    # Firewall / VPN
    fw = nid()
    bx(r, fw, "Firewall / Router<br/>VPN Endpoint IPSec",
       S_ONPREM_BOX.replace("fillColor=#5D4037", "fillColor=#BF360C").replace("strokeColor=#3E2723", "strokeColor=#8B2500"),
       270, 160, 200, 60, par=g_on)

    # On-prem internal arrows
    ed(r, nid(), avaya_sbc, avaya_ura, "SIP/RTP", S_ARROW.replace("strokeColor=#0078D4", "strokeColor=#5D4037;"), par=g_on)
    ed(r, nid(), avaya_ura, fw, "Audio stream", S_ARROW.replace("strokeColor=#0078D4", "strokeColor=#5D4037;"), par=g_on)
    ed(r, nid(), avaya_ura, backend, "Valida CNPJ", S_ARROW.replace("strokeColor=#0078D4", "strokeColor=#78909C;"), par=g_on)

    # ══════════════════════════════════════════════════════════════════════════
    # VPN TUNNEL (between on-prem and Azure)
    # ══════════════════════════════════════════════════════════════════════════

    vpn_line_src = nid()
    bx(r, vpn_line_src, "",
       "html=1;fillColor=none;strokeColor=none;", 400, 350, 10, 10)

    bx(r, nid(), "VPN Site-to-Site<br/>IPSec IKEv2 | AES-256-GCM | BGP<br/>Active-Active (2 tuneis)",
       "html=1;rounded=1;fillColor=#FFEBEE;strokeColor=#C62828;strokeWidth=2;dashed=1;dashPattern=8 8;"
       "fontColor=#C62828;align=center;verticalAlign=middle;fontSize=12;fontStyle=1;whiteSpace=wrap;",
       280, 365, 380, 70)

    # ══════════════════════════════════════════════════════════════════════════
    # AZURE SUBSCRIPTION
    # ══════════════════════════════════════════════════════════════════════════

    g_sub = nid()
    bx(r, g_sub, "Azure Subscription: sub-foursys-atento-prod",
       S_AZ_SUB, 30, 460, 2130, 1100)

    # Subscription icon
    icon(r, nid(), "", "subscription", 15, 5, 30, par=g_sub)

    # ── Resource Group ──
    g_rg = nid()
    bx(r, g_rg, "Resource Group: rg-atento-asr-prod  |  Brazil South",
       S_RG, 20, 50, 2090, 1020, par=g_sub)

    icon(r, nid(), "", "rg", 15, 5, 25, par=g_rg)

    # ══════════════════════════════════════════════════════════════════════════
    # VNET
    # ══════════════════════════════════════════════════════════════════════════

    g_vnet = nid()
    bx(r, g_vnet, "VNet: vnet-atento-asr  |  10.100.0.0/16",
       S_VNET, 20, 50, 1280, 930, par=g_rg)

    icon(r, nid(), "", "vnet", 15, 5, 30, par=g_vnet)

    # ── GatewaySubnet ──
    g_gw = nid()
    bx(r, g_gw, "GatewaySubnet  |  10.100.0.0/27",
       S_SUBNET, 30, 55, 500, 160, par=g_vnet)

    vpn_gw = nid()
    icon(r, vpn_gw, "VPN Gateway<br/>VpnGw2AZ<br/>Zone-Redundant", "vpn_gw", 60, 40, 50, par=g_gw)

    bx(r, nid(), "Active-Active<br/>BGP Enabled<br/>3 Availability Zones",
       S_LABEL + "fontSize=10;fontColor=#0078D4;align=left;", 180, 40, 200, 60, par=g_gw)

    # ── Subnet APIM ──
    g_apim = nid()
    bx(r, g_apim, "snet-apim  |  10.100.1.0/24",
       S_SUBNET, 30, 240, 500, 160, par=g_vnet)

    nsg_apim = nid()
    icon(r, nsg_apim, "NSG", "nsg", 430, 10, 40, par=g_apim)

    apim = nid()
    icon(r, apim, "API Management<br/>apim-atento-asr<br/>Standard v2", "apim", 60, 40, 50, par=g_apim)

    bx(r, nid(), "Auth: API Key + MI<br/>Rate Limiting<br/>Request Logging<br/>Internal VNet Mode",
       S_LABEL + "fontSize=10;fontColor=#0078D4;align=left;", 180, 35, 200, 70, par=g_apim)

    # ── Subnet App ──
    g_app = nid()
    bx(r, g_app, "snet-app  |  10.100.2.0/24",
       S_SUBNET, 30, 425, 500, 180, par=g_vnet)

    nsg_app = nid()
    icon(r, nsg_app, "NSG", "nsg", 430, 10, 40, par=g_app)

    app1 = nid()
    icon(r, app1, "ASR Orchestrator #1<br/>App Service P2v3<br/>AZ-1", "app_svc", 40, 45, 50, par=g_app)

    app2 = nid()
    icon(r, app2, "ASR Orchestrator #2<br/>App Service P2v3<br/>AZ-2", "app_svc", 180, 45, 50, par=g_app)

    aks_future = nid()
    icon(r, aks_future, "AKS (Fase 2)<br/>Kubernetes<br/>3-20 nodes", "aks", 330, 45, 50, par=g_app)

    bx(r, nid(), "Autoscale: min=2 max=20<br/>VNet Integration",
       S_LABEL + "fontSize=10;fontColor=#0078D4;align=left;", 130, 120, 200, 30, par=g_app)

    # ── Subnet Private Endpoints ──
    g_pe = nid()
    bx(r, g_pe, "snet-pe  |  10.100.3.0/24  |  Private Endpoints",
       S_SUBNET, 30, 630, 500, 140, par=g_vnet)

    pe1 = nid()
    icon(r, pe1, "PE: Speech<br/>Services", "private_link", 50, 40, 40, par=g_pe)

    pe2 = nid()
    icon(r, pe2, "PE: Redis<br/>Cache", "private_link", 170, 40, 40, par=g_pe)

    pe3 = nid()
    icon(r, pe3, "PE: Key<br/>Vault", "private_link", 290, 40, 40, par=g_pe)

    # ── Subnet Labels ──
    bx(r, nid(), "NSG Rule: Allow from Atento IPs only<br/>Deny all other inbound",
       S_LABEL + "fontSize=9;fontColor=#C62828;fontStyle=2;", 560, 250, 250, 30, par=g_vnet)

    bx(r, nid(), "NSG Rule: Allow from snet-apim only",
       S_LABEL + "fontSize=9;fontColor=#C62828;fontStyle=2;", 560, 440, 220, 20, par=g_vnet)

    # ══════════════════════════════════════════════════════════════════════════
    # PaaS SERVICES (fora do VNet, acessados via Private Endpoints)
    # ══════════════════════════════════════════════════════════════════════════

    g_paas = nid()
    bx(r, g_paas, "PaaS Services  (acesso via Private Endpoints)",
       S_PAAS, 1330, 50, 730, 420, par=g_rg)

    # Speech Services
    speech = nid()
    icon(r, speech, "Azure Speech Services<br/>speech-atento-asr<br/>S0 Standard | STT Real-Time", "speech", 40, 55, 50, par=g_paas)

    bx(r, nid(), "Custom Speech Model<br/>Treinado: CNPJ alfanumerico<br/>Sotaques regionais<br/>Alfabeto fonetico",
       "html=1;rounded=1;fillColor=#F3E5F5;strokeColor=#6A1B9A;strokeWidth=1;"
       "fontColor=#4A148C;align=center;verticalAlign=middle;fontSize=10;whiteSpace=wrap;",
       170, 55, 200, 80, par=g_paas)

    # Redis
    redis = nid()
    icon(r, redis, "Azure Cache for Redis<br/>redis-atento-asr<br/>Standard C1 | Zone-Redundant", "redis", 430, 55, 50, par=g_paas)

    # Key Vault
    kv = nid()
    icon(r, kv, "Key Vault<br/>kv-atento-asr<br/>Soft-delete | Purge protection", "key_vault", 580, 55, 50, par=g_paas)

    # Labels
    bx(r, nid(), "Sem acesso publico<br/>Apenas via Private Endpoints",
       S_LABEL + "fontSize=10;fontColor=#C62828;fontStyle=2;", 200, 160, 200, 30, par=g_paas)

    # ══════════════════════════════════════════════════════════════════════════
    # OBSERVABILITY
    # ══════════════════════════════════════════════════════════════════════════

    g_obs = nid()
    bx(r, g_obs, "Observabilidade",
       S_PAAS.replace("fillColor=#F5F5F5", "fillColor=#ECEFF1"), 1330, 500, 730, 230, par=g_rg)

    monitor = nid()
    icon(r, monitor, "Azure Monitor<br/>Metricas + Alertas", "monitor", 50, 50, 50, par=g_obs)

    app_ins = nid()
    icon(r, app_ins, "Application Insights<br/>APM + Distributed Tracing", "app_insights", 230, 50, 50, par=g_obs)

    log_an = nid()
    icon(r, log_an, "Log Analytics<br/>law-atento-asr<br/>Logs + KQL + Retention 90d", "log_analytics", 430, 50, 50, par=g_obs)

    bx(r, nid(), "KPIs: Latencia E2E (p50/p95/p99) | Taxa ASR | Retry/Fallback | Throughput | Saude VPN",
       S_LABEL + "fontSize=9;fontColor=#37474F;", 50, 160, 600, 20, par=g_obs)

    # ══════════════════════════════════════════════════════════════════════════
    # INFO BOXES
    # ══════════════════════════════════════════════════════════════════════════

    g_info = nid()
    bx(r, g_info, "Especificacoes Tecnicas",
       S_PAAS.replace("fillColor=#F5F5F5", "fillColor=#E8F5E9").replace("strokeColor=#BDBDBD", "strokeColor=#2E7D32"),
       1330, 760, 730, 230, par=g_rg)

    specs = [
        "Regiao: Brazil South (Sao Paulo)",
        "SLA Composto: 99.95%",
        "Latencia E2E: 300-900ms",
        "Volumetria: 1-1000 chamadas/min",
        "Sessoes concorrentes pico: ~166",
        "VPN: VpnGw2AZ 1.25 Gbps Active-Active",
        "Dados: Audio descartado pos-transcricao (LGPD)",
        "Criptografia: AES-256 rest | TLS 1.2+ transit",
        "Identidade: Managed Identity (zero secrets no codigo)",
    ]
    for i, spec in enumerate(specs):
        bx(r, nid(), spec, S_LABEL + "fontSize=10;fontColor=#1B5E20;align=left;",
           20, 45 + i * 20, 700, 18, par=g_info)

    # ══════════════════════════════════════════════════════════════════════════
    # ARROWS — Main Flow
    # ══════════════════════════════════════════════════════════════════════════

    # On-Prem VPN → Azure VPN Gateway
    ed(r, nid(), fw, vpn_gw, "VPN S2S IPSec<br/>IKEv2 AES-256", S_ARROW_VPN)

    # VPN GW → APIM
    ed(r, nid(), vpn_gw, apim, "Trafego VNet", S_ARROW)

    # APIM → App Service 1
    ed(r, nid(), apim, app1, "WebSocket", S_ARROW)

    # APIM → App Service 2
    ed(r, nid(), apim, app2, "WebSocket", S_ARROW)

    # App1 → PE Speech (via PE)
    ed(r, nid(), app1, pe1, "Audio STT", S_ARROW_PE)

    # App2 → PE Speech (via PE)
    ed(r, nid(), app2, pe1, "", S_ARROW_PE)

    # App1 → PE Redis
    ed(r, nid(), app1, pe2, "Cache", S_ARROW_PE)

    # App1 → PE KV
    ed(r, nid(), app2, pe3, "Secrets", S_ARROW_PE)

    # PE → PaaS (conceptual - Private Endpoint connections)
    ed(r, nid(), pe1, speech, "Private Endpoint", S_ARROW_PE)
    ed(r, nid(), pe2, redis, "Private Endpoint", S_ARROW_PE)
    ed(r, nid(), pe3, kv, "Private Endpoint", S_ARROW_PE)

    # Orchestrator → Monitor
    ed(r, nid(), app1, app_ins, "Telemetria", S_ARROW_PE)

    return m


# ═══════════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    d = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(d, "atento-asr-infra-azure.drawio")

    m, _ = build_infra(), None

    mxf = ET.Element("mxfile", host="app.diagrams.net",
        modified="2026-04-08T00:00:00.000Z", agent="Lyra-Architect",
        version="24.0.0", type="device")

    d1 = ET.SubElement(mxf, "diagram", id="infra", name="Infraestrutura Azure")
    result = build_infra()
    d1.append(result)

    raw = ET.tostring(mxf, encoding="unicode")
    pretty = minidom.parseString(raw).toprettyxml(indent="  ")
    lines = [l for l in pretty.split("\n") if l.strip()]

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    sz = os.path.getsize(path)
    print(f"[OK] {path}")
    print(f"     {sz:,} bytes")
    print()
    print("Componentes Azure com icones oficiais:")
    print("  - VPN Gateway (VpnGw2AZ Zone-Redundant)")
    print("  - Virtual Network + 4 Subnets + NSGs")
    print("  - API Management (Standard v2)")
    print("  - App Service P2v3 x2 (+ AKS futuro)")
    print("  - Azure Speech Services + Custom Model")
    print("  - Azure Cache for Redis")
    print("  - Key Vault")
    print("  - Azure Monitor + App Insights + Log Analytics")
    print("  - Private Endpoints x3")
    print("  - Resource Group + Subscription")
