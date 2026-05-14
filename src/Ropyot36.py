import encoder as en
import decoder as de

def menu():
    while True:
        en.clear()
        print("""
>>============================================================<<
||'||''|.                                       .   ____      ||
|| ||   ||    ...   ... ...  .... ...   ...   .||.  ` //   ,/ ||
|| ||''|'   .|  '|.  ||'  ||  '|.  |  .|  '|.  ||    //   //  ||
|| ||   |.  ||   ||  ||    |   '|.|   ||   ||  ||    \\   ((   ||
||.||.  '|'  '|..|'  ||...'     '|     '|..|'  '|.'   )) || ))||
||                   ||      .. |                    //  (( ||||
||                  ''''      ''                    /'    \// ||
>>============================================================<<
              
>>=================================<<
||                                 ||
|| [1] Iniciar Encoder (Converter) ||
|| [2] Decodificador   (Em breve)  ||
|| [0] Sair                        ||
||                                 ||
>>=================================<<
            """)
        escolha = (input("Selecione uma opção: "))
        if escolha == '1':
            en.encoder()
        elif escolha == '2':
            de.decoder_sstv()
        elif escolha == '0':
            print("Encerrando...")
            exit()


if __name__ == "__main__":
    menu()