from apps.service import style

def style_transfer(img_style_name, img_content_name, result_name):
    img_style_path = 'apps/assets/' + img_style_name
    img_content_path = 'apps/assets/' + img_content_name
    result_path = 'apps/results/' + result_name

    try:
        style.style_transfer(img_style_path, img_content_path, result_path)
    except Exception:
        return 2

    return 1