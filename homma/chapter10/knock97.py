import pickle
from gensim.models import KeyedVectors
from sklearn.cluster import KMeans

def main():
    data_path = 'knock96_country'
    with open(data_path, 'rb') as f:
        country_ids = pickle.load(f)
        vec = pickle.load(f)
        cls = KMeans(5).fit(vec)
        for i, label in enumerate(cls.labels_):
            print(label, country_ids[i])


if __name__ == '__main__':
    main()


''' 問
97. k-meansクラスタリング

96の単語ベクトルに対して，k-meansクラスタリングをクラスタ数k=5として実行せよ．
'''

''' 実行結果
3 Afghanistan
1 Albania
1 Algeria
0 Andorra
1 Angola
2 Argentina
3 Armenia
4 Australia
2 Austria
1 Azerbaijan
0 Bahamas
0 Bahrain
1 Bangladesh
0 Barbados
0 Belarus
2 Belgium
0 Belize
0 Benin
0 Bhutan
1 Bolivia
0 Botswana
2 Brazil
0 Brunei
3 Bulgaria
0 Burkina
0 Burundi
1 Cambodia
0 Cameroon
4 Canada
0 Chad
1 Chile
4 China
1 Colombia
0 Comoros
0 Congo
1 Croatia
2 Cuba
1 Cyprus
2 Denmark
0 Djibouti
0 Dominica
0 Ecuador
3 Egypt
0 Eritrea
0 Estonia
1 Ethiopia
1 Fiji
2 Finland
2 France
0 Gabon
0 Gambia
1 Georgia
2 Germany
1 Ghana
3 Greece
0 Grenada
0 Guatemala
1 Guinea
0 Guinea-Bissau
0 Guyana
0 Haiti
0 Honduras
3 Hungary
0 Iceland
4 India
1 Indonesia
1 Iran
3 Iraq
3 Israel
2 Italy
0 Jamaica
4 Japan
0 Jordan
0 Kazakhstan
1 Kenya
0 Kiribati
1 Kosovo
0 Kuwait
0 Kyrgyzstan
0 Laos
0 Latvia
1 Lebanon
0 Lesotho
0 Liberia
1 Libya
0 Liechtenstein
0 Lithuania
0 Luxembourg
3 Macedonia
0 Madagascar
0 Malawi
1 Malaysia
0 Maldives
0 Mali
0 Malta
0 Mauritania
0 Mauritius
2 Mexico
0 Micronesia
0 Moldova
0 Monaco
0 Mongolia
0 Montenegro
1 Morocco
0 Mozambique
0 Namibia
0 Nauru
1 Nepal
2 Netherlands
0 Nicaragua
0 Niger
1 Nigeria
2 Norway
0 Oman
1 Pakistan
0 Palau
1 Panama
0 Paraguay
1 Peru
1 Philippines
3 Poland
2 Portugal
0 Qatar
2 Romania
0 Rwanda
1 Samoa
0 Senegal
3 Serbia
0 Seychelles
1 Singapore
1 Slovakia
0 Slovenia
0 Somalia
2 Spain
1 Sudan
0 Suriname
0 Swaziland
2 Sweden
2 Switzerland
3 Syria
3 Taiwan
0 Tajikistan
1 Tanzania
1 Thailand
0 Togo
0 Tonga
0 Tunisia
3 Turkey
0 Turkmenistan
0 Tuvalu
1 Uganda
1 Ukraine
0 Uruguay
0 Uzbekistan
0 Vanuatu
1 Venezuela
3 Vietnam
0 Yemen
0 Zambia
0 Zimbabwe
'''
