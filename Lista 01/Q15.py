def formarGrupos(total_pessoas, pessoas_por_grupo):
    grupos = total_pessoas // pessoas_por_grupo
    pessoas_sem_grupo = total_pessoas % pessoas_por_grupo
    
    return grupos, pessoas_por_grupo, pessoas_sem_grupo
    
total_pessoas = int(input("Digite a quantidade total de pessoas: "))
pessoas_por_grupo = int(input("Digite a quantidade de pessoas em cada grupo: "))

grupos, pessoas_por_grupo, pessoas_sem_grupo = formarGrupos(total_pessoas, pessoas_por_grupo)

print("Serão formados", grupos, "grupos, com", pessoas_por_grupo, "pessoas em cada grupo.")
print("Ficarão", pessoas_sem_grupo, "pessoas sem grupo.")
