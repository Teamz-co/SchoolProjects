import flet as ft
def main(page: ft.Page):
    ### Functions ###
    def type(e):
        a = int(side1_textField.value)
        b = int(side2_textField.value)
        c = int(side3_textField.value)
        if a + b > c and a + c > b and b +c > a:
            if a == b == c:
                output_text.value = "This Triangle is Equilateral "
            elif a == b or a == c or b == c:
                output_text.value = "This Triangle is Isosceles"
            else:
                output_text.value = "This Triangle is Scalene"
        else:
            output_text.value = "This is not a Triangle"
        page.update()
    def clear(e):
        side1_textField.value = ""
        side2_textField.value = ""
        side3_textField.value = ""
        output_text.value = ""
        page.update()

    ### Page Setup ###
    page.title="Project 1"
    page.window.width=480
    page.window.height=800
    page.theme_mode="dark"
    page.window.center()
    page.vertical_alignment=ft.MainAxisAlignment.SPACE_EVENLY
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER

    ### Header ###
    header_text = ft.Text("Enter the length of each side of a triangle", color = "Blue", size = "30")

    ### Input ###
    side1_text = ft.Text("Side 1 ")
    side1_textField = ft.TextField(width = 300)
    side1_row = ft.Row(controls=[side1_text, side1_textField], alignment =ft.MainAxisAlignment.CENTER)

    side2_text = ft.Text("Side 2 ")
    side2_textField = ft.TextField(width = 300)
    side2_row = ft.Row(controls=[side2_text, side2_textField], alignment =ft.MainAxisAlignment.CENTER)

    side3_text = ft.Text("Side 3 ")
    side3_textField = ft.TextField(width = 300)
    side3_row = ft.Row(controls=[side3_text, side3_textField], alignment =ft.MainAxisAlignment.CENTER)

    ### Buttons ###
    clear_button = ft.ElevatedButton(text = " Clear ", on_click = clear)
    Triangle_type_button = ft.ElevatedButton(text = "Triangle Type", on_click = type)
    button_row = ft.Row( controls=[Triangle_type_button, clear_button ], alignment=ft.MainAxisAlignment.CENTER)

    ### Output ### 
    output_text = ft.Text()

    ### Page Add ###
    page.add(header_text, side1_row, side2_row, side3_row, button_row, output_text)

ft.app(main)