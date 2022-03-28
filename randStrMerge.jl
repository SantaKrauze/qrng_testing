file1=open("str1.txt","r")
file2=open("str2.txt","r")
if !isfile("str3.txt")
	touch("str3.txt")
end
file3=open("str3.txt","a")

for i = 0:(filesize("str1.txt")-1)
	seek(file1,i)
	seek(file2,i)
	b1=read(file1,Char)
	b2=read(file2,Char)
	b3=Int(b1)⊻Int(b2)
	write(file3,string(b3))
	#println(b1,' xor ',b2,' = ',string(b3))
end


close(file1)
close(file2)
close(file3)
