#素性の重み

import codecs
import numpy as np 

with codecs.open('features.txt','r',encoding='latin-1')as f:
    features = list(f)

theta = np.load('theta.npy')

index_sorted = np.argsort(theta)

print('top10')
for index in index_sorted[:-11:-1]:
    print('{}\t{}'.format(theta[index],features[index-1]))

print('bad10')
for index in index_sorted[:10]:
    print('{}\t{}'.format(theta[index],features[index-1]))


'''top10
0.899041776812356       beauti

0.7651344295157738      refresh

0.7604191846011016      heart

0.7603147517242621      enjoy

0.7443520295460141      entertain

0.7268654200233595      cinema

0.7196063448931028      fun

0.7044709703766622      still

0.698920521255853       human

0.6916551558472469      move

bad10
-1.3211860293730893     bad

-1.216481702392048      too

-1.0591202830547266     dull

-1.029832699144159      bore

-0.9977083742889413     lack

-0.8196168865202806     fail

-0.7743064671978859     worst

-0.6996487990072153     joke

-0.683487805180046      no

-0.6797148431403786     wast'''