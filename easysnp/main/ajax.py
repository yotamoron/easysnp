
import uuid

def call(url):
    u = "%s" % uuid.uuid1()
    ret = """
        <script language="Javascript">
            $(document).ready(function() {
                $("#%s").load("%s")
            })
        </script>
        <div id="%s"></div>
        """ % (u, url, u)

    return ret
