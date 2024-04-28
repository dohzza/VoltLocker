from ipycanvas import Canvas

canvas = Canvas(width=200, height=200, sync_image_data=True)

# Perform some drawings...

canvas.to_file("my_file.png")
