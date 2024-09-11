# three major operations that we can do on a file
# 1. Reading
# 2. Writing
# 3. Append

readme_file = open("readme.txt", "a")

# print(readme_file.read())

readme_file.write("Hello!!")

readme_file.close()