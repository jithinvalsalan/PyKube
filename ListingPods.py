from kubernetes import client, config
from columnar import columnar

config.load_kube_config()

v1 = client.CoreV1Api()

def list_all_pods():
    ret = v1.list_pod_for_all_namespaces(watch=False)
    fo=open("ListingPods.csv",'w')
    fo.write("NAMESPACE,POD_IP,HOST_IP,NODE_NAME,POD_NAME"+'\n')
    fo.close()
    for i in ret.items:
        #print("%s\t\t%s\t\t%s\t\t%s\t\t%s" % (i.metadata.namespace, i.status.pod_ip,  i.status.host_ip, i.spec.node_name,  i.metadata.name ))
        data1 = ("%s,%s,%s,%s,%s" % (i.metadata.namespace, i.status.pod_ip,  i.status.host_ip, i.spec.node_name,  i.metadata.name ))
        fo=open("ListingPods.csv",'a')
        fo.write(data1+'\n')
        fo.close()


list_all_pods()