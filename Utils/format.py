def hex_to_rgb(value, alpha=1):
    return tuple(int(value[i:i + 2], 16)/255.0 for i in (0, 2, 4)) + (alpha,)