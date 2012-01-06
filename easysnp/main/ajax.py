
import uuid

def load_url(url):
    u = "%s" % uuid.uuid1()
    u = u.replace("-", "_")
    ret = "<script language=\"Javascript\"> $(document).ready(function(){ $(\"#%s\").load(\"%s\") }) </script> <div id=\"%s\"></div> " % (u, url, u)

    return ret
