# # logarithm function
# # x = integer being altered logarithmically
# # l = rate at which x changes logarithmically in percentage (decimal)
# # n = number of instances to run the logarithmic recursion

# def logarithm(x, l, n):
#     if n == 1: return x
#     print(x)
#     return logarithm(x*l, l, n-1)

# def l(x, l, n):
#     return x*(n**l)

# # print(l(55000, 0.03, 72))

# # print(logarithm(100, 0.125, 4))

# ######################################################################

# # For each year t, the number of trees in Forest A is represented by 
# # the function A(t)=74(1.025)t. In a neighboring forest, the number 
# # of trees in Forest B is represented by the function B(t)=94(1.029)t.
# # Assuming the population growth models continue to represent the 
# # growth of the forests, which forest will have a greater number of 
# # trees after 20 years? By how many?

# # exponential growth function
# # trees = number of trees
# # growth_rate = percent rate at which trees grow
# # total_years = number of years to check growth rate
# # year = current year out of total_years

# def exponent(trees, growth_rate, year):
#     print(year, trees)
#     if year == 0: return trees
#     return exponent(trees*growth_rate, 
#                     growth_rate, year-1)

# # print(f'A = {exponent(74, 1.025, 20):,}')
# # print(f'B = {exponent(94, 1.029, 20):,}')

# # B has more trees within 20 years
# # A = rounded to 121 trees
# # B = rounded to 167 trees



# # exponential function
# # E(i) = x(r)^i

# # x = integer or float
# # r = percent rate at which x changes
# # i = total iterations of the function

# def e_recursive(x, r, i): # doesnt work for negative i
#     if i == 0: return x
#     return e_recursive(x*r, r, i-1)

# def exponent(x, r, i): # works for negative or positive i
#     return x*(r**i)

# # print(exponent(1.39, 1.006, 21))

# import numpy as np
# from scipy.interpolate import make_interp_spline
# import matplotlib.pyplot as plt 

# def base_e(n=1_000_000_000):
#     return (1+(1/n))**n

# def plot_base_e(transform=1, rng=11):
#     x_list = []
#     y_list = []

#     for n in range(1, rng):
#         x_list.append(n)
#         y_list.append(base_e(n*transform))

#     x_array = np.array(x_list)
#     y_array = np.array(y_list)
#     spline = make_interp_spline(x_array, y_array)
#     x = np.linspace(x_array.min(), x_array.max(), 500)
#     y = spline(x)

#     plt.plot(x, y)
#     plt.title("Euler's Constant | e = (1+(1/n))^n | The Logarithmic Curve Of e")
#     plt.xlabel("X")
#     plt.ylabel("Y")
#     plt.show()

# plot_base_e(transform=0.001, rng=10000)

# # print(points)

# # print(base_e())

# def e(x):
#     return base_e()**x

# # print(e(167))

# # for x in range(10):
# #     print(x, e(x))

# def decay(a, e, r, t):
#     return a*(e**(r*t))

# # print(f'{decay(220, base_e(), -0.173, 365):,}')

# # print(e(-0.7))

# # print(base_e(1_000_000_000))

# # print(e_recursive(30, 2, 3))
# # print(exponent(30, 2, 3))

# # print(exponent(8, 1.1, 4-6))

# # for i in range(20):
# #     print(exponent(5, 4, i) - 10)

# # print(exponent(-0.5, 0.5, -7)+4)

# # xs = (round(x/10) for x in range(1000))
# # for i in xs:
# #     print(round(i/10))
# #     e = e(110000, i, 20)
# #     if e == 146000: print(e)

# def g(a, e, r, t):
#     return a*(e**(r*t))

# def g_business(P, n, r, t):
#     return P*((1+(r/n))**t)

# # print(g_business(10200, 12, 0.04, 132))

# def f(b, x):
#     return b**x

# # plots_pos = []
# # plots_neg = []

# # for x in range(10):
# #     plots_pos.append((x, f(4, x)))
# # for x in range(0, -10, -1):
# #     plots_neg.append((x, f(4, x)))

# # print(plots_pos)
# # print(plots_neg)


import googletrans
from transformers import pipeline
# sentiment_pipeline = pipeline('sentiment-analysis')
# data = [
#     '''
#     does anyone need fridge magnets i have four boxes i dont need
#     '''
# ]
# print(sentiment_pipeline(data))

# question_bot = pipeline('question-answering')

# data = 'こんにちは'

# gl = googletrans.LANGUAGES
# gl_codes = googletrans.LANGCODES

# translator = googletrans.Translator()
# detected = translator.detect(data)
# lang = detected.lang
# print(gl[lang])

# if not gl[lang] in 'en':
#     translation = pipeline(f'translation_{lang}_to_en')
#     print(translation(data))


from transformers import pipeline

music_generator = pipeline(task="text-to-audio", model="facebook/musicgen-small", framework="pt")

# diversify the music generation by adding randomness with a high temperature and set a maximum music length
generate_kwargs = {
    "do_sample": True,
    "temperature": 0.7,
    "max_new_tokens": 35,
}

outputs = music_generator("lofi beats to study/relax to", generate_kwargs=generate_kwargs)