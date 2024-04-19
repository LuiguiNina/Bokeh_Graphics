import streamlit as st
from math import pi
from bokeh.plotting import figure, save
from bokeh.palettes import Category10

# Datos para los gráficos
x_scatter = [1, 2, 3, 4, 5]
y_scatter = [6, 7, 2, 4, 5]
x_line = [1, 2, 3, 4, 5]
y_line = [6, 7, 2, 4, 5]
categorias = ['A', 'B', 'C', 'D', 'E']
valores = [4, 7, 2, 5, 8]
etiquetas = ['A', 'B', 'C', 'D', 'E']
tamaños = [20, 30, 10, 20, 20]

# Crear gráfico de dispersión
p_scatter = figure(title="Gráfico de dispersión de ejemplo", x_axis_label='x', y_axis_label='y')
p_scatter.scatter(x_scatter, y_scatter, size=10, color="navy", alpha=0.5)

# Crear gráfico de líneas
p_line = figure(title="Gráfico de líneas de ejemplo", x_axis_label='x', y_axis_label='y')
p_line.line(x_line, y_line, line_width=2)

# Crear gráfico de barras
p_bar = figure(x_range=categorias, title="Gráfico de barras de ejemplo", x_axis_label='Categorías', y_axis_label='Valores')
p_bar.vbar(x=categorias, top=valores, width=0.5, color="navy")

# Crear gráfico de pastel
p_pie = figure(title="Gráfico de pastel de ejemplo")

# Calcular los ángulos de los sectores del gráfico de pastel
start_angle = [0] + [2 * pi * sum(tamaños[:i]) / sum(tamaños) for i in range(len(tamaños))]
end_angle = [2 * pi * sum(tamaños[:i+1]) / sum(tamaños) for i in range(len(tamaños))]

# Asegúrate de que las longitudes de todos los datos sean iguales
etiquetas = etiquetas[:len(tamaños)]

# Agregar el gráfico de pastel con los datos
for i in range(len(etiquetas)):
    p_pie.wedge(x=0, y=0, radius=0.5, start_angle=start_angle[i], end_angle=end_angle[i], 
                fill_color=Category10[5][i], legend_label=str(etiquetas[i]))  # Convierte a cadena legend_label

# Guardar los gráficos como archivos HTML
scatter_html = "scatter.html"
line_html = "line.html"
bar_html = "bar.html"
pie_html = "pie.html"

save(p_scatter, scatter_html)
save(p_line, line_html)
save(p_bar, bar_html)
save(p_pie, pie_html)

# Mostrar los gráficos HTML en Streamlit
st.title("Visualización de gráficos Bokeh en Streamlit Sharing")

st.header("Gráfico de dispersión")
st.components.v1.html(open(scatter_html, "r").read(), width=600, height=400)

st.header("Gráfico de líneas")
st.components.v1.html(open(line_html, "r").read(), width=600, height=400)

st.header("Gráfico de barras")
st.components.v1.html(open(bar_html, "r").read(), width=600, height=400)

st.header("Gráfico de pastel")
st.components.v1.html(open(pie_html, "r").read(), width=600, height=400)
