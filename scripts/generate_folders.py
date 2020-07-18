import os, sys
import pandas as pd

df = pd.read_csv('toc.csv')
print(df)

os.mkdir('paper')
for index, row in df.iterrows():
    this_folder = 'paper/' + str(row['ID'])
    os.mkdir(this_folder)
    f = open(this_folder + '/README.md', "w+")
    f.write('# ' + str(row["Title"]) + '\n\n')
    f.write('- **ID:** ' + str(row["ID"]) + '\n')
    f.write('- **Track:** ' + str(row["Track"]) + '\n')
    f.write('- **Title:** ' + str(row["Title"]) + '\n')
    f.write('- **Authors:** ' + str(row["Authors"]) + '\n')
    this_pdf_filename = 'https://acis2019.io/pdfs/ACIS2019_PaperFIN_' + str(row["ID"]).zfill(3) + '.pdf'
    f.write('- **Download**: [' + this_pdf_filename + '](' + this_pdf_filename + ')')