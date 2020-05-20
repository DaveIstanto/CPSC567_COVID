import pandas as pd
import scipy
import matplotlib.pyplot as plt
import seaborn as sb


seqtocountry_dict = {}
seqtotemp_dict = {}

seqtogenchange_dict = {}
seqtopp1a_change_dict = {}
seqtonsp2_change_dict = {}
seqtorbd_change_dict = {}
seqtospikes1_change_dict = {}
seqtospikes2_change_dict = {}

seqtogenchange_normalized_dict = {}
seqtopp1a_change_normalized_dict = {}
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

with open("/Users/prakruthiburra/Desktop/CPSC_567/CPSC567_COVID/dataset/meta_info_with_genetic_changes_no_isolation_source.csv", "r") as f:

#Skip index
    next(f)
    lines = f.readlines()
    for line in lines:
        line = line.strip().split(",")
        print(line)
        seq_id = line[0]

# 364 sequences were isolated of which two sequences did not contain a country label and were excluded from the analysis.
#Excluding sequences without a country label
        if(line[3] != "NA"):
            seqtocountry_dict[seq_id] = (line[3])

            seqtodate_dict[seq_id] = (line[4].strip())
            date = seqtodate_dict[seq_id].strip().split("-")
            year = date[0]
            month = date[1]
            if(len(date)==3):
                day = date[2]
            else:
                day = 15

            if(year == '2019'):
                seqtorelativedate_dict[line[0]] = int(day) - 15
            elif(month == '01'):
                seqtorelativedate_dict[line[0]] = 16 + int(day)
            elif(month == '02'):
                seqtorelativedate_dict[line[0]] = 47 + int(day)
            elif(month == '03'):
                seqtorelativedate_dict[line[0]] = 76 + int(day)

            seqtogenchange_dict[seq_id] = int(line[6])
            seqtopp1a_change_dict[seq_id] = int(line[7])
            seqtonsp2_change_dict[seq_id] = int(line[8])
            seqtorbd_change_dict[seq_id] = int(line[9])
            seqtospikes1_change_dict[seq_id] = int(line[10])
            seqtospikes2_change_dict[seq_id] = int(line[11])

            if(seqtorelativedate_dict[seq_id] != 0):
                seqtogenchange_normalized_dict[seq_id] = float(seqtogenchange_dict[seq_id])/float(seqtorelativedate_dict[seq_id])
                seqtopp1a_change_normalized_dict[seq_id] = float(seqtopp1a_change_dict[seq_id])/float(seqtorelativedate_dict[seq_id])
                seqtonsp2_change_normalized_dict[seq_id] = float(seqtonsp2_change_dict[seq_id])/float(seqtorelativedate_dict[seq_id])
                seqtorbd_change_normalized_dict[seq_id] = float(seqtorbd_change_dict[seq_id])/float(seqtorelativedate_dict[seq_id])
                seqtospikes1_change_normalized_dict[seq_id] = float(seqtospikes1_change_dict[seq_id])/float(seqtorelativedate_dict[seq_id])
                seqtospikes2_change_normalized_dict[seq_id] = float(seqtospikes2_change_dict[seq_id])/float(seqtorelativedate_dict[seq_id])
            else:
                seqtogenchange_normalized_dict[seq_id] = 'NA'
                seqtopp1a_change_normalized_dict[seq_id] = 'NA'
                seqtonsp2_change_normalized_dict[seq_id] = 'NA'
                seqtorbd_change_normalized_dict[seq_id] = 'NA'
                seqtospikes1_change_normalized_dict[seq_id] = 'NA'
                seqtospikes2_change_normalized_dict[seq_id] = 'NA'

# g = open("/Users/prakruthiburra/Desktop/CPSC_567/all_meta_data.csv", "w+")
# g.write("Accession,Geo Location,Collection Date,Relative Date,Temperature,Latitude,Longitude,gc,pp1a,nsp2,rbd,spike_s1,spike_s2,gc_normalized,pp1a_n,nsp2_n,rbd_n,spike_s1_n,spike_s2_n\n")
#
# for i in seqtocountry_dict.keys():
#     country = seqtocountry_dict[i]
#     g.write(i+","+str(country)+","+str(seqtodate_dict[i])+","+str(seqtorelativedate_dict[i])+","+
#     str(countrytotemp_dict[country])+","+str(countrytolat_dict[country])+","+str(countrytolong_dict[country])+","+
#     str(seqtogenchange_dict[i])+","+str(seqtopp1a_change_dict[i])+","+str(seqtonsp2_change_dict[i])+","+str(seqtorbd_change_dict[i])+","+
#     str(seqtospikes1_change_dict[i])+","+str(seqtospikes2_change_dict[i])+","+
#     str(seqtogenchange_normalized_dict[i])+","+str(seqtopp1a_change_normalized_dict[i])+","+str(seqtonsp2_change_normalized_dict[i])+","+str(seqtorbd_change_normalized_dict[i])+","+
#     str(seqtospikes1_change_normalized_dict[i])+","+str(seqtospikes2_change_normalized_dict[i])+"\n")
# Removed from correlations: NC_045512, MN908947 for they had relative date set to 0 and the sequences either corresponded to the reference or were identical to it.

data = pd.read_csv("/Users/prakruthiburra/Desktop/CPSC_567/all_meta_data.csv")
print(data.head())
Temperature = data['Temperature'].to_numpy()
Latitude = data['Latitude'].to_numpy()
Longitude = data['Longitude'].to_numpy()
gc = data['gc'].to_numpy()
pp1a = data['pp1a'].to_numpy()
nsp2 = data['nsp2'].to_numpy()
rbd = data['rbd'].to_numpy()
spike_s1 = data['spike_s1'].to_numpy()
spike_s2 = data['spike_s2'].to_numpy()
gc_n = data['gc_normalized'].to_numpy()
pp1a_n = data['pp1a_n'].to_numpy()
nsp2_n = data['nsp2_n'].to_numpy()
rbd_n = data['rbd_n'].to_numpy()
spike_s1_n = data['spike_s1_n'].to_numpy()
spike_s2_n = data['spike_s2_n'].to_numpy()

from scipy.stats import pearsonr
pearsonr(Temperature, gc)
pearsoncorr = data.corr(method='pearson')
pearsoncorr = pearsoncorr[['Temperature', 'Latitude', 'Longitude']]
pearsoncorr = pearsoncorr.drop(['Temperature', 'Latitude', 'Longitude', 'Relative Date'])
print(pearsoncorr)
sb.heatmap(pearsoncorr,
            xticklabels=pearsoncorr.columns,
            yticklabels=['Genomic Change', 'pp1a Change', 'nsp2a Change', 'RBD Change',
            'Spike_s1 Change', 'Spike_s2 Change', 'Norm. Genomic Change', 'Norm. pp1a Change', 'Norm. nsp2 Change', 'Norm. RBD Change', 'Norm. Spike_s1 Change', 'Norm. Spike_s2 Change'],
            cmap='YlGnBu',
            annot=True,
            linewidth=0.5)
plt.show()

print("TEMPERATURE")
print(scipy.stats.pearsonr(gc, Temperature))
print(scipy.stats.pearsonr(pp1a, Temperature))
print(scipy.stats.pearsonr(nsp2, Temperature))
print(scipy.stats.pearsonr(rbd, Temperature))
print(scipy.stats.pearsonr(spike_s1, Temperature))
print(scipy.stats.pearsonr(spike_s2, Temperature))
print(scipy.stats.pearsonr(gc_n, Temperature))
print(scipy.stats.pearsonr(pp1a_n, Temperature))
print(scipy.stats.pearsonr(nsp2_n, Temperature))
print(scipy.stats.pearsonr(rbd_n, Temperature))
print(scipy.stats.pearsonr(spike_s1_n, Temperature))
print(scipy.stats.pearsonr(spike_s2_n, Temperature))
print("\n")
print("LATITUDE")
print(scipy.stats.pearsonr(gc, Latitude))
print(scipy.stats.pearsonr(pp1a, Latitude))
print(scipy.stats.pearsonr(nsp2, Latitude))
print(scipy.stats.pearsonr(rbd, Latitude))
print(scipy.stats.pearsonr(spike_s1, Latitude))
print(scipy.stats.pearsonr(spike_s2, Latitude))
print(scipy.stats.pearsonr(gc_n, Latitude))
print(scipy.stats.pearsonr(pp1a_n, Latitude))
print(scipy.stats.pearsonr(nsp2_n, Latitude))
print(scipy.stats.pearsonr(rbd_n, Latitude))
print(scipy.stats.pearsonr(spike_s1_n, Latitude))
print(scipy.stats.pearsonr(spike_s2_n, Latitude))
print("\n")
print("LONGITUDE")
print(scipy.stats.pearsonr(gc, Longitude))
print(scipy.stats.pearsonr(pp1a, Longitude))
print(scipy.stats.pearsonr(nsp2, Longitude))
print(scipy.stats.pearsonr(rbd, Longitude))
print(scipy.stats.pearsonr(spike_s1, Longitude))
print(scipy.stats.pearsonr(spike_s2, Longitude))
print(scipy.stats.pearsonr(gc_n, Longitude))
print(scipy.stats.pearsonr(pp1a_n, Longitude))
print(scipy.stats.pearsonr(nsp2_n, Longitude))
print(scipy.stats.pearsonr(rbd_n, Longitude))
print(scipy.stats.pearsonr(spike_s1_n, Longitude))
print(scipy.stats.pearsonr(spike_s2_n, Longitude))
print("\n")
