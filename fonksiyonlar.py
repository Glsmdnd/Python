def krediListele():
    krediler = [
        "Hızlı Kredi", "Maaşını Halk Banktan Alanlara Özel",
        "Mutlu Emekli İhtiyac Kredisi"
    ]
    for kredi in krediler:
        print("<option>" + kredi + "<option>")


krediListele()
