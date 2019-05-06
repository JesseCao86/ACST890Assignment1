# Read the file and save it in memory.
# And for convenience, we use utf-8 to encode it
with open("twain.txt","r",encoding="utf-8") as f:
    lines = f.readlines()

# Re-write the file and replace “Huck” into “HucK”
with open("twain.txt","w",encoding="utf-8") as f_w:
    for line in lines:
        if "Huck" in line:
         #Replace
            line = line.replace("Huck","HucK")
        f_w.write(line)

# Read the file again and check result.
f = open("twain.txt","r",encoding="utf-8")
s = f.read()
print(s)