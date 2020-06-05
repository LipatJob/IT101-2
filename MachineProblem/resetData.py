cabuyaoCase = """BRGY,CONFIRMED,ACTIVE,RECOVERED,SUSPECT,PROBABLE,DECEASED
MARINIG,4,2,2,2,0,0
BANAY BANAY,2,0,2,0,0,0
MAMATID,2,0,0,3,0,2
DOS,2,1,1,3,0,0
BUTONG,2,2,0,2,0,0
BACLARAN,1,0,1,2,0,0
BANLIC,1,0,1,4,0,0
MABUHAY SUBD,1,0,1,5,0,0
PULO,1,1,0,3,0,0
UNO,1,0,1,0,0,0
SV MARINIG,1,0,1,0,0,0
NIUGAN,1,0,0,2,0,1
SV NIUGAN,1,0,0,2,0,1
SALA,1,1,0,3,0,0
SV BANAY BANAY,0,0,0,2,0,0
CASILE,0,0,0,1,0,0
DIEZMO,0,0,0,1,0,0
PITTLAND,0,0,0,1,0,0
SAN ISIDRO,0,0,0,8,0,0
BIGAA,0,0,0,2,0,0
GULOD,0,0,0,1,0,0"""

santaRosaCase = """BRGY,CONFIRMED,ACTIVE,RECOVERED,SUSPECT,PROBABLE,DECEASED
BALIBAGO,5,0,5,2,1,0
DON JOSE,5,1,3,1,0,1
MALITLIT,5,1,3,12,1,1
TAGAPO,4,0,4,16,1,0
CAINGIN,2,2,0,19,1,0
MARKET AREA,2,0,2,18,0,0
SANTO DOMINGO,2,0,2,0,0,0
DILA,1,0,1,7,0,0
LABAS,1,0,0,5,2,1
MACABLING,1,0,1,1,0,0
PULONG SANTA CRUZ,1,0,1,4,0,0
SINALHAN,1,0,1,26,1,0
APLAYA,0,0,0,6,5,0
DITA,0,0,0,11,0,0
IBABA,0,0,0,1,0,0
KANLURAN,0,0,0,0,1,0
MALUSAK,0,0,0,5,0,0
POOK,0,0,0,2,0,0"""

metaData = """{"cities": [["Sta Rosa", "StaRosaCase.txt"], ["Cabuyao", "CabuyaoCase.txt"]]}"""


with open("data/CabuyaoCase.txt", "w") as cabuyao:
    cabuyao.write(cabuyaoCase)

with open("data/StaRosaCase.txt", "w") as santaRosa:
    santaRosa.write(santaRosaCase)

with open("data/metadata.json", "w") as metaDataFile:
    metaDataFile.write(metaData)
    
