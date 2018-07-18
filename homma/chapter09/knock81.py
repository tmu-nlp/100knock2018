import bz2
from tqdm import tqdm


def main():
    replacements = []
    for line in open('countries.txt', encoding='utf8'):
        words = line.strip().split()
        if len(words) > 1:
            replacements.append((' '.join(words), '_'.join(words)))

    with open('knock81_out', 'w', encoding='utf8') as f:
        for line in tqdm(open('knock80_out', encoding='utf8')):
            for old, new in replacements:
                line = line.replace(old, new)
            f.write(line)


if __name__ == '__main__':
    main()


''' 問
81. 複合語からなる国名への対処

英語では，複数の語の連接が意味を成すことがある．
例えば，アメリカ合衆国は"United States"，イギリスは"United Kingdom"と表現されるが，
"United"や"States"，"Kingdom"という単語だけでは，指し示している概念・実体が曖昧である．
そこで，コーパス中に含まれる複合語を認識し，複合語を1語として扱うことで，複合語の意味を推定したい．
しかしながら，複合語を正確に認定するのは大変むずかしいので，ここでは複合語からなる国名を認定したい．

インターネット上から国名リストを各自で入手し，80のコーパス中に出現する複合語の国名に関して，
スペースをアンダーバーに置換せよ．
例えば，"United States"は"United_States"，"Isle of Man"は"Isle_of_Man"になるはずである．
'''

''' 実行結果
https://gist.github.com/kalinchernev/486393efcca01623b18d
からダウンロードした国名リストを使用

$ head knock81_out
Anarchism
Anarchism is a political philosophy that advocates stateless societies often defined as self-governed voluntary institutions but that several authors have defined as more specific institutions based on non-hierarchical free associations Anarchism holds the state to be undesirable unnecessary or harmful While anti-statism is central anarchism entails opposing authority or hierarchical organisation in the conduct of human relations including but not limited to the state system
As a subtle and anti-dogmatic philosophy anarchism draws on many currents of thought and strategy Anarchism does not offer a fixed body of doctrine from a single particular world view instead fluxing and flowing as a philosophy There are many types and traditions of anarchism not all of which are mutually exclusive Anarchist schools of thought can differ fundamentally supporting anything from extreme individualism to complete collectivism Strains of anarchism have often been divided into the categories of social and individualist anarchism or similar dual classifications Anarchism is usually considered a radical left-wing ideology and much of anarchist economics and anarchist legal philosophy reflect anti-authoritarian interpretations of communism collectivism syndicalism mutualism or participatory economics
The central tendency of anarchism as a social movement has been represented by anarcho-communism and anarcho-syndicalism with individualist anarchism being primarily a literary phenomenon which nevertheless did have an impact on the bigger currents and individualists have also participated in large anarchist organisations Many anarchists
oppose all forms of aggression supporting self-defense or non-violence anarcho-pacifism while others have supported the use of some coercive measures including violent revolution and propaganda of the deed as means to achieve anarchist ends
Etymology and terminology
The term anarchism is a compound word composed from the word anarchy and the suffix -ism themselves derived respectively from the Greek i.e anarchy from anarchos meaning
one without rulers from the privative prefix ἀν- an- i.e without and archos i.e leader ruler cf archon or arkhē i.e authority sovereignty realm magistracy and the suffix
or -ismos -isma from the verbal infinitive suffix -ίζειν -izein The first known use of this word was in 1539."Anarchist was the term adopted by Maximilien de Robespierre
to attack those on the left whom he had used for his own ends during the French Revolution but was determined to get rid of though among these anarchists there were few who exhibited the social revolt characteristics of later anarchists There would be many revolutionaries of the early nineteenth century who contributed to the anarchist doctrines of the next generation such as William Godwin and Wilhelm Weitling but they did not use the word anarchist or anarchism in describing themselves or their beliefs
Pierre-Joseph Proudhon was the first political philosopher to call himself an anarchist marking the formal birth of anarchism in the mid-nineteenth century Since the 1890s from France the term libertarianism has often been used as a synonym for anarchism and was used almost exclusively in this sense until the 1950s in the United_States its use as a synonym is still common outside the United_States On the other hand some use libertarianism to refer to individualistic free-market philosophy only referring to free-market anarchism as libertarian anarchism
History
Origins
The earliest anarchist themes can be found in the 6th century BC among the works of Taoist philosopher Laozi and in later centuries by Zhuangzi and Bao Jingyan Zhuangzi's philosophy has been described by various sources as anarchist Zhuangzi wrote A petty thief is put in jail A great brigand becomes a ruler of a Nation Diogenes of Sinope
and the Cynics their contemporary Zeno of Citium the founder of Stoicism also introduced similar topics Jesus is sometimes considered the first anarchist in the Christian anarchist tradition Georges Lechartier wrote that The true founder of anarchy was Jesus Christ and the first anarchist society was that of the apostles In early Islamic
history some manifestations of anarchic thought are found during the Islamic civil war over the Caliphate where the Kharijites insisted that the imamate is a right for each individual within the Islamic society Later some Muslim scholars such as Amer al-Basri and Abu Hanifa led movements of boycotting the rulers paving the way to the waqf endowments tradition which served as an alternative to and asylum from the centralized authorities of the emirs But such interpretations reverberates subversive religious conceptions like the aforementioned seemingly anarchistic Taoist teachings and that of other anti-authoritarian religious traditions creating a complex relationship regarding the question as to whether or not anarchism and religion are compatible This is exemplified when the glorification of the state is viewed as a form of sinful idolatry
The French renaissance political philosopher Étienne de La Boétie wrote in his most famous work the Discourse on Voluntary Servitude what some historians consider an important anarchist precedent
'''
