import xlsxwriter

class CreateExcel:

    def __init__(self, filename, header=[], width=[]):
        self.filename = filename
        self.workbook = xlsxwriter.Workbook(self.filename)
        self.worksheet = self.workbook.add_worksheet(self.filename)
        self.header = header
        self.width = width
        self.style = {
            'header': {'font_name': 'Roboto', 'font_size': 11, 'bold': True, 'align': 'center', 'valign': 'vcenter', 'bg_color': 'green', 'font_color': '#FFFFFF', 'border': 1},
            'content': {'font_name': 'Roboto', 'font_size': 11, 'align': 'center', 'valign': 'vcenter', 'border': 1}
        }
        self.add_header()

    def add_header(self):
        for col, value in enumerate(self.header):
            self.worksheet.write(0, col, value, self.workbook.add_format(self.style['header']))
            self.worksheet.set_column(col, col, self.width[col])

    def add_data(self, data):
        row = 1
        for item in data:
            for col, value in enumerate(item):
                self.worksheet.write(row, col, value, self.workbook.add_format(self.style['content']))
            row += 1

    def close(self):
        self.workbook.close()