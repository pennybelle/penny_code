# # # # logarithm function
# # # # x = integer being altered logarithmically
# # # # l = rate at which x changes logarithmically in percentage (decimal)
# # # # n = number of instances to run the logarithmic recursion

# # # def logarithm(x, l, n):
# # #     if n == 1: return x
# # #     print(x)
# # #     return logarithm(x*l, l, n-1)

# # # def l(x, l, n):
# # #     return x*(n**l)

# # # # print(l(55000, 0.03, 72))

# # # # print(logarithm(100, 0.125, 4))

# # # ######################################################################

# # # # For each year t, the number of trees in Forest A is represented by 
# # # # the function A(t)=74(1.025)t. In a neighboring forest, the number 
# # # # of trees in Forest B is represented by the function B(t)=94(1.029)t.
# # # # Assuming the population growth models continue to represent the 
# # # # growth of the forests, which forest will have a greater number of 
# # # # trees after 20 years? By how many?

# # # # exponential growth function
# # # # trees = number of trees
# # # # growth_rate = percent rate at which trees grow
# # # # total_years = number of years to check growth rate
# # # # year = current year out of total_years

# # # def exponent(trees, growth_rate, year):
# # #     print(year, trees)
# # #     if year == 0: return trees
# # #     return exponent(trees*growth_rate, 
# # #                     growth_rate, year-1)

# # # # print(f'A = {exponent(74, 1.025, 20):,}')
# # # # print(f'B = {exponent(94, 1.029, 20):,}')

# # # # B has more trees within 20 years
# # # # A = rounded to 121 trees
# # # # B = rounded to 167 trees



# # # # exponential function
# # # # E(i) = x(r)^i

# # # # x = integer or float
# # # # r = percent rate at which x changes
# # # # i = total iterations of the function

# # # def e_recursive(x, r, i): # doesnt work for negative i
# # #     if i == 0: return x
# # #     return e_recursive(x*r, r, i-1)

# # # def exponent(x, r, i): # works for negative or positive i
# # #     return x*(r**i)

# # # # print(exponent(1.39, 1.006, 21))

# # # import numpy as np
# # # from scipy.interpolate import make_interp_spline
# # # import matplotlib.pyplot as plt 

# # # def base_e(n=1_000_000_000):
# # #     return (1+(1/n))**n

# # # def plot_base_e(transform=1, rng=11):
# # #     x_list = []
# # #     y_list = []

# # #     for n in range(1, rng):
# # #         x_list.append(n)
# # #         y_list.append(base_e(n*transform))

# # #     x_array = np.array(x_list)
# # #     y_array = np.array(y_list)
# # #     spline = make_interp_spline(x_array, y_array)
# # #     x = np.linspace(x_array.min(), x_array.max(), 500)
# # #     y = spline(x)

# # #     plt.plot(x, y)
# # #     plt.title("Euler's Constant | e = (1+(1/n))^n | The Logarithmic Curve Of e")
# # #     plt.xlabel("X")
# # #     plt.ylabel("Y")
# # #     plt.show()

# # # plot_base_e(transform=0.001, rng=10000)

# # # # print(points)

# # # # print(base_e())

# # # def e(x):
# # #     return base_e()**x

# # # # print(e(167))

# # # # for x in range(10):
# # # #     print(x, e(x))

# # # def decay(a, e, r, t):
# # #     return a*(e**(r*t))

# # # # print(f'{decay(220, base_e(), -0.173, 365):,}')

# # # # print(e(-0.7))

# # # # print(base_e(1_000_000_000))

# # # # print(e_recursive(30, 2, 3))
# # # # print(exponent(30, 2, 3))

# # # # print(exponent(8, 1.1, 4-6))

# # # # for i in range(20):
# # # #     print(exponent(5, 4, i) - 10)

# # # # print(exponent(-0.5, 0.5, -7)+4)

# # # # xs = (round(x/10) for x in range(1000))
# # # # for i in xs:
# # # #     print(round(i/10))
# # # #     e = e(110000, i, 20)
# # # #     if e == 146000: print(e)

# # # def g(a, e, r, t):
# # #     return a*(e**(r*t))

# # # def g_business(P, n, r, t):
# # #     return P*((1+(r/n))**t)

# # # # print(g_business(10200, 12, 0.04, 132))

# # # def f(b, x):
# # #     return b**x

# # # # plots_pos = []
# # # # plots_neg = []

# # # # for x in range(10):
# # # #     plots_pos.append((x, f(4, x)))
# # # # for x in range(0, -10, -1):
# # # #     plots_neg.append((x, f(4, x)))

# # # # print(plots_pos)
# # # # print(plots_neg)


# # import googletrans
# # from transformers import pipeline
# # # sentiment_pipeline = pipeline('sentiment-analysis')
# # # data = [
# # #     '''
# # #     does anyone need fridge magnets i have four boxes i dont need
# # #     '''
# # # ]
# # # print(sentiment_pipeline(data))

# # # question_bot = pipeline('question-answering')

# # # data = 'こんにちは'

# # # gl = googletrans.LANGUAGES
# # # gl_codes = googletrans.LANGCODES

# # # translator = googletrans.Translator()
# # # detected = translator.detect(data)
# # # lang = detected.lang
# # # print(gl[lang])

# # # if not gl[lang] in 'en':
# # #     translation = pipeline(f'translation_{lang}_to_en')
# # #     print(translation(data))


# # from transformers import pipeline

# # music_generator = pipeline(task="text-to-audio", model="facebook/musicgen-small", framework="pt")

# # # diversify the music generation by adding randomness with a high temperature and set a maximum music length
# # generate_kwargs = {
# #     "do_sample": True,
# #     "temperature": 0.7,
# #     "max_new_tokens": 35,
# # }

# # outputs = music_generator("lofi beats to study/relax to", generate_kwargs=generate_kwargs)

# # import matplotlib.pyplot as plt
# # from time import time
# # from sys import setrecursionlimit
# # setrecursionlimit(10_000)

# # class cg():
# #     def __init__(self):
# #         self.global_cache = {}


# #     def collatz(self, x, seq_len=0): # TODO: recursively build cache up backwards
# #         if x in self.global_cache.keys():  
# #             return seq_len + self.global_cache[x]
# #         elif x == 1: # ends the recursion, returns the score (how many steps)
# #             return seq_len
# #         # elif x % 2 == 0: # if even, divide by 2
# #         #     x //= 2
# #         # else: # if odd, multiply by 3 and add 1
# #         #     x = x * 3 + 1
# #         # # TODO: LOOK AT THIS SHIT, I'M SO GOOD, THIS IS COOL
# #         # self.global_cache[x] = seq_len
# #         # print(self.global_cache)

# #         return self.collatz(lambda x: x//2 if x%2 else x*3+1, seq_len+1)
    
# # print(cg().collatz(1, 100000))



# from time import time
# from matplotlib import pyplot as plt


# class Collatz(dict):
    
#     def __getitem__(self, key):
#         val = self.get(key, None)
#         if val is None:
#             res = self.calc_steps(key)
#             self[key] = res
#             return res
#         else:
#             return val
    
#     def calc_steps(self, x, steps=0):
#         if x == 1:
#             return steps
#         if x % 2:
#             x = x * 3 + 1
#         else:
#             x //= 2
#         steps += 1
        
#         stored = self.get(x, None)
#         if stored is None:
#             return self.calc_steps(x, steps)
#         else:
#             return steps + stored


# def plotter(title, xlab, xpts, ylab, ypts):
#     plt.title(title)
#     plt.xlabel(xlab)
#     plt.ylabel(ylab)
#     plt.plot(xpts, ypts, marker='*', markersize=2, linestyle='')
#     plt.show()


# start = time()
# c = Collatz()
# for x in range(1, 10_000_001):
#     s = c[x]
# print(f'Duration of calculation: {time() - start} sec')

# title = f'Collatz Stopping Time Analysis (max={x:,})'
# xlab = 'Stopping Time'
# ylab = 'Frequency'
# points = {}
# for v in c.values():
#     points[v] = points.setdefault(v, 0) + 1
# plotter(title, xlab, points.keys(), ylab, points.values())

# print(12880%360)


# # r = Radius
# # A = Angle
# def ArcLength(r, A, radian=False):
#     return (r*(A*(0.017453 if radian else 1)))

# # print(ArcLength((3.1416/3), (18/2)))
# print(ArcLength(3, (3.1416/6)))

# def ArcArea(r, A, radian=False):
#     return (r**2)*((A*(0.017453 if radian else 1))/2)

# print(ArcArea(18/2, 3.1416/3))

# def FuckYouCasey(x):
#     if not x == 4: return (x**2)-(7*x-8)/(x-4)

# # # print(FuckYouCasey(2))

# strt = -10000
# rng = 10000

# x = [x*.001 if not x==4 else x for x in range(strt, rng)]
# y = [FuckYouCasey(y*.001) if not y==4 else y for y in range(strt, rng)]

# # print(zip(x, y))

# import matplotlib.pyplot as plt

# # x = [0, 1, 2]
# # y = [-2, 0.666, 7]

# def plotter(x, y):
#     # plt.title(title)
#     # plt.xlabel(xlab)
#     # plt.ylabel(ylab)
#     plt.plot(x, y)
#     # plt.savefig(title+'.png')
#     plt.show()

# plotter(x, y)

# def A(t):
#     return 195*(1.21**t)

# print(A(5))

# import googletrans
# print(googletrans.LANGUAGES)
# print(googletrans.LANGCODES)

# print(-1**5)

# string = ''

# is_string = 'Shell' if string == 'Shell' else True if string else False

# print(is_string)

hanzi = '''
的是不我一有大在人了中到资要可以这个你会好为上来就学交也用能如文时没说他看提那问生过下请天们所多麽小
想得之还电出工对都机自後子而讯站去心只家知国台很信成章何同道地发法无然但吗当於本现年前真最和新因果定
意情点题其事方清科样些吧叁此位理行作经者什谢名日正华话开实再城爱与二动比高面又车力或种像应女教分手打
已次长太明己路起相主关凤间呢觉该十外凰友才民系进使她着各少全两回加将感第性球式把被老公龙程论及别给听
水重体做校里常东风您湾啦见解等部原月美先管区错音否啊找网乐让通入期选较四场由书它快从欢数表怎至立内合
目望认几社告更版度考喜头难光买今身许弟若算记代统处完号接言政玩师字并男计谁山张党每且结改非星连哈建放
直转报活设变指气研陈试西五希取神化物王战近世受义反单死任跟便空林士台却北队功必声写平影业金档片讨色容
央妳向市则员兴利强白价安呵特思叫总办保花议传元求份件持万未究决投哪喔笑猫组独级走支曾标流竹兄阿室卡马
共需海口门般线语命观视朋联参格黄钱修失儿住八脑板吃另换即象料录拿专远速基帮形确候装孩备歌界除南器画诉
差讲类英案带久乎掉迷量引整似耶奇制边型超识虽怪飞始品运赛费梦故班权破验眼满念造军精务留服六图收舍半读
愿李底约雄课答令深票达演早卖棒够黑院假曲火准百谈胜碟术推存治离易往况晚示证段导伤调团七永刚哥甚德杀怕
包列概照夜排客绝软商根九切条集千落竟越待忘尽据双供称座值消产红跑嘛园附硬云游展执闻唱育斯某技唉息苦质
油救效须介首助职例热毕节害击乱态嗯宝倒注停古输规福亲查复步举鱼断终轻环练印随依趣限响省局续司角简极干
篇罗佛克阳武疑送拉习源免志鸟烦足馆仍低广土呀楼坏兵显率圣码众争初误楚责境野预具智压系青贵顺负魔适哇测
慢怀懂史配呜味亦医迎舞恋细灌甲帝句属灵评骑宜败左追狂敢春狗际遇族群痛右康佳杨木病戏项抓徵善官护博补石
尔营历只按妹里编岁择温守血领寻田养谓居异雨止跳君烂优封拜恶啥浪核聊急状陆激模攻忙良剧牛垒增维静阵抱势
严词亚夫签悲密幕毒厂爽缘店吴兰睡致江宿翻香蛮警控赵冷威微坐周宗普登母络午恐套巴杂创旧辑幸剑亮述堂酒丽
牌仔脚突搞父俊暴防吉礼素招草周房餐虑充府背典仁漫景绍诸琴忆援尤缺扁骂纯惜授皮松委湖诚麻置靠继判益波姐
既射欲刻堆释含承退莫刘昨旁纪赶制尚艺肉律铁奏树毛罪笔彩注归弹虎卫刀皆键售块险荣播施铭罗汉赏欣升叶萤载
嘿弄钟付寄鬼哦灯呆洋嘻布磁荐检派构妈蓝贴猪策纸暗巧努雷架享宣逢均担启济罢呼划伟岛歉郭训穿详沙督梅顾敌
协轮略慧幻脸短鹰冲朝忍游河批混窗乡蛋季散册弃熟奖唯藏婚镜紧猜喝尊乾县伯偏偷秋层颗食淡申冠衣仅帐赞购犯
敬勇洲束斗徒嘉柔绩笨拥漂狮诗围乖孤姓吸私避范抗盖祝序晓富译巨秀馀辉插察庆积愈端移宫挥爆港雪硕借帅丢括
挂盘偶末厅朱凡惊货灭醒虚瑞拍遗忠志透烈银顶雅诺圆熊替休材挑侠鸡累互掌念米伴辅降豪篮洗健饭怜疯宏困址兮
操临骗咧药绿尼蔡玉辛辈敏减彼街聚郎泡恨苏缩枢碰采默婆股童符抽获宇废赢肯砍钢欧届禁苍脱渐仙泪触途财箱厌
籍冰涛订哭稳析杰坚桥懒贤丝露森危占茶惯尘布爸阶夏谊瓶哩惨械隐丰旅椰亡汽贝娘寒遭吹暑珍零刊邮村乃予赖摇
纳烟伦尾狼浮骨杯隔洪织询振忽索惠峰席喵胡租款扰企刺芳鼠折频冒痴阴哲针伊寂嘴倚霸扬沉悔虫菜距复鼓摩郑庄
副页烧弱暂剩豆探耐祖遍萧握愁龟哀发延库隆盟傻眉固秘卷搭昭宁托辩覆吵耳閒拨沈升胖丁妙残违稍媒忧销恩颜船
奈映井拼屋乘京藉洞川宪拟寝塞倍户摆桌域劳赚皇逃鸿横牙拖齐农滚障搬奶乌了松戴谱酷棋吓摸额瓜役怨染迫醉锁
震床闹佩牠徐尺干潮帽盛孙屁净凯撞迴损伙牵厉惑羊冬桃舰眠伍溪飘泰宋圈竞闪纵崇滑乙俗浅莲紫沟旋摄聪毁庭麦
描妨勒仪陪榜板慕耀献审蟹巷谅姊逐踏岸葛卧洽寞邦藤拳阻蝎面殊凭拒池邪航驱裁翔填奥函镇丌宽颇枪遥穹啪阅锋
砂恭塔贺魂睛逸旗萨丸厚斋芬革庸舒饮闭励顿仰阁孟昌访绪裕勿州阐抢扫糊宙尝菩赐赤喊盗擎劝奋慈尽污狐罚幽准
兼尖彰灰番衡鲜扩毫夸炮拆监栏迟证倾郁汪纷托漏渡姑秒吾窝辆龄跌浩肥兽煞抹酸税陷谷冲杜胸甘胞诞岂辞墙凉碎
晶邱逻脆喷玫娃培咱潜祥筑孔柏叭邀犹妻估荒袋径垃傲淑圾旦亿截币羽妇泥欺弦筹舍忌串伸喇耻繁廖逛劲臭鲁壮捕
穷拔于丑莉糟炸坡蒙腿坦怒甜韩缓悉扯割艾胎恒玲朵泉汤猛驾幼坪巫弯胆昏鞋怡吐唐悠盾跃侵丹鑑泽薪逝彦后召吕
碧晨辨植痴瑰钓轩勤珠浓悟磨剪逼玄暖躲洛症挡敝碍亨逊蜜盼姆赋彬壁缴捷乏戒憾滴桑菲嫌愉爬恼删叹抵棚摘蒋箭
夕翁牲迹勉莱洁贪恰曰侨沧咖唷扣采奔泳迹涯夺抄疗署誓盃骚翼屠咪雾涉锺踢谋牺焦涵础绕俱霹坜唬氏彻吝曼寿粉
廉炎祸耗炮啡肚贡鼻挖貌捐融筋云稣捡饱铃雳鸣奉燃饰绘黎卷恢瞧茫幅迪柳瑜矛吊侯玛撑薄敦挤墨琪凌侧枫嗨梯梁
廷儒咬岚览兔怖稿齿狱爷迈闷乔姿踪宾家弘韵岭咦裤壳孝仇誉妮惧促驶疼凶粗耍糕仲裂吟陀赌爵哉亏锅刷旭晴蝶阔
洩顽牧契轰羞拾锦逆堕夹枝瓦舟悦惹疏锐翘哎综纲扇驻屏堪弥贯愚抬喂靖狠饼凝邻擦滋坤蛙灾莎毅卒汝征赠斗抛秦
辱涂披允侦欲夥朗笛劫魅钦慰荷挺矣迅禅迁鹿秤彭肩赞丙鹅痕液涨巡烤贱丈趋沿滥措么扭捉碗炉脏叔秘腰漠翅余胶
妥谣缸芒陵雯轨虾寸呦洒贞蜂钻厕鹤摔盒虫氛悄霖愧斜尸循俩堡旺恶叉燕津臣丧茂椅缠刑脉杉泊撒递疲杆趁欠盈晃
蛇牡慎粒系倦溜遵腐疾鸭璃牢劣患祂呈浑剂妖玻塑飙伏弊扮侬渴歪苗汗陶栋琳蓉埋叡澎并泣腾柯催畅勾樱阮斥搜踩
返坛垂唤储贩匆添坑柴邓糖昆暮柜娟腹煮泛稀兹抑携芭框彷罐虹拷萍臂袭叙吻仿贼羯浴体翠灿敲胁侣蚁秩佑谨寡岳
赔掩匙曹纽签晋喻绵咏摊馨珊孕杰拘哟羡肤肝袍罩叛御谜嫁庙肠谎潘埔卜占拦煌俄札骤陌澄仓匪宵钮岗荡卸旨粽贸
舌历叮咒钥苹祭屈陋雀睹媚娜诱衷菁殿撕蠢惟嚣踊跨膀筒纹乳仗轴撤潭佛桂愤捧袖埃壹赫谦汇魏粹傅寮猴衰辜恳桶
吋衫瞬冻猎琼卿戚卓殖泼譬翰刮斌枉梁庞闽宅麟宰梭纠丛雕澳毙颖腔伫躺划寺炼胃昂勋骄卑蚂墓冥妄董淋卢偿姻砸
践殷润铜盲扎驳湿凑炒尿穴蟑拓诡谬淫荡鼎斩尧伪饿驰蚊瘟肢挫槽扶兆僧昧螂匹芝奸聘眷熙猩癢帖贫贿扑笼丘颠讶
玮尹詗柱袁漆毋辣棍矩佐澡渊痞矮戈勃吞肆抖咳亭淘穗黏冈歧屑拢潇谐遣诊祈霜熬饶闯婉致雁觅讽膜挣斤帆铺凄瑟
艇壶苑悬詹诠滤掰稚辰募懿慨哼汁佬纤肃遨渔恕蝴垫昱竿缝蹈鞭仆豫岩辐歹甄斑淹崎骏薰婷宠棵弓犬涂刹郁坎煎螺
遮枯台昔瘾蒂坠唔瞎筝唇表吁冤祷甩伞酱范焉娇驼沦碳沾抚溶叠几蜡涌氧弦娱皓奴颓嘎趟揭噹剥垦狭魁坊盐屎郝佩
摧栗菊瘦钧匿砖嘘缚嘟盆债霞挽逍畔蕴颈获畏喂脾姬赴囊噪熄锡诀肇璋晕浊伐峡窃枕倘慌垮帕莹琦厢渺脏削锣虐豔
薇霉衍腊喧娶遂睁裙韦矢伺钉婴蓄奸廿堵葬蓬鸦尝挨蕾璿挚券厨醇呻霍剃浆葡暨滨履捞咕耕棉烁尉艰妓棺鹏蒸癌纬
菌撇惩绑甫崩魄拂汰氓歇萝呒萄蕃曝疋向胏烛腻襄妆髓朴薯颂薛滩橘贰嘲叹枚侮豹巢酬碑翩蚕辽矿屡谴卵撰攀肌冯
宴盏阪浦迦颁炼尬胀辟艘株只湘饲爹梨喽侍疫雕黯并铝弗爪鄙钗栽狸谘柄悸喉擅劈秉芷裸锵贾逗寓咚璞烫铅啸炳屿
竖惶仕挪栅迄顷窄鸥鲢郊倩兜茧磊抒夷绰溯拙僚芙杖溃凶鸽妒沌祺呐卦聆栖蝇佮唾汇楣匠蛛悼舜耿瞄芋瞒竭茵吼苛
浸拯克豆沛掠廊凸搅俺酌倡朦蕉暱焕掏蝉焰狄绳惰芽裹宛御赎燥滔贬悍袂坟颉啤押尴颤钝腥缔粮哑槟簿斧肿纶僵齣
辖蹲敷喘扎酿佑肖愈隧嗜檬迳碌襟凋圭寇污哨倪筠桦诈姜旬秃脂噢撼衅庚炫谭惭涩崔贷胡晒琉捏绮膝拭暗醋膨杠鑫
瀑喃剖袜逾涅扳惘凳呃掘捍榔窍蜗旷梵暇稻柠抉辗蔚钩卜莺匡蜘祯哔窟亟谛溢黛晦伶逮傍葱刁堤恍匣谍禧轿耸瀚斐
忿泓拐驴罕沫绽刃窈渝仄瑛葵噜绣奕窥浏隶蔽仟敛丞诘鳖疤膏锥窕皱晰晖舅孰煽姚钞袱绊焚芦咸沮呕瞪淳丐茹盘菱
篠涕衬蚀溉瑄翟怠钰躯肺掷丑奢荫靶纱芸佰峻阱哄肾庄囡阑戳腕菸凹蟾蒐呱巾雏螃盯馈垄毓犀逞姨穆樵阀弥跷搁隙
疵憧忏琨阙萱怅辄搏榕饥捣渣眺虞俯绅谤珑咫俏淆蜀楠乞诅匀貂寰迋敞跪囚溺骆憬苇脊瑶疆乍杆眸窜孽卅夭簧徘馒
趴鎚啼冗缉絮啄沸萃嘶鸳禽惫徨屐舆邂掀嫖苟檯矫铎棱哗徊拱蕙徬滞吠妞氾芹叩朽侪赦汐丰虔茅棠仑膳魉儡鸯懦渗
邵筱畜崖瑕蕊揣擒挂屯莽矽侏弧澈饺奎裘塌饵偎泻蔓彗樽衔茍磋萎廓悯铸茎歼壤浇蚤恃瞻拚汀椒嚼粥磅佫勘脖吨澜
锻笙厄嚷伽徽隅寥缤簾烘茜驯噎厦闰煤链锈诫颊俐曳蓓暧郤淌喀昆蔑峙躁菇逅雇殴泌酥缮莓辕骇巍糗扛杏茁琵礁秽
岔僻焊嗡诵瞌捌遁赃涡琮卯锯扔苏邹莅隘蹋湛昼岫蛰桩藐汲禄皂濑绒耽粪粤卤曜懋咎痘聂垢瞳闵睿跤鉴躬斟淇莒毯
幸骋岱庐殃橄恤叽鳞蒙芥榄楷硫苔麒椎禹喙厘袅亥倌吭诃裔梓蓦岩帜瓣狡惕蒙怯嫩龚嚎豚埠暸唆妃瓢蹄厮讥啃琶愿
噱狷搪氢橙咆靡砌筷兑溼呸镀踹冢祟懈术搓攸橡膛俞祉冀炊瓷遐揽鹭茄蜢塘郡韬挟牟糙阎旻赘霆呎炭霄媳瘤猿颺煚
铠蝠钜苓傀烬墅璇困愣恬嫉琐嫂淼梳憎搂藻酵屉陡摺箫飨桐蚱曦璧偈蹦昶咙铮嗤戌屌耘裳啾嵘胺笃烹巩厝疚鸶汹蔷
沐咽烙畸讳揍曙铐朔涓睬矶岐凄鲫楞鲤荆偕徜饥肮蔼辙恁霈诛鞠茉煜傭嗓酹昙铨艳绷峨揉珈鹃诲臆焰隽熔堇韧扒憨
舵肛戊坝抠骷碘鞍冕榨肘羔哺霓巳铲蚵惆驹撷稽羹纺蜕趾吊豁褪癸眨臻慷蝙胧沼舱柚抨葭枷靥硝绚绞缆讪褚砗嫣蒲
丫鹦蒹憩懊聋盎婊盔峦矜凛铺鹉蜴惚畴羁媛堑泛疮韶憋祁诟搔蜥袒奄忱玖拌悴祠扼髅筑蛤茱骐捶须亢葔艸筛岳岳慵
戮跎砰仑炜篱笈瘫吏痊庶厥棘娑沁窘鲸缕硷俨栈蔬鸠闲迢恣昀泠涟眩噫娥荼鳄镖侃虏俾樟榴咛炬窦笠翱莘躇翡姜枭
匕藩徉觞拣吱皈墉傌梢巅踌萌幌杭侥栾奠痲夸瘖芯蟀驿耨禾瑾塾俭沱腺橱僵惋擞噗呛抴蛀渲酋跆埸嬉怆噶耙憔挠羲
扑眶蛎蹉孵淀恸灸愕淤狙槛嗈霎嗽兢瑚冉甸怔蠹缀谄灼紊彤荐诣眛禀馏蒜窑讦机炯颐缪扉嵩缅朕蟋濒剔局钍肋噩佢
揖圳芜亵崭踅蜻坞绫冶惦梧罣殆兀讼臼踮炙雌啧褒竺匈葳旱骰阉甭欣霏酪雍饪勋煦漓娴揪囝婵佼玟荤俘癖瞋咄幢迂
蓊疹儸桔讹籐眯猖泄凿咻晏诬漪辫蔺症妾琇蜓烽舔娣汶诏侈膺渚槌鞘噬咐璀肪羚羿葫箔庇俪嘱颅玺褐擂遑萦罹粘栗
钊彪瘀蛾馁洹谕胚卉拇炽睦鲨碴辟漱窒惺谲勦迺臀痪褔渠弋咸狸吽痔霭轼姥璁钙漾跛翎磷嗳吩敕氮鲍俟婿尪谚恺裴
汞剿瞥氯桨仝瀛骸钳镕靓漩攘垣荻咯篑茗桓浒桠珀痠靴咀谷矗瘴璟籽晒沥弩洸婪翊背俑磕暐撩峥鹊昕寐徙遴濯堉跋
陨丕簇鹂笋鬓竑绎镍阕燿胥蚓嗔嬴榷尸蜍夙睐蚯谩璜湄鳗棕笺垚蛊讷鸵痹殉墟旄檀竣熹沂峭葾拈隍鞑嗅佯蚣躏雇乩
麓酗寅洒媲瞩钡诽拗朴罔螳撮睽渍摹扪搧蹂媄纾蔗晔隼惮睭箍奚掳咿渎霾叨邃稠淮骁咩岑聿吮铳癫敖蜈钣滂酉刍谙
虱坷笆竽梖賏闺浙疙蓁烷喈跩酣卍遏亘贔万掐蛹骥樊雱戾别匮崛咨湃账粟谯骖焜溅漳欸葆瘩剷恙陞榻潞哞锤琢簷仆
厘篷揆遽峘圃町馊潢岖蟆嚥怂琬镶侄庵瞑赂澹杵苯劭忡枣佗掺捅迩衿饕皎娓镉糯垠潺佣柿绸庠濂逑狈踝鲶傜叱缇懵
椭贻猥哄咁粱迭邰悚榆脓冇寨镁摒徕嗦烜萼壬诧碇镳锚迥孚陇豺悖搥钛肄脐唢诙拎戎崚喳鳕嗣砥枋沽渥黝鱿殇蔫爻
籁孜恿衙痣骧攒鎗闸孺洄昊踼沃妍拽牯逵泯龌銮镛雉梗麾胤馥髦璨浣鼐呗腑吁牒狒痰剌剽篡沬驭辇贮妲盥莞阖筏炖
纭雩涧筐藕垓垛齁鐽馅芮菠绥躄谆琅汨鮭啜晤惬苞毗倏哮伎杞歛荃呷麴糜旳绯饯颦煇荀悱鸾亩龊仞愫灶栩浬靦坍嗖
冽偌巿蒨隋劾裱蜃蚌吆毘鳍钏潦钵嗙龈柒娼脕徛倔唏黴碾瞰蝗魇譁钿悻螫唧觑箩窠薏踱浯腆烸睫谧舫瘪晌埵乒刽娉
捻谟锄閤屹哽蜿逄姗獗帑蹶桧鼾陲窿箇呆蝌砺蛟桢匝夯乓偬谏弭俸烨弼磺捆磐荏吒崁泱谑洼嵌栓踵鞦酯钾茸弛葯萏
滢玠鹬钲跻嬷蚪鳅燊捱狩骼掬酝祀琛獭箝菡隹邝楔缱诒婶擘愠釆稔槭摃帷黉镰鼹芎埤邢呓缥骛铀偃闾恫瞿蟒淦湮涤
琥轧槙忝崧诌飒喋舶箕墩哒晾砷濡猾阂韆琍宦樕鲷佞叟团沅疡啬眈肴豨囤裆蕨胱愎稼嵋瑙稷忖荟妩嚏箴绻湍爰颔痧
戕绢嗝褓梆晞锢剁慑嗟泷诤暝帼牴琏昴诩篆攫甯睨缎蹬犁蛆诋缨睾婢傥霁琅熏啻捎皿暄躅吃宥埕涣怦傧鲥迸釜踯簑
僮玆衲杳姒嬿忪鲲槁馋甡癞咋翌栱唠轶驮铬驽阜啐猷癈蝨淂楹氨菅泞戟拮踞忐骅彧纰罈郢聒跚犛驷姣谪堐忑焊饷钠
娄倭胭邋秧恻宸鲈妤椿锂猬嶙醺啵嘈逖涘爿卤鮀滕荪殡嫦臧峋坻暾鬩鈃俎据蜒褉邑缈涎沚沪綵袓轫蛢捺拴耆柑潁浚
喟棣嗷熨挓甕槐娩鑞蕤腋瘁铿澍莠糸悌勺涌枰伝锌饴幡铄胯岌痢姝诳醃瞠晡獠膫腮唰榛烯膊淅纣佶葩嫡狞缄诿帛甬
芩蹛玑鹫豊倜蹴镂丘腓邸脯毁菀犊珂盅挹烩錡胳叼馄猝谀卞俦雎菫炘鹄酮氟桀帚荔洱窖薮蔻捂锾苳夤璐恚沝氦颚遢
渤舀猕碉呣矬菈氰韭帘谒噤蓑蹼棹焢拧臾疝蛭捀烊绁衹邈踽尻淙銂嘹夆涪肓颳庖鸢炤跺愍啷讴壑辘胛绛匾臊壅睇忉
刈蹙泵珣孃畦蠋戍蝎羡兀靳殁伕蹒佚囱嘤趺贀脩砾臬罄艋邬掣钨缭糟撬噪矕哆脍粼孑氐嗄痉赣揩芊昝蹑鼬甥拄荧狰
鲛躂謢趐陛詘苹拺靼愔捩硐稹淩顸桎刎榭蠕埂迵罡颢圜赁墬纔刨筊彊筌葄蹊壼欉谖胫宕珪椆揶蓼赀屄觎鹧雕掴賸扈
淬贲蝣綑潸瘐玎辍赈鸲嘀昃婬囿坳滮蔘饨雹畀渭掔綩胝搾軂觊崽沓褛衮傩虌嗲柰鏖崴濠鶩忒揄挛缰锉筵鸪糠礴亳幔
宓瓒陕腱誏忾鳌玷谗鬟栲篓旌幄翳棻荞靛铛唅轭壕褟羌撂犷讫洵锭髻齰胼桹砝涔仃黔昂涸婀搀梏蛔偆纂堀倬晟紘锒
琱玹凊寤鲔囥珞蚜豋搵倨皕戡迤埼膑儆擤纨忻蠔熇囍毐瓯祚蜉骈怼褊镑熏俚恪觔鎯踫弁啣锟芍蕁擢盹听旸斡痍忸轾
測試
'''
from  googletrans import Translator
translator = Translator()
with open('hanzi.json', 'w') as print_hanzi:
    data = '{\n'
    for char in hanzi:
        if char == '\n': continue
        data += '\t"' + char + f'": "{translator.translate(char, src="zh-cn", dest="en").text}",\n'
    data += '}'
    # data.replace(',\n}', '}')
    print_hanzi.write(data)