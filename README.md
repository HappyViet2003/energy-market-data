# Dashboard for energy market data in Germany

## Owner: 
- Viet Anh Hönemann

## Quelle der Daten
Strommarktdaten der Bundesnetzagentur: [hier](
https://github.com/bundesAPI/smard-api.git)


## Anfragen
Zeitstempel-URL: https://www.smard.de/app/chart_data/{filter}/{region}/index_{resolution}.json

Anfrage gibt verfügbare Timestamps für Filter, Region und Auflösung aus.

Zeitreihen-URL: https://www.smard.de/app/chart_data/{filter}/{region}/{filter}_{region}_{resolution}_{timestamp}.json

Anfrage gibt Zeitreihendaten nach Filter, Region und zeitlicher Auflösung ab dem spezifizierten Timestamp aus.

## Configuration 

### Parameter: filter

Mögliche Filter:

    '1223' - Stromerzeugung: Braunkohle
    '1224' - Stromerzeugung: Kernenergie
    '1225' - Stromerzeugung: Wind Offshore
    '1226' - Stromerzeugung: Wasserkraft
    '1227' - Stromerzeugung: Sonstige Konventionelle
    '1228' - Stromerzeugung: Sonstige Erneuerbare
    '4066' - Stromerzeugung: Biomasse
    '4067' - Stromerzeugung: Wind Onshore
    '4068' - Stromerzeugung: Photovoltaik
    '4069' - Stromerzeugung: Steinkohle
    '4070' - Stromerzeugung: Pumpspeicher
    '4071' - Stromerzeugung: Erdgas
    '410'  - Stromverbrauch: Gesamt (Netzlast)
    '4359' - Stromverbrauch: Residuallast
    '4387' - Stromverbrauch: Pumpspeicher


### Parameter: region

Land / Regelzone / Marktgebiet:

    'DE' - Land: Deutschland
    'AT' - Land: Österreich
    'LU' - Land: Luxemburg
    'DE-LU' - Marktgebiet: DE/LU (ab 01.10.2018)
    'DE-AT-LU' - Marktgebiet: DE/AT/LU (bis 30.09.2018)
    '50Hertz' - Regelzone (DE): 50Hertz
    'Amprion'- Regelzone (DE): Amprion
    'TenneT' - Regelzone (DE): TenneT
    'TransnetBW' - Regelzone (DE): TransnetBW
    'APG' - Regelzone (AT): APG
    'Creos' - Regelzone (LU): Creos


### Parameter: resolution

Zeitliche Auflösung der Daten:

    'hour' - Stündlich
    'quarterhour' - Viertelstündlich
    'day' - Täglich
    'week' - Wöchentlich
    'month' - Monatlich
    'year' - Jährlich

