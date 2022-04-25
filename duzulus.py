# 123 ədədinin fərqli düzülüşü

#for ilk in "123":
#  for ikinci in "123":
#    if ikinci != ilk:
#        for ucuncu in "123":
#            if ucuncu != ilk and ucuncu != ikinci:
#                print(ilk + ikinci + ucuncu)

# ABCD ədədinin dördlü (fərqli) düzülüşü

for ilk in "ABCD":
    for ikinci in "ABCD":
        if ilk != ikinci:
            for ucuncu in "ABCD":
                if ucuncu != ilk and ucuncu != ikinci:
                    for dorduncu in "ABCD":
                        if dorduncu != ilk and dorduncu != ucuncu and dorduncu != ikinci:
                            print(ilk + ikinci + ucuncu + dorduncu)