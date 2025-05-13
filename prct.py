# s = str(input())
# temp = ''
# cnt = 1
# if len(s) == 1:
#     print(s[0]+'1')
# for i in range(1, len(s)):
#     if s[i-1] == s[i]:
#         cnt += 1
#         if i == len(s)-1:
#             temp += s[i-1] + str(cnt)
#     else:
#         if i == len(s)-1:
#             temp += s[i-1] + str(cnt) + s[i] + '1'
#         else:
#             temp += s[i-1] + str(cnt)
#             cnt = 1
# print(temp)




# st = ''
# s = [int(i) for i in input().split()]
# lst = [] 
# for i in range(len(s)):
#     if i == 0:
#         try:
#             lst.append(s[i+1] + s[-1])
#         except:
#             print(s[i])
#     elif i == len(s)-1:
#         lst.append(s[i-1] + s[0])
#     else:
#         lst.append(s[i-1] + s[i+1])
# if lst != []:
#     for i in lst:
#         st += str(i) + ' '
#     print(st)


# st = ''
# a = set()
# s = [int(i) for i in input().split()]
# for i in s:
#     if s.count(i) > 1:
#         a.add(i)
# for i in a:
#     st += str(i) + ' '
# print(st)


# i = int(input())
# sums = i**2
# while i != 0:
#     num = int(input())
#     sums += num**2
#     i += num
# print(sums)


    
# n = int(input())
# k = 0
# lst = []
# for i in range(1, n+1):
#     k += 1
#     for j in range(1, k+1):
#         lst.append(i)
# print(*lst[:n])
# for i in lst[:n]:
#     print(i, end = ' ')

# mas = []
# lst = [int(i) for i in input().split()]
# x = int(input())
# if x in lst:
#     for i in range(len(lst)):
#         if lst[i] == x:
#             mas.append(i)
#     print(*mas)
# else:
#     print('Отсутствует')


# st = input()
# matrix = []
# new_matrix = []
# matrix.append(st.split())
# while st != 'end':
#     st = input()
#     matrix.append(st.split())
# matrix = matrix[:-1]
# i = -1
# j = -1
# for row in matrix:
#     j = -1
#     i += 1
#     for num in row:
#         j += 1
#         if i != len(matrix)-1 and j != len(matrix[i])-1:
#             new_matrix.append(int(matrix[i-1][j]) + int(matrix[i+1][j]) + int(matrix[i][j-1]) + int(matrix[i][j+1]))
#         if i != len(matrix)-1 and j == len(matrix[i])-1:
#             new_matrix.append(int(matrix[i-1][j]) + int(matrix[i+1][j]) + int(matrix[i][j-1]) + int(matrix[i][0]))
#         if i == len(matrix)-1 and j != len(matrix[i])-1:
#             new_matrix.append(int(matrix[i-1][j]) + int(matrix[0][j]) + int(matrix[i][j-1]) + int(matrix[i][j+1]))
#         if i == len(matrix)-1 and j == len(matrix[i])-1:
#             new_matrix.append(int(matrix[i-1][j]) + int(matrix[0][j]) + int(matrix[i][j-1]) + int(matrix[i][0]))
# print(new_matrix)
# n = 0
# for k in range(1, i+2):
#     print(*new_matrix[n:n+len(matrix[i])])
#     n += len(matrix[i])




# l = [2, 4, 6, 8]
# def modify_list(l):
#     for i in l[::-1]:
#         if i % 2 != 0:
#             l.remove(i)
#     for i in range(len(l)):
#         l.insert(i, l[i]//2)
#         l.remove(l[i+1])
# modify_list(l)
# print(l)



# key = 1
# value = -1
# d = {}
# def update_dictionary(d, key, value):
#     if key in d:
#         d[key].append(value)
#     else:
#         try:
#             d[2*key].append(value)
#         except:
#             d[2*key] = [value]
# update_dictionary(d, key, value)
# print(d)




# s = str(input())
# s = s.upper().split()
# words_count = {}
# for word in s:
#     words_count[word] = s.count(word)
# for word in words_count:
#     print(word,words_count[word])



# xt = int(input('xt'))
# a = int(input('a'))
# xc = int(input('xc'))
# r = int(input('r'))

# if xc-r > xt + a/2 or xc+r < xt - a/2:
#  print("фигуры не пересекаются")
# if xc + r == xt-a/2 or xt + a/2 == xc - r:
#  print("касаются")
# if (xt - a/2 < xc + r and xt + a/2 > xc + r) or (xc - r < xt + a/2 and xt - a/2 < xc - r):
#  print("пересекаются")
# if ((xt - a/2 > xc - r) and (xc + r > xt + a/2) and (r >= (a*(3**0.5)/2))):
#  print("треугольник в полукруге")
# if ((xt - a/2 < xc - r) and (xt + a/2 > xc + r) and (r <= (a*(3**0.5)/2))):
#  print("полукруг в треугольнике")


# a = 0
# s1 = '123'
# s = '33644764876431783266621612005107543310302148460680063906564769974680081442166662368155595513633734025582065332680836159373734790483865268263040892463056431887354544369559827491606602099884183933864652731300088830269235673613135117579297437854413752130520504347701602264758318906527890855154366159582987279682987510631200575428783453215515103870818298969791613127856265033195487140214287532698187962046936097879900350962302291026368131493195275630227837628441540360584402572114334961180023091208287046088923962328835461505776583271252546093591128203925285393434620904245248929403901706233888991085841065183173360437470737908552631764325733993712871937587746897479926305837065742830161637408969178426378624212835258112820516370298089332099905707920064367426202389783111470054074998459250360633560933883831923386783056136435351892133279732908133732642652633989763922723407882928177953580570993691049175470808931841056146322338217465637321248226383092103297701648054726243842374862411453093812206564914032751086643394517512161526545361333111314042436854805106765843493523836959653428071768775328348234345557366719731392746273629108210679280784718035329131176778924659089938635459327894523777674406192240337638674004021330343297496902028328145933418826817683893072003634795623117103101291953169794607632737589253530772552375943788434504067715555779056450443016640119462580972216729758615026968443146952034614932291105970676243268515992834709891284706740862008587135016260312071903172086094081298321581077282076353186624611278245537208532365305775956430072517744315051539600905168603220349163222640885248852433158051534849622434848299380905070483482449327453732624567755879089187190803662058009594743150052402532709746995318770724376825907419939632265984147498193609285223945039707165443156421328157688908058783183404917434556270520223564846495196112460268313970975069382648706613264507665074611512677522748621598642530711298441182622661057163515069260029861704945425047491378115154139941550671256271197133252763631939606902895650288268608362241082050562430701794976171121233066073310059947366875'
# for i in range(len(s)):
#     a += int(s[i])
# print(a % 3)





# s = str(input())
# temp = ''
# cnt = 1
# if len(s) == 1:
#     print(s[0]+'1')
# for i in range(1, len(s)):
#     if s[i-1] == s[i]:
#         cnt += 1
#         if i == len(s)-1:
#             temp += s[i-1] + str(cnt)
#     else:
#         if i == len(s)-1:
#             temp += s[i-1] + str(cnt) + s[i] + '1'
#         else:
#             temp += s[i-1] + str(cnt)
#             cnt = 1
# print(temp)




# with open('C:/Users/Home-PC/Downloads/dataset_3363_2 (3).txt') as a:
#     sr = a.readline().strip()[::-1]
#     a.close()
# temp = ''
# i = 0
# while i < len(sr):
#     if sr[i] in '1234567890':
#         cnt = ''
#         while sr[i] in '1234567890':
#             cnt += sr[i]
#             i += 1
#     else:
#         temp += sr[i] * int(cnt[::-1])
#         i += 1
# with open('C:/Users/Home-PC/Downloads/output.txt', 'w') as b:
#     b.write(temp[::-1])
#     b.close()
        
# with open('C:/Users/Home-PC/Downloads/dataset_3363_2 (3).txt') as a:
# 	j = a.readline().strip()
# 	s = a.readline().strip()
# c = 0
# for i in s:
#     if i in j:
#         c += 1
# with open('C:/Users/Home-PC/Downloads/output.txt', 'w') as b:
# 	b.write(str(c))

print(11/13)
print(2/3)
            



#Большие буквы меньше всех малых
#Цифры меньше букв(и малых и больших)
