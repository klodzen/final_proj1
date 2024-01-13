import flet as ft
def main (page: ft.Page):
    #month/days eval function#
    def mtd_fnct(p):
        #leap year determination#
        if int(year_textField.value)%100 == 0 and int(year_textField.value)%400 == 0:
            leap_ev = "yes"
        elif int(year_textField.value)%100 != 0 and int(year_textField.value)%4 == 0:
            leap_ev = "yes"
        else:
            leap_ev = "no" 
        #og function#
        if int(month_textField.value) == 2:
            if leap_ev == "yes":
                days_textField.value = 29
            else:
                days_textField.value = 28
        elif int(month_textField.value) >= 1 and int(month_textField.value) <= 7:
            if int(month_textField.value)%2 == 0:
                days_textField.value = 30
            else:
                days_textField.value = 31
        elif int(month_textField.value) >= 8 and int(month_textField.value) <= 12:
            if int(month_textField.value)%2 == 0:
                days_textField.value = 31
            else:
                days_textField.value = 30
        else:
            days_textField.value = "error!"
        page.update()
    def clear_fnct(p):
        days_textField.value = ""
        year_textField.value = ""
        month_textField.value = ""
        page.update()
    #page setup#
    page.title="Days/Month App"
    page.window_width=500
    page.window_height=700
    page.bgcolor="WHITE"
    page.vertical_alignment=ft.MainAxisAlignment.SPACE_EVENLY
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    #page content#
    content_title_text=ft.Text("Days in a Month", color="BLACK", size=30)
    #month row#
    m_text=ft.Text("Month (1-12):", color="BLACK", size=20)
    month_textField=ft.TextField(width=100, height=100, color="BLACK", text_size=20, text_align="center")
    month_row = ft.Row(controls=[m_text, month_textField],alignment=ft.MainAxisAlignment.CENTER)
    #year row#
    y_text=ft.Text("Year:", color="BLACK", size=20)
    year_textField=ft.TextField(width=100, height=100, color="BLACK", text_size=20, text_align="center")
    year_row = ft.Row(controls=[y_text, year_textField],alignment=ft.MainAxisAlignment.CENTER)
    #days row#
    d_text=ft.Text("Days:", color="BLACK", size=20)
    days_textField=ft.TextField(width=100, height=100, color="BLACK", text_size=20, text_align="center")
    days_row = ft.Row(controls=[d_text, days_textField],alignment=ft.MainAxisAlignment.CENTER)
    #eval button#
    evalu_button=ft.ElevatedButton(content=ft.Row([ft.Text("Days",size=20, text_align="CENTER")]),width=250, height=100, bgcolor="PINK",color="WHITE", on_click=mtd_fnct)
    #clear button#
    clear_bu=ft.ElevatedButton(content=ft.Row([ft.Text("Clear",size=20, text_align="CENTER")]),width=250, height=100, bgcolor="PINK",color="WHITE", on_click=clear_fnct)
    #final setup#
    page.add(content_title_text, month_row, year_row, evalu_button, days_row, clear_bu)
ft.app(target=main)
            