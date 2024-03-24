import flet as ft
import os
import time

def main(page: ft.Page):
    
    switch = ft.Ref[ft.Switch]()
    hostTF = ft.Ref[ft.TextField]()
    portTF = ft.Ref[ft.TextField]()
    
    confirm_dialog = ft.AlertDialog(
        bgcolor=ft.colors.GREEN,
        title=ft.Text("Guardar proxy"),
        content=ft.Text("Datos guardados")
    )

    def show_confirm_dialog():
        page.dialog = confirm_dialog
        confirm_dialog.open = True
        page.update()
        time.sleep(2)
        confirm_dialog.open = False
        page.update()
    
    def save_data():
        page.client_storage.set("ProxyEnable", switch.current.value)
        page.client_storage.set("ProxyServer", f"{hostTF.current.value}:{portTF.current.value}")
    
    def set_proxy(e):
        save_data()

        os.system(f"REG ADD \"HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\" -v ProxyServer -t REG_SZ -d {hostTF.current.value}:{portTF.current.value} -f")
        
        if switch.current.value:
            os.system("REG ADD \"HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\" -v ProxyEnable -t REG_DWORD -d 1 -f")
        else:
            os.system("REG ADD \"HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\" -v ProxyEnable -t REG_DWORD -d 0 -f")
            
        show_confirm_dialog()
            
    def on_save_data(e):
        save_data()
    
    page.window_height = 300
    page.window_width = 300
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    enable = ""
    host = ""
    port = ""
    
    if page.client_storage.contains_key("ProxyEnable"):
        enable = page.client_storage.get("ProxyEnable")
    
    if page.client_storage.contains_key("ProxyServer"):
        host = str(page.client_storage.get("ProxyServer")).split(":")[0]
        port = str(page.client_storage.get("ProxyServer")).split(":")[1]
    
    page.add(
        ft.Column(
            [
                ft.Row(
                    [
                        ft.Switch(ref=switch, label="Activar proxy", on_change=set_proxy, value=enable)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=50
                ),
                ft.TextField(ref=hostTF, hint_text="Host", value=host),
                ft.TextField(ref=portTF, hint_text="Port", value=port),
                ft.Row(
                    [
                        ft.CupertinoFilledButton(content=ft.Text("Guardar", color=ft.colors.WHITE), on_click=set_proxy)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=50
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )
    
    page.on_close=on_save_data

ft.app(main, name="Windows Proxy Mannager", view=ft.FLET_APP)