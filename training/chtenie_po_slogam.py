with open("Kurochka_ryaba.txt", "r", encoding="utf-8") as chicken:
    glasnye = ['А', 'а', 'О', 'о', 'У', 'у', 'ы', 'Э', 'э', 'Е', 'е', 'Ё', 'ё', 'И', 'и', 'Ю', 'ю', 'Я', 'я', 'ь']
    punkt = [',', '.', ':', '!', '?', ';', '—', ' ', '\n']
    text = chicken.read()
    razbity_text = []
    for i in range(len(text) - 1):
        if text[i] in glasnye:
            if text[i + 1] in punkt:
                razbity_text.append(text[i])
            elif text[i + 1] not in glasnye and text[i + 2] in punkt:
                razbity_text.append(text[i])
            else:
                razbity_text.append(text[i] + '-')
        else:
            razbity_text.append(text[i])
        skazka = ''
        for i in razbity_text:
            skazka += i

with open("Kurochka_ryaba_po_slogam.txt", "w", encoding="utf-8") as chn_new:
    chn_new.write(skazka)
