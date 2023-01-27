import models as mod
import view as v

def use_data_base_phone(senson = 'Tel_Sprav.txt'):
    a = mod.get_data_tel_spravki('Tel_Sprav.txt')
    d = mod.data_tel_spravka(a)

    s = ([d[j][i] for i in range(3) for j in range(4)])

    data = {'Ф.И.О.' : s[0 :4],
            'номер телефона' : s[4 :8],
            'адрес' : s[8 :]
            }
    v.logger(data)
    return data

