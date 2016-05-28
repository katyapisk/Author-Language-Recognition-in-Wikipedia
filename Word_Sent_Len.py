


import codecs
import re


def middle_len_word(file_name):
    f = codecs.open(file_name, 'r', 'utf-8-sig')
    text = f.read()
    arr = []
    words = text.split()
    for word in words:
        word = word.strip(u',.!?":;[]()')
        arr.append(word)
    c = 0
    l = 0
    c = c + len(arr)
    
    for i in range(len(arr)):
        l = l + len(arr[i])
        
    a = l/c
    print str(file_name) + u"Средняя длина слова:", a
    return a

def middle_len_sent(file_name):
    f = codecs.open(file_name, 'r', 'utf-8-sig')
    sum_sent = 0
    middle_len_sent = 0
    text = f.read()
    lines = text.split(u".")
    for line in lines:
        line = line.split(u' ')
        #print u"Длина предложения:", len(line)
        #print u"Кол-во предложений:", len(lines)
        sum_sent +=len(line)

    middle_len_sent = sum_sent/len(lines)
    print u'Средняя длина предложения:', middle_len_sent
    return middle_len_sent


a = middle_len_word(u'1.txt')
d = middle_len_sent(u'1.txt')
print "_____________________"
a = middle_len_word(u'2.txt')
d = middle_len_sent(u'2.txt')
print "_____________________"
a = middle_len_word(u'3.txt')
d = middle_len_sent(u'3.txt')
print "_____________________"
a = middle_len_word(u'4.txt')
d = middle_len_sent(u'4.txt')
print "_____________________"
a = middle_len_word(u'5.txt')
d = middle_len_sent(u'5.txt')
print "_____________________"
a = middle_len_word(u'6.txt')
d = middle_len_sent(u'6.txt')
print "_____________________"
a = middle_len_word(u'7.txt')
d = middle_len_sent(u'7.txt')
print "_____________________"
a = middle_len_word(u'8.txt')
d = middle_len_sent(u'8.txt')
print "_____________________"
a = middle_len_word(u'9.txt')
d = middle_len_sent(u'9.txt')
print "_____________________"
a = middle_len_word(u'10.txt')
d = middle_len_sent(u'10.txt')
print "_____________________"
a = middle_len_word(u'11.txt')
d = middle_len_sent(u'11.txt')
print "_____________________"
a = middle_len_word(u'12.txt')
d = middle_len_sent(u'12.txt')
print "_____________________"
a = middle_len_word(u'13.txt')
d = middle_len_sent(u'13.txt')
print "_____________________"
a = middle_len_word(u'14.txt')
d = middle_len_sent(u'14.txt')
print "_____________________"
a = middle_len_word(u'15.txt')
d = middle_len_sent(u'15.txt')
print "_____________________"
a = middle_len_word(u'16.txt')
d = middle_len_sent(u'16.txt')
print "_____________________"
a = middle_len_word(u'17.txt')
d = middle_len_sent(u'17.txt')
print "_____________________"
a = middle_len_word(u'18.txt')
d = middle_len_sent(u'18.txt')
print "_____________________"
a = middle_len_word(u'19.txt')
d = middle_len_sent(u'19.txt')
print "_____________________"
a = middle_len_word(u'20.txt')
d = middle_len_sent(u'20.txt')
print "_____________________"
a = middle_len_word(u'21.txt')
d = middle_len_sent(u'21.txt')
print "_____________________"
a = middle_len_word(u'22.txt')
d = middle_len_sent(u'22.txt')
print "_____________________"
a = middle_len_word(u'23.txt')
d = middle_len_sent(u'23.txt')
print "_____________________"
a = middle_len_word(u'24.txt')
d = middle_len_sent(u'24.txt')
print "_____________________"
a = middle_len_word(u'25.txt')
d = middle_len_sent(u'25.txt')
print "_____________________"
a = middle_len_word(u'26.txt')
d = middle_len_sent(u'26.txt')
print "_____________________"
a = middle_len_word(u'27.txt')
d = middle_len_sent(u'27.txt')
print "_____________________"
a = middle_len_word(u'28.txt')
d = middle_len_sent(u'28.txt')
print "_____________________"
a = middle_len_word(u'29.txt')
d = middle_len_sent(u'29.txt')
print "_____________________"
a = middle_len_word(u'30.txt')
d = middle_len_sent(u'30.txt')
print "_____________________"
a = middle_len_word(u'31.txt')
d = middle_len_sent(u'31.txt')
print "_____________________"
a = middle_len_word(u'32.txt')
d = middle_len_sent(u'32.txt')
print "_____________________"
a = middle_len_word(u'33.txt')
d = middle_len_sent(u'33.txt')
print "_____________________"
a = middle_len_word(u'34.txt')
d = middle_len_sent(u'34.txt')
print "_____________________"
a = middle_len_word(u'35.txt')
d = middle_len_sent(u'35.txt')
print "_____________________"
a = middle_len_word(u'36.txt')
d = middle_len_sent(u'36.txt')
print "_____________________"
a = middle_len_word(u'37.txt')
d = middle_len_sent(u'37.txt')
print "_____________________"
a = middle_len_word(u'38.txt')
d = middle_len_sent(u'38.txt')
print "_____________________"
a = middle_len_word(u'39.txt')
d = middle_len_sent(u'39.txt')
print "_____________________"
a = middle_len_word(u'40.txt')
d = middle_len_sent(u'40.txt')
print "_____________________"
a = middle_len_word(u'41.txt')
d = middle_len_sent(u'41.txt')
print "_____________________"
a = middle_len_word(u'42.txt')
d = middle_len_sent(u'42.txt')
print "_____________________"
a = middle_len_word(u'43.txt')
d = middle_len_sent(u'43.txt')
print "_____________________"
a = middle_len_word(u'44.txt')
d = middle_len_sent(u'44.txt')
print "_____________________"
a = middle_len_word(u'45.txt')
d = middle_len_sent(u'45.txt')
print "_____________________"
a = middle_len_word(u'46.txt')
d = middle_len_sent(u'46.txt')
print "_____________________"
a = middle_len_word(u'47.txt')
d = middle_len_sent(u'47.txt')
print "_____________________"
a = middle_len_word(u'48.txt')
d = middle_len_sent(u'48.txt')
print "_____________________"
a = middle_len_word(u'49.txt')
d = middle_len_sent(u'49.txt')
print "_____________________"
a = middle_len_word(u'50.txt')
d = middle_len_sent(u'50.txt')
print "_____________________"
a = middle_len_word(u'51.txt')
d = middle_len_sent(u'51.txt')
print "_____________________"
a = middle_len_word(u'52.txt')
d = middle_len_sent(u'52.txt')
print "_____________________"
a = middle_len_word(u'53.txt')
d = middle_len_sent(u'53.txt')
print "_____________________"
a = middle_len_word(u'54.txt')
print "_____________________"
d = middle_len_sent(u'54.txt')
print "_____________________"
a = middle_len_word(u'55.txt')
d = middle_len_sent(u'55.txt')
print "_____________________"
a = middle_len_word(u'56.txt')
d = middle_len_sent(u'56.txt')
print "_____________________"
a = middle_len_word(u'57.txt')
d = middle_len_sent(u'57.txt')
print "_____________________"
a = middle_len_word(u'58.txt')
d = middle_len_sent(u'58.txt')
print "_____________________"
a = middle_len_word(u'59.txt')
d = middle_len_sent(u'59.txt')
print "_____________________"
a = middle_len_word(u'60.txt')
d = middle_len_sent(u'60.txt')
print "_____________________"
a = middle_len_word(u'61.txt')
d = middle_len_sent(u'61.txt')
print "_____________________"
a = middle_len_word(u'62.txt')
d = middle_len_sent(u'62.txt')
print "_____________________"
a = middle_len_word(u'63.txt')
d = middle_len_sent(u'63.txt')
print "_____________________"
a = middle_len_word(u'64.txt')
d = middle_len_sent(u'64.txt')
print "_____________________"
a = middle_len_word(u'65.txt')
d = middle_len_sent(u'65.txt')
print "_____________________"
a = middle_len_word(u'66.txt')
d = middle_len_sent(u'66.txt')
print "_____________________"
a = middle_len_word(u'67.txt')
d = middle_len_sent(u'67.txt')
print "_____________________"
a = middle_len_word(u'68.txt')
d = middle_len_sent(u'68.txt')
print "_____________________"
a = middle_len_word(u'69.txt')
d = middle_len_sent(u'69.txt')
print "_____________________"
a = middle_len_word(u'70.txt')
d = middle_len_sent(u'70.txt')
print "_____________________"
a = middle_len_word(u'71.txt')
d = middle_len_sent(u'71.txt')
print "_____________________"
a = middle_len_word(u'72.txt')
d = middle_len_sent(u'72.txt')
print "_____________________"
a = middle_len_word(u'73.txt')
d = middle_len_sent(u'73.txt')
print "_____________________"
a = middle_len_word(u'74.txt')
d = middle_len_sent(u'74.txt')
print "_____________________"
a = middle_len_word(u'75.txt')
d = middle_len_sent(u'75.txt')
print "_____________________"
a = middle_len_word(u'76.txt')
d = middle_len_sent(u'76.txt')
print "_____________________"
a = middle_len_word(u'77.txt')
d = middle_len_sent(u'77.txt')
print "_____________________"
a = middle_len_word(u'78.txt')
d = middle_len_sent(u'78.txt')
print "_____________________"
a = middle_len_word(u'79.txt')
d = middle_len_sent(u'79.txt')
print "_____________________"
a = middle_len_word(u'80.txt')
d = middle_len_sent(u'80.txt')
print "_____________________"
a = middle_len_word(u'81.txt')
d = middle_len_sent(u'81.txt')
print "_____________________"
a = middle_len_word(u'82.txt')
d = middle_len_sent(u'82.txt')
print "_____________________"
a = middle_len_word(u'83.txt')
d = middle_len_sent(u'83.txt')
print "_____________________"
a = middle_len_word(u'84.txt')
d = middle_len_sent(u'84.txt')
print "_____________________"
a = middle_len_word(u'85.txt')
d = middle_len_sent(u'85.txt')
print "_____________________"
a = middle_len_word(u'86.txt')
d = middle_len_sent(u'86.txt')
print "_____________________"
a = middle_len_word(u'87.txt')
d = middle_len_sent(u'87.txt')
print "_____________________"
a = middle_len_word(u'88.txt')
d = middle_len_sent(u'88.txt')
print "_____________________"
a = middle_len_word(u'89.txt')
d = middle_len_sent(u'89.txt')
print "_____________________"
a = middle_len_word(u'90.txt')
d = middle_len_sent(u'90.txt')
print "_____________________"
a = middle_len_word(u'91.txt')
d = middle_len_sent(u'91.txt')
print "_____________________"
a = middle_len_word(u'92.txt')
d = middle_len_sent(u'92.txt')
print "_____________________"
a = middle_len_word(u'93.txt')
d = middle_len_sent(u'93.txt')
print "_____________________"
a = middle_len_word(u'94.txt')
d = middle_len_sent(u'94.txt')
print "_____________________"
a = middle_len_word(u'95.txt')
d = middle_len_sent(u'95.txt')
print "_____________________"
a = middle_len_word(u'96.txt')
d = middle_len_sent(u'96.txt')
print "_____________________"
a = middle_len_word(u'97.txt')
d = middle_len_sent(u'97.txt')
print "_____________________"
a = middle_len_word(u'98.txt')
d = middle_len_sent(u'98.txt')
print "_____________________"
a = middle_len_word(u'99.txt')
d = middle_len_sent(u'99.txt')
print "_____________________"
a = middle_len_word(u'100.txt')
d = middle_len_sent(u'100.txt')
print "_____________________"
a = middle_len_word(u'101.txt')
d = middle_len_sent(u'101.txt')
print "_____________________"
a = middle_len_word(u'102.txt')
d = middle_len_sent(u'102.txt')
print "_____________________"
a = middle_len_word(u'103.txt')
d = middle_len_sent(u'103.txt')
print "_____________________"
a = middle_len_word(u'104.txt')
d = middle_len_sent(u'104.txt')
print "_____________________"
a = middle_len_word(u'105.txt')
d = middle_len_sent(u'105.txt')
print "_____________________"
a = middle_len_word(u'106.txt')
d = middle_len_sent(u'106.txt')
print "_____________________"
a = middle_len_word(u'107.txt')
d = middle_len_sent(u'107.txt')
print "_____________________"
a = middle_len_word(u'108.txt')
d = middle_len_sent(u'108.txt')
print "_____________________"
a = middle_len_word(u'109.txt')
d = middle_len_sent(u'109.txt')
print "_____________________"
a = middle_len_word(u'110.txt')
d = middle_len_sent(u'110.txt')
print "_____________________"
a = middle_len_word(u'111.txt')
d = middle_len_sent(u'111.txt')
print "_____________________"
a = middle_len_word(u'112.txt')
d = middle_len_sent(u'112.txt')
print "_____________________"
a = middle_len_word(u'113.txt')
d = middle_len_sent(u'113.txt')
print "_____________________"
a = middle_len_word(u'114.txt')
d = middle_len_sent(u'114.txt')
print "_____________________"
a = middle_len_word(u'115.txt')
d = middle_len_sent(u'115.txt')
print "_____________________"
a = middle_len_word(u'116.txt')
d = middle_len_sent(u'116.txt')
print "_____________________"
a = middle_len_word(u'117.txt')
d = middle_len_sent(u'117.txt')
print "_____________________"
a = middle_len_word(u'118.txt')
d = middle_len_sent(u'118.txt')
print "_____________________"
a = middle_len_word(u'119.txt')
d = middle_len_sent(u'119.txt')
print "_____________________"
a = middle_len_word(u'120.txt')
d = middle_len_sent(u'120.txt')
print "_____________________"
a = middle_len_word(u'121.txt')
d = middle_len_sent(u'121.txt')
print "_____________________"
a = middle_len_word(u'122.txt')
d = middle_len_sent(u'122.txt')
print "_____________________"
a = middle_len_word(u'123.txt')
d = middle_len_sent(u'123.txt')
print "_____________________"
a = middle_len_word(u'124.txt')
d = middle_len_sent(u'124.txt')
print "_____________________"
a = middle_len_word(u'125.txt')
d = middle_len_sent(u'125.txt')
print "_____________________"
a = middle_len_word(u'126.txt')
d = middle_len_sent(u'126.txt')
print "_____________________"
a = middle_len_word(u'127.txt')
d = middle_len_sent(u'127.txt')
print "_____________________"
a = middle_len_word(u'128.txt')
d = middle_len_sent(u'128.txt')
print "_____________________"
a = middle_len_word(u'129.txt')
d = middle_len_sent(u'129.txt')
print "_____________________"
a = middle_len_word(u'130.txt')
d = middle_len_sent(u'130.txt')
print "_____________________"
a = middle_len_word(u'131.txt')
d = middle_len_sent(u'131.txt')
print "_____________________"
a = middle_len_word(u'132.txt')
d = middle_len_sent(u'132.txt')
print "_____________________"
a = middle_len_word(u'133.txt')
d = middle_len_sent(u'133.txt')
print "_____________________"
a = middle_len_word(u'134.txt')
d = middle_len_sent(u'134.txt')
print "_____________________"
a = middle_len_word(u'135.txt')
d = middle_len_sent(u'135.txt')
print "_____________________"
a = middle_len_word(u'136.txt')
d = middle_len_sent(u'136.txt')
print "_____________________"
a = middle_len_word(u'137.txt')
d = middle_len_sent(u'137.txt')
print "_____________________"
a = middle_len_word(u'138.txt')
d = middle_len_sent(u'138.txt')
print "_____________________"
a = middle_len_word(u'139.txt')
d = middle_len_sent(u'139.txt')
print "_____________________"
a = middle_len_word(u'140.txt')
d = middle_len_sent(u'140.txt')
print "_____________________"
a = middle_len_word(u'141.txt')
d = middle_len_sent(u'141.txt')
print "_____________________"
a = middle_len_word(u'142.txt')
d = middle_len_sent(u'142.txt')
print "_____________________"
a = middle_len_word(u'143.txt')
d = middle_len_sent(u'143.txt')
print "_____________________"
a = middle_len_word(u'144.txt')
d = middle_len_sent(u'144.txt')
print "_____________________"
a = middle_len_word(u'145.txt')
d = middle_len_sent(u'145.txt')
print "_____________________"
a = middle_len_word(u'146.txt')
d = middle_len_sent(u'146.txt')
print "_____________________"
a = middle_len_word(u'147.txt')
d = middle_len_sent(u'147.txt')
print "_____________________"
a = middle_len_word(u'148.txt')
d = middle_len_sent(u'148.txt')
print "_____________________"
a = middle_len_word(u'149.txt')
d = middle_len_sent(u'149.txt')
print "_____________________"
a = middle_len_word(u'150.txt')
d = middle_len_sent(u'150.txt')
print "_____________________"
a = middle_len_word(u'151.txt')
d = middle_len_sent(u'151.txt')
print "_____________________"
a = middle_len_word(u'152.txt')
d = middle_len_sent(u'152.txt')
print "_____________________"
a = middle_len_word(u'153.txt')
d = middle_len_sent(u'153.txt')
print "_____________________"
a = middle_len_word(u'154.txt')
print "_____________________"
d = middle_len_sent(u'154.txt')
print "_____________________"
a = middle_len_word(u'155.txt')
d = middle_len_sent(u'155.txt')
print "_____________________"
a = middle_len_word(u'156.txt')
d = middle_len_sent(u'156.txt')
print "_____________________"
a = middle_len_word(u'157.txt')
d = middle_len_sent(u'157.txt')
print "_____________________"
a = middle_len_word(u'158.txt')
d = middle_len_sent(u'158.txt')
print "_____________________"
a = middle_len_word(u'159.txt')
d = middle_len_sent(u'159.txt')
print "_____________________"
a = middle_len_word(u'160.txt')
d = middle_len_sent(u'160.txt')
print "_____________________"
a = middle_len_word(u'161.txt')
d = middle_len_sent(u'161.txt')
print "_____________________"
a = middle_len_word(u'162.txt')
d = middle_len_sent(u'162.txt')
print "_____________________"
a = middle_len_word(u'163.txt')
d = middle_len_sent(u'163.txt')
print "_____________________"
a = middle_len_word(u'164.txt')
d = middle_len_sent(u'164.txt')
print "_____________________"
a = middle_len_word(u'165.txt')
d = middle_len_sent(u'165.txt')
print "_____________________"
a = middle_len_word(u'166.txt')
d = middle_len_sent(u'166.txt')
print "_____________________"
a = middle_len_word(u'167.txt')
d = middle_len_sent(u'167.txt')
print "_____________________"
a = middle_len_word(u'168.txt')
d = middle_len_sent(u'168.txt')
print "_____________________"
a = middle_len_word(u'169.txt')
d = middle_len_sent(u'169.txt')
print "_____________________"
a = middle_len_word(u'170.txt')
d = middle_len_sent(u'170.txt')
print "_____________________"
a = middle_len_word(u'171.txt')
d = middle_len_sent(u'171.txt')
print "_____________________"
a = middle_len_word(u'172.txt')
d = middle_len_sent(u'172.txt')
print "_____________________"
a = middle_len_word(u'173.txt')
d = middle_len_sent(u'173.txt')
print "_____________________"
a = middle_len_word(u'174.txt')
d = middle_len_sent(u'174.txt')
print "_____________________"
a = middle_len_word(u'175.txt')
d = middle_len_sent(u'175.txt')
print "_____________________"
a = middle_len_word(u'176.txt')
d = middle_len_sent(u'176.txt')
print "_____________________"
a = middle_len_word(u'177.txt')
d = middle_len_sent(u'177.txt')
print "_____________________"
a = middle_len_word(u'178.txt')
d = middle_len_sent(u'178.txt')
print "_____________________"
a = middle_len_word(u'179.txt')
d = middle_len_sent(u'179.txt')
print "_____________________"
a = middle_len_word(u'180.txt')
d = middle_len_sent(u'180.txt')
print "_____________________"
a = middle_len_word(u'181.txt')
d = middle_len_sent(u'181.txt')
print "_____________________"
a = middle_len_word(u'182.txt')
d = middle_len_sent(u'182.txt')
print "_____________________"
a = middle_len_word(u'183.txt')
d = middle_len_sent(u'183.txt')
print "_____________________"
a = middle_len_word(u'184.txt')
d = middle_len_sent(u'184.txt')
print "_____________________"
a = middle_len_word(u'185.txt')
d = middle_len_sent(u'185.txt')
print "_____________________"
a = middle_len_word(u'186.txt')
d = middle_len_sent(u'186.txt')
print "_____________________"
a = middle_len_word(u'187.txt')
d = middle_len_sent(u'187.txt')
print "_____________________"
a = middle_len_word(u'188.txt')
d = middle_len_sent(u'188.txt')
print "_____________________"
a = middle_len_word(u'189.txt')
d = middle_len_sent(u'189.txt')
print "_____________________"
a = middle_len_word(u'190.txt')
d = middle_len_sent(u'190.txt')
print "_____________________"
a = middle_len_word(u'191.txt')
d = middle_len_sent(u'191.txt')
print "_____________________"
a = middle_len_word(u'192.txt')
d = middle_len_sent(u'192.txt')
print "_____________________"
a = middle_len_word(u'193.txt')
d = middle_len_sent(u'193.txt')
print "_____________________"
a = middle_len_word(u'194.txt')
d = middle_len_sent(u'194.txt')
print "_____________________"
a = middle_len_word(u'195.txt')
d = middle_len_sent(u'195.txt')
print "_____________________"
a = middle_len_word(u'196.txt')
d = middle_len_sent(u'196.txt')
print "_____________________"
a = middle_len_word(u'197.txt')
d = middle_len_sent(u'197.txt')
print "_____________________"
a = middle_len_word(u'198.txt')
d = middle_len_sent(u'198.txt')
print "_____________________"
a = middle_len_word(u'199.txt')
d = middle_len_sent(u'199.txt')
print "_____________________"
a = middle_len_word(u'200.txt')
d = middle_len_sent(u'200.txt')

##b = sluz_words(u'100.txt')

##c = lexicon(u'77.txt')



