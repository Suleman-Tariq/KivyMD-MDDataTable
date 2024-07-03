# from kivy.uix.boxlayout import BoxLayout
# from kivymd.app import MDApp
# from kivymd.uix.datatables import MDDataTable
# from kivy.metrics import dp
#
# class RootWidget(BoxLayout):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.orientation = 'vertical'
#         data = []
#         for i in range(0, 20):
#             data.append((f"Row {i} Col 1", f"Row {i} Col 2"))
#         # Define the data table
#         self.data_table = MDDataTable(
#             size_hint=(1, 1),
#             check=False,
#             rows_num=10,
#             use_pagination=True,
#             column_data=[
#                 ("Column 1", dp(30)),
#                 ("Column 2", dp(30))
#             ],
#             row_data=data
#         )
#
#         # Bind the on_row_press event to the handler
#         self.data_table.bind(on_row_press=self.on_row_press)
#
#         # Add the data table to the layout
#         self.add_widget(self.data_table)
#
#         # Store the previously selected row index
#         self.previous_row_index = None
#
#     def on_row_press(self, instance_table, instance_row):
#         row_index = instance_row.index
#         new_row_data = []
#         row_index = int(row_index/2)
#         if self.data_table.pagination:
#             current_page = self.data_table.pagination.children[2].text.split('-')
#             per_page_records=current_page[0]
#             total_record = current_page[1].split('of')[0]
#             print(per_page_records, "/", total_record)
#             page=int(per_page_records)-1
#             new_index=row_index + page
#             print(new_index)
#         for index, row in enumerate(self.data_table.row_data):
#             if index == new_index:
#                 new_row_data.append([f"[b]{cell}[/b]" for cell in row])
#             else:
#                 new_row_data.append(row)
#
#         # Print the selected row data
#         print(f"Selected Row Data: {self.data_table.row_data[new_index]}")
#
# class TestApp(MDApp):
#     def build(self):
#         return RootWidget()
#
# if __name__ == '__main__':
#     TestApp().run()
