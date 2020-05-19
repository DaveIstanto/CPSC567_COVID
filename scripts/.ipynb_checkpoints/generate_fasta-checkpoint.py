import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sb

sequences_QC = ['NC_045512', 'MT263396', 'MT263400', 'MT263423', 'MT259241',
       'MT246462', 'MT163719', 'MN908947', 'LC529905', 'MT135041',
       'MT135042', 'MT135043', 'MT135044', 'MT049951', 'MT262896',
       'MT262897', 'MT262898', 'MT262899', 'MT262900', 'MT262901',
       'MT262902', 'MT262903', 'MT262904', 'MT262905', 'MT262906',
       'MT262911', 'MT262912', 'MT262913', 'MT262909', 'MT262910',
       'MT262907', 'MT262908', 'MT262916', 'MT262915', 'MT262914',
       'MT184909', 'MT184907', 'MT184913', 'MT184912', 'MT159705',
       'MT159722', 'MT159710', 'MT159715', 'MT159711', 'MT159712',
       'MT159717', 'MT159719', 'MT159720', 'MT159709', 'MT159718',
       'MT159721', 'MT159708', 'MT159714', 'MT159707', 'MT159706',
       'MT159713', 'MT118835', 'MT106053', 'MT106052', 'MT066175',
       'MT027063', 'MT027064', 'MT027062', 'MT020881', 'MT019532',
       'MT020880', 'MN996528', 'MN997409', 'MN988713', 'MN985325',
       'MT039887', 'MT044257', 'MT039888', 'MN994467', 'MT259226',
       'MT259229', 'MT259230', 'MT259231', 'MN996530', 'MT259228',
       'MT253696', 'MT253697', 'MT253699', 'MT253700', 'MT253701',
       'MT253702', 'MT253703', 'MT253710', 'MT253698', 'MT253707',
       'MT253708', 'MT253709', 'MT253704', 'MT253705', 'MT192772',
       'MT192759', 'MT019531', 'MT253706', 'MT198653', 'MT188340',
       'LC534418', 'MN988669', 'MN988668', 'MT246480', 'MT246667',
       'MT233526', 'MT072688', 'LR757995', 'MT093631', 'MN996531',
       'MN938384', 'MT121215', 'MT066156', 'MT066176', 'MT019533',
       'MN994468', 'MT019529', 'MT123292', 'MT020781', 'MT126808',
       'MT192773', 'MN975262', 'MT050493', 'LR757996', 'MT123290',
       'MT256924', 'MT233520', 'MT192765', 'MT039873', 'MT123291',
       'MT184908', 'MT106054', 'MT184910', 'MT184911', 'MT159716',
       'MT044258', 'MT263381', 'MT263449', 'MT263455', 'MT263456',
       'MT259279', 'MT259274', 'MT246452', 'MT263383', 'MT263385',
       'MT263414', 'MT246466', 'MT163718', 'MT259238', 'MT246468',
       'MT263405', 'MT259284', 'MT259271', 'MT259266', 'MT263425',
       'MT263463', 'MT246469', 'MT246485', 'MT163717', 'MT163721',
       'MT263397', 'MT263419', 'MT259254', 'MT246455', 'MT246478',
       'MT246479', 'MT246476', 'MT263422', 'MT263461', 'MT263448',
       'MT263462', 'MT251977', 'MT263451', 'MT259268', 'MT263412',
       'MT259236', 'MT263388', 'MT263452', 'MT263464', 'MT263434',
       'MT259282', 'MT263416', 'MT263399', 'MT263450', 'MT259275',
       'MT246477', 'MT263403', 'MT263420', 'MT259257', 'MT246486',
       'MT259245', 'MT246458', 'MT246471', 'MT246461', 'MT263444',
       'MT263447', 'MT246482', 'MT246483', 'MT263382', 'MT259259',
       'MT251978', 'MT152824', 'MT259262', 'MT246488', 'MT246464',
       'MT263440', 'MT263427', 'MT246489', 'MT246463', 'MT263457',
       'MT263453', 'MT263430', 'MT259270', 'MT251975', 'MT259280',
       'MT259247', 'MT246472', 'MT263390', 'MT263394', 'MT263407',
       'MT263432', 'MT246490', 'MT246449', 'MT263391', 'MT259239',
       'MT259240', 'MT251979', 'MT263446', 'MT259265', 'MT259278',
       'MT263439', 'MT259261', 'MT259251', 'MT246481', 'MT263442',
       'MT263428', 'MT263437', 'MT259260', 'MT263413', 'MT246450',
       'MT263431', 'MT246460', 'MT246484', 'MT246467', 'MT263402',
       'MT263438', 'MT259263', 'MT259264', 'MT263433', 'MT259256',
       'MT263392', 'MT259243', 'MT263406', 'MT263417', 'MT263436',
       'MT259286', 'MT263408', 'MT259281', 'MT259246', 'MT246487',
       'MT263445', 'MT251976', 'MT263465', 'MT263409', 'MT251974',
       'MT263426', 'MT263468', 'MT259235', 'MT259244', 'MT263415',
       'MT246453', 'MT259249', 'MT258381', 'MT258383', 'MT258380',
       'MT258378', 'MT258379', 'MT251973', 'MT259273', 'MT263467',
       'MT259250', 'MT259253', 'MT163720', 'LR757998', 'MT263441',
       'MT263404', 'MT259285', 'MT246454', 'MT163716', 'MT039890',
       'MT263384', 'MT263395', 'MT263401', 'MT263458', 'MT263429',
       'MT263435', 'MT263418', 'MT259237', 'MT259242', 'MT259269',
       'MT251972', 'MT246475', 'MT246474', 'MT246459', 'MT263386',
       'MT263443', 'MN996527', 'MT263454', 'MT263410', 'MT259287',
       'MT240479', 'MT263398', 'MT263421', 'MT258377', 'MT259272',
       'MT259252', 'MT246470', 'MT123293', 'MT093571', 'MT019530',
       'MT012098', 'MT263074', 'MT263459', 'LC534419', 'MN996529',
       'MT233522', 'MT263466', 'MT259227', 'MT188339', 'MT256918',
       'MT233519', 'MT233523', 'MT198652', 'MT233521', 'MT259267',
       'MT198651', 'MT188341', 'MT263387', 'MT263469', 'MT259283',
       'MT263393', 'MT263411', 'MT259258', 'MT251980', 'MT246473',
       'MT246457', 'MT246465', 'MT263460', 'MT246451', 'MT263424',
       'MT259248', 'MT259277', 'MT262993', 'MT246456', 'MT007544',
       'MT258382', 'MT259276', 'MT259255', 'MT256917', 'MT226610',
       'MT263389', 'LR757997']

# Read fasta file
def read_fasta(fasta_file):
    fasta_dict = dict()
    with open (fasta_file, 'r') as f:
        lines = f.readlines()

        for line in lines:
            if '>' in line:
                key = line[1:-1]
                key = key.split()
                key = key[0]
                fasta_dict[key] = ''
            else:
                fasta_dict[key] += line[:-1]
    return fasta_dict

# Read aligned fasta file
unaligned_fasta ='/Users/prakruthiburra/Desktop/CPSC_567/CPSC567_COVID/dataset/regional_sequences/multiple_regional_sequences_unaligned.fasta'
unaligned_dict = read_fasta(unaligned_fasta)
seqtocountry_dict = {}
seqtotemp_dict = {}

seqtogenchange_dict = {}
seqtopp1achange_dict = {}
seqtonsp2_change_dict = {}
seqtorbd_change_dict = {}
seqtospikes1_change_dict = {}
seqtospikes2_change_dict = {}

seqtogenchange_normalized_dict = {}
seqtopp1achange_normalized_dict = {}
seqtonsp2_change_normalized_dict = {}
seqtorbd_change_normalized_dict = {}
seqtospikes1_change_normalized_dict = {}
seqtospikes2_change_normalized_dict = {}

seqtodate_dict = {}
seqtorelativedate_dict = {}
countrytoseq_dict = {}
countrytolat_dict = {"Australia": -25.274398, "Brazil": -14.235004, "Colombia": 4.570868, "China": 35.86166, "Finland": 61.92411, "India": 20.593684, "Italy": 41.87194, "Japan": 36.204824,
"Nepal": 28.39486, "Pakistan": 30.375321, "Peru": -9.189967, "South Korea": -1.940278, "Spain": 40.463667, "Sweden": 60.128161, "Taiwan": 23.69781, "USA": 37.09024, "Vietnam": 14.058324}
countrytolong_dict = {"Australia": 133.775136, "Brazil": -51.92528, "Colombia": -74.297333, "China": 104.195397, "Finland": 25.748151, "India": 78.96288, "Italy": 12.56738, "Japan": 138.252924,
"Nepal": 84.124008, "Pakistan": 69.345116, "Peru": -75.015152, "South Korea": 29.873888, "Spain": -3.74922, "Sweden": 18.643501, "Taiwan": 120.960515, "USA": -95.712891, "Vietnam": 108.277199}
countrytotemp_dict = {"Australia": 69.8, "Brazil": 76.7, "Colombia": 65, "China": 57.3, "Finland": 39.5, "India": 96.8, "Italy": 54.5, "Japan": 58.1,
"Nepal": 70, "Pakistan": 74.3, "Peru": 69.1, "South Korea": 62.6, "Spain": 66.2, "Sweden": 41.9, "Taiwan": 72.3, "USA": 52.9, "Vietnam": 94}

with open("/Users/prakruthiburra/Desktop/CPSC_567/CPSC567_COVID/dataset/accession_data.csv", "r") as f3:
    next(f3)
    lines = f3.readlines()

    for line in lines:
        line = line.split(",")
        # if line[0] not in seqtocountry_dict.keys():
        #     seqtocountry_dict[line[0]] = []
        seqtocountry_dict[line[0]] = (line[3])
        seqtodate_dict[line[0]] = (line[5].strip())
        date = line[5].strip().split("-")
        year = date[0]
        month = date[1]
        if(len(date)==3):
            day = date[2]
        else:
            day = 14
        print(date, year, month, day)
        if(year == '2019'):
            seqtorelativedate_dict[line[0]] = int(day) - 15
        elif(month == '01'):
            seqtorelativedate_dict[line[0]] = 16 + int(day)
        elif(month == '02'):
            seqtorelativedate_dict[line[0]] = 47 + int(day)
        elif(month == '03'):
            seqtorelativedate_dict[line[0]] = 76 + int(day)


print(seqtorelativedate_dict.keys())
print(len(seqtorelativedate_dict.keys()))
with open("/Users/prakruthiburra/Desktop/CPSC_567/meta_info_with_genetic_changes.csv") as h:
    next(h)
    lines = h.readlines()
    for line in lines:
        print(line)
        line = line.strip().split(",")
        print(line)
        seqtogenchange_dict[line[0]] = int(line[7])
        seqtopp1achange_dict[line[0]] = int(line[8])
        seqtonsp2_change_dict[line[0]] = int(line[9])
        seqtorbd_change_dict[line[0]] = int(line[10])
        seqtospikes1_change_dict[line[0]] = int(line[11])
        seqtospikes2_change_dict[line[0]] = int(line[12])

f = open("/Users/prakruthiburra/Desktop/CPSC_567/sequences_QC.fasta", "w+")
g = open("/Users/prakruthiburra/Desktop/CPSC_567/accession_data_unnormalised.csv", "w+")
g.write("Accession,Geo Location,Collection Date,Relative Date,Genomic Change,pp1a,nsp2,rbd,spike_s1,spike_s2,Temperature,Latitude,Longitude\n")
j = open("/Users/prakruthiburra/Desktop/CPSC_567/accession_data_normalised.csv", "w+")
j.write("Accession,Geo Location,Collection Date,Relative Date,Genomic Change_normalized,pp1a_normalized,nsp2_normalized,rbd_normalized,spike_s1_normalized,spike_s2_normalized,Temperature,Latitude,Longitude\n")
for i in sequences_QC:
    country = seqtocountry_dict[i]

    f.write("> "+i+" "+str(country)+" "+str(seqtodate_dict[i])+"\n")
    f.write(unaligned_dict[i])
    f.write("\n")

    seqtogenchange_normalized_dict[i] = float(seqtogenchange_dict[i])/float(seqtorelativedate_dict[i])
    seqtopp1achange_normalized_dict[i] = float(seqtopp1achange_dict[i])/float(seqtorelativedate_dict[i])
    seqtonsp2_change_normalized_dict[i] = float(seqtonsp2_change_dict[i])/float(seqtorelativedate_dict[i])
    seqtorbd_change_normalized_dict[i] = float(seqtorbd_change_dict[i])/float(seqtorelativedate_dict[i])
    seqtospikes1_change_normalized_dict[i] = float(seqtospikes1_change_dict[i])/float(seqtorelativedate_dict[i])
    seqtospikes2_change_normalized_dict[i] = float(seqtospikes2_change_dict[i])/float(seqtorelativedate_dict[i])


    g.write(i+","+str(country)+","+str(seqtodate_dict[i])+","+str(seqtorelativedate_dict[i])+","+
    str(seqtogenchange_dict[i])+","+str(seqtopp1achange_dict[i])+","+str(seqtonsp2_change_dict[i])+","+str(seqtorbd_change_dict[i])+","+
    str(seqtospikes1_change_dict[i])+","+str(seqtospikes2_change_dict[i])+","+
    str(countrytotemp_dict[country])+","+str(countrytolat_dict[country])+","+str(countrytolong_dict[country])+"\n")
    j.write(i+","+str(country)+","+str(seqtodate_dict[i])+","+str(seqtorelativedate_dict[i])+","+
    str(seqtogenchange_normalized_dict[i])+","+str(seqtopp1achange_normalized_dict[i])+","+str(seqtonsp2_change_normalized_dict[i])+","+str(seqtorbd_change_normalized_dict[i])+","+
    str(seqtospikes1_change_normalized_dict[i])+","+str(seqtospikes2_change_normalized_dict[i])+","+
    str(countrytotemp_dict[country])+","+str(countrytolat_dict[country])+","+str(countrytolong_dict[country])+"\n")
    if seqtocountry_dict[i] not in countrytoseq_dict.keys():
        countrytoseq_dict[seqtocountry_dict[i]] = []
    countrytoseq_dict[seqtocountry_dict[i]].append(i)

data = pd.read_csv("/Users/prakruthiburra/Desktop/CPSC_567/accession_data_unnormalised.csv")
print(data.head())
Temperature = data['Temperature'].to_numpy()
Latitude = data['Latitude'].to_numpy()
Longitude = data['Longitude'].to_numpy()
GC = data['Genomic Change'].to_numpy()
pp1a = data['pp1a'].to_numpy()
nsp2 = data['nsp2'].to_numpy()
rbd = data['rbd'].to_numpy()
spike_s1 = data['spike_s1'].to_numpy()
spike_s2 = data['spike_s2'].to_numpy()
pearsoncorr = data.corr(method='pearson')
print(data.corr(method='pearson'))
sb.heatmap(pearsoncorr,
            xticklabels=pearsoncorr.columns,
            yticklabels=pearsoncorr.columns,
            cmap='RdBu_r',
            annot=True,
            linewidth=0.5)
plt.show()

data_normalized = pd.read_csv("/Users/prakruthiburra/Desktop/CPSC_567/accession_data_normalised.csv")
print(data_normalized.head())
Temperature = data_normalized['Temperature'].to_numpy()
Latitude = data_normalized['Latitude'].to_numpy()
Longitude = data_normalized['Longitude'].to_numpy()
GC = data_normalized['Genomic Change_normalized'].to_numpy()
pp1a = data_normalized['pp1a_normalized'].to_numpy()
nsp2 = data_normalized['nsp2_normalized'].to_numpy()
rbd = data_normalized['rbd_normalized'].to_numpy()
spike_s1 = data_normalized['spike_s1_normalized'].to_numpy()
spike_s2 = data_normalized['spike_s2_normalized'].to_numpy()
pearsoncorr = data_normalized.corr(method='pearson')
print(data_normalized.corr(method='pearson'))
sb.heatmap(pearsoncorr,
            xticklabels=pearsoncorr.columns,
            yticklabels=pearsoncorr.columns,
            cmap='RdBu_r',
            annot=True,
            linewidth=0.5)
plt.show()
