# на вход податся строка, и нужно сосчитать количество каждого символа в ней
# def strcounter(s):
#     print(set(s))
#     for sym in set(s):
#         count = 0
#         for syb_sym in s:
#             if sym == syb_sym:
#                 count += 1
#         print(sym,"-", count)
#
# strcounter("abcd")
# сложность O(N*M) -> O(N^2)

def strcounter(s):
    sym_counter = {}
    for sym in s:
        sym_counter[sym] = sym_counter.get(sym, 0) + 1
    for sym, count in sym_counter.items():
        print(sym, "-", count)
strcounter("anmmghhhhmnnnagaa")
# сложность O(N+M) -> O(N)