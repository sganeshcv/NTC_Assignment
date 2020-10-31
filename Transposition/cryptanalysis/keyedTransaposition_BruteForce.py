# CHARACTERS = "abcdefghijklmnopqrstuvwxyz"
# import itertools

# def getfactors(n):
#     factors = []
#     i = 1
#     while i <= n : 
#         if (n % i==0) : 
#             factors.append(i)
#         i += 1
#     return factors

# def getKeyPermutation(num):
#     permutation_list = list(itertools.permutations(range(num)))
#     print(permutation_list)
#     res = [] #[x + 1 for x in permutation_list] 
#     return res


# def deshuffle(part_message,key):
#     new_message = ""
#     for i in range(len(key)):
#         index_char = key.index(i+1)
#         new_message += part_message[index_char]
#     return new_message

# def decrypt(keys,message):
#     plainText = ''
#     i = 0
#     while i < len(message):
#             plainText += deshuffle(message[i:i+len(keys)],keys)
#             i += len(keys)
#     return plainText

# def main():
#     message = "qewe"  #gt pt
#     factors = getfactors(len(message))    
#     for factor in factors:
#         getKeyPermutation(factor)
#         # print(decrypt(getKeyPermutation(factor),message))

# if __name__ == "__main__":
#     main()