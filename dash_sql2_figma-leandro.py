from dash import Dash, dcc, html, dash_table, callback, Input, Output, State
import plotly.express as px
import plotly.graph_objects as go
import sqlite3
import pandas as pd

# Criando o app Dash
app = Dash(__name__)

# Conectando com o banco de dados SQLite
con = sqlite3.connect('cap03_dsa.db', check_same_thread=False)
cursor = con.cursor()

# Criando a tabela (se não existir)
create_table = '''CREATE TABLE IF NOT EXISTS cap03_dsa(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                sobrenome TEXT,
                nota_exame1 REAL,
                nota_exame2 REAL,
                tipo_sistema_operacional TEXT
)'''
cursor.execute(create_table)
con.commit()

# Verificando se há dados na tabela
cursor.execute("SELECT COUNT(*) FROM cap03_dsa")
if cursor.fetchone()[0] == 0:
    insert = '''INSERT INTO cap03_dsa (nome, sobrenome, nota_exame1, nota_exame2, tipo_sistema_operacional) 
                VALUES (?, ?, ?, ?, ?)'''
    data = [
        ('Xavier', 'Murphy', 86.0, 89.0, 'Linux'),
        ('Yara', 'Bailey', 80.5, 81.0, 'Windows'),
        ('Alice', 'Smith', 80.5, 85.0, 'Windows'),
        ('Quincy', 'Roberts', 86.5, 90.0, 'Mac'),
        ('Bob', 'Johnson', 75.0, 88.0, 'Linux'),
        ('Carol', 'Williams', 90.0, 90.5, 'Mac'),
        ('Grace', 'Miller', 95.5, 93.0, 'Windows'),
        ('Nina', 'Carter', 80.5, 81.0, 'Windows'),
        ('Ursula', 'Kim', 80.0, 82.5, 'Linux'),
        ('Eve', 'Jones', 90.0, 88.0, 'Mac'),
        ('Frank', 'Garcia', 79.0, 82.0, 'Linux'),
        ('Helen', 'Davis', 90.0, 89.5, 'Mac'),
        ('Grace', 'Rodriguez', 89.0, 88.0, 'Windows'),
        ('Jack', 'Martinez', 90.0, 80.0, 'Linux'),
        ('Karen', 'Hernandez', 93.5, 91.0, 'Windows'),
        ('Leo', 'Lewis', 82.0, 85.5, 'Mac'),
        ('Mallory', 'Nelson', 91.0, 89.0, 'Linux'),
        ('Oscar', 'Mitchell', 88.0, 87.5, 'Linux'),
        ('Paul', 'Perez', 94.0, 92.0, 'Windows'),
        ('Rita', 'Gomez', 77.0, 80.0, 'Linux'),
        ('Steve', 'Freeman', 89.5, 88.5, 'Windows'),
        ('Troy', 'Reed', 90.0, 92.0, 'Mac'),
        ('Victor', 'Morgan', 90.0, 85.0, 'Windows'),
        ('Oscar', 'Bell', 85.5, 87.0, 'Mac'),
        ('Zane', 'Rivera', 89.0, 90.5, 'Mac'),
        ('Aria', 'Wright', 75.0, 76.5, 'Linux'),
        ('Bruce', 'Cooper', 90.0, 84.0, 'Windows'),
        ('Karen', 'Peterson', 90.0, 92.5, 'Mac'),
        ('Dave', 'Brown', 88.5, 89.0, 'Windows'),
        ('Derek', 'Wood', 86.0, 87.5, 'Linux')
    ]
    cursor.executemany(insert, data)
    con.commit()

# Carregar dados para o DataFrame
query = 'SELECT * FROM cap03_dsa'
df = pd.read_sql_query(query, con)

# Criando um gráfico de barras com o DataFrame correto
fig = px.bar(df, x='nome', y='nota_exame1', title='Notas do Exame 1')

# Criando um gráfico de barras com o DataFrame correto
fig2 = px.bar(df, x='nome', y='nota_exame2', title='Notas do Exame 2')

fig3 = px.pie(df, values='nota_exame1', names='tipo_sistema_operacional', title='tipo_sistema_operaciona')

fig4 = go.Figure()

fig4.add_trace(go.Pie(
    name='tipo_sistema_operacional',
    title='tipo_sistema_operacional',
    labels=df['tipo_sistema_operacional'],
    values=df['nota_exame1'],
    hole=.3,
    pull=[0,0.1,0],
    marker=dict(colors = ['#141444', '#EC7C44','#12283F'])))


# Layout do Dash
app.layout = html.Div([
    # .pbiw-financeiro-pag011
    html.Div(
        style={
            'position': 'absolute',
            'top': '24px',
            'left': '43px',
            'background': 'linear-gradient(180deg, #fcfeff, #e8e8e8)',
            'width': '1194.7px',
            'height': '672px',
            'overflow': 'hidden',
        },
    ),
    # .pbiw-financeiro-pag01-item
    html.Div(
        style={
            'position': 'absolute',
            'top': '0px',
            'left': '0px',
            'border-radius': '60px',
            'width': '330px',
            'height': '340px',
        },
    ),
    # .pbiw-financeiro-pag01-child
    html.Div(
        style={
            'position': 'absolute',
            'top': '-2.16px',
            'left': '-18.5px',
            'background-color': 'rgba(20, 20, 68, 0.8)',
            'width': '311px',
            'height': '720px',
        },
    ),
    # .pbiw-financeiro-pag01-inner
    html.Div(
        style={
            'position': 'absolute',
            'top': '440px',
            'left': '-18.5px',
            'border-radius': '60px',
            'width': '330px',
            'height': '340px',
        },
    ),
    #.group-icon
    html.Div(
        style={
            'position': 'absolute',
            'top': '9px',
            'left': '10px',
            'width': '106px',
            'height': '106px',
        },
    ),    
    #.rectangle-div
    html.Div(
        style={
            'position': 'absolute',
            'top': '0px',
            'left': '0px',
            'background-color': 'rgba(20, 20, 68, 0.6)',
            'width': '73px',
            'height': '672px',
        },
    ),

    #.pbiw-financeiro-pag01-child1
    html.Div(
        style={
            'position': 'absolute',
            'top': '0px',
            'left': '73px',
            'background-color': 'rgba(20, 20, 68, 0.8)',
            'width': '195px',
            'height': '672px',
        },
    ),         

    # .pbiw-financeiro-pag01-child2
    html.Div(
        style={
            'position': 'absolute',
            'top': '85px',
            'left': '94px',
            'width': '154px',
            'height': '130px',
        },
    ),

    # .group-child
    html.Div(
        style={
            'position': 'absolute',
            'top': '0px',
            'left': '0px',
            'box-shadow': '0px 3.7333333492279053px 14.93px rgba(0, 0, 0, 0.16)',
            'border-radius': '3.73px',
            'background': 'linear-gradient(101.78deg, rgba(20, 20, 68, 0.8), rgba(20, 20, 68, 0.6))',
            'width': '154px',
            'height': '130px',
        },
    ),    


#.group-item
    html.Div(
        style={
            'position': 'absolute',
            'top': '0px',
            'left': '0px',
            'border-radius': '7.47px',
            'background-color': '#ec7c44',
            'width': '32.4px',
            'height': '32.9px',
        },
    ),
#.vector-icon
    html.Div(
        style = {
            'position': 'absolute',
            'height': '33.43%',
            'width': '55.56%',
            'top': '36.07%',
            'right': '22.21%',
            'bottom': '30.5%',
            'left': '22.24%',
            'max-width': '100%',
            'overflow': 'hidden',
            'max-height': '100%',
        },
    ),

#.rectangle-group {
    html.Div(
        style = {
            'position': 'absolute',
            'top': '13.4px',
            'left': '8.33px',
            'width': '32.4px',
            'height': '32.9px',

        },
    ),

#.rectangle-parent {
    html.Div(
        style = {
            'position': 'absolute',
            'top': '231px',
            'left': '94px',
            'width': '154px',
            'height': '130px',
        },
    ),

#.group-inner {
    html.Div(
        style = {
            'position': 'absolute',
            'top': '0px',
            'left': '0px',
            'box-shadow': '0px 3.7333333492279053px 14.93px rgba(0, 0, 0, 0.16)',
            'border-radius': '3.73px',
            'background': 'linear-gradient(101.78deg, rgba(20, 20, 68, 0.8), rgba(20, 20, 68, 0.6))',
            'width': '154px',
           'height': '129px',
        },
    ),
#.uilmoney-withdraw-icon {
    html.Div(
        style = {
            'position': 'absolute',
            'top': '6.39px',
            'left': '5.4px',
            'width': '21.6px',
            'height': '21.9px',
            'overflow': 'hidden',
        },
    ),
    
#.group-div {
    html.Div(
        style = {
            'position': 'absolute',
            'top': '13.38px',
            'left': '8.33px',
            'width': '32.4px',
            'height': '32.9px',
        },
    ),
    
#.rectangle-container {
    html.Div(
        style = {
            'position': 'absolute',
            'top': '377px',
            'left': '94px',
            'width': '154px',
            'height': '129px',
        },
    ),
#.pbiw-financeiro-pag01-child3 {
    html.Div(
        style = {
            'position': 'absolute',
            'top': '0px',
            'left': '0px',
            'background-color': '#ec7c44',
            'width': '73px',
            'height': '67px',
        },
    ),

#.pbiw-financeiro-pag01 {
    html.Div(
        style={
            'width': '100%',
            'position': 'relative',
            'background-color': '#e8edf6',
            'height': '720px',
            'overflow': 'hidden',
            'text-align': 'left',
            'font-size': '16.79px',
            'color': '#50535d',
            'font-family': 'DIN',
        },
    ),

    
#.iconlylightchart {
    html.Div(
        style = {
            'position': 'absolute',
            'height': '7.84%',
            'width': '100%',
            'top': '22.94%',
            'right': '0%',
            'bottom': '69.22%',
            'left': '0%',
            'max-width': '100%',
            'overflow': 'hidden',
            'max-height': '100%',
        },
    ),

#.iconlylightbag-3 {
    html.Div(
        style = {
            "position": "absolute",
            "height": "7.84%",
            "width": "100%",
            "top": "46.02%",
            "right": "0%",
            "bottom": "46.14%",
            "left": "0%",
            "max-width": "100%",
            "overflow": "hidden",
            "max-height": "100%",
        },
    ),

#.iconlylightpaper {
    html.Div(
        style = {
            "position": "absolute",
            "height": "7.84%",
            "width": "100%",
            "top": "69.09%",
            "right": "0%",
            "bottom": "23.07%",
            "left": "0%",
            "max-width": "100%",
            "overflow": "hidden",
            "max-height": "100%",
        },
    ),

#.iconlylight2-user {
    html.Div(
        style = {
            "position": "absolute",
            "height": "7.84%",
            "width": "100%",
            "top": "92.17%",
            "right": "0%",
            "bottom": "0%",
            "left": "0%",
            "max-width": "100%",
            "overflow": "hidden",
            "max-height": "100%",
        },
    ),

#.iconlylighttime-circle {
    html.Div(
        style = {
            "position": "absolute",
            "height": "7.84%",
            "width": "100%",
            "top": "0%",
            "right": "0%",
            "bottom": "92.16%",
            "left": "0%",
            "max-width": "100%",
            "overflow": "hidden",
            "max-height": "100%",
        },
    ),

#.iconlylightchart-parent {
    html.Div(
        style = {
            "position": "absolute",
            "height": "43.85%",
            "width": "1.93%",
            "top": "16.96%",
            "right": "95.97%",
            "bottom": "39.18%",
            "left": "2.09%",
        },
    ),

#.pbiw-financeiro-pag01-child4 {
    html.Div(
        style = {
            "position": "absolute",
            "top": "107px",
            "left": "69px",
            "border-radius": "4px 0px 0px 4px",
            "background-color": "#21bdca",
            "width": "4px",
            "height": "36px",
        },
    ),

#.receita {
    html.Div(
        style = {
            "position": "absolute",
            "top": "105px",
            "left": "144px",
            "font-weight": "600",
            "font-family": "'Segoe UI'",
            "color": "#fff",
            "display": "flex",
            "align-items": "center",
            "width": "83px",
            "height": "17.7px",
        },
    ),

# .custo {
    html.Div(
        style={
            "position": "absolute",
            "top": "251px",
            "left": "144px",
            "font-weight": "600",
            "font-family": "'Segoe UI'",
            "color": "#fff",
            "display": "flex",
            "align-items": "center",
            "width": "83px",
            "height": "17.7px",
        }
    ),
#.despesas {
    html.Div(
        style={
            "position": "absolute",
            "top": "396px",
            "left": "144px",
            "font-weight": "600",
            "font-family": "'Segoe UI'",
            "color": "#fff",
            "display": "flex",
            "align-items": "center",
            "width": "83px",
            "height": "17.7px",
        }
    ),
#.rectangle-parent2 {
    html.Div(
        style={
            "position": "absolute",
            "top": "14.29px",
            "left": "8.33px",
            "width": "32.4px",
            "height": "32.9px",
        }
    ),
#.lucro {
    html.Div(
        style={
            "position": "absolute",
            "top": "19px",
            "left": "50px",
            "font-weight": "600",
            "display": "flex",
            "align-items": "center",
            "width": "83px",
            "height": "17.7px",
        }
    ),
#.rectangle-parent1 {
    html.Div(
        style={
            "position": "absolute",
            "top": "522px",
            "left": "93px",
            "width": "154px",
            "height": "130px",
            "color": "#fff",
            "font-family": "'Segoe UI'",
        }
    ),
#.line-div {
    html.Div(
        style={
            "position": "absolute",
            "top": "184px",
            "left": "846px",
            "border-top": "2px solid #d5d6d6",
            "box-sizing": "border-box",
            "width": "330px",
            "height": "2px",
        }
    ),
#.pbiw-financeiro-pag01-child7 {
    html.Div(
        style={
            "position": "absolute",
            "top": "477px",
            "left": "846px",
            "border-top": "2px solid #d5d6d6",
            "box-sizing": "border-box",
            "width": "330px",
            "height": "2px",
        }
    ),
#.pbiw-financeiro-pag01-child9 {
    html.Div(
        style={
            "position": "absolute",
            "top": "378.5px",
            "left": "287px",
            "box-shadow": "0px 3.7333333492279053px 14.93px rgba(0, 0, 0, 0.16)",
            "border-radius": "0px 3.73px 3.73px 0px",
            "background-color": "#fcfbfc",
            "width": "540px",
            "height": "273.5px",
        }
    ),
#.receita-ano-anterior {
    html.Div(
        style={
            "position": "absolute",
            "top": "99px",
            "left": "301px",
        }
    ),
#.receita-por-conta {
    html.Div(
        style={
            "position": "absolute",
            "top": "99px",
            "left": "861px",
        }
    ),
#.pagamento-por-tipo {
    html.Div(
        style={
            "position": "absolute",
            "top": "392px",
            "left": "861px",
        }
    ),
#.pagamento-por-lanamento {
    html.Div(
        style={
            "position": "absolute",
            "top": "492px",
            "left": "861px",
        }
    ),
#.receita-por-cliente {
    html.Div(
        style={
            "position": "absolute",
            "top": "199px",
            "left": "861px",
        }
    ),
#.pagamento-por-tipo1 {
    html.Div(
        style={
            "position": "absolute",
            "top": "392.5px",
            "left": "301px",
        }
    ),
#.principais-indicadores {
    html.Div(
        style={
            "position": "absolute",
            "top": "0px",
            "left": "0px",
            "display": "flex",
            "align-items": "center",
            "width": "154px",
            "height": "29px",
        }
    ),
#line-icon {
    html.Div(
        style={
            "position": "absolute",
            "top": "29px",
            "left": "1px",
            "max-height": "100%",
            "width": "36px",
        }
    ),
#.principais-indicadores-parent {
    html.Div(
        style={
            "position": "absolute",
            "top": "38px",
            "left": "94px",
            "width": "154px",
            "height": "29px",
            "font-size": "13.48px",
            "color": "#fff",
            "font-family": "'Segoe UI'",
        }
    ),
#.marca-branco-7 {
    html.Div(
        style={
            "position": "absolute",
            "top": "22px",
            "left": "5px",
            "width": "63.8px",
            "height": "16.5px",
            "object-fit": "cover",
        }
    ),
#.viso-geral {
    html.Div(
        style={
            "position": "absolute",
            "top": "0px",
            "left": "0px",
            "letter-spacing": "0.16px",
        }
    ),
#.dashboard-financeiro {
    html.Div(
        style={
            "position": "absolute",
            "top": "28.72px",
            "left": "2.69px",
            "font-size": "9.28px",
            "letter-spacing": "1.83px",
            "text-transform": "uppercase",
        }
    ),
#.viso-geral-parent {
    html.Div(
        style={
            "position": "absolute",
            "top": "45px",
            "left": "330px",
            "width": "147px",
            "height": "40.7px",
            "font-size": "22.66px",
            "font-family": "'Segoe UI'",
        }
    ),

    # Conteudo Principal
    html.Div([
        html.H1("Meu Dashboard com Dash",style={"text-align": "center"}),
        # .pbiw-financeiro-pag01-child8
        dcc.Graph(figure=fig,style={
            'position': 'absolute',
            'top': '85px',
            'left': '287px',
            'box-shadow': '0px 3.7333333492279053px 14.93px rgba(0, 0, 0, 0.16)',
            'border-radius': '0px 3.73px 3.73px 0px',
            'background-color': '#fcfbfc',
            'width': '540px',
            'height': '273.5px'}),
        dcc.Graph(figure=fig2,style={
            'position': 'absolute',
            'top': '378px',
            'left': '287px',
            'box-shadow': '0px 3.7333333492279053px 14.93px rgba(0, 0, 0, 0.16)',
            'border-radius': '0px 3.73px 3.73px 0px',
            'background-color': '#fcfbfc',
            'width': '540px',
            'height': '273.5px'}),
        #.pbiw-financeiro-pag01-child6
        dcc.Graph(figure=fig3,style={
            'position': 'absolute',
            'top': '378px',
            'left': '847px',
            'box-shadow': '0px 3.7333333492279053px 14.93px rgba(0, 0, 0, 0.16)',
            'border-radius': '3.73px',
            'background-color': '#fcfbfc',
            'width': '328px',
            'height': '274px'}),
        # .pbiw-financeiro-pag01-child5
        dcc.Graph(figure=fig4,style={
            'position': 'absolute',
            'top': '85px',
            'left': '847px',
            'box-shadow': '0px 3.7333333492279053px 14.93px rgba(0, 0, 0, 0.16)',
            'border-radius': '3.73px',
            'background-color': '#fcfbfc',
            'width': '328px',
            'height': '274px'})]
        #dash_table.DataTable(
        #    columns=[{"name": col, "id": col} for col in df.columns],
        #    data=df.to_dict('records'),
        #    page_size=10
        )
], id="content", style={"margin-left": "0px", "transition": "0.5s", "padding": "20px"})

# Rodando o servidor
if __name__ == '__main__':
    app.run(debug=True)