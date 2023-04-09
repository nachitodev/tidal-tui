from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Button, Header, Footer, Static, DataTable

class main(App):
    def compose(self):
        yield DataTable()
    
    def on_mount(self):
        from funcs.select import ROWS
        table = self.query_one(DataTable)
        rows = iter(ROWS)
        table.add_columns(*next(rows))
        table.add_rows(rows)
    
global app
app = main()