#! /usr/bin/env python
# -*- coding: utf-8 -*-

import config
import telebot
from engine import get_random_quote
import time
import urllib
from glob import glob
from random import choice

bot = telebot.TeleBot(config.token)


        

@bot.message_handler(func=lambda message: True)
def main(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    text = str(message.text).lower()
    if text == "покажи накера":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/0/06/%D0%9D%D0%B0%D0%BA%D0%B5%D1%80%D0%93%D0%92.png', 'Представьте себе утопца, который роет подземные туннели, забирается на деревья и отличается исключительной злобностью, а если атакует, то всегда делает это в компании множества сородичей. Примерно так можно описать накера. Эти примитивные существа — мерзость пущи. Их боятся жители лесных деревень, а звери издалека обходят их гнезда. Накеры — коллективные твари и образуют нечто вроде племен, потому что только числом они могут отбиться от нападения более сильных противников.')
    if text == "покажи абайю":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/f/f7/%D0%90%D0%B1%D0%B0%D0%B9%D1%8F_%D0%923.jpg', 'Залив у Каэр Трольде всегда имел дурную репутацию. Время от времени рыбаки забросившие там сети, не возвращались домой с лова. Что-то утягивало гребцов с драккаров и переворачивало лодки. Местные винили во всем морских дьяволов — так на Скеллиге называют утопцев. Правда же оказалась гораздо хуже.')
    if text == "покажи альгуля":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/c/c8/%D0%93%D1%83%D0%BB%D1%8C_%E2%84%961.png', 'Альгули — это гули, которые питаются трупами на протяжении стольких лет, что сладкий вкус человеческой плоти вынудил их нападать на живых людей и съедать их неостывшие тела. Их можно встретить в склепах и на полях сражений, чаще всего в окружении простых гулей. Обычные люди не видят разницы между этими падальщиками. Только ведьмаки понимают, что альгули на самом деле являются более агрессивными и опасными противниками')
    if text == "покажи альпа":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/d/d6/B%26W_%D0%90%D0%BB%D1%8C%D0%BF.jpg', 'Альп — это вампир, внешне похожий на бруксу. Кое-кто зовет их приведениями, и это название им очень подходит, поскольку приведения тоже преследуют и терзают людей. Обычно они принимают женскую форму, но могут выглядеть и как животные. Чаще всего они бродят вблизи деревень. Нападают ночью и особенно активны при полной луне. Слюна альпа усыпляет бодрствующего человека, а у спящего вызывает ужасные кошмары. Бывает так, что человека ложится спать здоровым, а на утро находят его белым, как снег, и без капли крови в венах. ')
    if text == "покажи амбисфену":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/4/47/%D0%90%D0%BC%D1%84%D0%B8%D1%81%D0%B1%D0%B5%D0%BD%D0%B01.jpg', 'Амфисбена — гигантская змея с головой на каждом конце, живёт в водоёмах.')
    if text == "покажи арахноморфа":
       bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/4/41/%D0%90%D1%80%D0%B0%D1%85%D0%BD%D0%BE%D0%BC%D0%BE%D1%80%D1%84.png', 'Похожим образом дело обстоит, когда речь идет об арахноморфах и обо всем, что не в состоянии от них убежать, то есть, о большей части существ на белом свете. Однако их не стоит опасаться тому, кто собирается пахать поле или выбирается в лес на ягоды, ибо арахноморфы, будучи дальними, из эпохи Сопряжения Сфер, родственниками обычных пауков, особенно облюбовали для себя глубокие тенистые пещеры и непроходимые мрачные пущи. И все же, кто бы на них не наткнулся, ему наверное будет лучше заранее исповедаться в своих грехах и попрощаться с жизнью, ибо он погибнет наверняка, поскольку от них даже самый быстрый человек не в состоянии улизнуть. Наиболее опасная и агрессивная разновидность арахноморфов, арахноморф гигантский, в состоянии сожрать даже вола.')
    if text == "покажи археспору":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/d/d5/%D0%90%D1%80%D1%85%D0%B5%D1%81%D0%BF%D0%BE%D1%80%D0%B0_%D0%B2_%D1%84%D0%B5%D1%80%D0%BC%D0%B5%D0%BD%D1%82%D0%B8%D0%BD%D0%BE1.jpg', 'Архиспоры выглядят как гигантские, неприятные цветы с повадками исключительно жестокой и кровожадной росянки. Но они куда опаснее, чем даже самая крупная росянка. Их внешний вид делает их практически незаметными на фоне других растений. И когда кто-нибудь подходит достаточно близко, чтобы понять, что это, то бывает уже поздно.')
    if text == "покажи архигрифона":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/0/09/%D0%9E%D0%BF%D0%B8%D0%BD%D0%B8%D0%BA_3%D0%923.jpg', 'Архигрифоны – это более грозный подвид грифона, отличающийся от своих сородичей свирепостью, силой, а также уникальными чертами: подобно василискам, они могут плеваться ядом, который вырабатывается в специальной железе, а также не чувствительны к огню. В то время как шкура и оперение обычных грифонов бывает песочного, желтого или светло-бурого оттенков, архигрифоны куда более «нарядны»: их шкура, кожа и оперение черного цвета имеют красные, «пламенные» прожилки, особенно заметные на кромке каждого пера, шерсть, в частности, грива и кисточка хвоста, также черные. Встречаются также абсолютно белые особи-альбиносы.')
    if text == "покажи барбегаза":
       bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/9/9e/%D0%91%D0%B0%D1%80%D0%B1%D0%B5%D0%B3%D0%B0%D0%B7%D0%93%D0%92.png', 'То, что еще секунду назад он принимал за лежащие у основания сталагмитов округлые камни, теперь таращилось на него огромными горящими глазищами. В плотной массе серо-бурых, покрытых пылью патлов раскрывались огромные пасти и сверкали конусовидные зубы. Барбегазы. Барбегазы – их становилось все больше – сопровождали его, двигаясь следом и перекатываясь по почве. Он слышал их монотонную болтовню и сопение. Чувствовал их резкий кислый запах')
    if text == "покажи баргеста":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/f/fc/%D0%91%D0%B0%D1%80%D0%B3%D0%B5%D1%81%D1%82_%D0%9213.jpg', 'Считается, что баргесты — призраки, материализовавшиеся в призрачных псов и преследующие живых людей. По некоторым поверьям эти чудовища являются предзнаменованием Дикой Охоты. Другие же легенды гласят, что баргесты — воплощение божественной кары и олицетворенного возмездия. И только в одном все рассказы сходятся: баргесты всегда безжалостны по отношению к живым существам.')
    if text == "покажи барта":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/2/2d/%D0%91%D0%B0%D1%80%D1%82_%E2%84%964.png', '«Барт стерёг! Но было бум — и нет шомны… Барт болит — Барт меньше думать. Меньше думать — меньше грустный».')
    if text == "покажи баньши":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/f/f9/%D0%91%D0%B0%D0%BD%D1%88%D0%B8%D0%923.png', 'Древние сплетни утверждают, что баньши — это духи женщин, застрявших между жизнью и смертью из-за тяжёлых переживаний. Их стон и вой считается верным признаком скорой и неминуемой смерти, хотя, говорят, они на живых не нападают. Чаще всего они являются в виде бледных женщин в лохмотьях, с иссушенными лицами и сморщенными, мёртвыми телами.')
    if text == "покажи белую даму":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/b/b5/%D0%91%D0%B5%D0%BB%D0%B0%D1%8F_%D0%B4%D0%B0%D0%BC%D0%B0%D0%923.png', '— А что за Мирко?  Были тут такие четверо, лодыри и пропойцы. Осушили пару кружек и удумали, что если вместе Белую Даму отымеют, то она и уберется отсюда.')
    if text == "покажи беса":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/a/ad/0098.jpg/', 'Бесы — это ходячая гора мускулов, увенчанная рогатой головой с пастью, полной острых зубов. Как и его более редкий родственник, бука, бес живет в густых чащах, в топях и на болотах. Когда это возможно, он избегает людей. Но если этого не удается, то убивает их безо всякого труда.')
    if text == "покажи бруксу":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/a/a5/%D0%91%D1%80%D1%83%D0%BA%D1%81%D0%B0_%E2%84%961.png/', 'Легенды гласят, что брукса охотится по ночам за привлекательными юношами, а поймав свою жертву, до капли высасывает её кровь. Вампирица совершенно бесшумно передвигается во тьме, поэтому её нападение всегда является неожиданным. Брукса способна принимать вид прекрасной девушки, поэтому её часто ошибочно принимают за русалку. Однако длинные клыки бруксы и её неутолимая жажда крови всегда её выдают.')
    if text == "покажи варга":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/8/85/Tw3_Warg.png', 'От обычных волков варги отличаются бурым окрасом, красными глазами и более крупным размером. Они также более свирепы и выносливы. Варги часто предводительствуют в стаях волков и нападают всегда в сопровождении 5-10 обычных особей.')
    if text == "покажи василиска":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/5/53/%D0%92%D0%B0%D1%81%D0%B8%D0%BB%D0%B8%D1%81%D0%BA2%D0%923.jpg/', 'Люди называют василисков королями зерриканских пустынь и очень часто путают их с кокатриксами. По поверьям, эти создания настолько ненавидят все живое, что само их дыхание несет смерть, а их взгляд обращает людей в камень. В сказках василиска убивают, выставляя перед их мордой зеркало. Чудовище якобы умирает от собственного смертоносного взгляда. Однако, как любят пошутить ведьмаки, единственный способ убить василиска с помощью зеркала - садануть им зверю прямо по башке.')
    if text == "покажи вепря":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/5/55/%D0%92%D0%B5%D0%BF%D1%80%D1%8C%D0%923.png', 'Чудище лесно, зло и дико. До сего дня в некоторых деревушках на окраинах Каэдвена бытует убеждение, что его любимое блюдо — это девицы, однако истина заключается в том, что обычно вепрь довольствуется овощами, а нередко одной только морковкой. Зверь, учитывая крепкое строение тела и острые клыки, обладает большим батально-диверсионным потенциалом. Мать-природа наделила его комплектом из двух пар клыков: вепрь сеет страх среди людей и прочих обитателей леса. У вепря также есть твердое рыло, или свисток, однако свистеть им он не может. Народные предания указывают, что все вепри питают из-за этого к матери-природе большие претензии, и, выражая оные, валят заборы и пожирают картошку. Легче всего распознать вепря по характерному хрюканью, звучащему как «Чего?!». Обычно вепри встречаются небольшими стадами по 3-5 особей.')
    if text == "покажи виверну":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/b/bc/%D0%92%D0%B8%D0%B2%D0%B5%D1%80%D0%BD%D0%B0_3.jpg', 'Виверн, к сожалению, часто путают с драконами. При виде рептилии, которая летит к стаду овец, кметы начинают паниковать. Они ждут, что сейчас начнется выдыхание огня, резня и весь этот цирк с девицами. Виверны действительно охотятся на овец, однако они не выдыхают пламени и не угрожают целой деревне. И к девицам они абсолютно равнодушны.')
    if text == "покажи вия":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/b/bf/%D0%92%D0%B8%D0%B9.jpg', 'Последнее творение легендарного чародея Альзура и дитя Двойного креста, Вий – это неописуемое чудовище, напоминающее сколопендроморфа, но в сотню метров длиной. Изуродовав и убив своего создателя, монстр уничтожил половину города Марибора и сбежал в зареченский лес. Вряд ли он дал потомство, чтобы выжить и сохранить свой ужасный род.  ')
    if text == "покажи вилохвоста":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/8/8f/%D0%92%D0%B8%D0%BB%D0%BE%D1%85%D0%B2%D0%BE%D1%81%D1%82_4%D0%923.jpg', 'Своим звучным названием вилохвост обязан длинным острым отросткам, венчающим его хвост. Нанесенный им удар может пробить насквозь и дубовый щит, и руку, которая его держит, даже если её будет защищать кольчужная перчатка. Другими словами, с вилохвостом, даже молодым, шутки плохи.')
    if text == "покажи вихта":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/5/55/%D0%92%D0%B8%D1%85%D1%82%D0%923.png', 'Хотя вихты не похожи на дружелюбных созданий, к ним не следует относится враждебно. Будучи представлены самим себе, вихты не представляют никакой опасности. Их интересует не драка, а котлы, в которых они мешают своё варево. Этот вид обитает большей частью на старых кладбищах, но видели их и в окрестностях новых погребений и массовых захоронений. На зиму вихты впадают в спячку, напоминающую человеческий сон. Живут только поодиночке. Практически никогда не ходят группами.')
    if text == "покажи водную бабу":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/a/aa/%D0%92%D0%BE%D0%B4%D1%8F%D0%BD%D0%B0%D1%8F_%D0%B1%D0%B0%D0%B1%D0%B0_%E2%84%962.png', 'Некоторые предания говорят о том, как водные бабы и водницы заманивали путников в свои построенные на болотах катки, притворяясь заблудившимися старушками. На самом деле только очень пьяный или слепой мог бы перепутать смердящее тиной и падалью логово с уютным домиком, а само чудовище – с бабушкой. Сморщенное и покрытое бородавками тело водной бабы достигает почти сажени и воняет илом и рыбой. Из загривка у нее торчат длинные, до двух падей длиной, костяные отростки. Образ дополняют волосы, похожие на ворох спутанных водорослей, и когти, которых не постыдился бы волколак.')
    if text == "покажи волка":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/8/8c/%D0%92%D0%BE%D0%BB%D0%BA%D0%B8_%E2%84%964.jpg/', 'Некогда волки были безраздельными владыками лесов. Люди пугали ими детей, дрожали от одного звука волчьего воя. Чудовища, возникшие после Сопряжения Сфер, не просто оттеснили в глубокую глушь, но также заняли их место в сознании людей. Это однако не значит, что прежние хищники перестали быть опасными. Быть может, у волков нет и крупицы магии, они не пышут огнём, не плюют кислотой, но это никак не мешает им убивать неосторожных путников и охотников.')
    if text == "покажи волколака":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/2/2c/%D0%92%D0%BE%D0%BB%D0%BA%D0%BE%D0%BB%D0%B0%D0%BA_%E2%84%961.png', 'Волколак — это получеловек-полуволк. От обоих он берет самые худшие и самые опасные качества. Людскую ловкость и жестокость сочетает он со звериной жаждой крови и инстинктом убийцы. Волколаками становятся по причине проклятия, а потому процесс трансформации нельзя ни осознать, ни проконтролировать. Вернувшись в человеческий облик, волколак не помнит своих поступков. В противном случае он бы наверняка или сошел с ума, или попытался бы покончить с собой.')
    if text == "покажи высшего вампира":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/5/50/%D0%9E%D1%80%D0%B8%D0%B0%D0%BD%D0%B0_%E2%84%964.png', 'Высших вампиров с их далекими примитивными побратимами, такими как альпы, экиммы или катаканы, роднит лишь употребление крови. На самом деле они значительно ближе к людям, нежели к остальным кровопийцам. Они напоминают нас не только внешним видом, но также интеллектом и поведением. При этом они не живут на безлюдье и не скрываются в тени. Как раз наоборот: они особенно облюбовали города, где ведут с виду нормальную жизнь. Даже ведьмаки не в состоянии их распознать, поскольку их медальоны ни в малейшей степени не реагируют на присутствие высшего вампира. Однако все это сходство не должно скрывать очевидной разницы: в отличие от людей, высшие вампиры по-настоящему бессмертны. Тех, кто вышел против них на бой и уцелел, можно пересчитать по пальцам одной руки.')
    if text == "покажи гаргулью":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/5/5e/%D0%93%D0%B0%D1%80%D0%B3%D1%83%D0%BB%D1%8C%D1%8F%D0%923.png', 'Гарryльи – каменные статуи, оживленные с помощью магии, чтобы защищать лаборатории и жилища чародеев от вторжения незваных гостей. Один только их облик отпугивает большую часть взломщиков. Те же, кто не пугается при виде этих рогатых и крылатых чудовищ, обычно умирают вскоре после, разорванные каменными костями.')
    if text == "покажи гаркаина":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/1/18/%D0%93%D0%B0%D1%80%D0%BA%D0%B0%D0%B8%D0%BD_%D0%9A%D0%B8%D0%92.png', 'Гаркаины, как и фледеры, относятся к чрезвычайно опасной разновидности вампиров, превосходящих силой даже бесов. Встреча с любым из них почти неизбежно оканчивается смертью, и поэтому живых свидетелей крайне мало. Эти чудовища не довольствуются тем, что пьют кровь своих жертв. Из крови и кишок, разбросанных на месте каждого преступления, следователи сделали вывод, что гаркаины с наслаждением рвут тела жертв на части и кувыркаются в их окровавленных внутренностях.')
    if text == "покажи гарпию":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/7/79/%D0%93%D0%B0%D1%80%D0%BF%D0%B8%D0%B82%D0%922.png', 'Сложно сказать, что более отвратительно в гарпиях и родственных им шишигах. Их ужасный вид, исходящий от них смрад падали и птичьего помета или пронзительный писк, который они издают. Достаточно сказать, что даже крысы, привыкшие резвиться в сточных каналах и помойках, обходят их гнезда далеко стороной.')
    if text == "покажи гернихору":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/1/14/%D0%93%D0%B5%D1%80%D0%BD%D0%B8%D1%85%D0%BE%D1%80%D0%B0%D0%93%D0%92.png', 'Некоторые говорят, что Гернихора — высокая женщина, с головы до пят покрытая набухшими от крови пиявками. Другие утверждают, что она выглядит как сирена — с брюхом пиявки вместо рыбьего хвоста. Трудно сказать, кто прав: ни один из тех, кто получал возможность рассмотреть ее вблизи, не пережил этой встречи.')
    if text == "покажи главоглаза":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/5/5a/%D0%9F%D0%B0%D0%BD%D1%86%D0%B8%D1%80%D0%BD%D1%8B%D0%B9_%D0%B3%D0%BB%D0%B0%D0%B2%D0%BE%D0%B3%D0%BB%D0%B0%D0%B7.png', 'Все паукообразные охотятся в одиночку. Они терпеливо ждут свою добычу, а завидев ее, способны убить одним молниеносным ударом. То же самое касается и главоглаза, большого страшилища, которое облюбовало для себя леса возле рек, и стало неоспоримым властелином этих мест. Властелином, который терпеть не может на своей территории других охотников, в том числе ведьмаков.')
    if text == "покажи гнильца":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/e/ec/%D0%93%D0%BD%D0%B8%D0%BB%D0%B5%D1%86_%E2%84%961.png', 'Гнилец выглядит, как разлагающийся человек со снятой кожей, голова которого распухла от собравшихся в черепе газов. Появление гнильцов сопровождается удушливым запахом гнили, которому они обязаны своим названием. Опасная разновидность гнильца – пожиратель, которого отличает неуемная тяга к людской плоти.')
    if text == "покажи голема":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/d/d6/Tw3_journal_golem.png', 'Големы не пользуются никаким оружием, ведь им этого и не нужно. Их кулаки весом по сто фунтов каждый одним ударом сокрушают гранитные скалы. Ударов голема следует избегать любой ценой: нет ни щита, который их выдержит, ни меча, что сможет их отбить. Увернуться же от чудовищных кулаков вовсе не просто, ибо голем способен двигаться с ошеломляющей быстротой. К счастью, из-за своей огромной массы голем не слишком поворотлив. Начав атаку, он уже не может быстро остановиться, что опытные ведьмаки умеют обернуть себе на пользу.')
    if text == "покажи голиафа":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/6/68/%D0%93%D0%BE%D0%BB%D0%B8%D0%B0%D1%84_%E2%84%965.png', 'Согласно легенде, Голиаф когда-то был рыцарем, который пошёл против собственного обета, за что его покарала Владычица Озера. Обращённый в великана, он бежал в горы и спускался в долину лишь несколько раз в году, мучимый голодом. Неизвестно, сколько в легенде правды, однако же неоспоримый факт заключается в том, что грозный великан-одиночка убивал и пожирал пастухов с той же охотой, что и их овец, и пользовался столь недоброй славой, что няньки пугали им непослушных детей.')
    if text == "покажи гончую дикой охоты":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/9/92/%D0%93%D0%BE%D0%BD%D1%87%D0%B0%D1%8F_%D0%B4%D0%B8%D0%BA%D0%BE%D0%B9_%D0%BE%D1%85%D0%BE%D1%82%D1%8B%D0%923.png', 'В самом конце кавалькады призраков Дикой Охоты мчатся гончие, словно ледяная пыль, что тянется за кометой. Говорят, что иногда они сбиваются с пути и спускаются с ночного неба на землю, неся за собою холод и смерть.')
    if text == "покажи грайвера":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/8/88/Bestiary_Graveir_full.png', 'Гравейр — разновидность гулей. Он очень похож на гуля, но гораздо крупнее. Отличают его также, как видишь, три костяных гребня на черепе. Остальное — как у любого трупоеда. Обрати внимание: когти короткие и тупые, пригодные для разгребания могил, для рытья земли. Мощные зубы, которыми он дробит кости, и длинный тонкий язык, чтобы вылизывать из них разложившийся мозг и жир. Как следует провонявшее сало для грайвера — деликатес')
    if text == "покажи грифона":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/4/4a/%D0%93%D1%80%D0%B8%D1%84%D0%BE%D0%BD_%E2%84%965.png', 'Когда-то грифоны жили только высоко в горах, где охотились на сусликов и горных коз. Но однажды они поняли, что на населённых людьми равнинах найти себе пропитание гораздо проще. Не важно, корову, овцу или пастуха. Это чудовище, соединяющее в себе орла и дикого кота, буквально за несколько лет стало одним из самых ужасных бедствий Северных королевств. ')
    if text == "покажи гротника":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/a/af/Tw3_journal_spriggan_mh.png', 'Случилось вот что... Внезапный ливень застал меня в лесу, я и подумал, надо найти какую-нибудь пещерку, ибо богам неугодно, чтоб я промок до нитки и подхватил насморк, в мои-то годы. Итак, я забрался в пещеру. А там на меня как что-то зарычит! Я летел оттуда с такой скоростью, что по дороге домой вся моя одежда просохла на ветру.')
    if text == "покажи гуля":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/a/a8/%D0%93%D1%83%D0%BB%D1%8C%D0%923.png', 'Гулей и гравейров нелегко описать. С одной стороны, они напоминают человека, но с другой - они полная его противоположность. Хотя руки и ноги у них (за исключением ступней и ладоней) человеческие, ходят они на четвереньках, подобно собакам и барсукам. Лица у них, как у обычных мужчин, однако не стоит искать в них и следа хоть каких-то чувств, разума и хотя бы искру сознания. Ими движет только одно: неутолимая жажда свежего человеческого мяса.')
    if text == "покажи гэля":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/1/11/%D0%93%D1%8D%D0%BB%D1%8C%D0%923.png', 'Вопреки распространенному мнению, монстры не похожи друг на друга. Как и люди, они могут иметь свои собственные уникальные черты, сильные и слабые стороны. Хорошим примером этого является катакан которого когда-то кормили жители Оксенфурта. Возможно, под влиянием своей близости к "озорной" молодежи города, этот вампир приобрел острый аппетит к крови с алкоголем.')
    if text == "покажи дагона":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/8/8b/%D0%94%D0%B0%D0%B3%D0%BE%D0%BD_%D0%B3%D0%B2%D0%B8%D0%BD%D1%82_%D0%BA%D0%B0%D1%80%D1%82%D0%B0.jpg', 'В темных глубинах дремлют силы  древнее самого человечества. В подводных городах, куда никогда не проникают лучи солнца, спят боги и демоны. Спят и ждут, пока придет их время. Ибо сказано, что придет час, и пробудятся они, и разрушат весь мир. Одним из таких созданий и является Дагон. Он дремлет на дне озера, и ему поклоняются водяные и сумасшедшие, которых преследуют ночные кошмары. Дагон - воплощение силы и ярости, и, как только он выйдет на сушу, он станет и воплощением разрушения.')
    if text == "покажи дракона":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/3/3a/%D0%9E%D0%BA%D0%B2%D0%B8%D1%81%D1%82_%D0%93%D0%B2%D0%B8%D0%BD%D1%82.png', 'Некогда драконы встречались повсеместно и безраздельно владели континентом. Драконий огонь был погибелью для городов, а драконий аппетит - угрозой для первых колонизаторов. Против этих монстров выходили сражаться чародеи. Для борьбы с ними создали ведьмаков. Сейчас драконы почти что вывелись. Ещё встречаются вилохвосты да ослизги, но в сравнении с драконами они смотрятся так же, как чердачный кот на фоне тигра. Бестии эти были выбиты профессионалами, вроде знаменитых рубайл из Кринфрида. Алхимические ингредиенты, получаемые из тела дракона, относятся к числу самых дорогих на рынке и пользуются неослабевающим спросом у чародеев. Печёный хвост дракона - это настоящий деликатес.')
    if text == "покажи драуга":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/c/c8/%D0%94%D1%80%D0%B0%D1%83%D0%B31%D0%922.jpg', 'Это легендарное существо, пришедшее прямиком из древних сказаний о героях и эпических подвигах. Когда герой спускается в ад за своей возлюбленной или собирается отомстить за смерть отца, его противником часто оказывается именно драуг. Почему поэты склонны наделять ролью архимогущественного врага именно это чудвище? Видимо, потому, что драуг – это призрак, а значит, он подходит к любой мрачной истории, повествующей о проклятии или мести с того света. В сущности, не известно, как он выглядит. Поэтому его страшный вид можно описывать любыми способами, не рискуя быть обвиненным в вымысле. Кроме того, это могущественное существо, повелитель проклятых душ. Словом, такой монстр прекрасно подходит на роль идеального злодея.')
    if text == "покажи драугира":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/7/70/%D0%94%D1%80%D0%B0%D1%83%D0%B3%D0%B8%D1%80%D0%93%D0%92.jpg', 'Драуг - это вождь, а призрачные его солдаты зовутся драугирами. Они вернулись к жизни по воле драуга с древних полей сражений или кладбищ. Подобно драугу, они рождаются из проклятых душ, заключенных в скорлупу из остатков доспехов, оружия или разорванных падальщиками тел.')
    if text == "покажи жагницу":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/d/d4/%D0%96%D0%B0%D0%B3%D0%BD%D0%B8%D1%86%D0%B0%D0%93%D0%92.png', '...шершавое чудище, длиной в две сажени, напоминающее обросший водорослями пень с десятью лапами и челюстями словно пилы')
    if text == "покажи игошу":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/7/70/%D0%98%D0%B3%D0%BE%D1%88%D0%B0%D0%923.png', 'Игоша – это, пожалуй, наиболее отвратительное из чудовищ, с которыми приходится сталкиваться ведьмакам. Он возникает из мёртвого нежеланного ребёнка, которого после смерти даже не похоронили надлежащим образом. Выглядит он, как сгнивший новорождённый, искажённый наполняющими его ненавистью, прахом и злобой. Этот мерзкий монстр обычно питается силой и кровью беременных женщин, которых таким образом постепенно доводит до смерти.')
    if text == "покажи катакана":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/c/c2/%D0%9D%D0%BE%D1%81%D1%84%D0%B5%D1%80%D0%B0%D1%82%D0%93%D0%92.png', 'Катакан и его более грозный родич носферат — это воплощение людских страхов. Он скрывается в тени. Питается кровью. С виду напоминает огромного нетопыря, только с длинными клыками и еще более длинными когтями. И, словно этого мало, вдобавок еще умеет становиться невидимым.')
    if text == "покажи кащея":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/1/19/Koshchey_%28Lorenzo_Mastroianni%29.png', '— Кстати, как ты думаешь, что же такое кащей?  Боюсь, что смерть.')
    if text == "покажи кейрана":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/9/93/%D0%9A%D0%B5%D0%B9%D1%80%D0%B0%D0%BD%D0%93%D0%92.jpg', 'Кейран выделяется среди всех монстров: больших и малых, прекрасных и отвратительных. Он уникален и не похож ни на одно живое существо. Без сомнения, это чудовище появилось после Сопряжения Сфер и пришло в нашу действительность, когда с нашим миром соприкасался мир, совершенно чуждый нашему. Время от времени, на протяжении многих веков летописцы отмечали случаи появления кейрана в разных местах реки. Нельзя с уверенностью сказать, было ли это одно и то же чудовище, которое необычайно медленно двигалось вверх и вниз по течению, или же его потомки, которых видели то тут, то там.')
    if text == "покажи кикимору":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/0/05/Bestiary_Kikimore_warrior_full.png', 'Кикиморы это живое оскорбление богов, самые уродливые твари на свете. Они отвратительны в силу своей схожести с пауками, и даже самые мелкие из них - рабочие - смертельно опасны. Так говорят люди необразованные, суеверные и глупые. Истина совсем в другом! Кикиморы-рабочие редко появляются около поселений людей, и даже тогда нападают только, если им грозит опасность. Есть ли в мире что-то более прекрасное, чем кикимора, символ упорного труда, изобретательности и предусмотрительности?')
    if text == "покажи ключника":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/1/18/%D0%9A%D0%BB%D1%8E%D1%87%D0%BD%D0%B8%D0%BA.jpg', 'Существо, известное как Ключник, было призвано в имение фон Эвереков из другого мира, посему наиболее правильно называть его «демоном». Ключника принудили к службе с помощью магии. Его обязанности заключались в том, чтобы следить за домом и защищать его от вторжений. Он и выполнял их с достойной зависти педантичностью, ухаживая за цветами, ремонтируя ограду, присматривая за двором... и убивая всех, кто пытался проникнуть в имение. Затем он хоронил трупы аккуратными рядами на ничейной земле сразу за границами сада поместья.')
    if text == "покажи кокатрикса":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/f/f7/%D0%9A%D1%83%D1%80%D0%BE%D0%BB%D0%B8%D1%81%D0%BA.jpg', 'Кокатрикс вылупляется из яйца, которое снес петух, скрестившийся с другим петухом. При этом высиживать это яйцо должна жаба на протяжении сорока четырех дней. Эта самая жаба становится первой пищей вылупившегося создания. Кокатрикс ненавидит все живое и способен одним взглядом обратить человека в камень. Только тот смельчак способен победить кокатрикса, который вооружится зеркалом, поскольку зеркало отражает убийственный взгляд и обращает его против ящера, его самого превращая в камень.')
    if text == "покажи котолака":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/f/f8/Werecat_Gwent_card_art.jpg', '…и хоча он весьма до злата жаден, – бормотала бабка, щуря глаза, – не давать ему больше как за утопца серебряный грош либо полтора. За котолака два серебряных гроша. За вампира – четыре серебряных гроша…')
    if text == "покажи лешего":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/3/3b/QeUFZr345GY.jpg', 'Уже много лет ученые спорят, что же такое на самом деле леший. Большинство бестиариев относит их к реликтам, но многие специалисты подвергают сомнению такую оценку. Некоторые считают их порождением черной магии или даже некромантии. Другие доказывают, что это демоны, родственные джиннам или драугам. Если бы удалось вскрыть труп чудовища, это определенно пролило бы свет на загадку. Проблема лишь в том, что когда лешего убивают, его тело исчезает. Единственное, чтос после него остается, — это пожелтевший олений череп.')
    if text == "покажи мантихора":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/5/58/%D0%9C%D0%B0%D0%BD%D1%82%D0%B8%D0%BA%D0%BE%D1%80%D0%B0_%D0%93%D0%B2%D0%B8%D0%BD%D1%82.png', 'Мантикора — зверь с телом и головой льва, большими перепончатыми крыльями летучей мыши и хвостом скорпиона. Некоторые особи также имеют длинные козлиные рога, возможно, этой особенностью отличаются Королевские, или Императорские мантикоры. Имеют бледно-желтую или темную шкуру, на их телах растет короткая шесть и длинная львиная грива вокруг головы. На лапах — длинные когти, которые растут всю жизнь, что вынуждает бестий стачивать их, а жало на их хвостах отравлено.')
    if text == "покажи лесного тролля":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/b/b8/TrollTw2.png', 'Этот подвид троллей обитает, преимущественно, в лесах или же под мостами. Лесные тролли крупнее своих собратьев, однако не имеют столь крепкой, буквально «каменной» кожи. Носят подобие одежды и известны пристрастием к алкоголю и любовью к строительству. Живут обычно парами.')
    if text == "покажи скального тролля":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/5/5a/%D0%A1%D0%BA%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9_%D1%82%D1%80%D0%BE%D0%BB%D0%BB%D1%8C%D0%923.png', 'Этот подвид встречается повсеместно на территории Северных королевств, Скеллиге, Нильфгаарда и даже Зеррикании и предпочитает в качестве места жительства пещеры. Скальные тролли достаточно умны и часто контактируют с людьми, иногда даже выполняя для них простую работу — как правило, охраняют что-либо. Любят камни.')
    if text == "покажи йеннифер":
        bot.send_photo(chat_id, 'https://all-mods.ru/wp-content/uploads/2015/09/645-1-1441763695.jpg', 'Истинный облик Йен')
    if text == "покажи максима":
        bot.send_photo(chat_id, 'https://i.ibb.co/8cctKWS/photo-2021-01-27-11-34-10.jpg', 'В естественной среде обитания')
    if text == "покажи фледдера":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/2/2f/%D0%A4%D0%BB%D0%B5%D0%B4%D0%B5%D1%80%D0%93%D0%92.png', 'В народе говорят, что фледеры — умершие безбожники, после похорон ставшие вампирами и вышедшие из своих могил. Также считается, что фледеры предпочитают нападать на людей во сне и сосать их кровь. А среди кметов очень распространено поверье, что каждый, кого укусил фледер, сам становится вампиром. Совершенно очевидно, что подобное заявление является абсурдным.')
    if text == "покажи стрыгу":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/d/d1/%D0%A1%D1%82%D1%80%D1%8B%D0%B3%D0%B0%D0%93%D0%92.jpg', 'Принцесса выглядит как упырь, рявкнул Велерад, вскакивая со стула. Как самый что ни на есть упыристый упырь, о каком мне только доводилось слышать? В её высочестве, королевской доченьке, проклятом ублюдочном ублюдке, четыре локтя роста, она похожа на бочонок из-под пива, а пасть у нее от уха до уха, полная зубов, острых как кинжалы, у неё кроваво-красные зенки и рыжие патлы. Лапищи с когтями как у рыси, свисают до самой земли! Удивительно, как это мы ещё не начали посылать её миниатюры дружественным дворам! Принцессе, чтоб её чума взяла, уже четырнадцать годков, самое время выдать замуж за какого-нибудь принца!')
    if text == "покажи ивасика":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/d/d0/%D0%98%D0%B2%D0%B0%D1%81%D0%B8%D0%BA_TGG.jpeg', 'Молоко! Шишка! Улитка! Кролик! Телега! Корзинка! Пердёж! Ха! Как звучит!')
    if text == "покажи утопца":
        bot.send_photo(chat_id, 'https://static.wikia.nocookie.net/vedmak/images/f/f4/%D0%A3%D1%82%D0%BE%D0%BF%D0%B5%D1%86%D0%93%D0%92.png', 'Утопец видом своим напоминает труп, который долго лежал в воде. Кожа у него нездорового синего или зеленоватого оттенка, покрыта слизью, пахнет гнилью и илом. Потому считается, что утопцы, а также их более опасные родичи, такие как водяные, болотники или топляки, рождаются из тел несчастных, которые утонули на мелкой воде: заблудившихся путников, пьяных крестьян, сошедших с вьющейся среди болот тропинки, или детей, которые, играя, заплыли слишком далеко от берега.')
    if text == "покажи скального наездника":
        bot.send_photo(chat_id, 'https://cdn3.savepice.ru/uploads/2021/1/29/c06c2c6522554ad24a0f8bb3f812916e-full.jpg')
#   if text == "покажи паука":
#       bot.send_photo(chat_id, '')
#   if text == "покажи жука паука":
#       bot.send_photo(chat_id, '')

    names = ['Лютик', 'лютик', 'Гервант', 'Геральт', 'геральт', 'гервант', 'мастер', ' Мастер', 'ведьмак', 'Ведьмак', 'приблуда', 'Приблуда', 'ветер', 'Ветер', 'холодно', 'Холодно' ]
    for name in names:
        if name in message.text.lower():
                    bot.send_message(message.chat.id, text=get_random_quote())
    names1 = ['Гвинт', 'гвинт', 'карты', 'картишки', 'Карты', 'Картишки', 'ХВЭНДЭ', 'хвэндэ', 'Хвэндэ', 'Гвинтец', 'гвинтец', 'Партия', 'Партию', 'партия', 'партию', 'партейку', 'Партейку', 'Партейка', 'партейка']
    for name in names1:
        if name in message.text.lower():
                    bot.send_message(message.chat.id, 'Кто то тут сказал ГВИНТ?')
    names3 = ['Холера', 'холера']
    for name in names3:
        if name in message.text.lower():
                    bot.send_message(message.chat.id, 'Зараза')
    names4 = ['Зараза', 'зараза']
    for name in names4:
        if name in message.text.lower():
                    bot.send_message(message.chat.id, 'Холера')
    names5 = ['Ебнем', 'ебнем']
    for name in names5:
        if name in message.text.lower():
                    bot.send_message(message.chat.id, 'Na zdrowie!')
    names6 = ['Зелье', 'зелье','Зелья','зелья']
    for name in names6:
        if name in message.text.lower():
                    bot.send_message(message.chat.id, 'Зелья ебнул, как нахуячил им там!')
    names7 = ['Порталы', 'портал']
    for name in names7:
        if name in message.text.lower():
                    bot.send_message(message.chat.id, 'Ненавижу порталы')


    if message.text.lower() == 'каких существ ты знаешь?':
        bot.send_message(message.chat.id, 'В моем бестиарии есть информация о этих существах: Накер, Абая, Альгуль, Альп, Амбисфена, Арахноморф, Археспора, Архигрифон, Барбегаз, Баргест, Барт, Баньши, Белая дама, Бес, Брукса, Варг, Василиск, Вепрь, Виверна, Вий, Вилохвост, Вихт, Водная баба, Волк, Волколак, Высший вампир, Гаргулья, Гаркаин, Гарпия, Гернихора, Главоглаз, Гнилец, Голем, Голиаф, Гончая дикой охоты, Грайвер, Грифон, Гротник, Гуль, Гэль, Дагон, Дракон, Драуг, Драугир, Жагница, Утопец, Игоша, Катакан, Кащей, Кейран, Кикимора, Ключник, Кокатрикс, Котолак, Леший, Мантихор, Лесной тролль, Скальный наездник, Скальный Тролль, Йеннифер, Максим, Фледдер, Стрыга, Ивасик')
    if message.text.lower() == 'два':
        bot.send_message(message.chat.id, 'хера')
    if message.text.lower() == 'Два':
        bot.send_message(message.chat.id, 'хера')
    if message.text.lower() == '2':
        bot.send_message(message.chat.id, 'хера')
    if message.text.lower() == 'да':
        bot.send_message(message.chat.id, 'Пизда')
    if message.text.lower() == 'Да':
        bot.send_message(message.chat.id, 'Пизда')
    if message.text.lower() == 'покажи жопу':
        bot.send_message(message.chat.id, 'Нет')
    if message.text.lower() == 'покажи полужопие':
        bot.send_message(message.chat.id, 'Чирик вперед')








bot.polling()

