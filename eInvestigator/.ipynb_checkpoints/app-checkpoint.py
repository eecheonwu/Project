from shiny import App, ui, render, reactive
import pandas as pd
import matplotlib.pyplot as plt
import io

app_ui = ui.page_fluid(
    ui.panel_title("CSV Dashboard"),
    ui.layout_sidebar(
        ui.sidebar(
            ui.input_file("file", "Upload CSV file", accept=[".csv"]),
            ui.input_select("x_axis", "X-axis", choices=[]),
            ui.input_select("y_axis", "Y-axis", choices=[]),
            ui.input_select("plot_type", "Plot type", choices=["Scatter", "Line", "Bar"]),
            ui.input_numeric("font_size", "Font size", value=12, min=8, max=24),
        ),
        ui.output_plot("plot"),
        ui.output_table("data_preview"),
    )
)

def server(input, output, session):
    data = reactive.Value(None)

    @reactive.Effect
    @reactive.event(input.file)
    def _():
        file_content = input.file()
        if file_content is not None:
            content = file_content[0]["datapath"]
            df = pd.read_csv(content)
            data.set(df)
            
            choices = list(df.columns)
            ui.update_select("x_axis", choices=choices, selected=choices[0] if choices else None)
            ui.update_select("y_axis", choices=choices, selected=choices[1] if len(choices) > 1 else None)

    @render.plot
    def plot():
        if data() is None:
            return None
        
        df = data()
        x = input.x_axis()
        y = input.y_axis()
        plot_type = input.plot_type()
        font_size = input.font_size()

        fig, ax = plt.subplots(figsize=(10, 6))
        
        if plot_type == "Scatter":
            ax.scatter(df[x], df[y])
        elif plot_type == "Line":
            ax.plot(df[x], df[y])
        elif plot_type == "Bar":
            ax.bar(df[x], df[y])
        
        ax.set_xlabel(x, fontsize=font_size)
        ax.set_ylabel(y, fontsize=font_size)
        ax.set_title(f"{plot_type} Plot: {y} vs {x}", fontsize=font_size + 2)
        ax.tick_params(axis='both', which='major', labelsize=font_size)
        
        plt.tight_layout()
        return fig

    @render.table
    def data_preview():
        if data() is None:
            return None
        return data().head()

app = App(app_ui, server)
