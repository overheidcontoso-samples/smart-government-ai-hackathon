# Smart Government – AI Agentic Hackathon


## 🏭 Deel 1 Data Agents in Fabric

We gaan als eerste aan de slag met Microsoft Fabric Agents. Data Agents in Microsoft Fabric zijn slimme digitale assistenten die je helpen om makkelijker met data te werken. Je kunt ze zien als een laag tussen jou en de data: in plaats van zelf complexe queries te schrijven of precies te weten waar data staat, kun je een Data Agent vragen stellen in gewone taal. Hierdoor kunnen zowel technische als niet-technische gebruikers sneller inzichten krijgen uit data.

In dit document doorloop je stap voor stap hoe je inlogt op Microsoft Fabric, een Lakehouse aanmaakt, shortcuts aanmaakt naar een ander Lakehouse en hoe je deze data kunt gebruiken met Data Agents In Microsoft Fabric.

Deze hackathon is bedoeld voor developers, solution architects, data engineers, AIspecialisten en innovators binnen de gemeentes en andere overheidsorganisaties.

Inhoud van de Labs


- Lab 1: Opzetten van de omgeving
- Lab 2: Configureer een Data Agent
- Lab 3: Aan de slag met Data Agents


## 🧪 Lab 1: Opzetten van de omgeving

Om van start te gaan zullen we eerst inloggen in de Fabric omgeving en een aantal zaken opzetten om aan de slag te gaan met Data Agents.

Voordat we verder gaan


- Na de introductie heb je tijdelijke login gegevens (gebruikersnaam en wachtwoord) gekregen. Mocht dat niet het geval zijn, laat dat weten aan de instructeurs.
- Download alvast de PDF-bestanden die beschikbaar zijn in de GitHub repository.

Aan de slag met Fabric


### We zullen nu de volgende acties uitvoeren:


- Inloggen bij Microsoft Fabric met de tijdelijke login gegevens.
- Verifiëren dat we toegang hebben tot de workspace.
- Een shortcut aanmaken naar de data die we gaan gebruiken.


### 👣 Stap 1: Log in bij Microsoft Fabric


- Ga naar [https://app.fabric.microsoft.com](https://app.fabric.microsoft.com)


- Voer de username in en druk op submit:


<img src="images/image41.png" width="442px" alt="image1.png">


- Voer het ontvangen wachtwoord (TAP) in en druk  Sign in


<img src="images/image42.png" width="305px" alt="image2.png">


- Zodra je bent ingelogd kom je op de Fabric startpagina. Vanaf deze pagina zullen we navigeren naar je Workspace. De naam van je workspace is gelijk aan de gebruikte username, bijvoorbeeld Decentral01.


<img src="images/image43.png" width="308px" alt="image3.png">


### 👣 Stap 2: Lakehouse aanmaken


- Maak nu binnen je workspace een Lakehouse aan via New item.


<img src="images/image44.png" width="217px" alt="image4.png">


- Zoek naar Lakehouse in het geopende venster


<img src="images/image45.png" width="199px" alt="image5.png">


- Maak een Lakehouse aan met een eenvoudige naam zoals GebruikersnaamLakehouse


<img src="images/image46.png" width="410px" alt="image6.png">


### 👣 Stap 3: Maak een shortcut aan

Voor de Data Agent zullen we data gebruiken uit een gedeelde Workspace. Om deze data te benaderen vanuit je eigen Workspace maken we gebruik van Shortcuts. Deze shortcuts maken we aan vanuit het Lakehouse.


- Navigeer naar het zojuist aangemaakte Lakehouse:


<img src="images/image47.png" width="341px" alt="image7.png">


- Maak binnen het schema dbo onder Tables een shortcut aan.


<img src="images/image8.png" width="341px" alt="image8.png">


- De tabellen die we gaan gebruiken bevinden zich in een ander Lakehouse. Selecteer Microsoft OneLake.


<img src="images/image49.png" width="320px" alt="image9.png">


- Selecteer het volgende Lakehouse.


<img src="images/image50.png" width="384px" alt="image10.png">


- Selecteer de volgende twee tabellen.


<img src="images/image51.png" width="254px" alt="image11.png">


- Controleer of het klopt en druk op Create


<img src="images/image52.png" width="506px" alt="image12.png">


- Controleer of de tabellen zijn toegevoegd.


<img src="images/image53.png" width="263px" alt="image13.png">


- Ga terug naar de Workspace door op de Workspace naam te klikken.


<img src="images/image54.png" width="299px" alt="image14.png">

**Einde van Lab 1**

Hiermee sluiten we Lab 1 af en gaan we verder naar Lab 2 om een Data Agent aan te maken!


## 🧪 Lab 2: Configureer een Data Agent

In dit lab zullen we een eerste Data Agent aanmaken en deze testen op de data in ons Lakehouse.

Voordat we verder gaan


- Zorg ervoor dat je Lab 1: Opzetten van de omgeving hebt afgerond.

Aanmaken van een Data Agent


### We zullen nu de volgende acties uitvoeren:


- Aanmaken van een Data Agent
- De Data Agent verbinden met data in het Lakehouse
- Vragen stellen aan de Data Agent


### 👣 Stap 1: Maak een Data Agent aan


- Maak vanuit de Workspace een New Item aan


<img src="images/image55.png" width="268px" alt="image15.png">


- Zoek naar een Data Agent en selecteer Data Agent (Preview)


<img src="images/image56.png" width="252px" alt="image16.png">


- Geef de Data Agent een naam en maak deze aan met Create.


<img src="images/image57.png" width="268px" alt="image17.png">


- Zodra de Data Agent is aangemaakt zullen we de data uit het Lakehouse toewijzen. Onder No data added druk op Add Data.


<img src="images/image58.png" width="133px" alt="image18.png">


- Gebruik hier het eigen lakehouse en selecteer Add


<img src="images/image59.png" width="404px" alt="image19.png">


- Je ziet nu de Lakehouse toegevoegd aan de Data Agent, vervolgens selecteren we de tabel eindhoven_vergunningen:


<img src="images/image60.png" width="261px" alt="image20.png">


- Laten we nu proberen of de Data Agent inderdaad ook vragen kan beantwoorden op de data. Stel de volgende simpele vraag: Hoeveel vergunningen zitten er in de vergunningen tabel?


<img src="images/image61.png" alt="image21.png">

Einde van Lab 2

Hiermee sluiten we Lab 2 af en gaan we verder naar Lab 3 om de vergunningen-data verder te verkennen!


## 🧪 Lab 3: Aan de slag met Data Agents

Voordat we verder gaan


- Zorg ervoor dat je Lab 1 en 2 hebt afgerond.

Werken met Data Agents


### We zullen nu de volgende acties uitvoeren:


- Data verkennen met een Data Agent
- Resultaten verbeteren met Agent Instructions
- Resultaten verbeteren met Few Shots Queries
- Resultaten verbeteren met Datasource Instructions


### 👣 Stap 1: Data verkennen met een Data Agent


- Stel de volgende vraag aan de Data Agent: Geef me 10 willekeurige rijen uit de data set


- De output van deze vraag opgebouwd uit een aantal onderdelen:
  - Een uitgeschreven reactie, in dit geval krijgen we een lijst terug met adressen, aantallen en wat extra informatie.


<img src="images/image24.png" width="500px" alt="image24.png">


  - Als we iets verder inzoomen zien we dat de Data Agent 1 stap gebruikt heeft (1 step completed). Als we deze uitklappen kunnen we ook de SQL-query en output van de query bekijken.


<img src="images/image25.png" width="501px" alt="image25.png">


- Vraag nu zelf wat vragen over de de vergunningendata. Neem ook de tijd om te zien wat de Data Agent heeft gedaan om de data op te halen. Een aantal voorbeeldvragen om je op weg te helpen:


### 👣 Stap 2: Resultaten verbeteren met Agent Instructions


- We beginnen met het opschonen van het huidige chat venster. Druk daarvoor op Clear Chat in de rechterbovenhoek.


<img src="images/image26.png" width="169px" alt="image26.png">


- Selecteer Agent Instructions in the menu-bar


<img src="images/image27.png" width="295px" alt="image27.png">


- Voeg de volgende instructie toe aan de agent: “Zodra er resultaten worden getoond, maak altijd gebruik van een tabel in Markdown-formaat voor data die in tabelvorm moet worden weergeven.”


<img src="images/image28.png" width="515px" alt="image28.png">


- Stel nu de vragen aan de agent en bekijk het resultaat. Hoe worden de gegevens nu weergegeven?


### 👣 Stap 3: Resultaten verbeteren met Few Shots Queries


- Data Agent gebruikt de chat geschiedenis als onderdeel van de context. We beginnen daarom met het opschonen van het huidige chat-window. Druk daarvoor op Clear Chat in de rechterbovenhoek.


<img src="images/image26.png" width="169px" alt="image26.png">


- Vraag aan de Data Agent het volgende: Geef een top 5 van de straten met de meeste vergunningsaanvragen?


<img src="images/image29.png" width="525px" alt="image29.png">

De straatnamen zijn afgebroken na het eerste woord, dat klopt dus helaas bepaalde gevallen niet.


- Om dit te verbeteren kunnen we twee dingen doen:
  - De agent vragen om de logica in de SQL Query te optimaliseren; gebruik de tekst tot aan het eerste getal dat je tegenkomt.
  - Gebruik maken van een postcodetabel met daarin gestructureerde adresgegevens waaronder de straatnaam, regio.


- In dit geval gaan we gebruik maken van een officiële postcodetabel en geven we de Data Agent een voorbeeld hoe deze gebruikt kan worden.
  - Voeg eerst tabel eindhoven_postcode_buurt_wijk toe


<img src="images/image30.png" width="258px" alt="image30.png">


  - Ga vervolgens naar Example Queries


<img src="images/image31.png" width="462px" alt="image31.png">


- Klik op Add example


<img src="images/image32.png" width="264px" alt="image32.png">


- Voeg de volgen combinatie van vraag en query toe:
  - Question: Geef een top 5 van de straten met de meeste vergunningsaanvragen?
  - Query:


<img src="images/image33.png" width="426px" alt="image33.png">


  - Sluit het configuratie-tabblad


<img src="images/image34.png" width="338px" alt="image34.png">


- We beginnen met een nieuwe chat, druk daarom weer op Clear Chat
- Vraag de Data Agent het volgende:
  - Welke straat heeft de meeste vergunningsaanvragen?


<img src="images/image35.png" width="478px" alt="image35.png">


  - Geef een top 5 van de straten met de meeste vergunningsaanvragen?


<img src="images/image36.png" width="477px" alt="image36.png">

Je zult nu zien dat de Data Agent gebruik maakt van de postcodetabel.

Note: Valt er ook iets op aan de resultaten? Mocht je tijd over hebben, voel je vrij om eens op onderzoek te gaan doormiddel van het Lakehouse SQL Endpoint.


### 👣 Stap 4: Resultaten verbeteren met Datasource Instructions


- Data Agent gebruikt de chat geschiedenis als onderdeel van de context. We beginnen daarom met het opschonen van het huidige chat-window. Druk daarvoor op Clear Chat in de rechterbovenhoek.


<img src="images/image26.png" width="150px" alt="image26.png">


- Vraag de Data Agent: Geef me alle open aanvragen ouder dan 30 dagen. Sorteer deze op de oudste eerst.


<img src="images/image37.png" width="529px" alt="image37.png">

Als we kijken naar de gebruikte query, dan zullen we zien dat de agent Status = ‘Open’ gebruikt. Dat is niet juist en de Data Agent heeft dus meer context nodig.


- Om de Data Agent te helpen dit correct te bepalen geven we een extra instructie mee. Ga naar de Data Source Instructions


<img src="images/image38.png" width="325px" alt="image38.png">


- Voeg de volgende instructies toe onder Data source instructions:


<img src="images/image39.png" width="509px" alt="image39.png">


- We beginnen met een nieuwe chat, druk daarom weer op Clear Chat


<img src="images/image26.png" width="150px" alt="image26.png">


- Stel de vraag opnieuw: Geef me alle open aanvragen ouder dan 30 dagen. Sorteer deze op de oudste eerst.

Om het volgende hackathon onderdeel succesvol te vervolgen, gaan we eerst de aangemaakte Data Agent publiceren.


- Selecteer Publish


<img src="images/image22.png" width="534px" alt="image22.png">


- Geef een korte beschrijving en druk op Publish


<img src="images/image23.png" width="341px" alt="image23.png">

***Einde van Lab 3***

Dit was het laatste lab en hiermee sluiten we deel 1 van de hackathon af.

Laat vooral weten of je nog vragen hebt. Mocht je al snel klaar zijn, voel je vrij om verder te experimenteren door andere en complexere vragen te stellen.


### [Terug naar readme](./README.md)