def setting_fun( filename='settings',**details):
    if details:
        with open(filename,'w') as file:
            for k,v in details.items():
                file.write(f'{k} -> {v}\n')



setting_fun(color='blue',alpha=.1,gamma=3, filename='color_setting.txt')
setting_fun(ram=2,windows='95',version=3,wallpaper='cutiepie.jpg',
            filename='pc_setting.txt')
