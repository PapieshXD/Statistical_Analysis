import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = "C:\\Users\PC\PycharmProjects\Projekt Biostat\.venv\insurance.csv"

df = pd.read_csv(file_path)

#print(df.head())

bins = [0,18,35,44,59,100]
labels = ['0-18', '19-34', '35-44', '45-59', '60+']#skopiowane z starego zadania

bins1 = [0, 1, 2, 3, 4, float('inf')]  # Przedziały wiekowe
labels1 = ['0', '1', '2', '3', '4+']  # Etykiety dla przedziałów

age = df['age']
df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels)
age_group_count = df['age_group'].value_counts()

children = df['children']
df['children_group'] = pd.cut(df['children'], bins=bins1, labels=labels1, right=True)
children_group_counts = df['children_group'].value_counts()

bmi = df['bmi']

insurence = df['charges']
#obliczenia dla bmi
mean_bmi = bmi.mean()
std_bmi = bmi.std()
skew_bmi = bmi.skew()
kurt_bmi = bmi.kurt()
min_bmi = bmi.min()
max_bmi = bmi.max()

mean_charges = insurence.mean()
std_charges =  insurence.std()
skew_charges = insurence.skew()
kurt_charges = insurence.kurt()
min_charges =  insurence.min()
max_charges =  insurence.max()

#wyświetlanie wartości
print(f'the mean bmi is {mean_bmi}')
print(f'the std of bmi is {std_bmi}')
print(f'the skew of bmi is {skew_bmi}')
print(f'the kurt of bmi is {kurt_bmi}')
print(f'the min bmi is {min_bmi}')
print(f'the max bmi is {max_bmi}')
print('========================================')
print(f'the mean charges is {mean_charges}')
print(f'the std of charges is {std_charges}')
print(f'the skew charges is {skew_charges}')
print(f'the kurt charges is {kurt_charges}')
print(f'the min charges is {min_charges}')
print(f'the max charges is {max_charges}')
#wykresy
plt.title(f"pie chart of age distribution",)
plt.pie(age_group_count, labels=labels, autopct='%1.1f%%')
plt.show()
plt.savefig('pie chart')

plt.hist(bmi)
plt.title('BMI distribution')
plt.xlabel('BMI')
plt.ylabel('Count')
plt.show()
plt.savefig('bmi')

plt.pie(children_group_counts,  labels=children_group_counts.index, autopct='%1.1f%%' )
plt.title('Children distribution')
plt.show()
plt.savefig('children distribution')

plt.hist(insurence, bins = 20)
plt.title('Insurence payment distribution')
plt.xlabel('Insurence')
plt.ylabel('Count')
plt.show()
plt.savefig

df.boxplot(column='charges', by='smoker', grid=False)

# Dodanie tytułów i etykiet
plt.title('cost of insurence depending on smoking')
plt.suptitle('')
plt.xlabel('do you smoke?')
plt.ylabel('cost of insurance')
plt.show()
plt.savefig('cost of insurance')
print("==========================================")
# Tabela krzyżowa: palenie vs kwota ubezpieczenia

df['insurence_treashhold'] = df['charges'].apply(lambda x: '<20k' if x <20000 else '>20k')
cross_tab = pd.crosstab(df['insurence_treashhold'], df['smoker'], margins= True, margins_name = "sum")
print("cross table:")
print(cross_tab)

column_mapping = {'no': 0, 'yes': 1}
cross_tab = cross_tab.rename(columns=column_mapping)

TP = cross_tab.loc['<20k', 1]
FN = cross_tab.loc['>20k', 1]
FP = cross_tab.loc['<20k', 0]
TN = cross_tab.loc['>20k', 0]

sensivity = (TP / (TP + FN)) *100
specificity = (TN / (TN+FP)) *100
ppv = (TP / (TP + FP) )* 100
npv = (TN / (TN + FN)) *100
FA = abs((1 - specificity))
accuracy = ((TP + TN) / (TP + FN + FP + TN) )* 100
print(f'the amount of true positive cases is {TP}')
print(f'the amount of false negative cases is {FN}')
print(f'the amount of fale positive cases is {FP}')
print(f'the amount of true negative cases is {TN} ')
print("==============================================================")
print(f'The spensivity of diagnostics test is equeal to {sensivity}')
print(f'The specifity of diagnostics test is equeal to {specificity}')
print(f'The positive prognostics value is equeal to {ppv}')
print(f'The negative prognostics value is equeal to {npv}')
print(f'The falls alarm rate is equeal to {FA}')
print(f'The accuracy of diagnostics test is {accuracy}')

