from ipycanvas import Canvas

canvas = Canvas(width=500, height=281, sync_image_data=True)

# Perform some drawings...

canvas.to_file("my_file.png")
