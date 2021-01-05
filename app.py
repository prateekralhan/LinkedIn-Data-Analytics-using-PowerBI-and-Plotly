import dash
import dash_core_components as dcc
import plotly.express as px
import pandas as pd
import dash_html_components as html
import plotly.graph_objects as go
from wordcloud import WordCloud, STOPWORDS
import calendar
import dash_bootstrap_components as dbc
import plotly.io as plt_io


#Creating template for Dark Theme
plt_io.templates["custom_dark"] = plt_io.templates["plotly_dark"]
plt_io.templates["custom_dark"]['layout']['paper_bgcolor'] = '#1e1e2e'
plt_io.templates["custom_dark"]['layout']['plot_bgcolor'] = '#1e1e2e'
plt_io.templates['custom_dark']['layout']['yaxis']['gridcolor'] = '#342c47'
plt_io.templates['custom_dark']['layout']['xaxis']['gridcolor'] = '#342c47'


#Analysing the count of sent vs received messages year wise
dfMessages=pd.read_excel('./data/messages.xlsx')
dfMessages['DATE'] = pd.DatetimeIndex(dfMessages['DATE']).year
dfMessagesCount = dfMessages['DATE'].count()
dfMessagesSent=dfMessages[dfMessages['FROM']=='Prateek Ralhan']
dfMessagesReceived=dfMessages[dfMessages['TO']=='Prateek Ralhan']
dfMessagesSentCount=dfMessagesSent.groupby(['DATE']).size().reset_index(name="Count")
dfMessagesReceivedCount=dfMessagesReceived.groupby(['DATE']).size().reset_index(name="Count")
fig1 = go.Figure(data=[
    go.Bar(name='Sent', x=dfMessagesSentCount['DATE'].apply(lambda x: str(x)), y=dfMessagesSentCount['Count']),
    go.Bar(name='Received', x=dfMessagesReceivedCount['DATE'], y=dfMessagesReceivedCount['Count'])
],layout=go.Layout(
        title=go.layout.Title(text="Distribution of Messages 📥")
    ))
fig1.update_layout(barmode='stack')
fig1.layout.template = 'custom_dark'


#Analysing Incoming and Outgoing Invitations
dfInvitations=pd.read_csv('./data/Invitations.csv')
InvitationsCount= dfInvitations.shape[0]
dfInvitationsCount=dfInvitations.groupby(['Direction']).size().reset_index(name="Count")
fig2=px.pie(dfInvitationsCount,values='Count',names='Direction',title="Distribution of Invitations 📬",color_discrete_sequence=px.colors.qualitative.Set3)
fig2.layout.template = 'custom_dark'


#Analysing the Job Titles/ Jon Roles for my Connections
dfConnections=pd.read_csv('./data/Connections.csv')
dfConnections=dfConnections.dropna()
positionList=list(dfConnections['Position'])
positionString=''
for index,row in dfConnections.iterrows():
    z=row['Position']
    z1=str(z)
    positionString=positionString+z1+' ,'
wordcloud1 = WordCloud(width = 350, height = 300, random_state=1, background_color='#1e1e2e', colormap='viridis', collocations=False, stopwords = STOPWORDS).generate(positionString)
wordcloud1.to_file('./assets/wordcloud.png')


#Plotting locations where my connections belong to
dfLocation=pd.read_csv('./data/Locations.csv')
fig3 = px.scatter_geo(dfLocation, locations="CountryCode", size='ConnectionCount',
                     hover_name="Country",color='CountryCode',
                     projection="natural earth", title='Connections by Geographical location 🌄')

fig3.layout.template = 'custom_dark'


#Analysing Ads Clicked over time
dfAds=pd.read_csv('./data/AdsClicked.csv')
dfAds['Year']=pd.DatetimeIndex(dfAds['AdClickedDate']).year
dfAds['Month']=pd.DatetimeIndex(dfAds['AdClickedDate']).month
dfAds2020=dfAds[dfAds['Year']==2020]
dfAds2020Count=dfAds2020.groupby('Month').size().reset_index(name='Count')
dfAds2020Count['Month'] = dfAds2020Count['Month'].apply(lambda x: calendar.month_abbr[x])
dfAds2020Count['Time']=dfAds2020Count['Month'].apply(lambda x: x+',20')
dfAds2019=dfAds[dfAds['Year']==2019]
dfAds2019Count=dfAds2019.groupby('Month').size().reset_index(name='Count')
dfAds2019Count['Month'] = dfAds2019Count['Month'].apply(lambda x: calendar.month_abbr[x])
dfAds2019Count['Time']=dfAds2019Count['Month'].apply(lambda x: x+',19')
dfAdsTotal=dfAds2019Count.append(dfAds2020Count)
fig5 = px.area(dfAdsTotal, x="Time", y="Count", title='Distribution of Ads Clicked 👬')
fig5.layout.template = 'custom_dark'

#Creating a Dash App Instance

app = dash.Dash(__name__, title="LinkedIn Data Analytics 📈", external_stylesheets=[dbc.themes.BOOTSTRAP,dbc.themes.GRID])
server=app.server
card_row11=dbc.Card([
    dbc.CardImg(src='/assets/me.png',top=True, bottom=False,title="Prateek's Image",alt='Image not loading'),
    dbc.CardBody([
        html.Label("Prateek Ralhan 😁",className='label1'),
        html.Label("Jr. Digital Solutions Specialist @ SwissRe",className='label2'),
        html.Label("Tech aficionado 💻 | Swift learner 💪",className='label3'),

        dcc.Link(

            href='https://prateekralhan.github.io/',
            target="_blank",
            children=[
                html.Img(
                className='websitelogo',
                 src='/assets/website_logo.gif',
                 alt='logo not loading'
                     )]
        ),

        dcc.Link(

            href='https://www.linkedin.com/in/prateek-ralhan17/',
            target="_blank",
            children=[
                html.Img(
                className='linkedinlogo',
                 src='/assets/linkedin_logo.png',
                 alt='logo not loading'
                     )]
        ),

            dcc.Link(

                     href='https://github.com/prateekralhan',
                     target="_blank",
                        children=[
                         html.Img(
                         className='githublogo',
                        src='/assets/github_logo.png',
                        alt='logo not loading'
                     )]
        ),

            dcc.Link(

            href='mailto:ralhanprateek@gmail.com?subject= Hi There!😁😉',
            target="_blank",
            children=[
                html.Img(
                className='gmaillogo',
                 src='/assets/gmail_logo.png',
                 alt='logo not loading'
                     )]
        )


    ], className='cardbody1')
], color="dark", inverse=True,outline=False)

card_row12=dbc.Card([
    dbc.CardBody([
        html.Label('# of Connections 👩👨',className='connectionLabel'),
        html.Label("8193",className='connectionNumber')
    ], className='cardbody2')
],color="dark",inverse=True,outline=False,className='card2')

card_row13=dbc.Card([
    dbc.CardBody([
        html.Label('# of Messages 📧 ',className='endorsementLabel'),

        html.Label(dfMessagesCount,className='endorsementNumber')
    ],className='cardbody3')
],color="dark",inverse=True,outline=False,className='card3')

card_row14=dbc.Card([
    dbc.CardBody([
        html.Label('# of Invitations 📬', className='recommendationLabel'),

        html.Label(InvitationsCount,className='recommendationNumber')
    ],className='cardbody4')
], color="dark", inverse=True, outline=False, className='card4')



app.layout=html.Div(children=[

    html.Div([

        dbc.Row([
           dbc.Col(
               card_row11,
               width=2
           ),
            dbc.Col(
                html.Div([
                    card_row12,
                    html.Br(),
                    card_row13,
                    html.Br(),
                    card_row14,
                ], id='div123'),


                width=2
            ),
            dbc.Col(
                html.Div([
                    dcc.Graph(id='invitationGraph',figure=fig2)
                ], className='invitationGraphDiv'),
                width=4
            ),
            dbc.Col(
               html.Div([
                dcc.Graph(id='messageGraph',figure=fig1)
               ], className='messageGraphDiv'),
                width=4
            ),
        ]),

        html.Br(),

        dbc.Row([
           dbc.Col(

               html.Div([
                   html.Label('Most frequent Job Titles 👷 👮 in my network', className='wordgraphLabel'),
                   html.Img(id='wordCloudImage', src='./assets/wordcloud.png', className='wordcloudimage')
               ], className='wordclouddiv'), width=4,id='wordcloudcolumn'
           ),
            dbc.Col(
                html.Div([

                    dcc.Graph(id='mapGraph', figure=fig3)
                ]),width=4
            ),
            dbc.Col(
                html.Div([
                    dcc.Graph(id='areaGraph',figure=fig5)
                ]),width=4
            )

        ], className='row2')

    ])


    ])



if __name__ == '__main__':
    app.run_server(debug=True)
