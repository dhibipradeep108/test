from django import template
from django.utils.html import format_html
import datetime

register = template.Library()

class CurrentTimeNode(template.Node) :
    def __init__(self, format_string):
        self.format_string = format_string
        
    def render(self, context):
        context["current_time"] = datetime.datetime.now().strftime(self.format_string)
        return ""

@register.simple_block_tag(takes_context = True)
def msgbox(context, content, level) :
    format_kwargs = {
        'level' : level.lower(),
        'level_title' : level.capitalize(),
        'content' : content,
        'open' : " open" if level.lower() == "error" else "",
        'site' : context.get("site", "contacts"),
    }
    result = """
    <div class = "msgbox {level}">
        <details{open}>
            <summary>
                <strong>{level_title}</strong> : Please read for <i>{site}</i>
            </summary>
            <p>
                {content}
            </p>
        </details>
    </div>
    """
    return format_html(result, **format_kwargs)

def do_current_time(parser, token) :
    try :
        tag_name, format_string = token.split_contents()
    except ValueError :
        raise template.TemplateSyntaxError(
            "%r tag's argument should be in qoutes" % token.split_contents()[0]
        )
    if not (format_string[0] == format_string[-1] and format_string[0] in ("'", '"')) :
        raise template.TemplateSyntaxError( 
            "%r tag's argument should be in qoutes"
        )
    return CurrentTimeNode(format_string[1:-1])

register.tag("current_time", do_current_time)