from kubernetes import client, config
import os
#print(os.getcwd())

config.load_kube_config()

v1 = client.CoreV1Api()
def all_pods():
    print("Listing pods with their IPs")
    ret = v1.list_pod_for_all_namespaces(watch=False)
    print ('=' *120)
    print (f' {"NAMESPACE":^10} {"POD IP":^20} {"HOST IP":^20} {"NODE NAME":^10} {"NAME":^15}')
    print ('=' *120)
    for i in ret.items:
        print("%s\t\t%s\t\t%s\t\t%s\t\t%s" % (i.metadata.namespace, i.status.pod_ip,  i.status.host_ip, i.spec.node_name,  i.metadata.name ))
        #print(i)
all_pods()