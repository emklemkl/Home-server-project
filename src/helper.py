from flask import request
class Helper():
    @classmethod
    def template_selector(cls, sub_string: str = None):
        template_path = request.path
        print(sub_string,"<- Substring")
        if sub_string:
            template_path = template_path.replace("/" + sub_string, "")
        if template_path == "/" or not template_path:
            template_path = "index"
        print(template_path)
        return f"{template_path}.html.j2"
