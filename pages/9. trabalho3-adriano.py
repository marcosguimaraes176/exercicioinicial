import streamlit as st
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
import io

st.title("Relatório Técnico – Análise de Proficiência (PAEBES)")

# Botão para gerar PDF
if st.button("Gerar Relatório PDF"):
    buffer = io.BytesIO()

    # Criação do documento em memória
    doc = SimpleDocTemplate(buffer, pagesize=A4,
                            rightMargin=50, leftMargin=50,
                            topMargin=50, bottomMargin=50)
    
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Heading1Custom', parent=styles['Heading1'], spaceAfter=12))
    styles.add(ParagraphStyle(name='Heading2Custom', parent=styles['Heading2'], spaceAfter=8))
    styles.add(ParagraphStyle(name='BodyTextCustom', parent=styles['BodyText'], spaceAfter=10, leading=16))
    
    content = []
    content.append(Paragraph("<b>GOVERNO DO ESTADO DO ESPÍRITO SANTO</b><br/>"
                             "Secretaria de Estado da Educação (SEDU)<br/>"
                             "Gerência de Currículo da Educação Básica (GECEB)<br/><br/>"
                             "<b>RELATÓRIO TÉCNICO</b><br/>"
                             "Análise e Previsão da Proficiência no PAEBES – Língua Portuguesa (3ª Série do Ensino Médio)", 
                             styles['Heading1Custom']))
    content.append(Spacer(1, 12))

    sections = [
        ("1. Introdução", "Este relatório apresenta a análise da série temporal da proficiência média em Língua Portuguesa..."),
        ("2. Base de Dados", "A base de dados utilizada abrange o período de 2017 a 2024, com exceção de 2020..."),
        ("3. Visualização da Série Original", "A série temporal foi inicialmente representada graficamente..."),
        # (demais seções aqui — mesmas do código anterior)
    ]

    for title, text in sections:
        content.append(Paragraph(f"<b>{title}</b>", styles['Heading2Custom']))
        content.append(Paragraph(text, styles['BodyTextCustom']))

    # Exemplo de tabela
    data = [
        ["Etapa", "Objetivo", "Método", "Resultado"],
        ["Visualização", "Identificar padrões", "Gráfico temporal", "Tendência pós-pandemia"],
        ["ADF", "Verificar estabilidade", "Teste ADF", "Série não estacionária"],
        ["ARIMA", "Modelar tendência", "ARIMA(0,1,0)", "Leve crescimento"]
    ]

    table = Table(data, hAlign='LEFT', colWidths=[120, 150, 120, 120])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('ALIGN', (0,0), (-1,-1), 'CENTER')
    ]))
    content.append(table)

    doc.build(content)

    buffer.seek(0)

    st.success("Relatório gerado com sucesso!")
    st.download_button(
        label="📄 Baixar Relatório PDF",
        data=buffer,
        file_name="Relatorio_Analise_Paebes_2025.pdf",
        mime="application/pdf"
    )
