menus=[["egg", "broccoli"],["egg", "sausage", "broccoli"],["egg", "mushroom"],["egg", "broccoli", "mushroom"],["egg", "broccoli", "sausage", "mushroom"], ["mushroom", "broccoli", "sausage", "mushroom"],["mushroom", "sausage", "mushroom", "broccoli",
"mushroom", "tomato", "mushroom"],["mushroom", "egg", "mushroom", "mushroom",
"broccoli", "mushroom"]]
for menu in menus:
    while "mushroom" in menu:
      menu.remove("mushroom")
      
    print(menu)