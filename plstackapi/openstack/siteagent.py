import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "plstackapi.planetstack.settings")
import time
from plstackapi.core.models.site import Site
from plstackapi.openstack.driver import OpenStackDriver    

class SiteAgent:
    def run(self):
        driver = OpenStackDriver()
        # fill in null tenant ids 
        sites = Site.objects.filter(tenant_id=None)
        for site in sites:
            # calling save() on the model should force the tenant_id to be set
            site.driver = driver
            site.save() 
                                        
if __name__ == '__main__':
    SiteAgent().run()
                 
