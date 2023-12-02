def duplikasi(listLama):
    listBaru = []
    for x in listLama:
        listBaru.append(x)
        listBaru.append(x)
    return listBaru

isiList = duplikasi(['pepaya', 'mangga', 'pisang', 'durian', 'jambu'])
print(isiList)