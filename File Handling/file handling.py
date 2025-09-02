#file handling
# f=open("c:\\temp\\py-test.txt","w")
# for l in range(10):
#     f.write("This is line %d\n" % l)
# f.close()

f=open("c:\\temp\\py-test.txt","r")
text=f.read()
print(text)
f.close()


# f=open("c:\\temp\\py-test.txt","r")
# lines=f.readlines()
# for line in lines:
#     print(line)
# f.close()